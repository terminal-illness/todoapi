FROM python:3.12
COPY src/ requirements /
WORKDIR /
RUN pip install -r requirements
CMD ["uvicorn", "app:app", "--reload"]