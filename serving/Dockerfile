FROM pytorch/pytorch:2.3.0-cuda11.8-cudnn8-runtime
 
WORKDIR /app
 
COPY . .
 
RUN pip install -r requirements.txt
 
ENTRYPOINT [ "gunicorn", "main:app", "-c", "gunicorn_config.py" ]