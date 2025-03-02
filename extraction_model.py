import ollama
import re
import json

def json_model(text):
    """
    This function uses the nuextract-v1.5 model to convert the information text into JSON format.
    It takes a text and returns the JSON format of the information.

    Parameters
    ----------
    text : str
        The information text to be converted into JSON format.

    Returns
    -------
    json_data : str
        The JSON format of the information.
    """
    prompt_template = """Convert the following information text into JSON format:
    {text}
    Return NIL if information is not found.
    """
    if text:
        prompt = prompt_template.format(text=text)

        return ollama.chat(
            model="iodose/nuextract-v1.5",
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
    else:
        print("No text to process")
        return None


def extract_json_from_text(text):
    """
    This function extracts the JSON data from the given text.
    It takes a text and returns the JSON data from the given text.

    Parameters
    ----------
    text : str
        The text to be extracted from.

    Returns
    -------
    matches : json
        The JSON data from the given text.
    """
    if text:
        pattern = r'\{.*?\}'
        matches = re.findall(pattern, text, re.DOTALL)
        return matches
    else:
        print("No text to process regex pattern")
        return None


def parse_and_clean_json(matches):
    """
    This function parses and cleans the JSON data from the given text.
    It takes a list of text within {} and returns the cleaned JSON data.

    Parameters
    ----------
    matches : list
        The list of text within {} from the given text.

    Returns
    -------
    cleaned_data : str
        The cleaned JSON data.
    """
    cleaned_data = str()
    for match in matches:
        try:
            json_data = json.loads(match)
            cleaned_data += json.dumps(json_data)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
    return cleaned_data


def process_data(text):
    """
    This function processes the text and returns the cleaned JSON data.
    It takes a text and returns the cleaned JSON data.

    Parameters
    ----------
    text : str
        The text to be processed.

    Returns
    -------
    cleaned_json : str
        The cleaned JSON data.
    """
    if text:
        response = json_model(text)
        cleaned_text = response.get('message', {}).get('content', '')

        while True:
            matches = extract_json_from_text(cleaned_text)
            cleaned_json = parse_and_clean_json(matches)

            if cleaned_json:
                break
            else:
                print("Invalid format, retrying")
                response = json_model(text)
                cleaned_text = response.get('message', {}).get('content', '')
        print(cleaned_json)
        return cleaned_json
    else:
        print("No text to process")
        return None