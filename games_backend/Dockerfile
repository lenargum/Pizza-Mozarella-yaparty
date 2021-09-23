FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
EXPOSE 8000
COPY ./app/requirements.txt /app/
RUN pip install -r requirements.txt
RUN pip install uvicorn[standard]
COPY ./app /app
CMD ["python3", "main.py"]