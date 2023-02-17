import zipfile

# Name of the zip file you want to extract
zip_file = 'horizaura-master.zip'

# Open the zip file in read mode
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    # Extract all files to the current directory
    zip_ref.extractall('.')
