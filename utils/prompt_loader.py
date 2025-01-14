import os

def load_prompt(file_path):
    with open(file_path, "r") as file:
        return file.read()