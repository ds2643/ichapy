'''
module includes io functionality specific to csv
'''
import csv
import pandas as pd
import os
import shutil

def copy_csv_file(src, new_file_name):
    ''' copies csv file with specified name to disk using standard io utilities '''
    shutil.copy(src,new_file_name)
    try:
            os.path.isfile(new_file_name)
    except IOError:
            print("Due to an error in the IO component of this program, the expected output file has not been written")

def read_col(file_name,col):
    ''' returns csv column in list form using pandas csv reader given column header and file name'''
    try:
            os.path.isfile(file_name)
    except IOError:
            print("Due to an error in the IO component of this program, the referrenced output file does not exist")
    data = pd.read_csv(file_name)[col]
    return [col] + data.values.tolist()

def add_col(file_name, data):
    '''adds column to specified csv file at given column index given column data in list form using pandas csv utilities'''
    try:
            os.path.isfile(file_name)
    except IOError:
            print("Due to an error in the IO component of this program, the referrenced output file does not exist")
    table_data = pd.read_csv(file_name)
    table_data.insert(len(table_data.columns),str(data[0]),data[1:],allow_duplicates=True)
    table_data.to_csv(file_name,index=False)

def replace_col(file_name,data):
    ''' overwrites column at specified index with specified list data for given file using pandas csv writer'''
    try:
            os.path.isfile(file_name)
    except IOError:
            print("Due to an error in the IO component of this program, the referrenced output file does not exist")
    df = pd.read_csv(file_name)
    df.drop([str(data[0])], axis = 1 , inplace= True)
    df.insert(len(df.columns),str(data[0]),data[1:],allow_duplicates=True)
    df.to_csv(file_name,index=False)
