'''
use:
$> python -m pytest csv_io_test.csv 
'''
import csv_io
import os

sample_data = ["founded",1919,1960,1946]
sample_csv_file = "nfl_sample_data.csv"
output_file = "sample_out.csv"

def test_copy_csv_file():
	''' tests if copy_csv_file function produces output '''
	csv_io.copy_csv_file(sample_csv_file,output_file)
	assert os.path.isfile(output_file)

def test_read_col():
	''' tests read_col method from csv_io '''
	sample_col = csv_io.read_col(sample_csv_file,"team")	
	assert sample_col == ["team","bears","chargers","brown"]

def test_add_col():
	''' tests functionality of adding column to existing csv file '''
	csv_io.add_col(output_file,sample_data)
	assert csv_io.read_col(output_file,"founded") == ["founded",1919,1960,1946]

def test_replace_col():
	csv_io.add_col(output_file,["quarterback","","Mettenberger","McCown"])
	csv_io.replace_col(output_file,["quarterback","Leaf","Sanchez","Griffen"])
	assert csv_io.read_col(output_file,"quarterback") ==  ["quarterback","Leaf","Sanchez","Griffen"]

