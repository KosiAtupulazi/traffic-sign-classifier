import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# Dataset and output details
dataset_name = "mbornoe/lisa-traffic-light-dataset"
zip_file = "lisa-traffic-light-dataset.zip"
extract_dir = "lisa_dataset"

# Initialize and authenticate
api = KaggleApi()
api.authenticate()

# Download if the zip doesn't exist
if not os.path.exists(zip_file):
    print("📥 Downloading dataset...")
    api.dataset_download_files(dataset_name, path=".", quiet=False)
else:
    print("✅ Zip file already exists.")

# Extract if the dataset folder doesn't exist
if not os.path.exists(extract_dir):
    print("📦 Extracting dataset...")
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(extract_dir)
    print("✅ Extracted to:", extract_dir)
else:
    print("✅ Dataset folder already exists.")
