import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def page2():
    st.title("Government-to-Government Debt Analysis")

    # Data Preparation
    gov_data = pd.DataFrame({
        'Government': ['PMLN', 'PTI', 'PDM'],
        'Start Debt (Trillions)': [14.00, 24.73, 43.07],
        'End Debt (Trillions)': [23.77, 43.66, 63.80],
        'Percent Increase': [69, 78, 56.19]
    })

    # Line Plot for Debt Over Time
    st.subheader('Debt Over Time for Different Governments')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=gov_data, x='Government', y='End Debt (Trillions)', marker='o', color='blue', ax=ax)
    ax.set_title('Debt at End of Term for Different Governments', fontsize=16)
    ax.set_xlabel('Government', fontsize=14)
    ax.set_ylabel('Debt in Trillions (PKR)', fontsize=14)
    ax.grid(True)
    st.pyplot(fig)

    # Bar Plot for Debt Increase
    st.subheader('Bar Plot of Debt Increase by Government')
    fig, ax = plt.subplots(figsize=(12, 7))
    sns.barplot(data=gov_data, x='Government', y='Percent Increase', palette='viridis', ax=ax)
    ax.set_title('Debt Increase Percentage by Government', fontsize=16)
    ax.set_xlabel('Government', fontsize=14)
    ax.set_ylabel('Percentage Increase (%)', fontsize=14)
    st.pyplot(fig)

    # Pie Chart for Debt Distribution by Government
    st.subheader('Pie Chart of Debt Distribution by Government')
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(gov_data['End Debt (Trillions)'], labels=gov_data['Government'], autopct='%1.1f%%', startangle=140,
           colors=sns.color_palette('coolwarm', len(gov_data)))
    ax.set_title('Distribution of End Debt by Government', fontsize=18)
    st.pyplot(fig)

    # Scatter Plot for Start vs End Debt
    st.subheader('Scatter Plot of Start vs End Debt')
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=gov_data, x='Start Debt (Trillions)', y='End Debt (Trillions)', hue='Government',
                    palette='Set1', s=100, ax=ax)
    ax.set_title('Start vs End Debt for Different Governments', fontsize=16)
    ax.set_xlabel('Start Debt (Trillions)', fontsize=14)
    ax.set_ylabel('End Debt (Trillions)', fontsize=14)
    st.pyplot(fig)


page2()
