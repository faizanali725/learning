import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Personal Finance Dashboard",layout="wide")
st.title("Personal Finance Dashboard 💰")
st.write("Upload your expense CSV file to analyze your spending habits.")


# ----------> Sidebar

st.sidebar.header("Upload Your Data")
file_uploaded = st.sidebar.file_uploader("Upload Expense CVS",type=["csv"])

if file_uploaded is not None:
    df = pd.read_csv(file_uploaded)

    # ------------> Convert Date Type

    df["Date"] = pd.to_datetime(df["Date"])

    # ---------> Sidebar Filters

    st.sidebar.header("Filters")

    category_filter = st.sidebar.multiselect(
        "Select Category",
        options = df["Category"].unique(),
        default = df["Category"].unique()
    )

    payment_filter = st.sidebar.multiselect(
        "Payment Mode",
        options = df["Payment_Mode"].unique(),
        default = df["Payment_Mode"].unique()
    )

    filtered_df = df[
        (df["Category"].isin(category_filter)) &
        (df["Payment_Mode"].isin(payment_filter))
    ]

    # -------------> Top Metrics

    total_spent = filtered_df["Amount"].sum()
    avg_spent = filtered_df["Amount"].mean()
    max_spent = filtered_df["Amount"].max()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Spending",f"Rs.{total_spent:,.2f}")
    col2.metric("Average Spending",f"Rs.{avg_spent:,.2f}")    
    col3.metric("Highest Expense",f"Rs.{max_spent:,.2f}")

    st.divider()

    # ---------> Category Analysis

    st.subheader("💲 Spending by Category")

    category_data = filtered_df.groupby("Category")["Amount"].sum()
    fig1, ax1 = plt.subplots(figsize= (5, 3))
    category_data.plot(kind= "bar", ax= ax1)
    ax1.set_ylabel("Amount Spent")
    ax1.set_xlabel("Category")

    st.pyplot(fig1, use_container_width=False)

    st.divider()

    # ------------> Monthly Trend

    st.subheader("💹 Monthly Spending Trend")

    filtered_df["Month"] = filtered_df["Date"].dt.to_period("M")
    monthly_data = filtered_df.groupby("Month")["Amount"].sum()

    fig2, ax2 = plt.subplots(figsize = (5, 3))
    monthly_data.plot(kind="line", marker= "o", ax=ax2)
    ax2.set_ylabel("Amount Spent")
    ax2.set_xlabel("Month")

    st.pyplot(fig2, use_container_width=False)

    st.divider()

    # ------------> Raw Data

    st.subheader("📊 Transaction Data")
    st.dataframe(filtered_df)


else:
    st.info("Please upload CSV file to begin analysis")


