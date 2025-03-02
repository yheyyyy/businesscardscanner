import os
import ollama
import json
from extraction_model import process_data

def vision_model(image_path):
    """
    This function uses the llama3.2-vision:11b model to extract the name card information from the image.
    It takes an image path and returns the name card information in a JSON format.

    Parameters
    ----------
    image_path : str
        The path to the image file.

    Returns
    -------
    response : str
        The name card information in a JSON format.
    """

    prompt = """Return the name card information in the following format:
    "Name": "", "Job Title": "", "Company":"", "Contact Number":"", "Email Address":"", "Website":"", "Address": ""
    Keep it to a JSON format and do not output other information, separate any information with a comma.
    """

    if os.path.exists(image_path):
        response = ollama.chat(
            model="llama3.2-vision:11b",
            messages=[{
            "role": "user",
            "content": prompt,
            "images": [image_path],

        }]
    )
        return response['message']['content'].strip()
    else:
        print(f"Image {image_path} does not exist")
        return None

def image_to_json(image_path):
    """
    This function converts an image to a JSON format.
    It takes an image and returns the JSON format of the image.

    Parameters
    ----------
    image : str
        The image to be converted to JSON format.

    Returns
    -------
    json_data : str
        The JSON format of the image.
    """
    single_img_data = vision_model(image_path)
    if single_img_data:
        cleaned_data = process_data(single_img_data)
        return json.loads(cleaned_data)
    else:
        print(f"Image {image_path} does not exist")
        return None