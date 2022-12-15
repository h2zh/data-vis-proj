import pandas as pd

def preprocess(file_name):
    df = pd.read_csv(file_name)
    
    edu_dict = {31: 'High school or below', 32: 'High school or below',33: 'High school or below',34: 'High school or below',35: 'High school or below',36: 'High school or below',37: 'High school or below',38: 'High school or below',39: 'High school or below',40: 'College',41: 'College',42: 'College',43: 'Bachelor',44: 'Post graduate degree',45: 'Post graduate degree',46: 'Post graduate degree'}
    
    sex_dict = {1:'Male',2:'Female'}
    
    labor_dict = {1:'Employed',2:'Employed',3:'Unemployed',4:'Unemployed',5:'Not in labor force'}
    
    hispan_dict = {1:'Hispanic',2:'Non-Hispanic'}
    
    metro_dict = {1:"Metro", 2:"Non-metropolitan", 3:"Not identified"}
    
    df['PEEDUCA'] = df['PEEDUCA'].map(edu_dict)
    df['TESEX'] = df['TESEX'].map(sex_dict)
    df['TELFS'] = df['TELFS'].map(labor_dict)
    df['PEHSPNON'] = df['PEHSPNON'].map(hispan_dict)
    df['GTMETSTA'] = df['GTMETSTA'].map(metro_dict)
    
    df.rename(columns={'PEEDUCA':'education_level'}, inplace=True)
    df.rename(columns={'TESEX':'sex'}, inplace=True)
    df.rename(columns={'TELFS':'labor_status'}, inplace=True)
    df.rename(columns={'PEHSPNON':'Hispanic'}, inplace=True)
    df.rename(columns={'GTMETSTA':'Metropolitan_status'}, inplace=True)
    
    df.rename(columns={'TEAGE':'age'}, inplace=True)
    df.rename(columns={'TRERNWA':'weekly_income'}, inplace=True)

    return df