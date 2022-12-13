import os

from datetime import date

def save_file(file, filename, directory_path):
    
    today = date.today()
    today = today.strftime("%Y-%m-%d")
    
    filename = filename + '_{}.csv'.format(today)
    
    directory_exists = os.path.exists(directory_path)
    
    if not directory_exists:
        print("Creating Directory...")
        os.makedirs(directory_path)
    
    print("Saving File...")  

    filepath = directory_path + filename 
    
    file.to_csv(filepath, index=False)
        
    print("File Saved:", filename)
    print("Saved In:", filepath)