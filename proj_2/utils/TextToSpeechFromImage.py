
import cv2
import re
import os
import pyttsx3
import pytesseract
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from PIL.Image import fromarray
from dotenv import load_dotenv
# from googletrans import Translator

load_dotenv()
API_KEY = os.getenv('API_KEY_3')

def count_words(sentance,ret_words=False):
    if isinstance(sentance,list): # Assumes each obj is a word
        return len(list)
    ret_words = sentance.split(' ') # Default

    return len(ret_words), ret_words

class TextToSpeech:
    def __init__(self, image): # TODO is this needed?
        pass

    @staticmethod # TODO: Future update
    def translate_text(text, dest_language='en'):
        # translator = Translator()
        # translated_text = translator.translate(text, dest=dest_language)
        # return translated_text.text
        pass

    @staticmethod
    def read_text(text):
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # You can adjust the speaking rate
        engine.say(text)
        engine.runAndWait()

    @staticmethod
    def extract_biggest_title(image):
        text = TextToSpeech.extract_text_from_image(image)
        # Split the text into lines
        # def extract_title_from_text(text):
        # Define common title patterns (e.g., start with uppercase followed by lowercase)
        title_pattern = r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)*\b'

        # Extract potential titles using regex
        potential_titles = re.findall(title_pattern, text)

        # Filter out false positives
        known_non_titles = ['title:', 'chapter', 'chapter:', 'section', 'section:', 'part', 'part:']
        filtered_titles = [title for title in potential_titles if title not in known_non_titles]

        # Return the first extracted title (assuming the title is at the beginning of the text)
        if filtered_titles:
            return filtered_titles[0]
        else:
            return None

    @staticmethod
    def extract_text_from_image(image,language=r'--oem 3 --psm 6 -l swe'): # TODO: Working but needs prior attention
        # Use pytesseract to extract text from the image
        processed_image = fromarray(image)
        # extracted_text = pytesseract.image_to_string(processed_image)
        custom_config = language  # Specify language as Swedish
        extracted_text = pytesseract.image_to_string(processed_image, config=custom_config)

        return extracted_text
        
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

    def enhance_image(image): # TODO: It's bad
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

        return blurred#sharpened

