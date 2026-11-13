import streamlit as st

st.title("Загрузка изображения")

uploaded_file = st.file_uploader("Выберите фотографию", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Загруженное фото", use_container_width=True)
    
    if st.button("Отправить"):
        st.success("Успешно сожгли вместе с медведем!")
