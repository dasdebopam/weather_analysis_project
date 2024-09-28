import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def forecast_weather(data, forecast_period=7):
    columns_to_forecast = ['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation', 'Sunshine', 'WindGustSpeed', 'WindSpeed9am',
                           'WindSpeed3pm',
                           'Humidity9am', 'Humidity3pm',
                           'Pressure9am', 'Pressure3pm',
                           'Cloud9am', 'Cloud3pm',
                           'Temp9am', 'Temp3pm',
                           'RISK_MM']  # List of columns to forecast
    forecasts = {}

    for column in columns_to_forecast:
        model = ExponentialSmoothing(data[column], trend='add', seasonal='add', seasonal_periods=12)
        model_fit = model.fit()
        forecasts[column] = model_fit.forecast(forecast_period)
    forecasts=pd.DataFrame.from_dict(forecasts)
    return forecasts



def save_forecast_results(forecast, file_path):
    forecast.to_csv(file_path, header=True)
