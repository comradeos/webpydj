FROM python:alpine3.16
ENV PYTHONUNBUFFERED=1
WORKDIR /sources
COPY requires.txt .
RUN pip install --upgrade pip
RUN pip install -r requires.txt
ENTRYPOINT [ "python" ]
CMD [ "manage.py", "runserver", "0.0.0.0:8000"]