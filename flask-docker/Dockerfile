FROM python:3.8

ARG VERSION

LABEL org.label-schema.version=${VERSION}

RUN python3 -m pip install --upgrade pip

WORKDIR /ws
COPY ./requirements.txt /ws/requirements.txt


RUN pip install --no-cache-dir -r requirements.txt

# Flask 및 Werkzeug 패키지 업데이트
RUN pip install --no-cache-dir --upgrade flask
RUN pip install Werkzeug==0.16.1


COPY ./webapp/ /ws

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]