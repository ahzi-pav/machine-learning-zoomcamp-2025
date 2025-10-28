FROM agrigorev/zoomcamp-model:2025

# add your stuff here

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN pip install . 

COPY predict.py .
COPY models ./models

EXPOSE 9696

ENTRYPOINT [ "waitress-serve", "--listen=0.0.0.0:9696", "predict:app" ]

