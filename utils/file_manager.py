import os

def save_response(model_name, exam, datatype, output_filename, output_path, content):
    # Create the directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Save the response to the correct path
    with open(os.path.join(output_path, output_filename), "w") as file:
        file.write(content)
