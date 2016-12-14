# automatically generated pytest template with ttpy 
import imageprocessing as ip

TEST_IMAGE_PATH_0 = "data/test_data/test_img_0.png"
TEST_IMAGE_PATH_1 = "data/test_data/test_img_1.png"

def test_Slide__init__():
    ''' testing: __init__ method of Slide class: Calls any() method on resultant numpy ndarray, indicating if any of the elements of that matrix are truthy (i.e., is the matrix populated?) '''
    example_slide = ip.Slide(TEST_IMAGE_PATH_1)
    assert example_slide.bgr.any() and example_slide.gray.any()

def test_generate_mask():
    ''' testing: given the appropriate HSV bounds, generate_mask produces a mask for which some values are not null '''
    red_mask = {
            ''' threshold set liberally for red '''
            "hl": 0,
            "hh": 100,
            "sl": 50,
            "sh": 150,
            "vl": 50,
            "vh": 150}
    example_slide = ip.Slide(TEST_IMAGE_PATH_0)
    result = example_slide.generate_mask(red_mask)
    assert result.any()

def test_extract_custom_pigment():
    ''' testing: extract_custom_pigment (in place of dab and ap methods, which use the same logic, but use default arguments)... resultant filtered image for custom pigment  '''
    example_slide = ip.Slide(TEST_IMAGE_PATH_0)
    red_mask = {
            ''' threshold set liberally for red '''
            "hl": 0,
            "hh": 100,
            "sl": 50,
            "sh": 150,
            "vl": 50,
            "vh": 150}
    result = example_slide.extract_custom_pigment(red_mask)
    # TODO: check for some color avg or number of non-zero pixels
    assert result.any()

# TODO: complete the following after refactoring is complete

def test_apPixelRaw():
    # TODO: write test...
    example_slide = ip.Slide(TEST_IMAGE_PATH_1)
    assert False

def test_dabPixelRaw():
    # TODO: write test...
    example_slide = ip.Slide(TEST_IMAGE_PATH_1)
    assert False

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
