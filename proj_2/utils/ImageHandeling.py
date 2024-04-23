
import cv2
import os
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY_3')


class BasicImageHandeling:

    @staticmethod
    def read_image(image_path):
        return cv2.imread(image_path)

    @staticmethod
    def show_image(image):
        """
        Display the given image using Matplotlib.

        Args:
            image (numpy.ndarray): The image to be displayed.
        """
        # Convert the image from BGR to RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Turn off axis
        plt.axis('off')

        # Display the image
        plt.imshow(rgb_image)
        plt.show()

    @staticmethod
    def crop_image(image,coords):
        x, y, w, h = coords
        return image[y:y+h, x:x+w]
    
    @staticmethod
    def save_output_image(image, image_name='image.jpg', directory='data'):
        # TODO: If new dir defined by user, create it.
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the full path to the output directory
        output_dir = os.path.join(script_dir, directory)
        
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Change the current working directory to the output directory
        os.chdir(output_dir)
        
        # Save the image with the specified name
        cv2.imwrite(image_name, image)

    @staticmethod
    def find_dominant_colors(image, num_colors=3):
        # Read the image
        
        # Convert the image from BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Flatten the image array
        pixels = image.reshape(-1, 3)
        
        # Apply K-Means clustering to find dominant colors
        kmeans = KMeans(n_clusters=num_colors)
        kmeans.fit(pixels)
        
        # Get the labels assigned to each pixel
        labels = kmeans.labels_
        
        # Count the frequency of each label
        label_counts = np.bincount(labels)
        
        # Get indices of dominant colors sorted by frequency
        sorted_indices = np.argsort(label_counts)[::-1]
        
        # Get the dominant colors sorted by frequency
        dominant_colors = kmeans.cluster_centers_[sorted_indices]
        
        return dominant_colors.astype(int)

    @staticmethod
    def display_color(color_rgb):
        """
        Display a small square containing the specified color.

        Args:
            color_rgb (tuple): RGB values of the color (e.g., (R, G, B)).
        """
        # Convert RGB values to range 0-1
        color_rgb_normalized = (color_rgb[0] / 255, color_rgb[1] / 255, color_rgb[2] / 255)
        
        # Create a figure and axis
        fig, ax = plt.subplots()

        # Create a square patch with the specified color
        square = plt.Rectangle((0, 0), 0.5, 0.5, color=color_rgb_normalized)

        # Add the square to the axis
        ax.add_patch(square)

        # Set the aspect of the plot to equal
        ax.set_aspect('equal', adjustable='box')

        # Remove axes
        ax.axis('off')

        # Show the plot
        plt.show()


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
