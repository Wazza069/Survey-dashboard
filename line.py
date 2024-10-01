import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)


df = pd.read_csv("Dataset/intro_bees.csv")

app = Dash(__name__)

app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_impact",
                 options=[{"label": x, "value":x} for x in bee_killers],
                 value="Pesticides",
                 multi=False,
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})

])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output (component_id='my_bee_map', component_property='figure')],
    [Input (component_id='slct_impact', component_property='value')]
)

def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container ="The bee-killer chosen by user was: {}".format(option_slctd)

    dff= df.copy()
    dff = dff[dff["Affected by"] == option_slctd]
    dff = dff[(dff["State"] == "Idaho") | (dff["State"] =="New York") | (dff["State"] == "New Mexico")]

    fig = px.line(
          data_frame=dff,
          x='Year',
          y='Pct of Colonies Impacted',
          color='State',
          template='plotly_dark'
    )

    return container, fig

if __name__ =='__main__':
      app.run_server(debug=True)