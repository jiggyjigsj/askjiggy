FROM python:alpine

RUN apk --upgrade add bash

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
RUN chmod +x /app/run.sh

ENTRYPOINT [ "/app/run.sh" ]
