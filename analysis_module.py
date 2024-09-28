import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def impute_missing_values(df):

    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    object_cols = df.select_dtypes(include=['object']).columns


    numeric_means = df[numeric_cols].mean()


    object_modes = {}
    for col in object_cols:
        if df[col].isnull().any():
            object_modes[col] = df[col].mode()[0]


    fill_values = {**numeric_means.to_dict(), **object_modes}


    df.fillna(value=fill_values, inplace=True)

    return df




def load_weather_data(file_path):
    data = pd.read_csv(file_path)

    data=impute_missing_values(data)
    return data


def basic_statistics(data):
    a=data.describe()
    le = LabelEncoder()

    object_cols = data.select_dtypes(include=['object']).columns
    for i in data[object_cols]:
        data[i] = le.fit_transform(data[i])
    stats = {
        'describe': a,
        'correlation': data.corr()
    }
    return stats


def handle_outliers(data):
    for col in data.select_dtypes(include=[np.number]).columns:
        upper_limit = data[col].quantile(0.95)
        data[col] = np.where(data[col] > upper_limit, upper_limit, data[col])
    return data


def write_analysis_results(stats, file_path):
    with open(file_path, 'w') as file:
        file.write("Weather Data Analysis Results:\n")
        for key, value in stats.items():
            file.write(f"\n{key}:\n{value}\n")
