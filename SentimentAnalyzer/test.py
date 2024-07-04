import os
import chardet

csv_file_path = 'C:\\Users\\cu16b\\Downloads\\Pre-Processing\\merger.csv'
if os.path.exists(csv_file_path):
    print("File exists")
else:
    print("File does not exist")

with open(csv_file_path, 'rb') as f:
    result = chardet.detect(f.read(10000))  # Read the first 10000 bytes
    print(result)