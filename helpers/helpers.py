import pandas as pd


def extractCOVID_data(file):

    '''
    Purpose:
        -Extracts COVID-19 data from Excel File and imports as Pandas DataFrame

    Inputs:
        -file: path to excel file

    Outputs:
        -COVID19
    '''

    #Read CSV File
    COVID19 = pd.read_csv(file)
    #Resort By Date
    COVID19_resorted = COVID19.sort_values(by=['Date'])

    return COVID19_resorted
