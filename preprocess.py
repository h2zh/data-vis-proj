import pandas as pd

def preprocess(file_name):
    df = pd.read_csv(file_name)
    for i in df.index:
        edu_code = df.at[i, 'PEEDUCA']
        sex = df.at[i, 'TESEX']
        labor_force_status = df.at[i, 'TELFS']

        if edu_code <= 39:
            df.at[i, 'PEEDUCA'] = 'High school or below'
        elif edu_code >= 40 and edu_code <= 43:
            df.at[i, 'PEEDUCA'] = 'Undergraduate'
        else:
            df.at[i, 'PEEDUCA'] = 'Post graduate degree'

        if sex == 1:
            df.at[i, 'TESEX'] = 'Male'
        else:
            df.at[i, 'TESEX'] = 'Female'

        if labor_force_status <= 2:
            df.at[i, 'TELFS'] = 'Employed'
        elif labor_force_status <= 4:
            df.at[i, 'TELFS'] = 'Unemployed'
        else:
            df.at[i, 'TELFS'] = 'Not in labor force'
    return df