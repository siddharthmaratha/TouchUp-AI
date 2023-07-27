# TouchUp AI - Advanced Image Editing Model
![image](https://github.com/siddharthmaratha/TouchUp-AI/assets/80692281/33726e30-c1f0-4f9a-ae63-c376e1c5da8e)

1. Please note that this project is currently in it's early development stages and may have some limitations.
2. While being an exciting project, TouchUp AI is intended for recreational use and experimentation.

TouchUp AI is an innovative Python machine learning project that introduces a cutting-edge approach to image editing. Powered by a trained model, this system allows users to modify images through textual input, utilizing a specified input power to control the extent of the applied edits. The model then regenerates the image with the requested edits as provided by the user, delivering an intuitive and precise image enhancement experience. Whether adjusting brightness, applying artistic filters, or removing/adding objects, TouchUp AI empowers users to transform their images effortlessly and achieve the desired visual results.

## Features
**Intuitive Text-Based Input:** TouchUp AI enables users to provide textual instructions specifying desired edits to their images. Through natural language processing (NLP) techniques, the model interprets the instructions to understand the user's editing requirements.

**Customizable Input Power:** Users have the flexibility to control the intensity of the applied edits using the input power parameter. This empowers users to fine-tune the editing process according to their artistic vision.

**Seamless Image Regeneration:** With TouchUp AI, the user's input is translated into a regenerated image that incorporates the specified edits. The model ensures accurate execution of editing tasks based on the user's instructions.

## Getting Started
### Requirements
- Python 3.6+
- TensorFlow or PyTorch (choose your preferred backend)
- Other dependencies (listed in requirements.txt)

### Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/TouchUp-AI.git
cd TouchUp-AI
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Usage
1. Run the main file app.py to start the TouchUp AI web application:
```bash
python app.py
```
2. Access the application through your web browser at the provided local address (e.g., http://127.0.0.1:7860).
3. Upload an image, crop it if needed.
4. Enter textual instructions for desired edits in the "Text Input" box, and set the editing power using the slider.
5. Click "Apply" to process the image based on your input.
6. View the edited image along with the original image for comparison.
7. Modify instructions and apply edits iteratively until satisfied with the result.

## Contributing
- We welcome contributions from the community! If you want to make any improvements or report issues, you are welcome. Just fork the repo, and make the pull request with your added features or optimized code. We'll check it out and merge if everything works fine.

#### Made with ♥ by [Ronak Sharma](https://github.com/Ronaknowal)
