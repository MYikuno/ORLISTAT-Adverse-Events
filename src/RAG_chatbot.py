import os
import numpy as np
import pandas as pd
import sqlite3
import streamlit as st
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_community.llms import Ollama
from langchain_community.agent_toolkits import create_sql_agent
from langchain.agents import AgentType


def main():
    
    load_dotenv()
    os.environ['OPENAI_API_KEY'] = os.getenv("TOGETHER_API_KEY")
    os.environ["OPENAI_API_BASE"] = "https://api.together.xyz/v1"

    ##read csv data
    df = pd.read_csv('faers_data_cleand.csv')
   # print(df.columns)

    ##connect to SQLite database
    conn = sqlite3.connect("faers_db.sqlite")
    c = conn.cursor()

    ##create the Data table if not exist
    c.execute('''CREATE TABLE IF NOT EXISTS AdverseEvents (
              primaryid INTEGER,
              caseid INTEGER,
              caseversion INTEGER,
              i_f_code TEXT,
              mfr_dt TEXT,
              init_fda_dt TEXT,
              fda_dt TEXT,
              rept_cod TEXT,
              mfr_num TEXT,
              mfr_sndr TEXT,
              age INTEGER,
              age_cod TEXT,
              sex TEXT,
              e_sub TEXT,
              rept_dt TEXT,
              occp_cod TEXT,
              reporter_country TEXT,
              occur_country TEXT,
              outc_cod TEXT,
              adverse_events TEXT,
              drug_seq INTEGER,
              role_cod TEXT,
              drugname TEXT,
              prod_ai TEXT,
              val_vbm INTEGER,
              route TEXT,
              dose_vbm TEXT,
              dechal TEXT,
              lot_num TEXT,
              nda_num INTEGER,
              dose_form TEXT,
              indi_drug_seq INTEGER,
              indi_pt TEXT,
              dsg_drug_seq INTEGER,
              age_in_yrs INTEGER
              )''')

    conn.commit()

    ##insert data from the dataframe into the Data table
    df.to_sql("AdverseEvents", conn, if_exists="replace", index=False)

    ##retrieve and print all rows from Data table
    # c.execute('''SELECT * FROM Data''')

    # for row in c.fetchall():
    #     print(row)

    ##llma3 chatmodel
    llm = Ollama(model = "llama3")

    ##SQLite database
    db = SQLDatabase.from_uri("sqlite:///faers_db.sqlite")

    ##define agent executor
    agent_executor = create_sql_agent(llm, db=db, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                                       handle_parsing_erros=True, 
                                       max_iterations=10,
                                       #early_stopping_method='generate',
                                      verbose=False)

    st.title("FAERS QA Bot💬") ##set title

    ##ask question
    query = st.text_input("Ask a question:")
    k = 1
    while query:

        with st.spinner("Thinking..."):
            try:
                response = agent_executor.invoke(query)
                st.subheader("User Query:")
                st.write(response['input'])
                st.subheader("Answer:")
                st.write(response["output"])
            except Exception as e:
                st.error(f"Error: {e}")
        query = st.text_input("Ask a question:", key=k)   

if __name__=="__main__":
    main()
