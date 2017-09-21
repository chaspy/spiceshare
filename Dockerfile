FROM python:3.5.4-alpine
MAINTAINER Takeshi KONDO <take.she12@gmail.com>

RUN apk --update add git && rm -rf /var/cache/apk/*
RUN git clone https://github.com/takeshe12/spiceshare.git

WORKDIR spiceshare
RUN pip install -r requirements.txt -r test_requirements.txt

CMD python spiceshare/app.py
