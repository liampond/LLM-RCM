import os

def save_response(output_path, content, model):
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Extract filename and extension from the output path
    base_filename, extension = os.path.splitext(os.path.basename(output_path))
    directory = os.path.dirname(output_path)

    # Determine the version number
    version = 1
    new_filename = f"{base_filename}_V{version}{extension}"
    new_file_path = os.path.join(directory, new_filename)

    # Increment version number if file already exists
    while os.path.exists(new_file_path):
        version += 1
        new_filename = f"{base_filename}_V{version}{extension}"
        new_file_path = os.path.join(directory, new_filename)

    if model == "Claude":
        content = str(content)
        formatted_string = content.replace("type=text", "").replace("textblock", "")
        formatted_string = formatted_string.replace("\\n", "\n")
        formatted_string = formatted_string.strip()
        content = formatted_string

    # Save the response to the correct path
    with open(new_file_path, "w") as file:
        file.write(str(content))
