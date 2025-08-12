# superstore-data-analysis
📊 Superstore Data Analysis
📌 Overview
This project analyzes Superstore sales data to extract business insights and visualize key performance metrics. It involves:

Data cleaning & preprocessing

Exploratory data analysis (EDA)

Interactive dashboard creation using Power BI

✨ Features
Cleans and prepares raw sales data

Performs exploratory analysis using Python

Visualizes KPIs such as Sales, Profit, Category Performance, and Regional Trends

Includes a Power BI dashboard for interactive insights

📂 Project Structure

├── main.py                       # Main analysis script
├── superstore_cleaning.ipynb     # Data cleaning notebook
├── superstore.csv                # Dataset
├── Super storer Dashboard.pbix   # Power BI dashboard file
├── project_report.pdf            # Detailed project report
└── .idea/                        # IDE configuration (ignore in deployment)
🛠 Installation
Clone the repository


git clone https://github.com/Yashvardhansharma112/superstore-data-analysis/tree/main
cd superstore-data-analysis
Create a virtual environment


python -m venv .venv
source .venv/bin/activate    # Mac/Linux
.venv\Scripts\activate       # Windows
Install required packages
(Adjust if requirements.txt is available)


pip install pandas numpy matplotlib seaborn
🚀 Usage
Run Analysis Script


python main.py
View Jupyter Notebook


jupyter notebook superstore_cleaning.ipynb
Open Power BI Dashboard

Open Super Store Dashboard. pbix in Power BI Desktop

📊 Dashboard Insights
The Power BI Dashboard provides:

Sales & Profit trends over time

Top-performing product categories

Regional performance breakdown

Customer segmentation analysis

📌 Dataset
The dataset (superstore.csv) contains:

Order Details: Order ID, Order Date, Ship Date

Customer Information

Product Details

Sales & Profit Figures

Geographic Information

📜 License
This project is licensed under the MIT License.
