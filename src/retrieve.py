import os

# data from https://www.sciencedirect.com/science/article/pii/S2352340920303048

# Download the zipped dataset
zip_name = "data.zip"


# Unzip it and standardize the .csv filename
import zipfile
with zipfile.ZipFile(zip_name,"r") as zip_ref:
    zip_ref.filelist[0].filename = 'data_raw.csv'
    zip_ref.extract(zip_ref.filelist[0])

os.remove(zip_name)