FROM python:3.11.9-alpine3.20
RUN mkdir -p /etc/app
WORKDIR /etc/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt
COPY main.py .
COPY model.py .
COPY utility.py .
EXPOSE 5000
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=5000", "--workers=4"]
