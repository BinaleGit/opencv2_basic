import cv2
import numpy as np
import os
import time

# Load the pre-trained Haarcascade model for face detection
haar_cascade_path = 'haarcascade_frontalface_alt.xml'

if not os.path.isfile(haar_cascade_path):
    raise ValueError(f"Haarcascade XML file not found at {haar_cascade_path}")

face_cascade = cv2.CascadeClassifier(haar_cascade_path)
users_dir = 'users'

if not os.path.exists(users_dir):
    os.makedirs(users_dir)

# Function to recognize faces in an image
def recognize_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces

# Function to sign up a user
def sign_up():
    cap = cv2.VideoCapture(0)
    name = input("Enter your name: ")

    face_data_list = []

    while len(face_data_list) < 30:
        ret, frame = cap.read()
        if not ret:
            break

        faces = recognize_faces(frame)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Sign Up - Capturing face data', frame)

        if len(faces) == 1:
            (x, y, w, h) = faces[0]
            face = frame[y:y+h, x:x+w]
            face_data = cv2.resize(face, (100, 100))
            face_data = cv2.cvtColor(face_data, cv2.COLOR_BGR2GRAY)
            face_data_list.append(face_data)
            print(f"Captured {len(face_data_list)} frames.")
            time.sleep(0.2)  # Slow down the frame capture rate

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    if len(face_data_list) == 30:
        file_path = os.path.join(users_dir, f"{name}.npy")
        np.save(file_path, np.array(face_data_list))
        print(f"Face data for {name} saved successfully.")
    else:
        print("Failed to capture sufficient face data.")

    cap.release()
    cv2.destroyAllWindows()

# Function to compare faces
def compare_faces(face1, face2):
    return np.linalg.norm(face1 - face2)

# Function to sign in a user
# Function to sign in a user
def sign_in():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        faces = recognize_faces(frame)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            if len(faces) == 1:
                face = frame[y:y+h, x:x+w]
                face_data = cv2.resize(face, (100, 100))
                face_data = cv2.cvtColor(face_data, cv2.COLOR_BGR2GRAY)

                matched_user = None
                min_distance = float('inf')

                for user_file in os.listdir(users_dir):
                    user_face_data_list = np.load(os.path.join(users_dir, user_file))
                    distances = [compare_faces(face_data, user_face_data) for user_face_data in user_face_data_list]
                    average_distance = np.mean(distances)
                    if average_distance < min_distance:
                        min_distance = average_distance
                        matched_user = os.path.splitext(user_file)[0]
                        print(f"Matched user: {matched_user}, Distance: {average_distance}")

                if matched_user and min_distance < 30:  # Adjust the threshold as needed
                    cv2.putText(frame, f"Welcome, {matched_user}!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                    print(f"Welcome, {matched_user}!")

        cv2.imshow('Sign In - Looking for faces', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# Main function to run the application
def main():
    while True:
        choice = input("Enter '1' to sign up, '2' to sign in, or 'q' to quit: ")
        if choice == '1':
            sign_up()
        elif choice == '2':
            sign_in()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
