# 🛒 Customer Segmentation Dashboard

## 📌 Project Overview

Customer Segmentation is a data-driven approach used to group customers with similar characteristics and purchasing behaviors. This project leverages Machine Learning (K-Means Clustering) to identify distinct customer segments and provide actionable insights for targeted marketing strategies.

The dashboard is built using Streamlit and allows users to explore customer groups, analyze spending patterns, and understand customer behavior through interactive visualizations.

---

## 🎯 Objectives

- Segment customers based on demographics and purchasing behavior.
- Identify high-value and low-value customer groups.
- Analyze customer spending habits and preferences.
- Generate insights for personalized marketing campaigns.

---

## 📊 Dataset

The project uses the **Customer Personality Analysis Dataset**, which contains customer demographic information and purchasing behavior.

### Key Features Used

- Income
- Recency
- Number of Web Purchases
- Number of Catalog Purchases
- Number of Store Purchases
- Total Spending

### Feature Engineering

A new feature called **Total_Spending** is created by combining:

- MntWines
- MntFruits
- MntMeatProducts
- MntFishProducts
- MntSweetProducts
- MntGoldProds

---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Streamlit

---

## 🧠 Machine Learning Approach

### Data Preprocessing

- Missing value handling
- Feature selection
- Feature scaling using StandardScaler

### Clustering Algorithm

**K-Means Clustering**

The algorithm groups customers into clusters based on similarities in:

- Spending behavior
- Purchase frequency
- Income levels

---

## 📈 Dashboard Features

### Customer Overview

- Total Customers
- Average Income
- Average Spending
- Number of Customer Segments

### Interactive Visualizations

- Customer Distribution by Cluster
- Income vs Spending Analysis
- Purchase Behavior Analysis
- Cluster-wise Customer Insights

### Segment Exploration

Users can:
- Select a customer segment
- View segment characteristics
- Analyze customer behavior patterns

---

## 📷 Dashboard Preview

Add screenshots here after running the application.

### Home Dashboard

![Dashboard](images/dashboard.png)

### Customer Segments

![Clusters](images/clusters.png)

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/customer-segmentation-dashboard.git
```

### Navigate to Project Folder

```bash
cd customer-segmentation-dashboard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```text
customer-segmentation-dashboard/
│
├── Data/
│   └── marketing_campaign.csv
│
├── app.py
├── customer_segmentation.ipynb
├── requirements.txt
├── README.md
└── images/
```

---

## 📊 Business Insights

The clustering model helps businesses:

- Identify high-value customers
- Improve customer retention
- Design personalized marketing campaigns
- Increase customer engagement
- Optimize resource allocation

---

## 🔮 Future Enhancements

- Automatic cluster selection using Elbow Method
- Interactive Plotly visualizations
- Customer Persona Generation
- Downloadable segmentation reports
- Deployment on Streamlit Cloud

---

## 👩‍💻 Author

**Radhika Sharma**

Aspiring Data Analyst | Machine Learning Enthusiast | Python Developer

---

## ⭐ If you found this project useful, consider giving it a star!
