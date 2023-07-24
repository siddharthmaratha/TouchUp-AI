---
title: TouchUp AI
emoji:  🐨
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 3.24.1
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

---

# TouchUp AI - Advanced Image Editing Model
TouchUp AI Logo

TouchUp AI is a powerful Python-based machine learning project designed to revolutionize image editing. This sophisticated model takes textual input from the user and utilizes deep learning algorithms to perform advanced image editing, allowing users to effortlessly enhance and modify their images with precision.

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
