FROM alpine:3.6
MAINTAINER jsvazic@gmail.com

COPY . /app/

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
  && rm -rf /var/cache/apk/* \
  && /usr/bin/pip install -r /app/requirements.txt

WORKDIR /app/Tiredful-API

EXPOSE 8000

CMD ["/usr/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
