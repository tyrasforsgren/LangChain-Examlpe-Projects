# Image Processing and Text To Speech

## Overview
This project offers a robust solution for text extraction from images, primarily catering to enhancing accessibility for visually impaired users. By utilizing image processing techniques and advanced language models, it aims to provide a summarized audio translation, thereby facilitating easier comprehension of textual content.

## Key Features

### Image Processing:
Employs various image processing techniques to enhance image quality and extract relevant textual information.

### Text Extraction:
Facilitates the extraction of text and numerical data from specific regions within the image, improving accessibility and enabling efficient data retrieval.

### Text Summarization:
Utilizes advanced language models such as LangChain and OpenAI to generate concise summaries of extracted text, aiding in the comprehension of extensive textual content.

### Text-to-Speech Conversion:
Converts the extracted text into speech, providing auditory feedback and enhancing accessibility for visually impaired individuals.

## Usage

This toolkit can be seamlessly integrated into applications aimed at enhancing accessibility and facilitating text extraction from images. By leveraging its diverse range of features, developers can create user-friendly solutions tailored to the needs of visually impaired users.

See `txt_to_speech_DEMO.ipynb` file for detailed demo for use.

## Modules

### Basic Image Handling Module

The Basic Image Handling module provides functionality for basic image manipulation and analysis. Here are the key features of this module:

1. **Read Image**: The `read_image` function allows users to read an image from a specified file path.

2. **Show Image**: The `show_image` function displays the given image using Matplotlib, converting it from BGR to RGB format for proper visualization.

3. **Crop Image**: With the `crop_image` function, users can crop a specific region of interest (ROI) from an image based on the provided coordinates.

4. **Save Output Image**: The `save_output_image` function saves an image with a specified name to a designated directory. If the directory does not exist, it creates one.

5. **Find Dominant Colors**: Using K-Means clustering, the `find_dominant_colors` function identifies the dominant colors in an image. Users can specify the number of dominant colors to find.

6. **Display Color**: The `display_color` function visualizes a specified color by creating a small square patch with the given RGB values.

7. **Divide ROIs**: The `divide_rois` function draws rectangles around regions of interest (ROIs) specified by the user. It returns a dictionary containing the cropped images of each ROI.

This module offers fundamental image processing capabilities, including reading, displaying, cropping, saving, and analyzing images. It can be used as a building block for more advanced image processing tasks.

## Rectangle Drawer Module

The Rectangle Drawer module provides functionality for drawing rectangles on images and extracting regions of interest (ROIs). Here are the key features of this module:

1. **Initialization**: Users can initialize the `RectangleDrawer` class by providing the path to an image file. The class loads the image and creates a clone for drawing rectangles.

2. **Start Window**: The `start_window` method displays the image in a window, allowing users to draw rectangles interactively using the mouse.

3. **Draw Rectangle**: The `draw_rectangle` method enables users to draw rectangles on the image by clicking and dragging the mouse. Rectangles are drawn with a specified color and thickness.

4. **Wait for Input**: After drawing rectangles, the `wait_for_input` method updates the image with the drawn rectangles and waits for user input.

5. **Mouse Callback**: The `mouse_callback` method handles mouse events for drawing rectangles. It records the starting and ending points of rectangles and ensures proper ordering of coordinates.

6. **Calculate Rectangle Coordinates**: The `calc_rectangle_coords` method calculates the coordinates of a rectangle based on the top-left and bottom-right points.

7. **Get ROI Images**: Users can extract ROI images from the drawn rectangles using the `get_roi_images` method.

8. **Get Rectangle Coordinates**: The `get_rectangle_coordinates` method returns the coordinates of the drawn rectangles.

9. **Get Image with Rectangles**: The `get_image_with_rectangles` method returns the image with drawn rectangles overlayed.

This module facilitates the interactive drawing of rectangles on images, enabling users to define regions of interest for further analysis or processing.

## TextToSpeech Module

The TextToSpeech module provides functionality for text extraction from images, text summarization, translation, and speech synthesis. Here are the key features of this module:

1. **Text Extraction from Images**: Users can extract text from images using the `extract_text_from_image` method. This method utilizes pytesseract, an optical character recognition (OCR) tool, to extract text from images.

2. **Text Summarization**: The `summarize_text` method generates a summary of the input text using the LangChain library. It leverages the GPT-3.5-Turbo model to produce concise summaries within a specified character limit.

3. **Translation (Future Update)**: The module includes a placeholder method `translate_text` for translating text to different languages. However, this feature is currently not implemented and is marked for future updates.

4. **Speech Synthesis**: Users can convert text to speech using the `read_text` method, which utilizes the pyttsx3 library to synthesize speech from text. Users can adjust the speaking rate according to their preferences.

5. **Enhance Image**: Users can use the method `enhance_image` for image enhancement with the aim to optimize images for text extranction.

6. **Title Extraction**: The `extract_biggest_title` method attempts to extract the main title from the extracted text. It uses regular expressions to identify potential titles based on common patterns.

7. **Word Counting**: The `count_words` method counts the number of words in a sentence or a list of words. Users can optionally retrieve the list of words along with the word count.

The TextToSpeech module serves as a versatile tool for working with text data, offering capabilities such as text extraction, summarization, translation, and speech synthesis.
