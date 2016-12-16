# automatically generated pytest template with ttpy 
import imageprocessing as ip
import csv_io as c
import os

sample_data = ["founded",1919,1960,1946]
test_dir = "test_data/"
sample_csv_file = test_dir + "nfl_sample_data.csv"
output_file = test_dir + "sample_out.csv"
TEST_IMAGE_PATH_0 = test_dir + "test_img_0.png" # three red dots
TEST_IMAGE_PATH_1 = test_dir + "test_img_1.png" # black canvas

def test_copy_csv_file():
    ''' tests if copy_csv_file function produces output '''
    c.copy_csv_file(sample_csv_file, output_file)
    assert os.path.isfile(output_file)

def test_read_col():
    ''' tests read_col method from csv_io '''
    sample_col = c.read_col(sample_csv_file,"team")
    assert sample_col == ["team","bears","chargers","brown"]

def test_add_col():
    ''' tests functionality of adding column to existing csv file '''
    c.add_col(output_file,sample_data)
    assert c.read_col(output_file,"founded") == ["founded",1919,1960,1946]

def test_replace_col():
    c.add_col(output_file,["quarterback","","Mettenberger","McCown"])
    c.replace_col(output_file,["quarterback","Leaf","Sanchez","Griffen"])
    assert c.read_col(output_file,"quarterback") ==  ["quarterback","Leaf","Sanchez","Griffen"]

def test_Slide__init__():
    ''' testing: __init__ method of Slide class: Calls any() method on resultant numpy ndarray, indicating if any of the elements of that matrix are truthy (i.e., is the matrix populated?) '''
    example_slide = ip.Slide(TEST_IMAGE_PATH_1)
    assert example_slide.bgr.any() and example_slide.gray.any()

def test_generate_mask():
    ''' testing: given the appropriate HSV bounds, generate_mask produces a mask for which some values are not null '''
    red_mask = {
            "hl": 0,
            "hh": 255,
            "sl": 50,
            "sh": 255,
            "vl": 50,
            "vh": 255}
    example_slide = ip.Slide(TEST_IMAGE_PATH_0)
    result = example_slide.generate_mask(red_mask)
    assert result.any()

def test_extract_pigment():
    ''' testing: extract_custom_pigment (in place of dab and ap methods, which use the same logic, but use default arguments)... resultant filtered image for custom pigment  '''
    example_slide = ip.Slide(TEST_IMAGE_PATH_0)
    red_mask = {
            "hl": 0,
            "hh": 255,
            "sl": 50,
            "sh": 255,
            "vl": 50,
            "vh": 255} # TODO: test using more conservative mask
    result = example_slide.extract_pigment(red_mask)
    assert result.any() # TODO: test more rigiously (e.g., # pixels in range)

def test_count_pixels():
    ''' count pixels filtered when using some mask '''
    example_slide = ip.Slide(TEST_IMAGE_PATH_0)
    # TODO: write test
    red_mask = {
        "hl": 0,
        "hh": 255,
        "sl": 50,
        "sh": 255,
        "vl": 50,
        "vh": 255} # TODO: test using more conservative mask
    observed_pixel_count = example_slide.count_pixels(red_mask)
    return observed_pixel_count > 0

# TODO: complete the following after refactoring is complete

'''
def test_background():
    # TODO: write test...
    example_slide = ip.Slide(TEST_IMAGE_PATH_1)
    assert False

def test___init__():
    # TODO: write test...
    assert False

def test_contourData():
    # TODO: write test...
    assert False

def test_geoCenters():
    # TODO: write test...
    assert False

def test_areaNoise():
    # TODO: write test...
    assert False

def test_radii():
    # TODO: write test...
    assert False

def test_distanceInClass():
    # TODO: write test...
    assert False

def test_colocalization():
    # TODO: write test...
    assert False
'''
