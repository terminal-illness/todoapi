FROM python:3.12
COPY . /
WORKDIR /
RUN pip install -r requirements
CMD ["uvicorn", "app:app --reload"]