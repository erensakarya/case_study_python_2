FROM python:3.8


COPY requirements.txt ./requirements.txt

COPY fugo_games_final_table.csv ./fugo_games_final_table.csv

COPY assets ./assets

COPY flask_app.py ./flask_app.py


RUN pip install -r requirements.txt


CMD ["python", "./flask_app.py"]