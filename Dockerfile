FROM python:3.11-alpine
WORKDIR /app
COPY . /app
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "-w 4", "-b :8000", "app:flask_app"]
