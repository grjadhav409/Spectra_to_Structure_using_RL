import zipfile

# specify the path of the zip file you want to extract
zip_file_path = '/config/workspace/DeepSPInNTraining (1).zip' 

# specify the path where you want to extract the zip file content
extract_path = '/config/workspace/extracted' 

# open the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # extract all files to the specified path
    zip_ref.extractall(extract_path)

