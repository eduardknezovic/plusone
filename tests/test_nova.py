
from PIL import Image

from nova.app import filter_extracted_text, extract_data

def test_filtering():
    assert filter_extracted_text("+2.03") == "+2.03"
    assert filter_extracted_text("-2.23") == "-2.23"
    assert filter_extracted_text("-224") == "-2.24"
    assert filter_extracted_text("2..24") == "2.24"
    assert filter_extracted_text("-2..2.4") == "-2.24"
    assert filter_extracted_text("-2...24.") == "-2.24"
    assert filter_extracted_text("-2...24.") == "-2.24"

#1 Done
def test_image_extraction():
    # ARRANGE
    image_file_path = "nova/data/IVANCAN_FILIP_OS_11052022_095746_Large Map.JPG" 
    image = Image.open(image_file_path)

    # ACT
    data = extract_data(image)

    # ASSERT
    assert data["eye"] == "Left"
    assert data["pupil_center_x"] == 0.03
    assert data["pupil_center_y"] == 0.07
    assert data["pachy_apex_x"] == 0.00
    assert data["pachy_apex_y"] == 0.00
    assert data["pachy_apex_thickness"] == 367
    assert data["thinnest_local_thickness"] == 346
    assert data["pupil_diameter"] == 3.76
    assert data["k_max_x"] == -0.40
    assert data["k_max_y"] == -0.20

#2 Done
def test_image_extraction():
    # ARRANGE
    image_file_path = "nova/data/KOSTAJNSEK_ALEKSANDER_OS_12042023_131142_Large Map.JPG" 
    image = Image.open(image_file_path)

    # ACT
    data = extract_data(image)

    # ASSERT
    assert data["eye"] == "Left"
    assert data["pupil_center_x"] == 0.14
    assert data["pupil_center_y"] == 0.12
    assert data["pachy_apex_x"] == 0.00
    assert data["pachy_apex_y"] == 0.00
    assert data["pachy_apex_thickness"] == 464
    assert data["thinnest_local_thickness"] == 439
    assert data["pupil_diameter"] == 3.42
    assert data["k_max_x"] == -0.14
    assert data["k_max_y"] == -2.67

#3 Done
def test_image_extraction():
    # ARRANGE
    image_file_path = "nova/data/NOVAK_MATHIAS_OS_25032023_111050_Large Map.JPG" 
    image = Image.open(image_file_path)

    # ACT
    data = extract_data(image)

    # ASSERT
    assert data["eye"] == "Left"
    assert data["pupil_center_x"] == 0.11
    assert data["pupil_center_y"] == 0.06
    assert data["pachy_apex_x"] == 0.00
    assert data["pachy_apex_y"] == 0.00
    assert data["pachy_apex_thickness"] == 448
    assert data["thinnest_local_thickness"] == 394
    assert data["pupil_diameter"] == 2.78
    assert data["k_max_x"] == 1.53
    assert data["k_max_y"] == -0.80


#4 Done
def test_image_extraction():
    # ARRANGE
    image_file_path = "nova/data/PENTEK_TIN_OD_17052023_145610_Large Map.JPG" 
    image = Image.open(image_file_path)

    # ACT
    data = extract_data(image)

    # ASSERT
    assert data["eye"] == "Right"
    assert data["pupil_center_x"] == -0.21
    assert data["pupil_center_y"] == -0.02
    assert data["pachy_apex_x"] == 0.00
    assert data["pachy_apex_y"] == 0.00
    assert data["pachy_apex_thickness"] == 523
    assert data["thinnest_local_thickness"] == 520
    assert data["pupil_diameter"] == 3.57
    assert data["k_max_x"] == 0.08
    assert data["k_max_y"] == -0.31

#5 Done
def test_image_extraction():
    # ARRANGE
    image_file_path = "nova/data/PETREA_NARCIS DANIEL_OD_12062023_115031_Large Map.JPG" 
    image = Image.open(image_file_path)

    # ACT
    data = extract_data(image)

    # ASSERT
    assert data["eye"] == "Right"
    assert data["pupil_center_x"] == -0.17
    assert data["pupil_center_y"] == 0.17
    assert data["pachy_apex_x"] == 0.00
    assert data["pachy_apex_y"] == 0.00
    assert data["pachy_apex_thickness"] == 468
    assert data["thinnest_local_thickness"] == 453
    assert data["pupil_diameter"] == 2.80
    assert data["k_max_x"] == -0.15
    assert data["k_max_y"] == -1.33

#6
def test_image_extraction():
    # ARRANGE
    image_file_path = "nova/data/PUSKARIC_MARIO_OS_11072023_122109_Large Map.JPG" 
    image = Image.open(image_file_path)

    # ACT
    data = extract_data(image)

    # ASSERT
    assert data["eye"] == "Left"
    assert data["pupil_center_x"] == -0.14
    assert data["pupil_center_y"] == -0.19
    assert data["pachy_apex_x"] == 0.00
    assert data["pachy_apex_y"] == 0.00
    assert data["pachy_apex_thickness"] == 477
    assert data["thinnest_local_thickness"] == 419
    assert data["pupil_diameter"] == 2.31
    assert data["k_max_x"] == 1.05
    assert data["k_max_y"] == 0.20