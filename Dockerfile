FROM python:3.8.3-alpine3.12

WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./ ./

CMD ["python3", "-m", "app.main"]