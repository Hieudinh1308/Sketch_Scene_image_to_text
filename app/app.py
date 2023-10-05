from transformers import AutoProcessor
from transformers import AutoModelForCausalLM
import streamlit as st 
from PIL import Image

checkpoint = "microsoft/git-base"
processor = AutoProcessor.from_pretrained(checkpoint)

checkpoint = "hieudinhpro/git-base-on-diffuision-dataset2"
model = AutoModelForCausalLM.from_pretrained(checkpoint)

st.title("Sketch Scene image to text")

st.markdown('''
    :red[Input] :orange[image] :green[file]  .''')

img = st.file_uploader("_", type=['png','jpg','jpeg'])

if img :
    images=Image.open(img)
    st.image(images)

    inputs = processor(images=images, return_tensors="pt")
    pixel_values = inputs.pixel_values

    generated_ids = model.generate(pixel_values=pixel_values, max_length=50)
    generated_caption = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    st.subheader(f'Predict:  :blue[{generated_caption}]')
     
