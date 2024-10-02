import streamlit as st
from PIL import Image
import io
import os

st.markdown("<h1 style='text-align: center;'>Image Editor and Converter</h1>", unsafe_allow_html=True)

image_file = st.file_uploader("Upload Your Image", type=["png", "jpg", "jpeg", "webp", "ico"])

info = st.empty()
size = st.empty()
format_ = st.empty()

if image_file:
    img = Image.open(image_file)

    info.markdown("<h3 style='text-align: center;'>Image Information</h3>", unsafe_allow_html=True)
    size.markdown(f"**Size:** {img.size[0]}x{img.size[1]} pixels")
    format_.markdown(f"**Format:** {img.format if img.format else 'Unknown'}")  # Tratamento para formato desconhecido
    
    st.image(img, caption="Uploaded Image", use_column_width=True)
    
    st.markdown("<h3 style='text-align: center;'>Edit Image</h3>", unsafe_allow_html=True)
    
    width = st.number_input("Width", value=img.size[0], min_value=1)
    height = st.number_input("Height", value=img.size[1], min_value=1)

    degree = st.number_input("Degree (Rotation)", value=0, min_value=0, max_value=360)

    filters = st.selectbox("Filters", options=["None", "Grayscale", "Sepia"])

    st.markdown("<h3 style='text-align: center;'>Convert Image Format</h3>", unsafe_allow_html=True)
    format_conversion = st.selectbox("Choose format to convert", options=["Not Convert", "PNG", "JPEG", "WEBP", "ICO"])

    if st.button("Submit"):
        img = img.resize((width, height)).rotate(degree)

        if filters == "Grayscale":
            img = img.convert("L")
        elif filters == "Sepia":
            sepia = [(r * 240 // 255, g * 200 // 255, b * 145 // 255) for r, g, b in img.getdata()]
            img.putdata(sepia)

        st.image(img, caption="Edited Image", use_column_width=True)

        original_filename = os.path.splitext(image_file.name)[0]

        if format_conversion == "Not Convert":
            output_format = img.format.lower() if img.format else 'png'  # Se o formato for None, usar PNG como fallback
        else:
            output_format = format_conversion.lower()

        img_buffer = io.BytesIO()

        if output_format:
            img.save(img_buffer, format=output_format.upper())
        else:
            img.save(img_buffer, format='PNG')

        img_buffer.seek(0)

        if format_conversion == "Not Convert":
            new_filename = image_file.name
        else:
            new_filename = f"{original_filename}.{output_format}"

        st.download_button(
            label="Download Edited and Converted Image",
            data=img_buffer,
            file_name=new_filename,
            mime=f"image/{output_format if output_format else 'png'}"
        )
