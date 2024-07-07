FROM python:3.8

COPY ./requirements.txt /ws/requirements.txt

WORKDIR /ws

RUN pip install -r requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir flask==2.0.3 werkzeug==2.0.3

COPY ./webapp/ /ws

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]