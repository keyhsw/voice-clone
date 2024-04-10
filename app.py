import gradio as gr

def clone(text, audio):
    return audio

iface = gr.Interface(fn=clone, 
                     inputs=["text","audio"], 
                     outputs="audio")
iface.launch()