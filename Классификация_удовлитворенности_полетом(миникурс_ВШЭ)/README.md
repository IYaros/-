# Классификация удовлитворенности авикомпанией
# Содержание
- Подготовка данных
- Построение моделей
- Тестирование модели
- Вывод
- Создание веб серивиса streamlit
# Описание проекта
Я работаю в авикомпании, моя цель подобрать модель, определяющую степень удовлитворенности клиента авиакомпнии и
 разработать веб сервис с опросом для клиентов, чтобы улучшить свои слабые места.


# Описание данных

# Целевая переменная

- satisfaction: удовлетворенность клиента полетом, бинарная (satisfied или neutral or dissatisfied)

# Признаки

- Gender (categorical: Male или Female): пол клиента
- Age (numeric, int): количество полных лет
- Customer Type (categorical: Loyal Customer или disloyal Customer): лоялен ли клиент авиакомпании?
- Type of Travel (categorical: Business travel или Personal Travel): тип поездки
- Class (categorical: Business или Eco, или Eco Plus): класс обслуживания в самолете
- Flight Distance (numeric, int): дальность перелета (в милях)
- Departure Delay in Minutes (numeric, int): задержка отправления (неотрицательная)
- Arrival Delay in Minutes (numeric, int): задержка прибытия (неотрицательная)
- Inflight wifi service (categorical, int): оценка клиентом интернета на борту
- Departure/Arrival time convenient (categorical, int): оценка клиентом удобство времени прилета и вылета
- Ease of Online booking (categorical, int): оценка клиентом удобства онлайн-бронирования
- Gate location (categorical, int): оценка клиентом расположения выхода на посадку в аэропорту
- Food and drink (categorical, int): оценка клиентом еды и напитков на борту
- Online boarding (categorical, int): оценка клиентом выбора места в самолете
- Seat comfort (categorical, int): оценка клиентом удобства сиденья
- Inflight entertainment (categorical, int): оценка клиентом развлечений на борту
- On-board service (categorical, int): оценка клиентом обслуживания на борту
- Leg room service (categorical, int): оценка клиентом места в ногах на борту
- Baggage handling (categorical, int): оценка клиентом обращения с багажом
- Checkin service (categorical, int): оценка клиентом регистрации на рейс
- Inflight service (categorical, int): оценка клиентом обслуживания на борту
- Cleanliness (categorical, int): оценка клиентом чистоты на борту

# Статус проекта: завершен.
# Вывод: Все модели показали высокие метрики F1, однако более хорошие метрики полноты, точности и AUC-ROC показада модель LGB. На тестовых данных F1_score 0.89, отличный результат. Веб сервис также исправно работает