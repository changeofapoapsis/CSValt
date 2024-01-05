import csv

def find_greatest_height(~/Users/Account/Library/Downloads/drone_events_exported.csv):
    # Initialize variables to store the maximum height and corresponding row
    max_height = float('-inf')
    max_height_row = None

    # Read the CSV file
    with open(~/Users/Account/Library/Downloads/drone_events_exported.csv, 'r') as csv_file:
        csv_reader = csv.DictReader(drone_events_exported.csv)
        
        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Extract the relevant columns
            begin_position = int(row['detection begin position'])
            height = float(row['height'])

            # Check if the current height is greater than the maximum height
            if height > max_height:
                max_height = height
                max_height_row = row

    return max_height_row

# Example usage:
~/Users/Account/Library/Downloads/drone_events_exported.csv = 'drone_events_exported.csv'  # Replace with the actual path to your CSV file
result_row = find_greatest_height(~/Users/Account/Library/Downloads/drone_events_exported.csv)

if result_row:
    print(f"The greatest height is {result_row['height']} at detection begin position {result_row['detection begin position']}.")
else:
    print("No data found.")

