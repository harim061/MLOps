FROM python:3.8

ARG VERSION

LABEL org.label-schema.version=${VERSION}

RUN python3 -m pip install --upgrade pip

COPY ./requirements.txt /ws/requirements.txt

WORKDIR /ws

RUN pip install -r requirements.txt

# Werkzeug 패키지 업데이트
RUN pip install --upgrade Werkzeug

COPY ./webapp/ /ws

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]