ARG BUILD_IMAGE=python:3.12.3

FROM ${BUILD_IMAGE} as base-build

WORKDIR /src

COPY requirements.txt /src/
RUN pip install --upgrade && pip install -r requirements.txt

COPY src /src

RUN pytest

USER root
RUN chmod u+x /src/gunicorn.sh

RUN useradd -ms /bin/sh admin
USER admin

EXPOSE 8080

ENTRYPOINT [ "sh", "/src/gunicorn.sh" ]