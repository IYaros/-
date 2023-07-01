mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[deprecation]\n\
showfileUploaderEncoding = false\n\
" > ~/.streamlit/config.toml

# Копируем файл df_features.csv в папку data
mkdir data
cp df_features.csv data/

# Копируем папку data
cp -R data ~/.streamlit/

# Установка необходимых зависимостей
pip install -r requirements.txt