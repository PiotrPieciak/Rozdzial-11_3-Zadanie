from dash import dcc
from dash import html
import plotly.graph_objects as go

def render_tab(df):

#    layout = html.Div([html.H1('Kanały sprzedaży',style={'text-align':'center'}),
#                        html.Div([dcc.DatePickerRange(id='chanel-range',
#                        start_date=df['tran_date'].min(),
#                        end_date=df['tran_date'].max(),
#                        display_format='YYYY-MM-DD')],style={'width':'100%','text-align':'center'}),
#                        html.Div([html.Div([dcc.Graph(id='bar-chanel')],style={'width':'50%'}),
#                        html.Div([dcc.Dropdown(id='chanel_dropdown',
#                            options=[{'label':prod_cat,'value':prod_cat} for prod_cat in df['prod_cat'].unique()],
#                            value=df['prod_cat'].unique()[0]),
#                            dcc.Graph(id='barh-chanel-subcat')],style={'width':'50%'})],style={'display':'flex'})
#                        ])   

# 
    layout = html.Div([html.H1('Kanały sprzedaży',style={'text-align':'center'}),
                        html.Div([dcc.DatePickerRange(id='chanel-range',
                        start_date=df['tran_date'].min(),
                        end_date=df['tran_date'].max(),
                        display_format='YYYY-MM-DD')],style={'width':'100%','text-align':'left'}),
                        html.Div([html.Div([dcc.Graph(id='bar-chanel')],style={'width':'50%'}),
                        html.Div([dcc.Dropdown(id='chanel_dropdown',
                            options=[{'label':Store_type,'value':Store_type} for Store_type in df['Store_type'].unique()],
                            value=df['Store_type'].unique()[0]),
                            dcc.Graph(id='barh-chanel-subcat')],style={'width':'50%'})],style={'display':'flex'})
                        ])   


    return layout