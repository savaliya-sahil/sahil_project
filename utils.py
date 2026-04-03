def load_data(filepath):
    """
    Load data from a specified filepath.
    
    Parameters:
    filepath (str): The path to the data file.
    
    Returns:
    DataFrame: Loaded data as a pandas DataFrame.
    """
    import pandas as pd
    return pd.read_csv(filepath)


def visualize_data(data):
    """
    Visualize the provided data.
    
    Parameters:
    data (DataFrame): The data to visualize.
    """
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.set(style='whitegrid')
    plt.figure(figsize=(10, 6))
    sns.countplot(data['Attrition'])
    plt.title('Attrition Count')
    plt.xlabel('Attrition')
    plt.ylabel('Count')
    plt.show()


def calculate_metrics(data):
    """
    Calculate and return various metrics related to attrition.
    
    Parameters:
    data (DataFrame): The data for metrics calculation.
    
    Returns:
    dict: A dictionary containing metrics.
    """
    total = len(data)
    attrition_rate = data['Attrition'].value_counts(normalize=True).get('Yes', 0)

    return {
        'Total Employees': total,
        'Attrition Rate': attrition_rate * 100,
    }


def categorize_risk(data):
    """
    Categorize employees into risk categories based on features.
    
    Parameters:
    data (DataFrame): The data to analyze.
    
    Returns:
    DataFrame: Updated DataFrame with risk categories.
    """
    conditions = [
        (data['MonthlyIncome'] < 3000),
        (data['YearsAtCompany'] < 2),
    ]
    choices = ['High Risk', 'Medium Risk']
    data['Risk Category'] = np.select(conditions, choices, default='Low Risk')
    return data
