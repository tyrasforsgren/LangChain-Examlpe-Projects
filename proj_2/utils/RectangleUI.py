import cv2

# start win
# draw rect
# wait for input

class RectangleDrawer:
    def __init__(self, image_path):
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
        cv2.namedWindow("Image")
        cv2.setMouseCallback("Image", self.mouse_callback, self.image)
        cv2.imshow("Image", self.image)

    def draw_rectangle(self): # TOT: Use calc coords?
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

    def wait_for_input(self): # TODO: Use calc rect coords?
        self.image_with_rectangles = self.image.copy()
        for rect in self.rectangles:
            x1, y1, x2, y2, _, _ = rect  # Extract coordinates from the rectangle
            top_left = (x1, y1)
            bottom_right = (x2, y2)
            cv2.rectangle(self.image_with_rectangles, top_left, bottom_right, (0, 0, 255), 2)
        # cv2.imwrite("image_with_rectangles.jpg", self.image_with_rectangles)

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.rect_start = (x, y)
        elif event == cv2.EVENT_LBUTTONUP:
            self.rect_end = (x, y)
            # Ensure that the rectangle coordinates are ordered from top-left to bottom-right
            x1, y1 = self.rect_start
            x2, y2 = self.rect_end
            rectangle = self.calc_rectangle_coords((min(x1, x2), min(y1, y2)), (max(x1, x2), max(y1, y2)))
            self.rectangles.append(rectangle)
            self.window_closed = False

    def calc_rectangle_coords(self, top_left, bottom_right):
        x1, y1 = top_left
        x2, y2 = bottom_right
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        return x1, y1, x2, y2, width, height

    def get_roi_images(self, roi_coord_list):
        roi_images = []
        for roi_coordinates in roi_coord_list:
            x1, y1, x2, y2, _, _ = roi_coordinates  # Extract coordinates from the rectangle
            roi_image = self.image[y1:y2, x1:x2].copy()
            roi_images.append(roi_image)
        return roi_images

    def get_rectangle_coordinates(self):
        return self.rectangles

    def get_image_with_rectangles(self):
        return self.image_with_rectangles

# TODO: Resize to fit screen