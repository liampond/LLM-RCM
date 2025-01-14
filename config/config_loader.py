import os
from config.settings import EXTENSION_MAP

# Load dynamic runtime configurations
def load_runtime_config():
    return {
        "EXAM": os.getenv("EXAM", "RCM6"),
        "CONTEXT": os.getenv("CONTEXT", "NoContext"),
        "DATATYPE": os.getenv("DATATYPE", "MEI"),
        "QUESTION": os.getenv("QUESTION", "Q1a"),
        "YEAR": os.getenv("YEAR", "August2024"),
    }

# Build the encoded filename dynamically based on the current configuration
def build_encoded_filename(config):
    extension = EXTENSION_MAP.get(config["DATATYPE"], ".txt")
    return f"{config['EXAM']}_{config['YEAR']}_{config['QUESTION']}{extension}"

# Check if the encoded file exists in the correct path
def check_encoded_file_exists(config):
    encoded_file_path = os.path.join("EncodedFiles", config["EXAM"], config["DATATYPE"], build_encoded_filename(config))
    if not os.path.exists(encoded_file_path):
        print(f"❌ Encoded file not found: {encoded_file_path}")
        return False
    return True
