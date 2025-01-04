import csv

def load_data(file_path):
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            year = int(row['Year'])
            data[year] = {key: float(value) for key, value in row.items() if key != 'Year'}
    return data

def interpolate_fertility(data, start, end, target_range):
    interpolated_data = {}
    for year in target_range:
        interpolated_data[year] = {}
        for age_group in data[start].keys():
            x1, x2 = start, end
            y1, y2 = data[start][age_group], data[end][age_group]
            # Linear interpolation formula
            interpolated_data[year][age_group] = y1 + (y2 - y1) * ((year - x1) / (x2 - x1))
    return interpolated_data
def write_to_csv(data, output_file):
    years = sorted(data.keys())
    age_groups = list(next(iter(data.values())).keys())
    
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Year'] + age_groups)
        # Write rows
        for year in years:
            row = [year] + [data[year][age_group] for age_group in age_groups]
            writer.writerow(row)

data = load_data('Data/fertility.csv')
interpolated_data = interpolate_fertility(data, start=2020, end=2025, target_range=range(2021, 2025))

for year, values in interpolated_data.items():
    data[year] = values


write_to_csv(data, 'Interpolations/interpolated-fertility.csv')