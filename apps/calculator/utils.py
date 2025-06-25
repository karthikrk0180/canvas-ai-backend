import google.generativeai as genai
import ast
import json
import re
from PIL import Image
from constants import GEMINI_API_KEY


genai.configure(api_key = GEMINI_API_KEY)
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def read_prompt():
    with open("apps/calculator/prompt.txt", "r", encoding="utf-8") as f:
        prompt = f.read()
        return prompt

def clean_json_response(text):
    """
    Finds and extracts the content of a JSON code block from a string.
    """
    match = re.search(r'```(json)?\s*(?P<json_data>\[.*\])\s*```', text, re.DOTALL)
    if match:
        return match.group('json_data')
    return text # Return original text if no JSON block is found

def analyze_Image(img: Image):
    prompt = (read_prompt()) 
    response = model.generate_content([prompt, img])
    
    cleaned_response = clean_json_response(response.text)
    
    answers = []
    try:
        answers = ast.literal_eval(cleaned_response)
    except Exception as e:
        print(f"Error in parsing response from Gemini API: {e}")
        print(f"Original response: {response.text}")
    
    # print('returned answer ', answers)
    return answers
