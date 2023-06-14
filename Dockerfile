FROM python:3.10-slim

WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./project /usr/src/app

CMD ["uvicorn", "project.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
