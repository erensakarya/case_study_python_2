FROM python:3.8
COPY requirements.txt ./requirements.txt
COPY final_table.csv ./final_table.csv
COPY assets ./assets
COPY flask_app.py ./flask_app.py
RUN pip install -r requirements.txt
CMD ["python", "./flask_app.py"]
