# Use uma imagem base do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código-fonte para o container
COPY . .

# Expõe a porta do FastAPI (8000)
EXPOSE 8000

# Comando para rodar o serviço
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
