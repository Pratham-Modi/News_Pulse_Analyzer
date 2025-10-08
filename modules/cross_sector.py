import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def compute_category_correlation(trends_df, date_column="published_at", category_column="category", metric_column="article_count"):
    """
    Compute correlation matrix between categories based on article counts or sentiment.

    Parameters:
        trends_df (pd.DataFrame): DataFrame containing trends data.
        date_column (str): Column representing date.
        category_column (str): Column name representing categories/topics.
        metric_column (str): Column representing metric to correlate (article_count or sentiment score).

    Returns:
        pd.DataFrame: Correlation matrix of categories.
    """
    # Pivot data: rows = date, columns = category, values = metric
    pivot_df = trends_df.pivot_table(index=date_column, columns=category_column, values=metric_column, fill_value=0)

    # Compute correlation matrix
    corr_matrix = pivot_df.corr()
    return corr_matrix

def plot_correlation_heatmap(corr_matrix, title="Category Correlation Heatmap"):
    """
    Plot a heatmap of the correlation matrix.

    Parameters:
        corr_matrix (pd.DataFrame): Correlation matrix of categories.
        title (str): Plot title.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title(title)
    plt.tight_layout()
    plt.show()
