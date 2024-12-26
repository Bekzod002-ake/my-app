import streamlit as st
import pandas as pd
import pickle


with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
 



# Sarlavha
st.title("Olmos narxini bashorat qilish")

# Kiruvchi ma'lumotlar uchun foydalanuvchi interfeysi
st.header("Kiritish uchun parametrlar")

def user_input_features():
    karat = st.number_input("Karat (Olmos kesimining karat qiymati)", min_value=0.0, max_value=5.0, step=0.01)
    
    cut_options = ['Ideal', 'Premium', 'Juda yaxshi', 'Yaxshi', 'Adolatli']
    cut = st.selectbox("Olmos kesimi turi", cut_options)
    cut_index = cut_options.index(cut)   # Index 1-dan boshlanadi
    
    color_options = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
    color = st.selectbox("Olmos rangi", color_options)
    color_index = color_options.index(color)   # Index 1-dan boshlanadi
    
    clarity_options = ['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1']
    clarity = st.selectbox("Olmos aniqligi", clarity_options)
    clarity_index = clarity_options.index(clarity)  # Index 1-dan boshlanadi
    
    depth = st.number_input("Chuqurlik (foizda)", min_value=50.0, max_value=80.0, step=0.1)
    table = st.number_input("Stolning yuzasi", min_value=50.0, max_value=80.0, step=0.1)
    x = st.number_input("Kenglik (mm)", min_value=0.0, max_value=10.0, step=0.1)
    y = st.number_input("Uzunlik (mm)", min_value=0.0, max_value=10.0, step=0.1)
    z = st.number_input("Balandlik (mm)", min_value=0.0, max_value=10.0, step=0.1)
    
    # Ma'lumotlarni DataFrame ko'rinishida saqlash
    data = {
        'carat': karat,
        'cut': cut_index,  # Index qiymati saqlanadi
        'color': color_index,  # Index qiymati saqlanadi
        'clarity': clarity_index,  # Index qiymati saqlanadi
        'depth': depth,
        'table': table,
        'x': x,
        'y': y,
        'z': z
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Bashorat qilish
if st.button("Narxni bashorat qilish"):
    prediction = model.predict(input_df)
    st.subheader(f"Bashorat qilingan narx: ${prediction[0][0]:,.2f}")