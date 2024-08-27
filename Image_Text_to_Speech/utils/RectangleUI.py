import cv2

class RectangleDrawer:
    """
    Class for drawing rectangles on an image and retrieving their coordinates.

    Attributes:
        image_path : str
            The path to the image file.
        image : numpy.ndarray
            The loaded image.
        clone : numpy.ndarray
            A copy of the original image.
        rectangles : list
            A list to store rectangle coordinates.
        window_closed : bool
            Flag to indicate if the window is closed.

    Methods:
        - __init__: Initializes the RectangleDrawer object.
        - start_window: Starts the window and sets up mouse callback.
        - draw_rectangle: Draws rectangles on the image.
        - wait_for_input: Waits for user input to finish drawing rectangles.
        - mouse_callback: Callback function for mouse events.
        - calc_rectangle_coords: Calculates rectangle coordinates.
        - get_roi_images: Retrieves region of interest (ROI) images based on rectangle coordinates.
        - get_rectangle_coordinates: Retrieves the list of rectangle coordinates.
        - get_image_with_rectangles: Retrieves the image with drawn rectangles.
    """

    def __init__(self, image_path):
        """
        Initialize the RectangleDrawer object.

        Parameters
        ----------
        image_path : str
            The path to the image file.
        """
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise ValueError(f"Error: Unable to load the image. \
                             Please check the file path and ensure it exists. \
                             Current path: {image_path}")

        self.clone = self.image.copy()
        self.rectangles = []
        self.window_closed = False

    def start_window(self):
        """
        Start the window and set up mouse callback.
        """
        cv2.namedWindow("Image")
        cv2.setMouseCallback("Image", self.mouse_callback, self.image)
        cv2.imshow("Image", self.image)

    def draw_rectangle(self):
        """
        Draw rectangles on the image.
        """
        while True:
            for rect in self.rectangles:
                x1, y1, x2, y2, _, _ = rect  # Extract coordinates from the rectangle
                top_left = (x1, y1)
                bottom_right = (x2, y2)
                cv2.rectangle(self.clone, top_left, bottom_right, (0, 0, 255), 2)
            cv2.imshow("Image", self.clone)
            key = cv2.waitKey(1)
            if key == ord("q") or cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) < 1:
                break

    def wait_for_input(self):
        """
        Wait for user input to finish drawing rectangles.
        """
        self.image_with_rectangles = self.image.copy()
        for rect in self.rectangles:
            x1, y1, x2, y2, _, _ = rect  # Extract coordinates from the rectangle
            top_left = (x1, y1)
            bottom_right = (x2, y2)
            cv2.rectangle(self.image_with_rectangles, top_left, bottom_right, (0, 0, 255), 2)

    def mouse_callback(self, event, x, y, flags, param):
        """
        Callback function for mouse events.

        Parameters
        ----------
        event : int
            The mouse event type.
        x : int
            The x-coordinate of the mouse pointer.
        y : int
            The y-coordinate of the mouse pointer.
        flags : int
            Additional flags from OpenCV.
        param : object
            Additional parameters (not used in this function).
        """
        if event == cv2.EVENT_LBUTTONDOWN:
            self.rect_start = (x, y)
        elif event == cv2.EVENT_LBUTTONUP:
            self.rect_end = (x, y)
            x1, y1 = self.rect_start
            x2, y2 = self.rect_end
            rectangle = self.calc_rectangle_coords((min(x1, x2), min(y1, y2)), (max(x1, x2), max(y1, y2)))
            self.rectangles.append(rectangle)
            self.window_closed = False


    def calc_rectangle_coords(self, top_left, bottom_right):
        """
        Calculate rectangle coordinates.

        Parameters
        ----------
        top_left : tuple
            Coordinates of the top-left corner.
        bottom_right : tuple
            Coordinates of the bottom-right corner.

        Returns
        -------
        tuple
            Rectangle coordinates.
        """
        x1, y1 = top_left
        x2, y2 = bottom_right
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        return x1, y1, x2, y2, width, height

    def get_roi_images(self, roi_coord_list):
        """
        Retrieve region of interest (ROI) images based on rectangle coordinates.

        Parameters
        ----------
        roi_coord_list : list
            List of rectangle coordinates.

        Returns
        -------
        list
            List of ROI images.
        """
        roi_images = []
        for roi_coordinates in roi_coord_list:
            x1, y1, x2, y2, _, _ = roi_coordinates  # Extract coordinates from the rectangle
            roi_image = self.image[y1:y2, x1:x2].copy()
            roi_images.append(roi_image)
        return roi_images

    def get_rectangle_coordinates(self):
        """
        Retrieve the list of rectangle coordinates.

        Returns
        -------
        list
            List of rectangle coordinates.
        """
        return self.rectangles

    def get_image_with_rectangles(self):
        """
        Retrieve the image with drawn rectangles.

        Returns
        -------
        numpy.ndarray
            Image with drawn rectangles.
        """
        return self.image_with_rectangles
