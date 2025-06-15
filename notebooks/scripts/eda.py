import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs('../figures', exist_ok=True)
df = pd.read_csv('../insurance_data.txt', sep='|', nrows=100000)
df['TotalPremium'] = pd.to_numeric(df['TotalPremium'], errors='coerce')
df['TotalClaims'] = pd.to_numeric(df['TotalClaims'], errors='coerce')
df['Province'] = df['Province'].astype('str')
print("Columns:", df.columns.tolist())
print("Data Types:\n", df.dtypes)
print("Missing Values:\n", df.isnull().sum())
print("Descriptive Statistics:\n", df[['TotalPremium', 'TotalClaims']].describe())

df['LossRatio'] = df['TotalClaims'] / df['TotalPremium'].replace(0, float('nan')).fillna(0)
print("Overall Loss Ratio:", df['LossRatio'].mean())
print(df.groupby('Province')['LossRatio'].mean())

plt.figure(figsize=(8, 6))
sns.histplot(df['TotalPremium'].dropna(), bins=30)
plt.title('Distribution of Total Premium')
plt.savefig('../figures/total_premium_histogram.png')
plt.close()

plt.figure(figsize=(8, 6))
sns.countplot(x=df['Gender'])
plt.title('Gender Distribution')
plt.savefig('../figures/gender_distribution.png')
plt.close()