import pandas as pd

def strip_punct(df: pd.DataFrame, cols: [str, list], punct: str) -> pd.DataFrame:
    ''' 
    Takes in dataframe, column name or list of columns, and regex string of characters to remove
    overwrites original column with corrected column
    '''
    if isinstance(cols, str):
        df.loc[:,cols] = df.loc[:,cols].str.replace(f'{punct}','',regex=True)
    if isinstance(cols, list):
        for i in cols:
            df.loc[:,i] = df.loc[:,i].str.replace(f'{punct}','',regex=True)
    
def dedupe(input: str) -> str:
    '''
    Takes in a string and processes it to return unique gender(s).
    '''
    n = [i.capitalize() for i in input.strip().split(' ')]
    if len(set(n)) == 1:
        if n[0] is None or n[0] == '':
            return 'N/A'
        return list(set(n))[0]
    return str(set([i for i in n if i != '']))[1:-1].replace('\'','')