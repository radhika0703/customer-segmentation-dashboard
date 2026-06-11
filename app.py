import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="🛒",
    layout="wide"
)

# -----------------------
# LOAD DATA
# -----------------------
@st.cache_data
def load_data():
    df = pd.read_csv(
        "data/marketing_campaign.csv",
        sep="\t"
    )
    return df

df = load_data()

# -----------------------
# DATA CLEANING
# -----------------------
df = df.dropna()

df["Total_Spending"] = (
    df["MntWines"]
    + df["MntFruits"]
    + df["MntMeatProducts"]
    + df["MntFishProducts"]
    + df["MntSweetProducts"]
    + df["MntGoldProds"]
)

# -----------------------
# SIDEBAR
# -----------------------
st.sidebar.title("Dashboard Controls")

n_clusters = st.sidebar.slider(
    "Number of Clusters",
    2,
    8,
    4
)

# -----------------------
# CLUSTERING
# -----------------------
features = [
    "Income",
    "Recency",
    "NumWebPurchases",
    "NumCatalogPurchases",
    "NumStorePurchases",
    "Total_Spending"
]

X = df[features]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(
    n_clusters=n_clusters,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

# -----------------------
# TITLE
# -----------------------
st.title("🛒 Customer Segmentation Dashboard")

st.markdown("""
This dashboard segments customers based on purchasing behavior
and demographics using K-Means Clustering.
""")

# -----------------------
# KPI CARDS
# -----------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Customers",
    len(df)
)

col2.metric(
    "Average Income",
    f"${int(df['Income'].mean())}"
)

col3.metric(
    "Average Spending",
    f"${int(df['Total_Spending'].mean())}"
)

col4.metric(
    "Clusters",
    n_clusters
)

# -----------------------
# DATASET
# -----------------------
st.subheader("📊 Dataset Preview")

st.dataframe(df.head())

# -----------------------
# CLUSTER DISTRIBUTION
# -----------------------
st.subheader("Customer Distribution by Cluster")

cluster_counts = (
    df["Cluster"]
    .value_counts()
    .sort_index()
)

st.bar_chart(cluster_counts)

# -----------------------
# VISUALIZATION
# -----------------------
col1, col2 = st.columns(2)

with col1:

    st.subheader("Income vs Spending")

    fig, ax = plt.subplots(figsize=(6,4))

    sns.scatterplot(
        data=df,
        x="Income",
        y="Total_Spending",
        hue="Cluster",
        palette="Set2",
        ax=ax
    )

    st.pyplot(fig)

with col2:

    st.subheader("Web Purchases by Cluster")

    fig2, ax2 = plt.subplots(figsize=(6,4))

    sns.boxplot(
        data=df,
        x="Cluster",
        y="NumWebPurchases",
        ax=ax2
    )

    st.pyplot(fig2)

# -----------------------
# SEGMENT ANALYSIS
# -----------------------
st.subheader("📈 Segment Analysis")

summary = df.groupby("Cluster")[[
    "Income",
    "Total_Spending",
    "NumWebPurchases",
    "NumStorePurchases",
    "NumCatalogPurchases"
]].mean()

st.dataframe(summary)

# -----------------------
# SEGMENT FILTER
# -----------------------
st.subheader("🔍 Explore Segment")

selected_cluster = st.selectbox(
    "Select Cluster",
    sorted(df["Cluster"].unique())
)

filtered = df[df["Cluster"] == selected_cluster]

st.write(
    f"Customers in Cluster {selected_cluster}:",
    len(filtered)
)

st.dataframe(filtered.head(20))

# -----------------------
# INSIGHTS
# -----------------------
st.subheader("💡 Business Insights")

for cluster in sorted(df["Cluster"].unique()):

    temp = df[df["Cluster"] == cluster]

    st.info(
        f"""
        Cluster {cluster}

        Customers: {len(temp)}

        Avg Income: ${temp['Income'].mean():,.0f}

        Avg Spending: ${temp['Total_Spending'].mean():,.0f}
        """
    )

# -----------------------
# FOOTER
# -----------------------
st.markdown("---")

st.markdown(
    "Built with Python, Scikit-Learn and Streamlit 🚀"
)