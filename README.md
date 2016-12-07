# ichapy
An tool for analysis of immunohistochemical images that using Python bindings for OpenCV (computer vision) library to extract quantitative information from microscopy data. Given a set of stained tissue images, this software allows an automated and efficient extraction of data on colocalization, toplogy, and volume of cell clusters of different phenotype (e.g., distribution of B-Cells in a slice of cardiac tissue). While originally intended to be used in the context of heart tissue, this tool may be used for arbitrary physiological images.

## Motivation
The contents of this repository reflect a subset of tools salvaged from prior use in research I contributed to in Cardiac Immunology. While that project has been deprecated, I hope to eventually repurpose this tool in a manner that is generalized in applicability, safe, and easy to use for anyone who is interested in learning more about medical image data.

## Tests
**Automated tests are not yet implemented.**
However, these instructions are to be followed once tests are available:
`> pip install pytest # use the installation manager of your choosing`
`> python -m pytest -v test.py`

## Dataset
A new, unrestricted dataset is now included (source: https://imagej.nih.gov/ij/plugins/ihc-toolbox/index.html). The dataset originally used to calibrate this program is not available for reasons relating to patient privacy.

## Current State
While this code is currently under-documented, incomplete, and packaged without tests, I hope to at some point in the future salvage the contents for open distribution. Please contact me by email if you are interested in such a tool.
