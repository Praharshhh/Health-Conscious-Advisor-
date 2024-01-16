from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label
import cv2
import numpy as np
import pytesseract

# Set the path to Tesseract executable (replace with your path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class CameraScannerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Create a camera widget
        self.camera = Camera(resolution=(640, 480), play=True)
        self.layout.add_widget(self.camera)

        # Create a button to capture image and perform OCR
        self.capture_button = Button(text='Capture and Scan', on_press=self.capture_and_scan)
        self.layout.add_widget(self.capture_button)

        # Create a label to display OCR result
        self.result_label = Label(text='')
        self.layout.add_widget(self.result_label)

        return self.layout

    def capture_and_scan(self, instance):
        # Capture frame from camera
        frame = self.capture_frame()

        # Preprocess image for better OCR (optional)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Perform OCR
        try:
            menu_text = pytesseract.image_to_string(gray, lang='eng')  # Use grayscale image for OCR
            self.result_label.text = f"OCR Result:\n{menu_text}"
        except Exception as e:
            print("OCR error:", e)
            self.result_label.text = "OCR failed."
        

    def capture_frame(self):
         # Capture frame from camera using OpenCV
        buf = self.camera.texture.pixels
        image_data = np.frombuffer(buf, dtype=np.uint8)
        image_data = image_data.reshape((self.camera.texture.height, self.camera.texture.width, 4))
        frame = image_data[:, :, :3]
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame

if __name__ == '__main__':
    CameraScannerApp().run()
