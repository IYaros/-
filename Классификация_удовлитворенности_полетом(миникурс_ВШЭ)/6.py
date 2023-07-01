import streamlit as st
import pandas as pd
import lightgbm as lgb
from PIL import Image
# Загрузка данных и обучение модели
df = pd.read_csv("df_features.csv")

# Map categorical features to integers
df['gender'] = df['gender'].map({'Male': 0, 'Female': 1})
df['customer_type'] = df['customer_type'].map({'Loyal Customer': 0, 'disloyal Customer': 1})
df['type_of_travel'] = df['type_of_travel'].map({'Business travel': 0, 'Personal Travel': 1})
df['class'] = df['class'].map({'Business': 0, 'Eco': 1, 'Eco Plus': 2})

# Separate features and target variable
y = df[['satisfaction']]
X = df[['gender', 'age', 'customer_type', 'type_of_travel', 'class',
        'flight_distance', 'departure_delay_in_minutes',
        'arrival_delay_in_minutes', 'inflight_wifi_service',
        'departure_arrival_time_convenient', 'ease_of_online_booking',
        'gate_location', 'food_and_drink', 'online_boarding', 'seat_comfort',
        'inflight_entertainment', 'on_board_service', 'leg_room_service',
        'baggage_handling', 'checkin_service', 'inflight_service',
        'cleanliness']]

# Initialize and train the model
model = lgb.LGBMClassifier(boosting_type='dart', learning_rate=0.2, n_estimators=200, num_leaves=30, categorical_feature=[0, 2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
model.fit(X, y)

# Заголовок и описание приложения
image = Image.open("8.jpg")
st.image(image)
st.write(
        """
        # Нам важно Ваше мнение
        Заполните нашу форму и мы станем лучше.
        """
    )


# Ввод данных пользователем
gender = st.selectbox("Пол", ("Мужской", "Женский"))
age = st.sidebar.slider("Возраст", min_value=1, max_value=80, value=20,
                            step=1)
customer_type = st.selectbox("Являетесь ли Вы лояльным клиентом?", ("Да", "Нет"))
type_of_travel = st.selectbox("Тип перелета", ("Личная поездка", "Деловая поездка"))
clas = st.selectbox("Класс", ("Эконом", "Эконом-плюс","Бизнес"))
flight_distance = st.number_input("Расстояние", min_value=80, max_value=500, value=100)
departure_delay_in_minutes = st.number_input("Задержка отправления", min_value=0, max_value=180, value=0)
arrival_delay = st.number_input("Задержка прибытия", min_value=0, max_value=180, value=0)

wifi_service = st.slider("Оценка Wi-Fi на борту", min_value=0, max_value=5, step=1)
time_convenience = st.slider("Удобство времени вылета/прилета", min_value=0, max_value=5, step=1)
online_booking = st.slider("Удобство онлайн-бронирования", min_value=0, max_value=5, step=1)
gate_location = st.slider("Расположение гейта", min_value=0, max_value=5, step=1)
food_and_drink = st.slider("Качество еды и напитков", min_value=0, max_value=5, step=1)
online_boarding = st.slider("Оценка онлайн-посадки", min_value=0, max_value=5, step=1)
seat_comfort = st.slider("Комфорт сидений", min_value=0, max_value=5, step=1)
entertainment = st.slider("Качество развлечений на борту", min_value=0, max_value=5, step=1)
service = st.slider("Качество обслуживания на борту", min_value=0, max_value=5, step=1)
legroom = st.slider("Простор для ног", min_value=0, max_value=5, step=1)
baggage_handling = st.slider("Обработка багажа", min_value=0, max_value=5, step=1)
checkin_service = st.slider("Обслуживание при регистрации", min_value=0, max_value=5, step=1)
inflight_service = st.slider("Обслуживание на борту", min_value=0, max_value=5, step=1)
cleanliness = st.slider("Чистота на борту", min_value=0, max_value=5, step=1)



# Кнопка для запуска модели
if st.button("Проверить модель"):

    translatetion = {
        "Мужской": 0,
        "Женский": 1,
        "Да": 0,
        "Нет": 1,
        "Эконом": 1,
        "Эконом-плюс": 2,
        "Бизнес": 0,
        "Личная поездка": 1,
        "Деловая поездка": 0
    }
    # Создаем DataFrame с пользовательскими данными
    user_data = pd.DataFrame({
        "gender": translatetion[gender],
        "age": [age],
        "customer_type": translatetion[customer_type],
        "type_of_travel": translatetion[type_of_travel],
        "class": translatetion[clas],
        "flight_distance": [flight_distance],
        "departure_delay_in_minutes": [departure_delay_in_minutes],
        "arrival_delay_in_minutes": [arrival_delay],
        "inflight_wifi_service": [wifi_service],
        "departure_arrival_time_convenient": [time_convenience],
        "ease_of_online_booking": [online_booking],
        "gate_location": [gate_location],
        "food_and_drink": [food_and_drink],
        "online_boarding": [online_boarding],
        "seat_comfort": [seat_comfort],
        "inflight_entertainment": [entertainment],
        "on_board_service": [service],
        "leg_room_service": [legroom],
        "baggage_handling": [baggage_handling],
        "checkin_service": [checkin_service],
        "inflight_service": [inflight_service],
        "cleanliness": [cleanliness]
    })

    # Применяем модель к данным пользователя и выводим результат
    prediction = model.predict(user_data)
    if prediction[0] == 0:
        result = "Извините за предоставленные неудобства, мы станем лучше"
    else:
        result = "Спасибо, что выбрали нашу авиакомпанию"

    st.write("Результат:", result)
