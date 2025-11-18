FROM python:3.13.5-slim-bookworm

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN pip install . 

COPY predict.py .
COPY model ./model

EXPOSE 9696

ENTRYPOINT [ "waitress-serve", "--listen=0.0.0.0:9696", "predict:app" ]

