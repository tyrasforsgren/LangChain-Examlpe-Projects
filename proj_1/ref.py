
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate,HumanMessagePromptTemplate

# Set your OpenAI API key
load_dotenv()
API_KEY = os.getenv('API_KEY')


def generate_marketing(system_template, product_description): # TODO : Make the warnings go away ? 
    llm = ChatOpenAI(model_name="gpt-3.5-turbo",
                               openai_api_key=API_KEY,
                               temperature=1,
                               max_tokens=300)
    # Create human prompt with proper template
    human_template = "{product_description_temp}"
    human_prompt = HumanMessagePromptTemplate.from_template(human_template)
    # traanslate prompt
    chat_prompt = ChatPromptTemplate.from_messages([
        system_template,
        human_prompt])
    final_prompt = chat_prompt.format_prompt(
        product_description_temp = product_description)
    # Generate
    result = llm.invoke(final_prompt)
    return result.content

class MarketingGenerator():

    def generate_titles(self, description):
        system_template = "You are a marketing expert and will generate creative presuasive \
                        titles for a product. Come up with several options."
        return generate_marketing(system_template, description)

    def generate_marketing_text(self, description):
        system_template = "You are a marketing expert and will generate creative presuasive \
                        marketing about a product."
        return generate_marketing(system_template, description)

    def generate_advanced_course_outline(self, description):
        system_template = "You are a teacher in the following subjects : IT, cloud soulutions, \
                        system architecture, ML and AI. You will generate an ADVANCED course \
                        plan/outline FOR PROFESSIONALS based on the description of a course."
        return generate_marketing(system_template, description)
    
    def generate_beginner_course_outline(self, description):
        system_template = "You are a teacher in the following subjects : IT, cloud soulutions, \
                        system architecture, ML and AI. You will generate a SIMPLE course \
                        plan/outline FOR BEGINNERS based on the description of a course."
        return generate_marketing(system_template, description)

    def generate_coding_exersizes(self, subject, difficulty=None):
        system_template = "You are a teacher in programming in Python. Generate a coding exersize for \
                        the given subject. If a difficulty is given, match that in the complexity of \
                        the problem"
        if difficulty:
            subject += f'Make this problem at {difficulty} difficulty'
        return generate_marketing(system_template, subject)

marketing_aid = MarketingGenerator()

description = '''A course that teaches juniors how to code python'''
course_description = '''A course teaching data analasys'''
subject = '''Pandas module'''

# print(marketing_aid.generate_marketing_text(description))
# print(marketing_aid.generate_titles(description))
# print(marketing_aid.generate_beginner_course_outline(course_description))
# print(marketing_aid.generate_advanced_course_outline(course_description))
# print(marketing_aid.generate_coding_exersizes(subject))#,difficulty='extreme'))
