FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9


COPY ./app /app
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
