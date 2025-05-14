python
import pandas as pd

# Load the dataset
file_path = 'OpenData_Publishers_2025_05 (1)_2_20.xlsx'
df = pd.read_excel(file_path)

# Display the first few rows of the dataset
df_head = df.head()
print(df_head)

# Example: Filter contacts by a specific government entity
def filter_contacts_by_entity(entity_name):
    filtered_data = df[df['Entity Name'] == entity_name]
    return filtered_data

# Use the function to get contacts for 'Department of Community Development'
entity_contacts = filter_contacts_by_entity('Department of Community Development')
print(entity_contacts)
