import cv2
import pytesseract
import matplotlib.pyplot as plt
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

class MedicinePackageAnalyzer:
    def __init__(self, image_path, template_coordinates):
        self.image_path = image_path
        self.full_image = self.read_image(self.image_path)
        self.template_coordinates = template_coordinates
    
    def extract_text_from_image(self):
        # Obtain the text and numbers from each text/numeric area in the template
        self.extracted_text = {}
        for area, image in self.sub_images.items():
            self.extracted_text[area] = pytesseract.image_to_string(image)
    
    def find_title_and_info(self):
        # Find the title, main color, and any special info in the package picture
        pass

    @staticmethod
    def read_image(image_path):
        return cv2.imread(image_path)
    
    @staticmethod
    def crop_image(image,coords):
        x, y, w, h = coords
        return image[y:y+h, x:x+w]

    @staticmethod
    def generate_summary_text():
        # Generate a summary text using LangChain and/or OPEN AI API
        summary_text = ""  # Placeholder for generated summary text
        return summary_text
    
    staticmethod
    def generate_speech():
        # Use LangChain and/or OPEN AI API to generate speech for the summary text
        speech = ""  # Placeholder for generated speech
        return speech

    @staticmethod
    def save_output_images():
        # Save o
        # utput images and other results
        pass

    @staticmethod
    def divide_rois(image, roi_coordinates):
        """
        Draws rectangles around the regions of interest (ROIs) on the image.

        Parameters
        ----------
        image : numpy.ndarray
            Input image.
        roi_coordinates : dict
            Dictionary containing ROI coordinates.

        Returns
        -------
        numpy.ndarray
            Image with rectangles drawn around the ROIs.
        """
        image_to_crop = image.copy()
        roi_imgs = {}
        # Iterate through each ROI
        for roi_name, (x, y, w, h) in roi_coordinates.items():
            roi_imgs[roi_name] = MedicinePackageAnalyzer.crop_image(image_to_crop,(x,y,w,h))

        return roi_imgs

    @staticmethod
    def view_rois(image,roi_coordinates): # TODO: Quality of life
        image_with_rectangles = image.copy()
        
        # Iterate through each ROI
        for roi_name, (x, y, w, h) in roi_coordinates.items():
            # Draw rectangle around the ROI
            cv2.rectangle(image_with_rectangles, (x, y), (x + w, y + h), (0, 0, 255), 10)
            text_x = 10  # Adjust as needed to leave some space between text and rectangle
            text_y = y + 70  # Adjust as needed to position the text below the top edge of the rectangle

            # Draw the text inside the rectangle
            cv2.putText(image_with_rectangles, roi_name,
                        (text_x, text_y), fontFace=cv2.FONT_HERSHEY_SIMPLEX, thickness=5,
                        color=(255, 0, 0), fontScale=2, lineType=cv2.LINE_AA)
        
        # Display the image with rectangles
        plt.imshow(cv2.cvtColor(image_with_rectangles, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.show()

