import pandas as pd

# Load the full CSV
csv_path = "/home/atupulazi/personal_projects/traffic-sign-classifier/gtsrb_filtered/Train.csv"
df = pd.read_csv(csv_path)

# Filter only ClassId 13 (Yield) and 14 (Stop)
filtered_df = df[df['ClassId'].isin([13, 14])]

# Save the cleaned CSV
filtered_df.to_csv("Train_stop_yield_only.csv", index=False)

print(f"Saved filtered CSV with only Stop and Yield signs to 'Train_stop_yield_only.csv'")
