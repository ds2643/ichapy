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
TEST_MASK = {
            "hl": 0,
            "hh": 255,
            "sl": 50,
            "sh": 255,
            "vl": 50,
            "vh": 255}

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
    example_slide = ip.Slide(TEST_IMAGE_PATH_0)
    result = example_slide.generate_mask(TEST_MASK)
    assert result.any()

def test_extract_pigment():
    ''' testing: extract_custom_pigment (in place of dab and ap methods, which use the same logic, but use default arguments)... resultant filtered image for custom pigment  '''
    example_slide = ip.Slide(TEST_IMAGE_PATH_0)
    result = example_slide.extract_pigment(TEST_MASK)
    assert result.any() # TODO: test more rigiously (e.g., # pixels in range)

def test_count_pixels():
    ''' count pixels filtered when using some mask '''
    example_slide = ip.Slide(TEST_IMAGE_PATH_0)
    observed_pixel_count = example_slide.count_pixels(TEST_MASK)
    return observed_pixel_count > 0

# def test_background(): assert False

def test_contour_data():
    ''' contour data not empty '''
    slide = ip.Slide(TEST_IMAGE_PATH_0)
    layer = slide.extract_pigment(TEST_MASK)
    contour_data, img = slide.contour_data(layer)
    assert contour_data

def test_draw_contours():
    '''  '''
    # TODO: write test
    # TODO: write docstring
    assert False

'''
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
