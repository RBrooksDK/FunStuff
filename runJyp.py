import os
import datetime

# Set the path to your Jupyter Notebook
notebook_path = 'C:/Users/Richard/OneDrive - ViaUC/Arbejde/GitHub/FunStuff/football.ipynb'

# Set the path to your log file
log_file_path = 'C:/Users/Richard/OneDrive - ViaUC/Arbejde/GitHub/FunStuff/log.txt'

# Get the current date and time
now = datetime.datetime.now()

# Run the Jupyter Notebook
os.system(f'jupyter nbconvert --execute --inplace --to notebook "{notebook_path}" >> "{log_file_path}" 2>&1')
