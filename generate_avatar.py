import dlib
import numpy as np
import cv2


# Initialize the camera
cam = cv2.VideoCapture(0)

# Create a window to display the camera feed
cv2.namedWindow("Camera Feed")

# Initialize the face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Initialize the array to store the data
data = []

# Collect the data
while True:
    # Read a frame from the camera
    ret, frame = cam.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = detector(gray)

    # Loop over the faces and detect facial landmarks
    for face in faces:
        landmarks = predictor(gray, face)

        # Extract the x, y coordinates of the facial landmarks
        coords = np.zeros((68, 2), dtype=int)
        for i in range(68):
            coords[i] = (landmarks.part(i).x, landmarks.part(i).y)

        # Append the coordinates to the data array
        data.append(coords)

        # Draw the facial landmarks on the frame
        for (x, y) in coords:
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

    # Display the frame in the window
    cv2.imshow("Camera Feed", frame)

    # Press 'q' to exit the loop and stop collecting data
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and destroy the window
cam.release()
cv2.destroyAllWindows()

# Convert the data array to a NumPy array and save it to a file
data = np.array(data)
np.save("data.npy", data)



#https://plainenglish.io/blog/get-ready-to-build-your-own-ai-animated-avatar-step-by-step-guide