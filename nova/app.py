import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import base64
from PIL import Image
import io
import pytesseract
import re

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

# Handling of exceptions with replacements
def filter_extracted_text(extracted_text):
    
    # Needed replacements to correct the text regognition errors
    replacements = {
    "p": "",
    "u": "",
    "m": "",
    "o": "0",
    "O": "0",
    "‘": "",
    "“": "",
    r"\+(\d)": r"+\1.",                     # Handle missing dot on plus
    r"-(\d)": r"-\1.",                      # Handle missing dot on minus
    r"(\d)\.\.": r"\1.",                    # Handle tow dots ..
    r"\.(\.+)": r"\1",                      # Handle any additinal dots
    r"(\d+)\.(\d+)\.(\d+)": r"\1.\2\3",     # Handle any additinal dots
    r"(\d+)\.\.{2,}(\d+)": r"\1.\2"         # Handle any additinal dots
    }

    # Additional replacement to keep only the first dot after the first character
    replacements[r"(\d)([.]+)(\d+)"] = r"\1.\3"

    # Execute the replacements
    for pattern, replacement in replacements.items():
        extracted_text = re.sub(pattern, replacement, extracted_text)

    # Hande the occuring of additional char at end error
    if len(extracted_text) > 5:
        extracted_text = extracted_text[:-1]
    
    return extracted_text

def extract_data(image):

    # Dict for keys and coordinates
    crop_coordinates_dict = {
        "eye":                      (281,367,359,381),   # Crop 1  coordinates
        "pupil_center_x":           (258,905,295,920),   # Crop 2  coordinates
        "pupil_center_y":           (318,905,356,920),   # Crop 3  coordinates
        "pachy_apex_x":             (258,934,295,951),   # Crop 4  coordinates
        "pachy_apex_y":             (319,936,356,953),   # Crop 5  coordinates
        "pachy_apex_thickness":     (156,936,224,953),   # Crop 6  coordinates
        "thinnest_local_thickness": (156,968,224,983),   # Crop 7  coordinates
        "pupil_diameter":           (302,1104,357,1119), # Crop 8  coordinates
        "k_max_x":                  (259,999,295,1015),  # Crop 9  coordinates
        "k_max_y":                  (319,999,357,1014)   # Crop 10 coordinates
    }

    # Dict to store the data extracted
    extracted_data = {}

    for idx, crop_coordinates in enumerate(crop_coordinates_dict.values()):
        cropped_image = image.crop(crop_coordinates)
        
        # Perform OCR on the cropped image region
        extracted_text = pytesseract.image_to_string(cropped_image, config='--psm 6').strip()
        
        # Handle missing - sing
        if idx in [1, 2, 8, 9]:
            if '-' not in extracted_text and '+' not in extracted_text:
                if extracted_text != "0.00" and extracted_text != "0.0":
                    extracted_text = '-' + extracted_text

        extracted_text = filter_extracted_text(extracted_text)

        # Convert to right type
        key_at_idx = list(crop_coordinates_dict.keys())[idx]
        if idx == 0:
            extracted_value = extracted_text
        elif idx == 5 or idx == 6:
            extracted_value = int(extracted_text)
        else:
            extracted_value = float(extracted_text)
        extracted_data[key_at_idx] = extracted_value

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