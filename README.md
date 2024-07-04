# opencv2_basic Face Recognition Project

This project implements a basic face recognition system using Python and OpenCV (opencv2). It allows users to sign up by capturing their face and name, and then sign in by recognizing their face based on the captured data.

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd opencv2_basic

Install dependencies:

Ensure you have Python installed. Install the required libraries using pip:

    pip install opencv-python numpy

Sign Up
To sign up, follow these steps:

Run the sign-up script:

    python sign_up.py

Enter your name when prompted.

The script will capture 30 frames of your face. Ensure good lighting and vary your facial expressions for better recognition.

Sign In
To sign in, follow these steps:

Run the sign-in script:

    python sign_in.py

The script will start the camera and attempt to recognize your face based on the captured data.

If recognized, it will display your name on the console and above your head in the video feed.

Notes
Adjust the compare_faces function in sign_in.py to fine-tune face recognition accuracy.
Ensure proper lighting and face alignment during sign-up and sign-in processes for better results.
Contributing
Contributions are welcome! Fork the repository and submit a pull request with your improvements.


### How to Use:

1. **Clone the Repository:** Clone the repository to your local machine using Git.
2. **Install Dependencies:** Install necessary Python libraries (`opencv-python` and `numpy`) using pip.
3. **Download XML File:** Obtain the `haarcascade_frontalface_alt.xml` file for face detection and place it in the project directory.
4. **Sign Up:** Run `python sign_up.py` to capture your face and name for sign-up.
5. **Sign In:** Run `python sign_in.py` to start the recognition process and authenticate based on captured data.

This Markdown README file provides clear instructions for installation, usage, contributing, and licensing of your "opencv2_basic" face recognition project. Adjust it further as needed based on your project's specifics and additional functionalities.
