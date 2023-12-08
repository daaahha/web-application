import streamlit as st
import pandas as pd
from keras.models import load_model


# Загрузка обученной модели из файла
model = load_model('model (1).h5')

# Заголовок и описание приложения
st.title("Предсказание цены на автомобиль")
st.write("Это веб-приложение использует обученную модель нейронной сети для предсказания цены автомобиля. НО: для дальнейшей работы нашего веб-приложения нужно посмотреть смешной мем")

# Загрузка и отображение видео
video_path = "cat.mp4"
st.video(video_path)

# Поля для ввода значений
year = st.number_input("Введите год выпуска", min_value=1900, max_value=2023)
mileage = st.number_input("Введите текущий пробег автомобиля", min_value=0)
tax = st.number_input("Введите налог на автомобиль", min_value=0.0)
mpg = st.number_input("Введите количество миль на галлон", min_value=0.0)
engineSize = st.number_input("Введите объем двигателя", min_value=0.0)
transmission = st.selectbox("Выберите тип коробки передач", ['Automatic', 'Manual', 'Semi-Auto'])
fuelType = st.selectbox("Выберите тип топлива", ['Diesel', 'Petrol'])

def preprocess_input_for_prediction(year, mileage, tax, mpg, engineSize, transmission, fuelType):
    features = pd.DataFrame({
        'Year': [year],
        'Mileage': [mileage],
        'Tax': [tax],
        'MPG': [mpg],
        'EngineSize': [engineSize],
        'Automatic': [int(transmission == 'Automatic')],
        'Manual': [int(transmission == 'Manual')],
        'Semi-Auto': [int(transmission == 'Semi-Auto')],
        'Diesel': [int(fuelType == 'Diesel')],
        'Petrol': [int(fuelType == 'Petrol')]
    })
    return features

# Функция обратного масштабирования
def inverse_scale(prediction, min_val, max_val):
    prediction = prediction * (max_val - min_val) + min_val
    return prediction

def predict_price(features):
    prediction = model.predict(features)[0][0]  # Предсказание цены
    return prediction
    
# Обработка пользовательского ввода и предсказание цены автомобиля
preprocessed_features = preprocess_input_for_prediction(year, mileage, tax, mpg, engineSize, transmission, fuelType)
if st.button("Предсказать цену"):
    prediction = predict_price(preprocessed_features)
    
    # Загрузка сохраненных значений минимальной и максимальной цены
    price_min = 899
    price_max = 69994
    # Применение обратного масштабирования
    predicted_price = inverse_scale(prediction, price_min, price_max)
    
    st.write("Предсказанная цена:", predicted_price)
   
# Загрузка и отображение видео
image_path = "мем.jpg"
st.image(image_path)

st.markdown('''
    :rainbow[Спасибо] :rainbow[за] :rainbow[внимание!] :rainbow[Надеюсь] :rainbow[вам]
    :rainbow[все] :rainbow[100 баллов].''')