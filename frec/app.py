import cv2
from deepface import DeepFace

# Initialize webcam
camera = cv2.VideoCapture(0)  # 0 is the default webcam

# Check if the camera is opened successfully
if not camera.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 's' to capture the image and analyze emotion, 'q' to quit.")

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()

    if not ret:
        print("Failed to grab frame.")
        break

    # Display the resulting frame
    cv2.imshow("Webcam - Press 's' to capture", frame)

    # Wait for key press
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):  # Capture and analyze when 's' is pressed
        # Save the captured image
        image_path = "captured_image.jpg"
        cv2.imwrite(image_path, frame)
        print(f"Image saved to {image_path}")

        # Analyze emotion using DeepFace
        try:
            result = DeepFace.analyze(img_path=image_path, actions=['emotion'])
            print("Emotion Analysis Result:", result["emotion"])
        except Exception as e:
            print("Error in emotion analysis:", e)

    elif key == ord('q'):  # Quit when 'q' is pressed
        print("Exiting...")
        break

# Release the camera and close windows
camera.release()
cv2.destroyAllWindows()
