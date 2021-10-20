# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /project
COPY ./project/requirements.txt /project/
RUN pip install -r requirements.txt
COPY . /project/

CMD ["python", "manage.py", "makemigrations", "search"]
CMD ["python", "manage.py", "migrate", "search"]
CMD ["python", "manage.py", "loaddata", "search/fixtures/data.json"]