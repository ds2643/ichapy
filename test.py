# automatically generated pytest template with ttpy 
import imageprocessing as ip

TEST_IMAGE_PATH_0 = "data/test_data/test_img_0.png"
TEST_IMAGE_PATH_1 = "data/test_data/test_img_1.png"

def test_Slide__init__():
    ''' testing: __init__ method of Slide class: Calls any() method on resultant numpy ndarray, indicating if any of the elements of that matrix are truthy (i.e., is the matrix populated?) '''
    example_slide = ip.Slide(TEST_IMAGE_PATH_1)
    assert example_slide.bgr.any() and example_slide.gray.any()

def test_generate_mask():
    ''' testing: generate_mask '''
    # TODO: write test...
    example_slide = ip.Slide(TEST_IMAGE_PATH_1)
    assert False

# TODO: complete the following after refactoring is complete
def test_dab():
    # TODO: write test...
    example_slide = ip.Slide(TEST_IMAGE_PATH_1)
    assert False

def test_ap():
    # TODO: write test...
    example_slide = ip.Slide(TEST_IMAGE_PATH_1)
    assert False

def tst_apPixelRaw():
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
