#CV2.py 
# I need to add data for the program regarding facial recognition

import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect faces and draw rectangles around them
def detect_faces(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    return frame

# Main function
def main():
    # Open the video capture device (0 is usually the webcam)
    cap = cv2.VideoCapture(0)
    
    while True:
        # Read a frame from the video capture
        ret, frame = cap.read()
        
        if ret:
            # Detect faces in the frame
            frame_with_faces = detect_faces(frame)
            
            # Display the frame with faces
            cv2.imshow('Face Detection', frame_with_faces)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the video capture device and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Call the main function
if __name__ == "__main__":
    main()
