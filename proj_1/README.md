# Course Generator Module

## Overview
The Course Generator Module empowers users to effortlessly create marketing content and course outlines using the LangChain and OpenAI API. With a suite of functions and a dedicated class, it streamlines the process of generating persuasive titles, captivating marketing text, comprehensive course outlines, and challenging coding exercises.

## Functions/Classes

### `generate_output(system_template:str, product_description:str, max_tokens=1000) -> str`
Generates output content for the chat utilizing the ChatOpenAI model. This function aids in producing text based on the provided system template and product description.

### `CourseGenerator`
A class offering static methods to generate marketing content and course outlines. It serves as the backbone of the module, orchestrating the generation of titles, marketing text, course outlines, and coding exercises.

#### Methods:

- `generate_titles(description:str, max_tokens=1000) -> str`: Generates creative persuasive titles for a product.
- `generate_marketing_text(description:str, max_tokens=1000) -> str`: Generates persuasive marketing text about a product.
- `generate_course_outline(description:str, course_difficulty='Intermediate', max_tokens=1000) -> str`: Generates a course plan/outline for students at any level.
- `generate_coding_exercises(subject:str, difficulty=None, max_tokens=1000) -> str`: Generates coding exercises for the given subject.

## Usage
See `course_generation_DEMO.ipynb` file for detailed demo for use.
