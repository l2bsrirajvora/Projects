from dash import Dash, html, dcc
import datetime as dt

app = Dash(__name__)
server = app.server

app.layout = html.Div(style={'backgroundColor': 'lavenderblush'}, children=[
    html.Div([
        html.H1(
            children="Welcome to the Stock Dash App!", 
            style={
                'textAlign': 'center',
                'color': 'midnightblue'
            }
        ),
        html.Div(
            style={
            'display': 'flex',
            'flex-direction': 'column',
            'width': '25vw',
            'padding': '10',
            'justify-content': 'flex-start'},
            children=[
            html.Div([                
                html.H3(
                    children="Input Stock Code:",
                ),            
                html.Div([
                    html.Div([
                        dcc.Input(id="stock-code", type="text", placeholder="Stock Code", style={'font-size': '14px'}),
                        html.Button('Submit', id='Submit-button', style={'font-size': '14px', 'margin-right': '20px'}, n_clicks=0)
                    ])
                ])
            ]),
            html.Div([
                html.H3(
                    children="Enter Date Range:"
                ),
                dcc.DatePickerRange(
                    id="date-range-picker",
                    max_date_allowed=dt.date.today(),
                    style={'font-size': '14px'}                
                ),
                html.Div([
                    html.Br(),
                    html.Button('Stock Price', id='Stock-Price', style={'font-size': '14px', 'width': '100px', 'height': '50px', 'margin-right': '20px'}),
                    html.Button('Indicators', id='Indicators', style={'font-size': '14px', 'width': '100px', 'height': '50px', 'margin-right': '20px'}),
                    html.Br(),
                    html.Br(),
                    dcc.Input(id="Number-of-Days", type="number", placeholder="Number of Days", style={'font-size': '14px'}),
                    html.Br(),
                    html.Br(),
                    html.Button('Forecast', id='Forecast', style={'font-size': '14px', 'width': '100px', 'height': '50px', 'margin-right': '20px'})
                ])
            ]),
        ],
        className="nav"        
        ),
    html.Div([
        html.Div([
            # Logo
            # Company Name
        ],
        className="header"),
        html.Div(
            # Description
            id="description", className="description_ticker"
        ),
        html.Div([
            # Stock price plot
        ], id="graphs-content"),
        html.Div([
            # Indicator Plot
        ], id='main-content'),
        html.Div([
            # Forecast plot
        ], id="forecast-content")
    ], className="content")
], className='container')
])


if __name__ == '__main__':
    app.run_server(debug=True)

