import os

import gradio as gr
import pandas as pd

from vision_model import image_to_json


def json_to_df(cleaned_data):
    if isinstance(cleaned_data, dict):
        cleaned_data = [cleaned_data]
    columns = ["Name", "Job Title", "Company", "Contact Number", "Email Address", "Website", "Address"]
    df = pd.DataFrame(cleaned_data, columns=columns)
    return df

def upload_and_process(images):
    """
    This function processes the uploaded images and converts them to Excel format.
    It takes a list of image files and returns the path to the updated Excel file.

    Parameters
    ----------
    images : list
        A list of image files to process.

    Returns
    -------
    excel_file_path : str
        The path to the updated Excel file.
    """
    excel_file_path = os.path.join(os.getcwd(), "name_card.xlsx")
    new_data = []

    for image_path in images:
        try:
            print(f'Processing image {image_path}')
            cleaned_data = image_to_json(image_path)
            new_data.append(cleaned_data)
            print(f'Processed image {image_path}')
        except Exception as e:
            print(f"Error processing image {image_path}: {e}")

    if new_data:
        new_df = json_to_df(new_data)
        os.makedirs(os.path.dirname(excel_file_path), exist_ok=True)

        if os.path.exists(excel_file_path):
            existing_df = pd.read_excel(excel_file_path)
            updated_df = pd.concat([existing_df, new_df], ignore_index= True)
        else:
            updated_df = new_df
        updated_df.to_excel(excel_file_path, index=False)
    else:
        print("No data to process")
        return None
    return excel_file_path

# Create the Gradio interface
iface = gr.Interface(
    inputs=gr.File(label="Upload Image(s)", file_types=[".jpg", ".png", ".jpeg"], file_count="multiple"),
    outputs=gr.File(label="Download Excel File"),
    fn=upload_and_process,
    title="Business Card Reader and Converter",
    description="Upload multiple name cards and get the processed data in Excel format."
)

if __name__ == "__main__":
    iface.launch(share=True)