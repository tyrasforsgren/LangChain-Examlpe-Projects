import openai
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser

from langchain.schema import HumanMessage,SystemMessage
from langchain.prompts import (ChatPromptTemplate , 
                               SystemMessagePromptTemplate,
                               HumanMessagePromptTemplate,
                               AIMessagePromptTemplate,
                               
                               )

# Set your OpenAI API key

load_dotenv()
API_KEY = os.getenv('API_KEY')


class MarketingGenerator():
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo",
                               openai_api_key=API_KEY,
                               temperature=1,
                               max_tokens=300)

    def generate_marketing_content(self,product_description,pros):
        """
        Generate persuasive marketing content using CHATGPT3.5 and DALL-E for LinkedIn.

        Args:
        - description (str): Brief description of the course or product.

        Returns:
        - str: Persuasive marketing content.
        """
        
        # create System prompt template
        system_template = "You are a marketing expert and will generate creative presuasive \
                        marketing about a product. You highlight the {pros_temp}."
        human_template = "{product_description_temp}"
        human_prompt = HumanMessagePromptTemplate.from_template(human_template)
        chat_prompt = ChatPromptTemplate.from_messages([
            system_template,
            human_prompt])
        final_prompt = chat_prompt.format_prompt(
            pros_temp = pros,
            product_description_temp = product_description)

        result = self.llm.invoke(final_prompt)
        return result.content

    def generate_catchy_titles(self,product_description):
        """
        Generate catchy titles for IT, cloud solutions, architecture, and ML/AI courses.

        Args:
        - description (str): Brief description of the course.

        Returns:
        - str: Catchy title.
        """
        system_template = "You are a marketing expert and will generate creative presuasive \
                        titles for a product. Come up with several options."
        human_template = "{product_description_temp}"
        human_prompt = HumanMessagePromptTemplate.from_template(human_template)
        
        chat_prompt = ChatPromptTemplate.from_messages([
            system_template,
            human_prompt])
        final_prompt = chat_prompt.format_prompt(
            product_description_temp = product_description)

        result = self.llm.invoke(final_prompt)
        return result.content

# # Example usage:
# course_description = "Learn how to build scalable cloud solutions using AWS services."
# marketing_content = generate_marketing_content(course_description)
# catchy_title = generate_catchy_titles(course_description)

# print("Generated Marketing Content:\n", marketing_content)
# print("\nGenerated Catchy Title:\n", catchy_title)

description = '''A course that teaches juniors how to code python'''
pros = ['Free','Long Distance','Short']
marketing_aid = MarketingGenerator()
# print(marketing_aid.generate_marketing_content(description,pros))
# print(marketing_aid.generate_catchy_titles(description))