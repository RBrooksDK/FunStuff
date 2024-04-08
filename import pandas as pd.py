import pandas as pd

# Specify the path to your Excel file
excel_file_path = 'C:/Users/Richard/OneDrive - ViaUC/Arbejde/GitHub/FunStuff/Football_Predictions_Results.xlsx'

# Load the Excel file
xls = pd.ExcelFile(excel_file_path)

# Loop through each sheet in the Excel file
for sheet_name in xls.sheet_names:
    # Load the sheet into a DataFrame
    df = xls.parse(sheet_name)
    
    # Specify the path and name for the CSV file you want to create
    # This example saves each CSV in a specific directory, with the sheet name as the file name
    #csv_file_path = f'C:/Users/Richard/OneDrive - ViaUC/Arbejde/GitHub/FunStuff/{sheet_name}.csv'
    
    # Save the DataFrame to CSV
    #df.to_csv(csv_file_path, index=False)  # Set index=False if you don't want the DataFrame index in your CSV

#print("CSV files have been created for each sheet.")
print(df)