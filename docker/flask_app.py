import pandas as pd
import dash
import dash_table
import dash_html_components as html
import flask

fugo_games_final_table = pd.read_csv('fugo_games_final_table.csv')


server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)

app.config.suppress_callback_exceptions = True
tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': 'rgb(230,0,0)',
    'color': 'white',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': 'PaleVioletRed',
    'color': 'white',
    'padding': '6px',
    'fontWeight': 'bold'
}

app.layout = html.Div([
    html.Div([
        html.H3('Fugo Games Case'),
        html.H4('''
        >>> SQL Tables' observation dashboard;
        '''),
        html.Img(
            src="https://www.fugo.com.tr/images/logo_256.png"),
    ], className='banner'),
    html.Div([
        dash_table.DataTable(id='datatable-interactivity',
                             columns=[
                                 {"name": ["Person_Id"], "id": "Person_Id", 'type': 'numeric', "deletable": True},
                                 {"name": ["Name"], "id": "Name", "deletable": True},
                                 {"name": ["Gender"], "id": "Gender", "deletable": True},
                                 {"name": ["Known_For"], "id": "Known_For", "deletable": True},
                                 {"name": ["Popularity"], "id": "Popularity", "deletable": True},
                                 {"name": ["TV_Show_Name_Involved"], "id": "TV_Show_Name_Involved", "deletable": True}
                             ],
                             data=fugo_games_final_table.to_dict('records'),
                             merge_duplicate_headers=True,
                             export_format='csv',
                             fixed_rows={'headers': True, 'data': 0},
                             style_cell={'padding': '10px',
                                         'backgroundColor': 'rgb(30,22,56)'},
                             style_table={'overflowX': 'scroll',
                                          'overflowY': 'scroll'},
                             style_header={
                                 'color': 'white',
                                 'backgroundColor': 'rgb(70,60,99)',
                                 'fontWeight': 'bold',
                                 'font-size': '14px',
                                 'textAlign': 'center',
                                 'border': '1px solid pink'
                             },
                             style_data={
                                 'color': 'white',
                                 'border': '1px solid pink'
                             },
                             style_data_conditional=[
                                 {
                                     'if': {'row_index': 'even'},
                                     'backgroundColor': 'rgb(45,36,72)',
                                 }
                             ],

                             style_cell_conditional=[
                                 {'if': {'column_id': 'Person_Id'},
                                  'width': '15%'},
                                 {'if': {'column_id': 'Name'},
                                  'width': '15%'},
                                 {'if': {'column_id': 'Gender'},
                                  'width': '15%'},
                                 {'if': {'column_id': 'Known_For'},
                                  'width': '15%'},
                                 {'if': {'column_id': 'Popularity'},
                                  'width': '15%'},
                                 {'if': {'column_id': 'TV_Show_Name_Involved'},
                                  'width': '15%'},
                             ],
                             style_filter={
                                 'backgroundColor': 'rgb(45,36,72)',
                                 'color': 'white',
                                 'fontWeight': 'bold',
                             },
                             editable=True,
                             filter_action="native",
                             sort_action="native",
                             sort_mode="multi",
                             row_deletable=True,
                             page_size=100),
    ])])

"""
Filtering Operators
operators = [['ge ', '>='],
             ['le ', '<='],
             ['lt ', '<'],
             ['gt ', '>'],
             ['ne ', '!='],
             ['eq ', '='],
             ['contains '],
             ['datestartswith ']]
"""

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True, port=8050)
