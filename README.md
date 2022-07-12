# Python Case Study - 2

In this repository, you may find some python codes in order to get data from themoviedb.org by using its own API and import these datas to a Database (Sqlite in my case).
Finally, a flask code sample for displaying the desired table in a website app.

Instructions;


1) the_moviedb_api python code finds out the TV Series which have the standarts like below.

    - May be watched in Turkey.
    - May only be watched in Amazon Prime Video platform.
    - Have at least 750 votes.
    - Have at least 8.4/10 like ratio.
  
  Besides, this code also finds out the cast, crew and director informations about the related TV Series.
  
  Finally, generates .csv files from the related datas.
  
  Important Note!
  -  If the API Key does not work, you should be creating your own key from http://api.themoviedb.org/.
  
  
2) database codes;
  
    - Create a database.
    - Create required tables.
    - Import datas from the .csv files to created tables. 
  
  by using sqlite3 library.


3) flask_app is a flask/plotly/dash website which shows the final desired table.

   Finally, Docker Image and Docker Container can be created by using below commands.

    - docker build -t flask_app -f Dockerfile .
    - docker run -d -p 8050:8050 --name flask_app flask_app
    
    
Cheers!
