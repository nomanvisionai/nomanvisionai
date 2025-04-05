import gradio as gr
from rembg import remove
from PIL import Image

def remove_bg(image):
    output = remove(image)
    return output

with gr.Blocks() as demo:
    gr.Markdown("# Noman Vision AI\n### Developed by Abdullah-Al Noman")

    with gr.Tab("1. Background Remover"):
        gr.Interface(fn=remove_bg, inputs=gr.Image(type="pil"), outputs="image").render()

demo.launch()
