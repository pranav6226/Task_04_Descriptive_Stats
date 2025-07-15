import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

FILENAME = 'SocialMediaTop100.csv'

def main():
    df = pd.read_csv(FILENAME, encoding='ISO-8859-1')
    numeric_cols = df.select_dtypes(include='number').columns
    cat_cols = df.select_dtypes(include='object').columns

    # Histograms for numeric columns
    for col in numeric_cols:
        plt.figure()
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f'Histogram of {col}')
        plt.savefig(f'hist_{col}.png')
        plt.close()

    # Bar charts for categorical columns (top 10 values)
    for col in cat_cols:
        plt.figure(figsize=(10,4))
        df[col].value_counts().head(10).plot(kind='bar')
        plt.title(f'Top 10 {col}')
        plt.ylabel('Count')
        plt.savefig(f'bar_{col}.png')
        plt.close()

    # Boxplots for numeric columns by Platform
    for col in numeric_cols:
        plt.figure(figsize=(8,4))
        sns.boxplot(x='Platform', y=col, data=df)
        plt.title(f'Boxplot of {col} by Platform')
        plt.savefig(f'boxplot_{col}_by_platform.png')
        plt.close()

if __name__ == '__main__':
    main() 