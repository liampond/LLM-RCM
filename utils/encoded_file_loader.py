import os

def load_encoded_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Encoded file not found: {file_path}")
    
    with open(file_path, "r") as file:
        return file.read()
