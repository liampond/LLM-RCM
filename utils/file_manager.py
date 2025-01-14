import os

def save_response(model_name, filename, response):
    output_dir = f"outputs/{model_name}"
    os.makedirs(output_dir, exist_ok=True)
    
    with open(os.path.join(output_dir, filename), "w") as file:
        file.write(response)