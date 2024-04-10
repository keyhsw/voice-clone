import spaces
import gradio as gr
import torch
from TTS.api import TTS
import os
os.environ["COQUI_TOS_AGREED"] = "1"

device = "cuda"

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

@spaces.GPU(enable_queue=True)
def clone(text, audio):
    tts.tts_to_file(text=text, speaker_wav=audio, language="en", file_path="./output.wav")
    return "./output.wav"

iface = gr.Interface(fn=clone, 
                     inputs=["text",gr.Audio(type='filepath')], 
                     outputs=gr.Audio(type='filepath'),
                     title='Voice Clone',
                     description="""
                     by [Tony Assi](https://www.tonyassi.com/)
                     
                     Please ❤️ this Space. I build custom AI apps for companies. <a href="mailto: tony.assi.media@gmail.com">Email me</a> for business inquiries.
                     """,
                     theme = gr.themes.Base(primary_hue="teal",secondary_hue="teal",neutral_hue="slate"))
iface.launch()