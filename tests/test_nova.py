
from PIL import Image

from nova.app import filter_extracted_text, extract_data

def test_filtering():
    assert filter_extracted_text("+2.03") == "+2.03"
    assert filter_extracted_text("-2.23") == "-2.23"
    assert filter_extracted_text("-2..24") == "-2.24"
    # TODO add more tests 

def test_image_extraction():
    # ARRANGE
    image_file_path = "nova/data/IVANCAN_FILIP_OS_11052022_095746_Large Map.JPG"
    image = Image.open(image_file_path)

    # ACT
    data = extract_data(image)

    # ASSERT
    assert data["eye"] == "Left"
    assert data["pupil_center_x"] == 0.03
    assert data["pupil_center_y"] == -0.07
    assert data["pachy_apex_x"] == 0.00
    assert data["pachy_apex_y"] == 0.00
    assert data["pachy_apex_thickness"] == 367
    assert data["thinnest_local_thickness"] == 346
    assert data["pupil_diameter"] == 3.76
    # TODO first make these tests above pass, then uncomment these below
    # assert data["k_max_x"] == -0.40
    # assert data["k_max_y"] == -0.2
    # -------
    # TODO after the tests above are passing, copy and paste code above
    # to write more tests for another images


