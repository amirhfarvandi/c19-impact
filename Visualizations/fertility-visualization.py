import matplotlib.pyplot as plt
import csv

def load_data(file_path):
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            year = int(row['Year'])
            data[year] = {key: float(value) for key, value in row.items() if key != 'Year'}
    return data
def compare_original_and_interpolated(data_original, data_interpolated, age_group, start, end):
    """Compare original and interpolated data for a specific age group."""
    years = list(range(start, end + 1))
    
    # Extract data for original and interpolated scenarios
    original_values = [data_original[year][age_group] for year in years]
    interpolated_values = [data_interpolated.get(year, {}).get(age_group, data_original[year][age_group]) for year in years]
    
    # Plot data
    plt.figure(figsize=(10, 6), facecolor="#D6E1F1")
    ax = plt.gca()  # Get current axes
    ax.set_facecolor("#D6E1F1")
    plt.plot(years, original_values, label="Original Data", marker='o', linestyle='--', color='blue', alpha=0.7)
    plt.plot(years, interpolated_values, label="Interpolated Data", marker='x', linestyle='-', color='red', alpha=0.9)
    
    # Fill the area between the two curves
    plt.fill_between(
        years, original_values, interpolated_values, 
        color="#ACB5F4", alpha=0.5, label="Difference Area"
    )

    # Customize the plot
    plt.title(f"Comparison of Fertility Rates for Age Group {age_group} (Years {start}-{end})", fontsize=16)
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Mortality Rate", fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(alpha=0.4)
    plt.tight_layout()
    
    # Show plot
    plt.show()



idata = load_data('Interpolations/interpolated-fertility.csv')
odata = load_data('Data/fertility.csv')
compare_original_and_interpolated(odata, idata, age_group="0-14", start=2010, end=2030)
