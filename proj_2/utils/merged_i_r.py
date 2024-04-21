import cv2
import matplotlib.pyplot as plt

class BasicImageHandeling:

    @staticmethod
    def read_image(image_path):
        return cv2.imread(image_path)
    
    @staticmethod
    def show_image(image):
        plt.axis('off')
        plt.imshow(image)

    @staticmethod
    def crop_image(image, coords):
        x, y, w, h = coords
        return image[y:y+h, x:x+w]
    
    @staticmethod
    def save_output_images(output_path='proj_2\data'): # TODO
        # Save output images and other results
        pass

    @staticmethod
    def get_main_color_from_image(image): # TODO
        return (255,255,255)

    @staticmethod
    def divide_rois(image, roi_coordinates):
        image_to_crop = image.copy()
        roi_imgs = {}
        for roi_name, (x, y, w, h) in roi_coordinates.items():
            roi_imgs[roi_name] = BasicImageHandeling.crop_image(image_to_crop,(x,y,w,h))
        return roi_imgs

    
    @staticmethod
    def draw_rectangle(image, rectangles, output_path='proj_2\data\rect_image.jpg'):
        clone = image.copy()
        rect_start = None

        def mouse_callback(event, x, y, flags, param):
            nonlocal rect_start
            if event == cv2.EVENT_LBUTTONDOWN:
                rect_start = (x, y)
            elif event == cv2.EVENT_LBUTTONUP:
                rect_end = (x, y)
                rectangle = BasicImageHandeling.calc_rectangle_coords(rect_start, rect_end)
                rectangles.append(rectangle)

        cv2.namedWindow("Image")
        cv2.setMouseCallback("Image", mouse_callback)

        while True:
            # Draw existing rectangles
            for rect in rectangles:
                x1, y1, x2, y2, _, _ = rect
                top_left = (x1, y1)
                bottom_right = (x2, y2)
                cv2.rectangle(clone, top_left, bottom_right, (0, 0, 255), 2)

            # Show the image
            cv2.imshow("Image", clone)
            
            # Wait for key press
            key = cv2.waitKey(1)
            if key == ord("q"):
                break

        # Save the image with rectangles
        for rect in rectangles:
            x1, y1, x2, y2, _, _ = rect
            top_left = (x1, y1)
            bottom_right = (x2, y2)
            cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 2)
        cv2.imwrite(output_path, image)

        # Close the OpenCV window
        cv2.destroyWindow("Image")


        """
        clone = image.copy()

        def mouse_callback(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                param['rect_start'] = (x, y)
            elif event == cv2.EVENT_LBUTTONUP:
                rect_end = (x, y)
                rectangle = BasicImageHandeling.calc_rectangle_coords(param['rect_start'], rect_end)
                param['rectangles'].append(rectangle)
                param['window_closed'] = False

        cv2.namedWindow("Image")
        cv2.setMouseCallback("Image", mouse_callback, param={'rectangles': rectangles})
        
        while True:
            for rect in rectangles:
                x1, y1, x2, y2, _, _ = rect
                top_left = (x1, y1)
                bottom_right = (x2, y2)
                cv2.rectangle(clone, top_left, bottom_right, (0, 0, 255), 2)
            cv2.imshow("Image", clone)
            key = cv2.waitKey(1)
            if key == ord("q") or cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE) < 1:
                break
            """

    @staticmethod
    def calc_rectangle_coords(top_left, bottom_right):
        x1, y1 = top_left
        x2, y2 = bottom_right
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        return x1, y1, x2, y2, width, height

    @staticmethod
    def get_roi_images(image, roi_coord_list):
        roi_images = []
        for roi_coordinates in roi_coord_list:
            x1, y1, x2, y2, _, _ = roi_coordinates
            roi_image = image[y1:y2, x1:x2].copy()
            roi_images.append(roi_image)
        return roi_images

    @staticmethod
    def get_rectangle_coordinates(rectangles): # TODO
        return rectangles

    @staticmethod
    def get_image_with_rectangles(image, rectangles):
        image_with_rectangles = image.copy()
        for rect in rectangles:
            x1, y1, x2, y2, _, _ = rect
            top_left = (x1, y1)
            bottom_right = (x2, y2)
            cv2.rectangle(image_with_rectangles, top_left, bottom_right, (0, 0, 255), 2)
        return image_with_rectangles
