import os
import shutil

reports_dir = "Reports"

# Step 1: Create reports folder if not exists
if not os.path.exists(reports_dir):
    os.mkdir(reports_dir)
    print(f"Directory is Created: {reports_dir}")
else:
    print(f"Directory is exists: {reports_dir}")

# Step 2: List all .txt files in current directory
txt_files = [f for f in os.listdir() if f.endswith(".txt") and os.path.isfile(f)]
print("Text files found:", txt_files)
# Step 3: Process each file
for file in txt_files:
    print(f"Processing: {file}")
    shutil.move(file, os.path.join(reports_dir, file))
    print(f"Appended {file} to {reports_dir}")