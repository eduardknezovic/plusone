
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import base64

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Image Upload and Display"),
    
    dcc.Upload(
        id='upload-image',
        children=html.Div(['Drag and Drop or ', html.A('Select a File')]),
        multiple=False,
        style={
            'width': '100%',
            'height': '200px',  # Adjust the height as needed
            'lineHeight': '200px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px 0'
        }
    ),
    
    html.Div(id='output-numbers'),
    html.Div(id='output-image'),
])

def extract_data(image):
    content_type, content_string = image.split(',')

    # Do something with the image (content_string)

    new_image = f"{content_type},{content_string}"
    extracted_data = {
        "eye": "Left",
        "pupil_center_x": 0.03,
        "pupil_center_y": 0.07,
        "pachy_apex_x": 0.00,
        "pachy_apex_y": 0.00,
        "pachy_apex_thickness": 367,
        "thinnest_local_thickness": 346,
        "pupil_diameter": 3.76
    }
    return extracted_data, new_image


# Decode and display the uploaded image
@app.callback(
    Output('output-image', 'children'),
    Output('output-numbers', 'children'),
    Input('upload-image', 'contents')
)
def update_output(image):
    if image is None:
        return [], [] # Return nothing
    
    data, cropped_image = extract_data(image)
    
    img_element = html.Img(src=cropped_image, style={'max-width': '100%'})

    numbers = html.Div([
        html.P(f"{k}: {v}") for k, v in data.items() 
    ])
    
    return img_element, numbers

if __name__ == '__main__':
    app.run_server(debug=True)
