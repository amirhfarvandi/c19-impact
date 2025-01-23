import numpy as np
import csv

def load_data(file_path):
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            year = int(row['Year'])
            data[year] = {key: float(value) for key, value in row.items() if key != 'Year'}
    return data

def quantify_differences(data_original, data_interpolated, age_group, years):
    original_values = [data_original[year][age_group] for year in years]
    interpolated_values = [data_interpolated.get(year, {}).get(age_group, data_original[year][age_group]) for year in years]
    
    # Compute Error Metrics
    mae = np.mean(np.abs(np.array(original_values) - np.array(interpolated_values)))
    mse = np.mean((np.array(original_values) - np.array(interpolated_values)) ** 2)
    rmse = np.sqrt(mse)
    mape = np.mean(np.abs((np.array(original_values) - np.array(interpolated_values)) / np.array(original_values))) * 100
    
    # Compute Area Difference using trapz
    area_diff = np.trapz(np.abs(np.array(original_values) - np.array(interpolated_values)), x=years)
    
    return {
        "MAE": mae,
        "MSE": mse,
        "RMSE": rmse,
        "MAPE": mape,
        "Area Difference": area_diff
    }
def print_results(results):
    print("Quantification of Differences:")
    print(f"{'Metric':<20}{'Value':<10}")
    print("-" * 30)
    for metric, value in results.items():
        if metric == "MAPE":
            print(f"{metric:<20}{value:.2f}%")
        elif metric == "Area Difference":
            print(f"{metric:<20}{value:.3f} (units²)")
        else:
            print(f"{metric:<20}{value:.3f}")



# Specify years and age group for comparison
idata = load_data('Interpolations/male-interpolated-mortality.csv')
odata = load_data('Data/male-mortality.csv')
years_to_compare = range(2020, 2026)
results = quantify_differences(data_original=odata, data_interpolated=idata, age_group="80+", years=years_to_compare)
print_results(results)
