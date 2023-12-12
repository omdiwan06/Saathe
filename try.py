import pandas as pd

def order_csv_by_pairs(csv_file_path):
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(csv_file_path)
    
    # Define a custom sorting order based on pairs of 'avd_for' and 'type'
    custom_order = {
        ('Group', 'Complaint'): 0,
        ('Group', 'Request'): 3,
        ('Group', 'Suggestion'): 5,
        ('Individual', 'Complaint'): 1,
        ('Individual', 'Request'): 4,
        ('Individual', 'Suggestion'): 6,
        ('Other', 'Complaint'): 2,
        ('Other', 'Request'): 7,
        ('Other', 'Suggestion'): 8
    }
    
    # Create a new column to represent the combined pairs of 'avd_for' and 'type'
    data['pair_order'] = data.apply(lambda row: custom_order.get((row['avd_for'], row['type'])), axis=1)
    
    # Sort the DataFrame based on the 'pair_order' column
    sorted_data = data.sort_values(by='pair_order')
    
    # Drop the 'pair_order' column if it's no longer needed
    sorted_data = sorted_data.drop(columns=['pair_order'])
    
    sorted_data.to_csv('sorted_output.csv', index=False) 
    return sorted_data

# Replace 'your_csv_file.csv' with the actual path to your CSV file
sorted_csv_data = order_csv_by_pairs('details.csv')

# Display the sorted data
print(sorted_csv_data)

