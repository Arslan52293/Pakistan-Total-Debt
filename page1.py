import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def page1():
    st.title("Pakistan Debt Analysis (2011-2024)")

    # Data Preparation
    years = np.arange(2011, 2025)
    debt = [9.256, 11.34, 13.06, 15.51, 16.40, 18.17, 19.88, 22.69, 27.07, 32.99, 36.47, 42.39, 54.94, 64.84]
    percent_change = [None, 21.03, 15.22, 18.57, 5.56, 10.88, 9.04, 14.14, 19.28, 21.92, 10.69, 16.27, 29.80, 18.19]

    data = pd.DataFrame({
        'Year': years,
        'Debt (Trillions)': debt,
        'Percent Change': percent_change
    })

    # Line Plot
    st.subheader('Line Plot of Debt Over Time')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='Year', y='Debt (Trillions)', data=data, marker='o', color='blue', ax=ax)
    ax.set_title('Pakistan Total Debt (2011-2024)', fontsize=16)
    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Debt in Trillions (PKR)', fontsize=14)
    ax.grid(True)
    st.pyplot(fig)

    # Bar Plot
    st.subheader('Bar Plot of Debt with Percentage Change')
    fig, ax = plt.subplots(figsize=(12, 7))
    sns.barplot(x='Year', y='Debt (Trillions)', data=data, palette='viridis', ax=ax)
    for i in range(len(data)):
        ax.text(i, data['Debt (Trillions)'][i] + 0.5, f"{data['Percent Change'][i]}%", ha='center', fontsize=10)
    ax.set_title('Pakistan Total Debt and Annual Percentage Change (2011-2024)', fontsize=16)
    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Debt in Trillions (PKR)', fontsize=14)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

    # Scatter Plot with Regression Line
    st.subheader('Scatter Plot with Regression Line')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.regplot(x='Year', y='Debt (Trillions)', data=data, marker='o', color='red', scatter_kws={'s': 100},
                line_kws={'color': 'green'}, ax=ax)
    ax.set_title('Regression Analysis of Pakistan Total Debt (2011-2024)', fontsize=16)
    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Debt in Trillions (PKR)', fontsize=14)
    ax.grid(True)
    st.pyplot(fig)

    # Heatmap
    st.subheader('Heatmap of Debt Growth')
    fig, ax = plt.subplots(figsize=(14, 8))  # Larger figure size
    debt_growth = np.array(debt).reshape(-1, 1)  # Reshaping the data for the heatmap
    sns.heatmap(debt_growth, annot=True, cmap='YlGnBu', cbar=True, fmt='.2f', linewidths=1, annot_kws={"size": 14},
                ax=ax)
    ax.set_title('Heatmap of Pakistan Total Debt (2011-2024)', fontsize=20)
    ax.set_yticks(np.arange(len(years)) + 0.5)
    ax.set_yticklabels(years, fontsize=12)
    ax.set_xticks([])
    st.pyplot(fig)

    # Pie Chart
    st.subheader('Pie Chart of Debt Distribution')
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(debt, labels=years, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('coolwarm', len(debt)))
    ax.set_title('Distribution of Pakistan\'s Total Debt (2011-2024)', fontsize=18)
    st.pyplot(fig)


page1()
