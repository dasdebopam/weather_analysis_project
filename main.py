import configparser
import logging
import os
from analysis_module import load_weather_data, basic_statistics, handle_outliers, write_analysis_results
from forecast_generator import forecast_weather, save_forecast_results

# Read configuration settings
config = configparser.ConfigParser()
config.read('D:\Courses\Experiments\PycharmProjects\weather_analysis_project\config.ini')  # Adjust path as necessary

# Extract configuration values
historical_data = config['Settings']['historical_data']
log_file = config['Settings']['log_file']
output_analysis_file = config['Settings']['output_analysis_file']
output_forecast_file = config['Settings']['output_forecast_file']

# Ensure the log directory exists
os.makedirs(os.path.dirname(log_file), exist_ok=True)

# Configure logging
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('Logging is configured successfully.')

# Step 1: Load the historical weather data
data = load_weather_data(historical_data)
logging.info("Loaded historical weather data.")

# Step 2: Handle outliers
data = handle_outliers(data)
logging.info("Outliers handled.")

# Step 3: Calculate basic statistics
statistics = basic_statistics(data)
logging.info(f"Calculated basic statistics: {statistics}")

# Step 4: Write analysis results to a file
write_analysis_results(statistics, output_analysis_file)
logging.info(f"Analysis results saved to {output_analysis_file}")

# Step 5: Perform forecasting for the next 7 days
forecast = forecast_weather(data, forecast_period=7)
save_forecast_results(forecast, output_forecast_file)
logging.info(f"Weather forecast saved to {output_forecast_file}")
