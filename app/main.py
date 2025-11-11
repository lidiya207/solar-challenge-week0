import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Solar Data Dashboard", layout="wide")
st.title("Solar Data Dashboard")

# Load cleaned CSVs
benin = pd.read_csv(r"C:\Users\Lidiya Getale\Downloads\data\data\benin-malanville.csv")
sierra = pd.read_csv(r"C:\Users\Lidiya Getale\Downloads\data\data\sierraleone-bumbuna.csv")
togo = pd.read_csv(r"C:\Users\Lidiya Getale\Downloads\data\data\togo-dapaong_qc.csv")

# Sidebar: country selection
countries = st.multiselect("Select countries", ["Benin", "Sierra Leone", "Togo"], default=["Benin"])

# Sidebar: metric selection
metric = st.selectbox("Select metric", ["GHI", "DNI", "DHI"])

# Combine selected countries
dfs = []
if "Benin" in countries:
    dfs.append(benin.assign(Country="Benin"))
if "Sierra Leone" in countries:
    dfs.append(sierra.assign(Country="Sierra Leone"))
if "Togo" in countries:
    dfs.append(togo.assign(Country="Togo"))

if dfs:
    combined = pd.concat(dfs)

    st.subheader("Data Preview")
    st.dataframe(combined.head())

    st.subheader(f"{metric} Boxplot by Country")
    fig, ax = plt.subplots(figsize=(8,5))
    sns.boxplot(x="Country", y=metric, data=combined, ax=ax)
    st.pyplot(fig)

    st.subheader(f"{metric} Line Plot (First 100 Rows)")
    fig2, ax2 = plt.subplots(figsize=(10,5))
    for country in countries:
        subset = combined[combined["Country"]==country].head(100)
        ax2.plot(subset.index, subset[metric], label=country)
    ax2.set_xlabel("Index")
    ax2.set_ylabel(metric)
    ax2.legend()
    st.pyplot(fig2)
