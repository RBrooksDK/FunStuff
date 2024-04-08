import requests
import pandas as pd
from io import BytesIO
import numpy as np
import pickle

# Function to apply to each cell
def convert_cell(cell):
    if pd.isnull(cell):  # Check if the cell is NaN
        return ' '  # Replace NaN with a space
    elif isinstance(cell, (int, float)):  # Check if the cell is a number
        return int(cell)  # Convert numbers to integers
    return cell  # Leave any other values unchanged

def main():
    # Direct download link for the Google Drive file
    direct_link = 'https://drive.google.com/uc?export=download&id=1OV_SnmOufEOhH2kSRHjd_gZYgEeKO9G8'

    response = requests.get(direct_link)
    if response.status_code == 200:
        # The content is an Excel file, so we use BytesIO to handle it
        excel_data = BytesIO(response.content)
        # Read all sheets into a dictionary of DataFrames
        dfs = pd.read_excel(excel_data, sheet_name=None)

        # Mapping of original sheet names to new names
        name_mapping = {
            'League_119': 'Superligaen',
            'League_39': 'Premier League',
            'League_140': 'La Liga',
            'League_135': 'Serie A',
            'League_78': 'Bundesliga'
        }

        # Create a new dictionary to store the adjusted DataFrames
        new_dfs = {}

        # Iterate over the dictionary and adjust each DataFrame
        for sheet_name in list(dfs.keys()):  # Use list(dfs.keys()) to safely iterate
            df = dfs[sheet_name]
            # Apply the function to each cell in the DataFrame
            df = df.applymap(convert_cell)

            # Use the mapping to get the new name, or default to the original name if not found in the mapping
            new_name = name_mapping.get(sheet_name, sheet_name)

            # Adjust row index to start at 1
            df.index = range(1, len(df) + 1)

            # Add the adjusted DataFrame to the new dictionary
            new_dfs[new_name] = df

        # Save the processed DataFrames to a pickle file
        with open('processed_data.pkl', 'wb') as f:
            pickle.dump(new_dfs, f)

    else:
        print("Failed to download the file.")

if __name__ == "__main__":
    main()
