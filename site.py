import random
import streamlit as st

st.title("Определитель ориентации")

RESULTS = [
    "Гетеросексуал",
    "Гомосексуал",
    "Бисексуал",
    "Пансексуал",
    "Асексуал"
]

uploaded_file = st.file_uploader("Загрузите любую картинку", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Загруженное фото", use_container_width=True)
    
    if st.button("Узнать результат"):
        choice = random.choice(RESULTS)
        st.success(f"Результат: {choice}")

