# fugo_games_case



the_moviedb_api python code finds out the TV Series which have the standarts like below;

  - May be watched in Turkey.
  - May only be watched in Amazon Prime Video platform.
  - Have at least 750 votes.
  - Have at least 8.4/10 like ratio.
  
database codes;
  
  - Create a database.
  - Create required tables
  - Import datas from .csv files to created tables. 
  
by using sqlite3 library.

flask_app is a flask/plotly/dash website which shows the final desired table.

Finally, Docker Image and Docker Container can be created by using below commands.

  - docker build -t flask_app -f Dockerfile .
  - docker run -d -p 8050:8050 --name flask_app flask_app
  
Cheers!
