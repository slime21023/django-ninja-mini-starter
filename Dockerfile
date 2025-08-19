FROM public.ecr.aws/docker/library/python:3.12-alpine3.21

WORKDIR /app
COPY . /app


RUN pip install uvicorn \
    && pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "src.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
