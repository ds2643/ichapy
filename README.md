# ichapy
An tool for analysis of immunohistochemical images that using Python bindings for OpenCV (computer vision) library to extract quantitative information from microscopy data. Given a set of stained tissue images, this software allows an automated and efficient extraction of data on colocalization, toplogy, and volume of cell clusters of different phenotype (e.g., distribution of B-Cells in a slice of cardiac tissue). While originally intended to be used in the context of heart tissue, this tool may be used for arbitrary physiological images.

## Motivation
The contents of this repository reflect a subset of tools salvaged from prior use in research I contributed to in Cardiac Immunology. While that project has been deprecated, I hope to eventually repurpose this tool in a manner that is generalized in applicability, safe, and easy to use for anyone who is interested in learning more about medical image data.

## Tests
Unit tests are included in the test.py file.

`> pip install pytest # use the installation manager of your choosing`

`> pytest test.py`

## Dataset
A new, unrestricted dataset is now included ([source](https://imagej.nih.gov/ij/plugins/ihc-toolbox/index.html)). The dataset originally used to calibrate this program is not available for reasons relating to patient privacy.

## Future
- Interface ideas: data querying language, graphic user interface, command line interface
- Fix distance method to slide class in image processing module
- Misc custodial work (addressing several todos)
