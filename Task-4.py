# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('expanded_dataset_500_entries.csv')

# Display the first few rows of the dataframe
print("First few rows of the dataset:")
print(df.head())

# Basic summary statistics
print("\nSummary statistics of the dataset:")
print(df.describe())

# Check for missing values
print("\nChecking for missing values:")
print(df.isnull().sum())

# Visualizing the distribution of variables

# Distribution of Age
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Distribution of Salary
plt.figure(figsize=(10, 6))
sns.histplot(df['Salary'], kde=True)
plt.title('Distribution of Salary')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# Distribution of Years of Experience
plt.figure(figsize=(10, 6))
sns.histplot(df['Years_of_Experience'], kde=True)
plt.title('Distribution of Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Frequency')
plt.show()

# Identifying outliers with box plots

# Box plot for Age
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Age'])
plt.title('Box Plot of Age')
plt.show()

# Box plot for Salary
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Salary'])
plt.title('Box Plot of Salary')
plt.show()

# Box plot for Years of Experience
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Years_of_Experience'])
plt.title('Box Plot of Years of Experience')
plt.show()

# Checking for correlations

# Correlation Matrix
corr_matrix = df.corr()

# Heatmap of the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# Scatter plot to check correlation between Salary and Years of Experience
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Years_of_Experience', y='Salary', data=df)
plt.title('Scatter Plot between Years of Experience and Salary')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Additional explorations

# Box plot for Salary across different Departments
plt.figure(figsize=(10, 6))
sns.boxplot(x='Department', y='Salary', data=df)
plt.title('Salary Distribution across Departments')
plt.show()

# Performance Score Distribution across Departments
plt.figure(figsize=(10, 6))
sns.countplot(x='Performance_Score', hue='Department', data=df)
plt.title('Performance Score Distribution across Departments')
plt.show()