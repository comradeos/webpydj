FROM python:alpine3.16
ENV PYTHONUNBUFFERED=1
WORKDIR /sources
COPY required.txt .
RUN pip install --upgrade pip
RUN pip install -r required.txt
ENTRYPOINT [ "python" ]
CMD [ "manage.py", "runserver", "0.0.0.0:8000"]