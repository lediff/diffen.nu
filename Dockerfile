FROM python:3.7.2-stretch

LABEL key="Diffen"

COPY . /application/requirements.txt /application/requirements.txt

WORKDIR /application

RUN apt update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /application

CMD python basic.py run -h 0.0.0.0