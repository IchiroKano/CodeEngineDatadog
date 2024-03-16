FROM python:3
USER root
WORKDIR /usr
COPY . .
RUN pip3 install datadog-api-client
CMD [ "python", "./send-to-datadog.py" ]
