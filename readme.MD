# Image Editor and Converter

This Streamlit app allows users to upload an image, perform basic editing (resize, rotate), and convert it to various formats. The app also enables downloading the edited and converted image.

## Features
- Upload images in PNG, JPG, JPEG, WEBP, and ICO formats.
- Edit image size and rotation.
- Convert images to PNG, JPEG, WEBP, and ICO.
- Download the edited and converted image.

## Installation

1. **Clone the repository:**
   ```
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Create a virtual environment (venv):**

    ```
    python3 -m venv venv
    ```

3. **Activate the virtual environment:**

    #### On Linux/macOS:
        
        source venv/bin/activate
        

    #### On Windows:
        
        .\venv\Scripts\activate
    


4. **Install the dependencies:**

    ```
    pip install -r requirements.txt
    ```

5. **Run the Streamlit application:**

    ```
    streamlit run app.py
    ```