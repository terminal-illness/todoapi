FROM python:3.12
COPY src/ requirements /
WORKDIR /
RUN pip install -r requirements
EXPOSE 8000
CMD ["python", "app.py"]