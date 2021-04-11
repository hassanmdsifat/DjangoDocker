FROM python:3.6.13-alpine3.13
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir RestApi
WORKDIR /RestApi
COPY ["requirements.txt", "."]
RUN ["pip", "install", "-r" ,"requirements.txt"]
COPY [".", "."]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]