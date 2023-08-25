import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import base64
from PIL import Image
import io
import pytesseract

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Image Upload and Display"),
    
    dcc.Upload(
        id='upload-image',
        children=html.Div(['Drag and Drop or ', html.A('Select a File')]),
        multiple=False,
        style={
            'width': '100%',
            'height': '200px',
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

def filter_extracted_text(extracted_text):
    # Handle text recognition common errors
    extracted_text = extracted_text.replace("p", "")
    extracted_text = extracted_text.replace("u", "")
    extracted_text = extracted_text.replace("m", "")
    extracted_text = extracted_text.replace("o", "0")
    extracted_text = extracted_text.replace("O", "0")
    extracted_text = extracted_text.replace("+0", "+0.")
    extracted_text = extracted_text.replace("+0..", "+0.")
    extracted_text = extracted_text.replace("-0", "-0.")
    extracted_text = extracted_text.replace("-0..", "-0.")
    extracted_text = extracted_text.replace("+1", "+1.")
    extracted_text = extracted_text.replace("+1..", "+1.")
    extracted_text = extracted_text.replace("-1", "-1.")
    extracted_text = extracted_text.replace("-1..", "-1.")
    extracted_text = extracted_text.replace("+2", "+2.")
    extracted_text = extracted_text.replace("+2..", "+2.")
    extracted_text = extracted_text.replace("-2", "-2.")
    extracted_text = extracted_text.replace("-2..", "-2.")

    # Hande the occuring of additional . error
    if len(extracted_text) > 5:
        extracted_text = extracted_text[:-1]
    
    return extracted_text

def extract_data(image):

    crop_coordinates_list = [
        (281,367,359,381),  # Crop 1 coordinates
        (258,905,295,920),  # Crop 2 coordinates
        (318,905,356,920),  # Crop 3 coordinates
        (258,934,295,951),  # Crop 4 coordinates
        (319,936,356,953),  # Crop 5 coordinates
        (156,936,224,953),  # Crop 6 coordinates
        (156,968,224,983),  # Crop 7 coordinates
        (302,1104,357,1119) # Crop 8 coordinates
    ]

    extracted_data = {}

    keys = [
        "eye:",
        "pupil_center_x:",
        "pupil_center_y:",
        "pachy_apex_x:",
        "pachy_apex_y:",
        "pachy_apex_thickness:",
        "thinnest_local_thickness:",
        "pupil_diameter:"
    ]

    for idx, crop_coordinates in enumerate(crop_coordinates_list):
        cropped_image = image.crop(crop_coordinates)
        
        # Perform OCR on the cropped image region
        extracted_text = pytesseract.image_to_string(cropped_image, config='--psm 6').strip()
        
        # Handle missing - sing
        if idx == 1 or idx == 2:
            if '+' not in extracted_text:
                extracted_text = '-' + extracted_text

        extracted_text = filter_extracted_text(extracted_text)

        # Use the key to label the values and make them the right type
        if idx == 0:
            extracted_data[idx + 1] = f"{keys[idx]} {extracted_text}"
        elif idx == 5 or idx == 6:
            extracted_value = int(extracted_text)
            extracted_data[idx + 1] = f"{keys[idx]} {extracted_value}"
        else:
            extracted_value2 = float(extracted_text)
            extracted_data[idx + 1] = f"{keys[idx]} {extracted_value2:.2f}"

    return extracted_data

def crop_output_image(image):
    crop_coordinates = (682, 440, 1389, 1160)
    cropped_image = image.crop(crop_coordinates)
    return cropped_image

# Decode and display the uploaded image
@app.callback(
    Output('output-image', 'children'),
    Output('output-numbers', 'children'),
    Input('upload-image', 'contents')
)
def update_output(image):
    if image is None:
        return [], [] # Return nothing
    

    content_type, content_string = image.split(',')
    image = Image.open(io.BytesIO(base64.b64decode(content_string)))
    data = extract_data(image)
    cropped_image = crop_output_image(image)
    
    # Crop the image

    img_element = html.Img(src=cropped_image, style={'max-width': '100%'})

    numbers = html.Div([
        html.P(f"{k}: {v}") for k, v in data.items() 
    ])
    
    return img_element, numbers

if __name__ == '__main__':
    app.run_server(debug=True)