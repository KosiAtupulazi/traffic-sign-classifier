import pandas as pd
import os
import pathlib
import shutil

gtrsb_csv_path = "/home/atupulazi/personal_projects/traffic-sign-classifier-1/datasets/gtrsb_dataset/Train_stop_yield_only.csv"
gtrsb_image_path = "/home/atupulazi/personal_projects/traffic-sign-classifier-1/raw_dataset/images"
output_img_dir = "/home/atupulazi/personal_projects/traffic-sign-classifier-1/processed_dataset/images/raw_images"
output_label_dir = "/home/atupulazi/personal_projects/traffic-sign-classifier-1/processed_dataset/yolo_labels/raw_labels"

class_map = {
    14: 0, 
    13: 1
}

df = pd.read_csv(gtrsb_csv_path)

for _, row in df.iterrows():
    class_id = class_map[row["ClassId"]]
    xmin = int(row["Roi.X1"])
    xmax = int(row["Roi.X2"])
    ymin = int(row["Roi.Y1"])
    ymax = int(row["Roi.Y2"])
    width = int(row["Width"])
    height = int(row["Height"])

    image_name = os.path.basename(row["Path"])
    image_path = os.path.join(gtrsb_image_path, image_name)
    image_stem = pathlib.Path(image_name).stem # gets just the image name without the .png

    # xcenter and ycenter defines a center point of the box
    #box width and height is how big the box around the point is
    x_center = ((xmin + xmax)/2) / width
    y_center = ((ymin + ymax)/2) / height
    box_width = (xmax - xmin) / width
    box_height = (ymax - ymin) / height

    label_path = os.path.join(output_label_dir, f"{image_stem}.txt")
    with open(label_path, "w") as f:
        f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}\n")
    
    shutil.copy(image_path, os.path.join(output_img_dir, image_name))


