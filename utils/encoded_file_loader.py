import os

def load_encoded_file(exam, datatype, filename):
    # Build the path to the encoded file
    file_path = os.path.join("EncodedFiles", exam, datatype, filename)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ Encoded file not found: {file_path}")
    
    with open(file_path, "r") as file:
        return file.read()
