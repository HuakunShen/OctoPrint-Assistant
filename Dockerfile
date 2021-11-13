FROM python:3.10.0-buster

COPY . /OctoPrint-Assistant/
WORKDIR /OctoPrint-Assistant/

ENV OCTOPRINT_PORT=5000
ENV OCTOPRINT_PROTOCOL=http

# these once must be passed
ENV OCTOPRINT_ADDRESS=raspberrypi.local
ENV OCTOPRINT_X_API_KEY=TODO
ENV API_KEY=api_key
ENV MASTER_NAME=Master
EXPOSE 8000

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000