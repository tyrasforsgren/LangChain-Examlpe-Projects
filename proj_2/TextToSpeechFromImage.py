
import cv2
import pytesseract
import matplotlib.pyplot as plt
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from PIL.Image import fromarray
import os
from dotenv import load_dotenv
from ImageHandeling import BasicImageHandeling
import pyttsx3

load_dotenv()
API_KEY = os.getenv('API_KEY_3')

class TextToSpeech:
    def __init__(self, image): # TODO is this needed?
        pass

    @staticmethod
    def read_text(text):
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # You can adjust the speaking rate
        engine.say(text)
        engine.runAndWait()

    @staticmethod
    def extract_text_from_image(image): # TODO: Working but needs prior attention
        # Use pytesseract to extract text from the image
        processed_image = fromarray(image)
        # extracted_text = pytesseract.image_to_string(processed_image)
        custom_config = r'--oem 3 --psm 6 -l swe'  # Specify language as Swedish
        extracted_text = pytesseract.image_to_string(processed_image, config=custom_config)

        return extracted_text
    
    def find_title_and_info(self):
        # Find the title, main color, and any special info in the package picture
        pass
    
    @staticmethod
    def generate_speech():
            # Use LangChain and/or OPEN AI API to generate speech for the summary text
            speech = ""  # Placeholder for generated speech
            return speech
        
    def summarize_text(text, max_char=300, summary_div=5):
        max_char = max_char // summary_div
        llm = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            openai_api_key=API_KEY,
            temperature=1,
            max_tokens=max_char
        )

        system_template = f'You are a professional writer. \
            You are supposed to summarize the following text: {text}. \
            Finish the summary before reaching {max_char} characters.'
        chat_prompt = ChatPromptTemplate.from_messages([system_template])
        final_prompt = chat_prompt.format_prompt(product_description_temp=text)

        result = llm.invoke(final_prompt)
        return result.content

    def enhance_text(image): # TODO: It's bad
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply adaptive thresholding to create a binary image
        binary = cv2.adaptiveThreshold(gray,
                                255,
                                cv2.ADAPTIVE_THRESH_MEAN_C, # A alg
                                cv2.THRESH_BINARY,
                                15,
                                4)

        # Apply median blur to reduce noise
        blurred = cv2.medianBlur(binary, 5)
        # plt.imshow(binary)
        # Sharpen the image using the unsharp masking technique
        sharpened = cv2.addWeighted(blurred, 1.0, binary, -0.5, 0)

        return binary#sharpened



# TODO : Method to let u select coords w mouse?


# TODO:
# Fix API!!!!
# find main color, title, info from PACKAGE image
# Save the img
# summarize txt
# read out





'''
# def format_text(text):
#     max_char = 300
#     if '\n' in text:
#         return text
#     llm = ChatOpenAI(
#     model_name="gpt-3.5-turbo",
#     openai_api_key=API_KEY,
#     temperature=1,
#     max_tokens=max_char
#     )

#     system_template = f'You are a professional text editor. \
#         You are supposed to reformat the following text: {text}. \
#         Your goal is to add linebreaks to make the text into a paragraph.'
#     chat_prompt = ChatPromptTemplate.from_messages([system_template])
#     final_prompt = chat_prompt.format_prompt(product_description_temp=text)

#     result = llm.invoke(final_prompt)
#     return result.content
'''