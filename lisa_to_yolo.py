import pandas as pd
import os
import pathlib
import shutil
import cv2

lisa_csv_path = "/home/atupulazi/personal_projects/traffic-sign-classifier-1/datasets/lisa_sample/combinedframeAnnotationsBULB.csv"
lisa_image_path = "/home/atupulazi/personal_projects/traffic-sign-classifier-1/raw_dataset/images"
output_img_dir = "/home/atupulazi/personal_projects/traffic-sign-classifier-1/processed_dataset/images/raw_images"
output_label_dir = "/home/atupulazi/personal_projects/traffic-sign-classifier-1/processed_dataset/yolo_labels/raw_labels"

class_map = {
    "go": 2,
    "stopLeft": 2,
    "stop": 3
    
}

df = pd.read_csv(lisa_csv_path)

for _, row in df.iterrows():
    if row["Annotation tag"] not in class_map:
        continue

    class_id = class_map[row["Annotation tag"]]
    Xmin = int(row["Upper left corner X"]) #left edge - left wall
    Xmax = int(row["Lower right corner X"]) #right edge - right wall
    Ymin = int(row["Upper left corner Y"]) #top edge - ceiling
    Ymax = int(row["Lower right corner Y"]) #bottom edge - floor

    image_name = os.path.basename(row["Filename"]) # get the file name
    image_path = os.path.join(lisa_image_path, image_name) #the actual image
    image_stem = pathlib.Path(image_name).stem # gets just the image name without the .png
    
    img = cv2.imread(image_path) #img is a numpy array of pixel values

    if img is None: #no pixel values in the arr so img doesnt exist
        continue

    height, width = img.shape[:2] # img.shape = (height, width, 3) → 3 is for the 3 color channels

    xcenter = ((Xmin + Xmax)/2) / width 
    ycenter = ((Ymax + Ymin)/2) / height
    box_height = (Ymax - Ymin )/ height # xmax - xmin
    box_width = (Xmax - Xmin)/ width #ymax - ymin

    label_path = os.path.join(output_label_dir, f"{image_stem}.txt")
    with open(label_path, "w") as f:
        f.write(f"{class_id} {xcenter:.6f} {ycenter:.6f} {box_width:.6f} {box_height:.6f}\n")
    
    shutil.copy(image_path, os.path.join(output_img_dir, image_name))
