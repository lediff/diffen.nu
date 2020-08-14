FROM python:3.7.2-stretch

LABEL key="Diffen"

COPY . requirements.txt /app/requirements.txt

WORKDIR /app

RUN apt update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

CMD python basic.py run -h 0.0.0.0