import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from Visualisations_CheckIn import fig_checkin_family_size, fig_checkin_land_rights, fig_checkin_children_school, fig_checkin_meals_per_day, fig_checkin_annual_income, fig_checkin_cultivated_land, fig_checkin_production_size, fig_checkin_pest_management, fig_checkin_production_status
from Visualisations_Initial import fig_initial_family_size, fig_initial_land_rights, fig_initial_children_school, fig_initial_meals_per_day, fig_initial_annual_income, fig_initial_cultivated_land, fig_initial_production_size, fig_initial_pest_management, fig_initial_production_status

# Setup the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Comparative Data Visualizations'),
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Social Details', children=[
            html.H2('Initial vs Check-in Family Size'),
            html.Div([
                dcc.Graph(figure=fig_initial_family_size),
                dcc.Graph(figure=fig_checkin_family_size)
            ], style={'display': 'flex', 'justifyContent': 'space-between'}),

            html.H2('Initial vs Check-in Land Rights'),
            html.Div([
                dcc.Graph(figure=fig_initial_land_rights),
                dcc.Graph(figure=fig_checkin_land_rights)
            ], style={'display': 'flex', 'justifyContent': 'space-between'}),

            html.H2('Initial vs Check-in Children School'),
            html.Div([
                dcc.Graph(figure=fig_initial_children_school),
                dcc.Graph(figure=fig_checkin_children_school)
            ], style={'display': 'flex', 'justifyContent': 'space-between'}),

            html.H2('Initial vs Check-in Meals Per Day'),
            html.Div([
                dcc.Graph(figure=fig_initial_meals_per_day),
                dcc.Graph(figure=fig_checkin_meals_per_day)
            ], style={'display': 'flex', 'justifyContent': 'space-between'}),
        ]),
        dcc.Tab(label='Farmer Production and Economic Details', children=[
            html.H2('Initial vs Check-in Annual Income'),
            html.Div([
                dcc.Graph(figure=fig_initial_annual_income),
                dcc.Graph(figure=fig_checkin_annual_income)
            ], style={'display': 'flex', 'justifyContent': 'space-between'}),

            html.H2('Initial vs Check-in Cultivated Land'),
            html.Div([
                dcc.Graph(figure=fig_initial_cultivated_land),
                dcc.Graph(figure=fig_checkin_cultivated_land)
            ], style={'display': 'flex', 'justifyContent': 'space-between'}),

            html.H2('Initial vs Check-in Production Size'),
            html.Div([
                dcc.Graph(figure=fig_initial_production_size),
                dcc.Graph(figure=fig_checkin_production_size)
            ], style={'display': 'flex', 'justifyContent': 'space-between'}),
        ]),
        dcc.Tab(label='Growing Practices', children=[
            html.H2('Initial vs Check-in Pest Management'),
            html.Div([
                dcc.Graph(figure=fig_initial_pest_management),
                dcc.Graph(figure=fig_checkin_pest_management)
            ], style={'display': 'flex', 'justifyContent': 'space-between'}),

            html.H2('Initial vs Check-in Production Status'),
            html.Div([
                dcc.Graph(figure=fig_initial_production_status),
                dcc.Graph(figure=fig_checkin_production_status)
            ], style={'display': 'flex', 'justifyContent': 'space-between'}),
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
