import gradio as gr

def clone(text, audio):
    return audio

iface = gr.Interface(fn=clone, 
                     inputs=["text",gr.Audio(type='filepath')], 
                     outputs=gr.Audio(type='filepath'))
iface.launch()