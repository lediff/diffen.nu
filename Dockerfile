FROM python:3.7.2-stretch

LABEL key="Diffen"

#COPY . /application/requirements.txt /application/requirements.txt
COPY . /application

WORKDIR /application

RUN apt update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt



CMD python app.py run -h 0.0.0.0