import cv2
from pyzbar.pyzbar import decode
import requests
from bs4 import BeautifulSoup
import csv

def extract_text_from_link(url):
    try:
        # Send an HTTP request to the user-given URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract text from the HTML
            text = soup.get_text()

            return text
        else:
            print(f"Failed to retrieve content. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

cam = cv2.VideoCapture(0)

# Set the camera resolution
cam.set(3, 640)  # 3 corresponds to CV_CAP_PROP_FRAME_WIDTH
cam.set(4, 480)  # 4 corresponds to CV_CAP_PROP_FRAME_HEIGHT

qr_code_scanned = False
extracted_text = None

while not qr_code_scanned:
    # Read a frame from the camera
    success, frame = cam.read()

    # Decode QR codes and barcodes
    decoded_objects = decode(frame)

    # Iterate over all decoded objects
    for obj in decoded_objects:
        # Print the type and data of the object
        print(f'Type: {obj.type}, Data: {obj.data.decode("utf-8")}')
        
        # Extract text from the link
        user_url = obj.data.decode("utf-8")
        extracted_text = extract_text_from_link(user_url)

        # Print the extracted text
        if extracted_text:
            print("\nExtracted Text:")
            print(extracted_text)

        # Set the flag to indicate that a QR code has been scanned
        qr_code_scanned = True

    # Display the frame with QR code annotations
    cv2.imshow("Our QR Code Scanner", frame)

    # Break the loop if a QR code has been scanned or the 'q' key is pressed
    if qr_code_scanned or cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cam.release()
cv2.destroyAllWindows()

# Write extracted text to a CSV file
if extracted_text:
    csv_filename = 'data_of_food.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write each line of the extracted text as a separate row in the CSV file
        for line in extracted_text.split('\n'):
            csv_writer.writerow([line])
    print(f"Extracted text saved to {csv_filename}")





