
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
    """
    Count the number of words in a sentence or list of words.

    Parameters
    ----------
    sentance : str or list
        The input sentence or list of words.
    ret_words : bool, optional
        Flag to indicate whether to return the list of words.
        Default is False.

    Returns
    -------
    int or tuple
        If ret_words is False, returns the count of words.
        If ret_words is True, returns a tuple containing the count of words and the list of words.

    """
    if isinstance(sentance,list): # Assumes each obj is a word
        return len(list)
    ret_words = sentance.split(' ') # Default

    return len(ret_words), ret_words

class TextToSpeech:
    """
    Class providing static methods for text-to-speech conversion, text extraction from images, and text summarization.

    Methods:
        - translate_text: Translate text to the specified language.
        - read_text: Convert text to speech.
        - extract_biggest_title: Extract the biggest title from the given image.
        - extract_text_from_image: Extract text from the given image.
        - summarize_text: Summarize the given text.
        - enhance_image: Enhance the given image.

    """

    @staticmethod # TODO: Future update
    def translate_text(text, dest_language='en'):
        """
        Translate text to the specified language.

        Parameters
        ----------
        text : str
            The text to be translated.
        dest_language : str, optional
            The destination language to translate the text into.
            Default is 'en' (English).

        Returns
        -------
        None
        """
        # translator = Translator()
        # translated_text = translator.translate(text, dest=dest_language)
        # return translated_text.text
        pass

    @staticmethod
    def read_text(text,s_rate=150):
        """
        Convert text to speech.

        Parameters
        ----------
        text : str
            The text to be converted to speech.
        s_rate : int, optional
            Rate at which the speech is read.
            Default : 150

        Returns
        -------
        None
        """
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()
        engine.setProperty('rate', s_rate)  # You can adjust the speaking rate
        engine.say(text)
        engine.runAndWait()

    @staticmethod
    def extract_biggest_title(image):
        """
        Extract the biggest title from the given image.

        Parameters
        ----------
        image : numpy.ndarray
            The image containing the text.

        Returns
        -------
        str or None
            The extracted title, if found. Otherwise, returns None.
        """
        text = TextToSpeech.extract_text_from_image(image)
        
        # Define common title patterns (start with uppercase followed by lowercase etc.)
        title_pattern = r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)*\b'
        # Extract potential titles using regex
        potential_titles = re.findall(title_pattern, text)

        # Filter out false positives : Words that should not be in a title
        known_non_titles = ['title:', 'chapter', 'chapter:', 'section', 'section:', 'part', 'part:']
        filtered_titles = [title for title in potential_titles if title not in known_non_titles]

        # Return the first extracted title (assuming the title is at the beginning of the text)
        if filtered_titles:
            return filtered_titles[0]
        else:
            return None

    @staticmethod
    def extract_text_from_image(image,language=r'--oem 3 --psm 6 -l swe'): # TODO: make lang optional
        """
        Extract text from the given image.

        Parameters
        ----------
        image : numpy.ndarray
            The image containing the text.
        language : str, optional
            The language of the text in the image.
            Default is 'swe' (Swedish).

        Returns
        -------
        str
            The extracted text from the image.
        """
        # Use pytesseract to extract text from the image
        processed_image = fromarray(image)
        custom_config = language  # Specify language as Swedish (Changed in update)
        extracted_text = pytesseract.image_to_string(processed_image, config=custom_config)

        return extracted_text
        
    def summarize_text(text, max_char=300, summary_div=5):
        """
        Summarize the given text.

        Parameters
        ----------
        text : str
            The text to be summarized.
        max_char : int, optional
            The maximum number of characters for the summary.
            Default is 300.
        summary_div : int, optional
            The divisor for calculating the maximum number of characters per summary.
            Default is 5.

        Returns
        -------
        str
            The summarized text.
        """
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

    def enhance_image(image): # TODO: Improved in update
        """
        Enhance the given image.

        Parameters
        ----------
        image : numpy.ndarray
            The image to be enhanced.

        Returns
        -------
        numpy.ndarray
            The enhanced image.
        """
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

        return blurred
