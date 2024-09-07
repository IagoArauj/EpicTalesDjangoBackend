# Use a imagem oficial do Python como base
FROM python:3.11.9

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de dependências
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação
COPY . .

# Exponha a porta que o Django vai usar
EXPOSE 8000

# Defina o comando para iniciar o Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
