import streamlit as st
import pickle


# Membaca Model
model_cancer = pickle.load(open('Diabates_Model.sav', 'rb'))


st.title("Prediksi Diabetes Dengan Algoritma Random Forest")
col1, col2 = st.columns(2)


with col1 :
    pregnancies = st.number_input('pregnancies', 0)

with col2 :
    glucose = st.number_input('glucose', 0)

with col1 :
    bloodspressure = st.number_input('bloodspressure', 0)

with col2 :
    skinthickness = st.number_input('skinthickness', 0)

with col1 :
    insulin = st.number_input('insulin', 0)
with col2 :
    bmi = st.number_input('bmi', 0)

with col1 :
    diabetespedigreefunction = st.number_input('diabetespedigreefunction', 0)
with col2 :
    age = st.number_input('age', 0)


if st.button('Prediksi') :
    # Diaknosis
    diaknosis = ''

    # Menjalankan Model
    prediksi = model_cancer.predict([[pregnancies, glucose, bloodspressure, skinthickness, insulin, bmi, diabetespedigreefunction, age]])

    if(prediksi[0] != 0) :
        diaknosis = 'Anda Tidak Terkena Diabetes'
    else :
        diaknosis = 'Anda Terkena Diabetes'

    st.success(diaknosis)
