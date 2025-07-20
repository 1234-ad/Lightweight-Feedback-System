FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install flask flask_sqlalchemy flask_cors
CMD ["python", "app.py"]