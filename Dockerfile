FROM python:3.7

ENV FLASK_APP=app

WORKDIR /app

COPY Pipfile Pipfile.lock .

RUN pip install pipenv
RUN pipenv install --system

COPY . .

CMD ["python", "app.py"]
