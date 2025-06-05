import os
import shutil
import random

# Source folders
stop_folder = "gtrsb_dataset/StopSign"
yield_folder = "gtrsb_dataset/YieldSign"

# Collect all image paths
image_files = []
for folder in [stop_folder, yield_folder]:
    for file in os.listdir(folder):
        if file.endswith(".png"):  # or .jpg
            image_files.append(os.path.join(folder, file))

# Shuffle and split 80/20
random.shuffle(image_files)
split = int(0.8 * len(image_files))
train_images = image_files[:split]
val_images = image_files[split:]

# Target folders
train_dir = "gtrsb_dataset/images/train"
val_dir = "gtrsb_dataset/images/val"

os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Copy images
for img in train_images:
    shutil.copy(img, os.path.join(train_dir, os.path.basename(img)))

for img in val_images:
    shutil.copy(img, os.path.join(val_dir, os.path.basename(img)))

print(f"✅ Done! {len(train_images)} images in train/, {len(val_images)} in val/")
