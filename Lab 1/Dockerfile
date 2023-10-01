FROM --platform=linux/amd64 python:3.8

RUN touch /var/run/uwsgi-touch-reload

COPY lab1.py .
COPY *.23o .

RUN pip install georinex
RUN pip install matplotlib
RUN pip install pandas==0.25.3
RUN pip install numpy==1.20
RUN pip install xarray==0.12.1

CMD [ "python", "lab1.py" ]
