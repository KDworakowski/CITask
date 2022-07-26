FROM python:3.9-alpine3.14
COPY . /app
RUN pip install -r requirements.txt
CMD python /app/main.py
