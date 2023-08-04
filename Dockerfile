FROM python:3.10-slim

WORKDIR /forcespain

COPY requirements.txt /forcespain/ 

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /forcespain

CMD python3 main.py