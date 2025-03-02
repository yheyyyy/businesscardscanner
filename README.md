# Business Card Scanner

This Business Card Scanner uses the Llama3.2-Vision model and NuExtract-v1.5 model to extract useful information from business cards using a Vision Language Model. This method can capture more than 99% of different formats of namecards, including modern namecards without indicated fields. This tool is capable of batch processing with Gradio's Image function and is suitable for running on GPU-starved computers.

The output of the tool will be a excel spreadsheet containing information as such "Name", "Job Title", "Company", "Contact Number", "Email Address", "Website" and "Address".

## Installation

To use the Business Card Scanner, you need to have Python installed on your system. Follow these steps to install the required dependencies:

1. Clone the repository:

```bash
git clone https://github.com/yheyyyy/business-card-scanner.git
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Install Ollama:

- go to https://ollama.com/ and download the application , then download the following models in the command line.

```bash
ollama pull llama3.2-vision:11b
ollama pull iodose/nuextract-v1.5
```

## Usage
To run the Business Card Scanner, use the following command:

```bash
python gradio-app.py
```
This will start the gradio interface, allowing you to upload your business card images and start extracting the information for output into a excel file.
