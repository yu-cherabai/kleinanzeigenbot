FROM python:3.8

ADD src .
ADD requirements.txt .

RUN apt-get -y update
RUN apt-get -y upgrade
RUN pip install -r requirements.txt

CMD [ "python3", "./main.py" ]
