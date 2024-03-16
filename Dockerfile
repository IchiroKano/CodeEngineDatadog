FROM python:3
USER root
WORKDIR /usr
ARG DD-API-KEY
ENV DD_API_KEY $DD_API_KEY
COPY . .
RUN pip3 install datadog-api-client
CMD [ "python", "./send-to-datadog.py" ]
