# Adverse Events Identification and Trend Analysis of Weight Loss Drugs (Orlistat and Relaglutide)

This project analyzes the adverse events associated with **Orlistat** and **Relaglutide**, weight loss drugs, using the **FDA Adverse Event Reporting System (FAERS) dataset**. The goal is to identify trends in reported adverse events over the years and gain insights into potential safety concerns.

## 📌 Project Objectives
- **Extract and preprocess** FAERS data for Orlistat and Relaglutide related adverse events.
- **Identify key adverse event patterns** using data analysis techniques.
- **Perform trend analysis** to examine variations over time.
- **Visualize** the results using interactive charts and reports.

## 📂 Project Structure
Weight-Loss-Drugs-Adverse-Events/ │── data/ # Raw and processed FAERS data │── notebooks/ # Jupyter notebooks for EDA and modeling ├── data cleaning and preprocessing.ipynb │ ├── adverse events EDA.ipynb ├── data preparation.ipynb ├── clustering_reactions.ipynb │── src/ # Python script for AI chatbot │──RAG_chatbot.py │── results/ # Output visualizations and reports │── requirements.txt # Dependencies │── README.md # Project documentation │── .gitignore # Ignore unnecessary files │── LICENSE # License information

## 📊 Dataset: FAERS
- **Source:** [FDA Adverse Event Reporting System (FAERS)](https://www.fda.gov/drugs/questions-and-answers-fda-adverse-event-reporting-system-faers)
- **Data Format:** Quarterly reports containing adverse event records.
- **Preprocessing Steps:**
  - Data cleaning and transformation.
  - Filtering reports related to **Orlistat and Relaglutide**.
  - Standardizing event descriptions for trend analysis.

## 🛠 Installation & Setup
### **1. Clone the Repository**
    bash 
    git clone https://github.com/MYikuno/Orlistat-Relaglutide-Adverse-Events.git
    cd ORLISTAT-Adverse-Events

### **2. Install Dependencies**
    bash 
    pip install -r requirements.txt
### **3. Run the Analysis**
    bash
    python src/data_cleaning.py \newline
    python src/trend_analysis.py

## 📈 Expected Results
- **Time-series plots** showing how adverse events vary over the years.
- **Top reported adverse events** for Orlistat and Relaglutide.
- **Correlation analysis** between age, gender, and event frequency.

## 📝 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

## 🤝 Contributing
Contributions are welcome! To contribute:
1. **Fork** the repository.
2. Create a **new branch** (`feature/your-feature`).
3. **Commit** your changes with a descriptive message.
4. **Push** to your fork and submit a **Pull Request**.

