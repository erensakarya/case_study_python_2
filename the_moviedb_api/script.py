import config
import requests
import pandas as pd

# config has been used to hide private api key.
api_key = config.tmdb_api_key

# An example url
"https://api.themoviedb.org/3/discover/tv?api_key=9af958bc4044d2aed502c3ed48597431&page=2&vote_average.gte=8.5&vote_count.gte=750&watch_region=TR"

base_url = "https://api.themoviedb.org/"
api_version = 3
api_path = "/discover/tv"

"""Finding the TV Shows
which have at least 750 votes
and at least 8.4 vote average
in Turkey at Amazon Prime Platform"""

additional_parameter = "&sort_by=vote_count.desc"
additional_parameter_2 = "&sort_by=vote_average.desc"
additional_parameter_3 = "&vote_count.gte=750"  # TV Shows have at least 750 unique votes.
additional_parameter_4 = "&vote_average.gte=8.4"  # TV Shows have greater than or equals to 8.4 vote_average.

"""
additional_parameter_5 = "&with_watch_providers=Amazon%20Prime%20Video"  # Filter for Amazon Prime Video as a provider.
additional_parameter_6 = "&watch_region=TR"  # Filter for Turkey as a country.
# Said that these filters has been added to API but it seems that they don't work properly.
# Therefore, I have used another GET Method below.
"""

# My whole url using f-string
endpoint = f"{base_url}{api_version}{api_path}?api_key={api_key}" \
           f"{additional_parameter_3}{additional_parameter_4}"

response = requests.get(endpoint)
desired_tv_shows_dictionary = response.json()

"""
print(desired_tv_shows_dictionary)
https://api.themoviedb.org/3/discover/tv?api_key=9af958bc4044d2aed502c3ed48597431&vote_count.gte=750&vote_average.gt=8.4&sort_by=vote_count.desc&sort_by=vote_average.desc
'total_pages': 2, 'total_results': 46!!!
"""

total_pages = desired_tv_shows_dictionary['total_pages']
total_results = desired_tv_shows_dictionary['total_results']

whole_desired_tv_shows_dictionary = list()
for page in range(1, total_pages + 1):
    endpoint = f"{base_url}{api_version}{api_path}?api_key={api_key}" \
               f"{additional_parameter_3}{additional_parameter_4}" \
               f"{additional_parameter}{additional_parameter_2}&page={page}"
    response = requests.get(endpoint)  # The response coming from api.
    desired_tv_shows_dictionary = response.json()  # The response has been stored as a json format.
    whole_desired_tv_shows_dictionary.append(desired_tv_shows_dictionary)

id_list = []
name_list = []
overview_list = []
number_of_seasons_list = []
number_of_episodes_list = []
popularity_list = []
vote_average_list = []
vote_count_list = []
first_air_date_list = []
last_air_date_list = []
status_list = []

for element in range(len(whole_desired_tv_shows_dictionary)):
    for element_2 in range(len(whole_desired_tv_shows_dictionary[element].get('results'))):
        id_list.append(whole_desired_tv_shows_dictionary[element].get('results')[element_2].get('id'))
        name_list.append(whole_desired_tv_shows_dictionary[element].get('results')[element_2].get('name'))
        overview_list.append(whole_desired_tv_shows_dictionary[element].get('results')[element_2].get('overview'))
        number_of_seasons_list.append(
            whole_desired_tv_shows_dictionary[element].get('results')[element_2].get('number_of_seasons'))
        number_of_episodes_list.append(
            whole_desired_tv_shows_dictionary[element].get('results')[element_2].get('number_of_episodes'))
        popularity_list.append(whole_desired_tv_shows_dictionary[element].get('results')[element_2].get('popularity'))
        vote_average_list.append(
            whole_desired_tv_shows_dictionary[element].get('results')[element_2].get('vote_average'))
        vote_count_list.append(whole_desired_tv_shows_dictionary[element].get('results')[element_2].get('vote_count'))
        first_air_date_list.append(
            whole_desired_tv_shows_dictionary[element].get('results')[element_2].get('first_air_date'))
        last_air_date_list.append(
            whole_desired_tv_shows_dictionary[element].get('results')[element_2].get('last_air_date'))
        status_list.append(whole_desired_tv_shows_dictionary[element].get('results')[element_2].get('status'))

df = pd.DataFrame(list(
    zip(name_list, id_list, overview_list, number_of_seasons_list, number_of_episodes_list, popularity_list,
        vote_average_list, vote_count_list, first_air_date_list, last_air_date_list, status_list)),
    index=range(1, total_results + 1),
    columns=['name', 'id', 'overview', 'number_of_seasons', 'number_of_episodes', 'popularity',
             'vote_average', 'vote_count', 'first_air_date', 'last_air_date', 'status'])

# for each of the desired TV Shows make an api call for that specific TV Show to return the parameters.
amazon_turkey_tv_series = list()
id_to_name_list = list()
for provider in id_list:
    provider_request = requests.get(
        'https://api.themoviedb.org/3/tv/' + str(provider) + '/watch/providers' + '?api_key=' + api_key)
    provider_request = provider_request.json()
    if provider_request['results'].get('TR') is not None and provider_request['results'].get('TR').get(
            'flatrate') is not None and provider_request['results'].get('TR').get('flatrate')[0].get('provider_name') == 'Amazon Prime Video':
        id_to_name_list.append(provider)
        amazon_turkey_tv_series.append(provider_request['results'].get('TR'))
    else:
        continue

preparation_for_final_list = list()
for i in df['id']:
    if i in id_to_name_list:
        preparation_for_final_list.append(df['name'][df.id == i].values.tolist())

final_tv_series_list = list()
for i in preparation_for_final_list:
    final_tv_series_list.append(i[0])

print("""
******************************************
Türkiye'de Amazon Prime Video Platformunda
en az 750 kez oylanmış ve en az 8.4 ortalama
beğeni kazanmış TV Dizileri;
{}
******************************************
""".format(final_tv_series_list))

# Cast and Crew session

cast_id_list, cast_name_list, cast_gender_list, cast_known_for_department_list, cast_popularity_list = list(), list(), list(), list(), list()
crew_id_list, crew_name_list, crew_gender_list, crew_known_for_department_list, crew_popularity_list = list(), list(), list(), list(), list()
cast_connection_for_all_tables_list = list()
crew_connection_for_all_tables_list = list()

for cast_and_crew in id_to_name_list:
    cast_and_crew_request = requests.get(
        'https://api.themoviedb.org/3/tv/' + str(cast_and_crew) + '/credits' + '?api_key=' + api_key)
    cast_and_crew_request = cast_and_crew_request.json()
    for element in range(len(cast_and_crew_request.get('cast'))):
        cast_id_list.append(cast_and_crew_request.get('cast')[element].get('id'))
        cast_name_list.append(cast_and_crew_request.get('cast')[element].get('original_name'))
        cast_gender_list.append(cast_and_crew_request.get('cast')[element].get('gender'))
        cast_known_for_department_list.append(cast_and_crew_request.get('cast')[element].get('known_for_department'))
        cast_popularity_list.append(cast_and_crew_request.get('cast')[element].get('popularity'))
        cast_connection_for_all_tables_list.append(cast_and_crew)
    for element in range(len(cast_and_crew_request.get('crew'))):
        crew_id_list.append(cast_and_crew_request.get('crew')[element].get('id'))
        crew_name_list.append(cast_and_crew_request.get('crew')[element].get('original_name'))
        crew_gender_list.append(cast_and_crew_request.get('crew')[element].get('gender'))
        crew_known_for_department_list.append(cast_and_crew_request.get('crew')[element].get('known_for_department'))
        crew_popularity_list.append(cast_and_crew_request.get('crew')[element].get('popularity'))
        crew_connection_for_all_tables_list.append(cast_and_crew)

df_cast = pd.DataFrame(
    list(zip(cast_id_list, cast_name_list, cast_gender_list, cast_known_for_department_list, cast_popularity_list,
             cast_connection_for_all_tables_list)),
    index=range(1, len(cast_name_list) + 1),
    columns=['id', 'name', 'gender', 'known_for_department', 'popularity', 'tv_show_id_played'])

df_crew = pd.DataFrame(
    list(zip(crew_id_list, crew_name_list, crew_gender_list, crew_known_for_department_list, crew_popularity_list,
             crew_connection_for_all_tables_list)),
    index=range(1, len(crew_name_list) + 1),
    columns=['id', 'name', 'gender', 'known_for_department', 'popularity', 'tv_show_id_involved'])

# Save as .csv files the dataframes.
df.to_csv(r'***\fugo_games_case\database\tv_shows.csv', index=False)
df_cast.to_csv(r'***\fugo_games_case\database\cast.csv', index=False)
df_crew.to_csv(r'***\fugo_games_case\database\crew.csv', index=False)

# We have found that there are 4 directors (Bryan Singer,Ira Hurvitz, Ken Kwapis, Philip Sgriccia) for these 3 TV Series.
# So we have to do another get request whether they directed another TV Series or not and how many episodes directed etc...


director_name_list = ['Bryan Singer', 'Ira Hurvitz', 'Ken Kwapis', 'Philip Sgriccia']
directors_dictionary = {9032: [{'tv_show_names': [], 'episode_count': [], 'director_id': []}],
                        1533790: [{'tv_show_names': [], 'episode_count': [], 'director_id': []}],
                        29009: [{'tv_show_names': [], 'episode_count': [], 'director_id': []}],
                        1225933: [{'tv_show_names': [], 'episode_count': [], 'director_id': []}]}

for director in directors_dictionary.keys():
    director_request = requests.get(
        'https://api.themoviedb.org/3/person/' + str(director) + '/tv_credits' + '?api_key=' + api_key)
    director_request = director_request.json()

    for element in range(len(director_request.get('crew'))):
        if director_request.get('crew')[element].get('job') == "Director":
            directors_dictionary.get(director)[0]['director_id'].append(str(director))
            directors_dictionary.get(director)[0]['tv_show_names'].append(
                director_request.get('crew')[element].get('name'))
            directors_dictionary.get(director)[0]['episode_count'].append(
                director_request.get('crew')[element].get('episode_count'))
        else:
            continue

directors_df_1 = pd.DataFrame.from_dict(directors_dictionary.get(9032)[0])
directors_df_2 = pd.DataFrame.from_dict(directors_dictionary.get(1533790)[0])
directors_df_3 = pd.DataFrame.from_dict(directors_dictionary.get(29009)[0])
directors_df_4 = pd.DataFrame.from_dict(directors_dictionary.get(1225933)[0])

frames = [directors_df_1, directors_df_2, directors_df_3, directors_df_4]

directors_df = pd.concat(frames)

directors_df.to_csv(r'***\database\directors.csv',
                    index=False)
