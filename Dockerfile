FROM python:3.9-slim
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt
COPY ./ /code/
EXPOSE 5000
# Start the FastAPI application
CMD ["python", "main.py", "--host", "0.0.0.0", "--port", "5000", "--reload"]