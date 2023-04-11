import gradio as gr
from help_function import help_function
from PIL import Image
import numpy as np

model_helper = help_function()

def greet(image,text,power):
    PIL_image = Image.fromarray(np.uint8(image)).convert('RGB')
    image_edit = model_helper.image_from_text(text,PIL_image,power)
    return image_edit

description = "demo for model to edit face with text, you can see the [github repo CelebrityLook](https://github.com/amit154154/CelebrityLook) \n" \
              "note that the model is in alpha version, so it's not perfect, but it's fun to play with it, some guidelines:\n " \
              "1. the image you give the model need to be aligin to the camera such that your eyes are infront of the camera\n" \
              "2.play with the power of the text and the text itself, it will look like 💩 sometimes" \

title = "FaceOver - edit face with text 🐨 "

examples = [
    ["examples/jennifer lawrence.jpg", "dark hair smiling woman with glasses", 0.58],
    ["examples/thanos.jpg", "woman with pink wig and big hat", 0.88],
    ["examples/kim kardashian.jpg", "woman with pink wig",1.15],
    ["examples/kim kardashian.jpg", "beautiful asian woman with short haired ", 0.88],
    ["examples/Arnold Schwarzenegger.jpg", "happy man with long hair and hat", 0.44],
    ["examples/varundhawan.jpg", "man wearing black sunglasses", 0.9]
]

iface = gr.Interface(fn=greet,
                     inputs=["image", "text", gr.inputs.Slider(0.0, 1.5)],
                     outputs="image",
                     title=title,
                     description=description,
                     cache_examples=False,
                     examples=examples
                     )
iface.launch()