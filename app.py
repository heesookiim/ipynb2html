from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
from base64 import b64encode
import numpy as np
np.random.seed(1)

app = Dash(__name__)


app.layout = html.Div([
    html.H4('Rendering options of plots in Dash '),
    html.P("Choose render option:"),
    dcc.RadioItems(
        id='static-image-export-x-render-option',
        options=['interactive', 'image'],
        value='image'
    ),
    html.Div(id='static-image-export-x-output'),
])


@app.callback(
    Output("static-image-export-x-output", "children"),
    Input('static-image-export-x-render-option', 'value'))
def display_graph(render_option):
    x, y, sz, cl = np.random.rand(4, 100) # replace with your own data source
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='markers',
        marker=dict(
            size=sz*20,  # Scale the size for visibility
            color=cl,
            colorscale='Viridis',
            showscale=True
        )
    ))

    if render_option == 'image':
        img_bytes = fig.to_image(format="png")
        encoding = b64encode(img_bytes).decode()
        img_b64 = "data:image/png;base64," + encoding
        return html.Img(src=img_b64, style={'height': '500px'})
    else:
        return dcc.Graph(figure=fig)


if __name__ == "__main__":
    app.run(debug=True)
