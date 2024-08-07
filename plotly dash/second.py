# imports
import dash
from dash import html, dcc, Output, Input
import plotly.express as px

# create (dash object) the app
app = dash.Dash(__name__)

# app layout
# app.layout = html.Div([
#     html.H1('INTERACTIVE SLIDER'),
#     dcc.Slider(1, 10, 1, value=5, id='slider'),
#     html.Div(id='slider-output', style={'fontSize': 60})
# ])

app.layout = html.Div([
    html.H1('INTERACTIVE SLIDER'),
    dcc.Slider(1, 10, 1, value=5, id='slider'),
    html.Div(id='slider-output', style={'fontSize': 60} )])
    
 





# #Now let's set the layout colors of our app
# fig.update_layout(
#     plot_bgcolor ='#121212',    # The bg of the plot
#     paper_bgcolor = '#121212',  # The bg of the paper 
#     font_color = '#1876AE'      # The text on the plot (Inside the plot only)
# )

# callback
@app.callback(
    Output(component_id='slider-output', component_property='children'),
    Input(component_id='slider', component_property='value'),
)
def updata_figure(number):
    return number * number

# run app
if __name__ == '__main__':
    app.run_server(debug=True)