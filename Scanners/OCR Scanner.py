
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label
import cv2
import csv
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

            # Save OCR result to CSV file
            csv_filename = 'ocr_result.csv'
            with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                # Write each line of the OCR result as a separate row in the CSV file
                for line in menu_text.split('\n'):
                    csv_writer.writerow([line])
            print(f"OCR result saved to {csv_filename}")

        except Exception as e:
            print("OCR error:", e)
            self.result_label.text = "OCR failed."

        finally:
            # Stop the camera after capturing and scanning
            self.camera.play = False

            # Remove widgets from the layout
            self.layout.clear_widgets()

            # Close the camera window
            self.stop()

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


