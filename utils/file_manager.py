import os

def save_response(model_name, exam, datatype, filename, content):
    # Construct the full output directory
    output_dir = f"outputs/{model_name}/{exam}/{datatype}"
    
    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Save the response to the correct path
    with open(os.path.join(output_dir, filename), "w") as file:
        file.write(content)
