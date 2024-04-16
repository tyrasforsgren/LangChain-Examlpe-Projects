
import cv2
# import pytesseract
import matplotlib.pyplot as plt
# from langchain_openai import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate
# from PIL.Image import fromarray
# import os
# from dotenv import load_dotenv

class BasicImageHandeling:

    @staticmethod
    def read_image(image_path):
        return cv2.imread(image_path)
    
    @staticmethod
    def show_image(image):
        plt.axis('off')
        plt.imshow(image)

    @staticmethod
    def crop_image(image,coords):
        x, y, w, h = coords
        return image[y:y+h, x:x+w]
    
    @staticmethod
    def save_output_images(): # TODO
        # Save o
        # utput images and other results
        pass

    @staticmethod
    def get_main_color_from_image(image): # TODO
        return (255,255,255)

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
            roi_imgs[roi_name] = BasicImageHandeling.crop_image(image_to_crop,(x,y,w,h))
        return roi_imgs

    @staticmethod # Not neccessary
    def view_rois(image,roi_coordinates): # TODO: Quality of life
        image_with_rectangles = image.copy()
        # Iterate through each ROI
        for _ , (x, y, w, h) in roi_coordinates.items():
            # Draw rectangle around the ROI
            cv2.rectangle(image_with_rectangles, (x, y), (x + w, y + h), (0, 0, 255), 5)
            # Display the image with rectangles
        plt.imshow(cv2.cvtColor(image_with_rectangles, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.show()
