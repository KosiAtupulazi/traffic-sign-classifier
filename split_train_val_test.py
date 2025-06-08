import os
import random
import shutil
from pathlib import Path

#split the dataset into train, val and test
# Set your raw image and label dirs 
image_dir = Path("/home/atupulazi/personal_projects/traffic-sign-classifier-1/processed_dataset/images/raw_images")
label_dir = Path("/home/atupulazi/personal_projects/traffic-sign-classifier-1/processed_dataset/yolo_labels/raw_labels")

# Where to move them
splits = ['train', 'val', 'test']
split_ratio = {
    'train': 0.7,
    'val': 0.2,
    'test': 0.1
}

# Get all image files
images = list(image_dir.glob("*.*"))
images = [img for img in images if img.suffix.lower() in [".jpg", ".jpeg", ".png"]]

random.shuffle(images)  # Shuffle so the splits are random

# How many per split
total = len(images)
train_end = int(split_ratio['train'] * total)
val_end = train_end + int(split_ratio['val'] * total)

# Assign to each split
split_data = {
    'train': images[:train_end],
    'val': images[train_end:val_end],
    'test': images[val_end:]
}

for split in splits:
    for subfolder in ['images', 'yolo_labels']:
        os.makedirs(f"clean_dataset/{subfolder}/{split}", exist_ok=True)

    for img_path in split_data[split]:
        label_path = label_dir / (img_path.stem + ".txt")

        shutil.copy(img_path, f"clean_dataset/images/{split}/{img_path.name}")
        shutil.copy(label_path, f"clean_dataset/yolo_labels/{split}/{label_path.name}")
