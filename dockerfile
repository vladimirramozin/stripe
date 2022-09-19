FROM python:3.7-slim

WORKDIR /app

COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./backend/ ./

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "&"]
