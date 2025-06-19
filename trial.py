import os
import google.generativeai as genai
from PyPDF2 import PdfReader

# Replace with your actual API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyCMqnIUe8vHMU2TShOeduh9aFJpSJ1cr14" 

genai.configure(api_key=os.environ["GOOGLE_API_KEY"]) 
model = genai.GenerativeModel("gemini-1.5-flash")

def extract_text_from_pdf(pdf_path):
  """Extracts text from a PDF file."""
  with open(pdf_path, 'rb') as f:
    pdf_reader = PdfReader(f)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
      page = pdf_reader.pages[page_num]
      text += page.extract_text()
  return text

def generate_questions(text):
  """Generates questions based on the given text and marking scheme using Gemini."""
  questions = []

  # Generate two-marker questions
  prompt = f"Generate a 5 one-markers, 3 two-markers, 2 five markers question based on the following text to test my studies that can be asked in examination. No need to provide answers. No need to add any additonal information or note or any advice. Also while generating, just generate questions, no need to write headings for 2 markers 3 markers or 5 markers. Just go from 1 and end it to 10 in which 1-5 will be one marker questions, 6-8 sill be two markers and 9-10 will be five markers. **Here's the content**: {text}"
  response = model.generate_content(prompt)
  questions.append({"question": response.text})

  return questions

if __name__ == "__main__":
  pdf_path = "D:/Desktop/DIPLOMA 6th SEM/ML/ML_Notes.pdf"
  text = extract_text_from_pdf(pdf_path)

  num_one_marker = 2
  num_two_marker = 2
  num_five_marker = 1

  questions = generate_questions(text)

  for question in questions:
    print(f"{question['question']}")
