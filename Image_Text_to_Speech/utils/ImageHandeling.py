import cv2
import os
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY_3')

class BasicImageHandeling:
    """
    Class for basic image handling operations such as reading images, cropping images, 
    displaying images, saving output images, finding dominant colors, and dividing 
    regions of interest (ROIs) on images.

    Attributes:
        API_KEY : str
            API key for external services (not currently used).
    
    Methods:
        - read_image: Read an image from a given file path.
        - show_image: Display the given image using Matplotlib.
        - crop_image: Crop the specified region of interest (ROI) from the image.
        - save_output_image: Save the image with the specified name and directory.
        - find_dominant_colors: Find the dominant colors in the image using K-Means clustering.
        - display_color: Display a small square containing the specified color.
        - divide_rois: Divide regions of interest (ROIs) on the image and return them as separate images.
    """

    @staticmethod
    def read_image(image_path):
        """
        Read an image from a given file path.

        Parameters
        ----------
        image_path : str
            The path to the image file.

        Returns
        -------
        numpy.ndarray
            The loaded image.
        """
        return cv2.imread(image_path)

    @staticmethod
    def show_image(image):
        """
        Display the given image using Matplotlib.

        Parameters
        ----------
        image : numpy.ndarray
            The image to be displayed.
        """
        # Convert the image from BGR to RGB
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Turn off axis
        plt.axis('off')

        # Display the image
        plt.imshow(rgb_image)
        plt.show()

    @staticmethod
    def crop_image(image, coords):
        """
        Crop the specified region of interest (ROI) from the image.

        Parameters
        ----------
        image : numpy.ndarray
            The input image.
        coords : tuple
            The coordinates of the region to be cropped (x, y, w, h).

        Returns
        -------
        numpy.ndarray
            The cropped image.
        """
        x, y, w, h = coords
        return image[y:y+h, x:x+w]

    @staticmethod
    def save_output_image(image, image_name='image.jpg', directory='data'):
        """
        Save the image with the specified name and directory.

        Parameters
        ----------
        image : numpy.ndarray
            The image to be saved.
        image_name : str, optional
            The name of the output image file. (default is 'image.jpg')
        directory : str, optional
            The directory to save the output image file. (default is 'data')
        """
        # Construct the full path to the output directory
        output_dir = os.path.join(os.getcwd(), directory)
        
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Construct the full path to the output image file
        output_path = os.path.join(output_dir, image_name)
        
        # Save the image with the specified name
        cv2.imwrite(output_path, image)

    @staticmethod
    def find_dominant_colors(image, num_colors=3):
        """
        Find the dominant color(s) in the image using K-Means clustering.

        Parameters
        ----------
        image : numpy.ndarray
            The input image.
        num_colors : int, optional
            The number of dominant colors to find. (default is 3)

        Returns
        -------
        numpy.ndarray
            Array containing the dominant colors.
        """
        # Read the image
        # Convert the image from BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pixels = image.reshape(-1, 3)
        
        # Apply K-Means clustering to find dominant colors
        kmeans = KMeans(n_clusters=num_colors)
        kmeans.fit(pixels)
        
        # Get the labels and frequency assigned to each pixel
        labels = kmeans.labels_
        label_counts = np.bincount(labels)
        
        # Get indices of dominant colors sorted by frequency
        sorted_indices = np.argsort(label_counts)[::-1]
        # Get the dominant colors sorted by frequency
        dominant_colors = kmeans.cluster_centers_[sorted_indices]
        
        return dominant_colors.astype(int)

    @staticmethod
    def display_color(color_rgb, square_size=50):
        """
        Display a small square containing the specified color.

        Parameters
        ----------
        color_rgb : tuple
            RGB values of the color (e.g., (R, G, B)).
        square_size : int, optional
            Size of the square in pixels. Default is 50.
        """
        # Convert RGB values to range 0-1
        color_rgb_normalized = (color_rgb[0] / 255, color_rgb[1] / 255, color_rgb[2] / 255)

        # Create a figure and axis with specified size
        _, ax = plt.subplots(figsize=(square_size / 100, square_size / 100))
        square = plt.Rectangle((0, 0), 1, 1, color=color_rgb_normalized)
        ax.add_patch(square)

        ax.set_aspect('equal', adjustable='box')
        ax.axis('off')

        # Show the plot
        plt.show()


    @staticmethod
    def divide_rois(image, roi_coordinates):
        """
        Divide regions of interest (ROIs) on the image and return them as separate images.

        Parameters
        ----------
        image : numpy.ndarray
            Input image.
        roi_coordinates : dict
            Dictionary containing ROI coordinates.

        Returns
        -------
        dict
            Dictionary containing ROI images.
        """
        image_to_crop = image.copy()
        roi_imgs = {}
        # Iterate through each ROI
        for roi_name, (x, y, w, h) in roi_coordinates.items():
            roi_imgs[roi_name] = BasicImageHandeling.crop_image(image_to_crop, (x, y, w, h))
        return roi_imgs
