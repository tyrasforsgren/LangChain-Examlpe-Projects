"""
Course Generator Module

This module provides functionality to generate marketing content 
and course outlines using the LangChain and OpenAI API.

Functions/Classes:
    - generate_output: Generates output for the chat using 
    ChatOpenAI model.
    - CourseGenerator: Class providing static methods to 
    generate titles, marketing text, and course outlines.

Example
-------
from course_generator import CourseGenerator

# Set API key from environment variables
load_dotenv()
API_KEY = os.getenv('API_KEY')

# Generate marketing content
description = "A course that teaches juniors how to code python"
marketing_aid = CourseGenerator()
print(marketing_aid.generate_titles(description))
print(marketing_aid.generate_marketing_text(description))
print(marketing_aid.generate_course_outline(description, course_difficulty='beginner'))
print(marketing_aid.generate_coding_exercises("Pandas module"))
"""

import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

# Get secret API key from hidden .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')


def generate_output(system_template, product_description, max_tokens=300): # TODO: Make sure this is optimal
    """
    Generate output content for the chat using the ChatOpenAI model.

    Parameters
    ----------
    system_template : str
        The system template for generating content.
    product_description : str
        The product description.
    max_tokens : int, optional
        The maximum number of tokens for the output.

    Returns
    -------
    str
        Generated content.
    """
    # Init model
    llm = ChatOpenAI(model_name="gpt-3.5-turbo",
                     openai_api_key=API_KEY,
                     temperature=1,
                     max_tokens=max_tokens)

    # Create human prompt with proper template
    human_template = "{product_description_temp}"
    human_prompt = HumanMessagePromptTemplate.from_template(human_template)

    # Translate prompt
    chat_prompt = ChatPromptTemplate.from_messages([
        system_template,
        human_prompt])
    final_prompt = chat_prompt.format_prompt(
        product_description_temp=product_description)

    # Generate
    result = llm.invoke(final_prompt)
    return result.content


class CourseGenerator:
    """
    Class providing static methods to generate marketing content
    and course outlines. It's purpose is to structure the module.
    """

    @staticmethod
    def generate_titles(description, max_tokens=300):
        """
        Generate creative persuasive titles for a product.

        Parameters
        ----------
        description : str
            Description of the product.
        max_tokens : int, optional
            The maximum number of tokens for the output.

        Returns
        -------
        str
            Generated titles.
        """
        system_template = "You are a marketing expert and will generate creative persuasive \
                        titles for a product. Come up with several options."
        return generate_output(system_template, description, max_tokens)

    @staticmethod
    def generate_marketing_text(description, max_tokens=300):
        """
        Generate creative persuasive marketing text about a product.

        Parameters
        ----------
        description : str
            Description of the product.
        max_tokens : int, optional
            The maximum number of tokens for the output.

        Returns
        -------
        str
            Generated marketing text.
        """
        system_template = "You are a marketing expert and will generate creative persuasive \
                        marketing about a product."
        return generate_output(system_template, description, max_tokens)

    @staticmethod
    def generate_course_outline(description, course_difficulty, max_tokens=300):
        """
        Generate a course plan/outline for beginners or advanced students.

        Parameters
        ----------
        description : str
            Description of the course.
        course_difficulty : str
            The difficulty level of the course. It must be either 'beginner' or 'advanced'.
        max_tokens : int, optional
            The maximum number of tokens for the output.

        Returns
        -------
        str
            Generated course outline.

        Raises
        ------
        ValueError
            If the course_difficulty is not one of the specified choices.
        """
        if course_difficulty not in ['beginner', 'advanced']:
            raise ValueError("course_difficulty must be either 'beginner' or 'advanced'")

        system_template = f"You are a teacher in the following subjects: IT, cloud solutions, \
                        system architecture, ML and AI. You will generate a course \
                        plan/outline for {course_difficulty} students based on the \
                        description of a course."
        return generate_output(system_template, description, max_tokens)


    @staticmethod
    def generate_coding_exercises(subject, difficulty=None, max_tokens=300):
        """
        Generate coding exercises for the given subject.

        Parameters
        ----------
        subject : str
            The subject for which coding exercises are to be generated.
        difficulty : str, optional
            The difficulty level of the coding exercises.
        max_tokens : int, optional
            The maximum number of tokens for the output.

        Returns
        -------
        str
            Generated coding exercises.
        """
        system_template = "You are a teacher in programming in Python. Generate a coding exercise for \
                        the given subject. If a difficulty is given, match that in the complexity of \
                        the problem"
        if difficulty:
            subject += f'Make this problem at {difficulty} difficulty'
        return generate_output(system_template, subject, max_tokens)
