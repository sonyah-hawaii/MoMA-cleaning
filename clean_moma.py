import re
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
def format_date(date: [int,str]) -> (int,[str,int,None]):
    '''
    Used for cleaning date column. 
    Accepts an integer or string and returns a tuple with an integer and int or string.
    `except` return statement generates review flag
    '''
    date_1 = None
    date_2 = None
    date = str(date)
    if len(date)==4 and re.search(r'\D', date) is None:
        return int(date), None
    if 6 <= len(date) <=8 and re.search(r'\D', date) is None: # yyyyyyyy and yyyyyy
        date_1, date_2 = date[0:4], date[4:]
    if re.search('\d{9}[^\D]', date) is not None: # yyyyyyyyyy
        date_1, date_2 = date[0:4], date[6:]
    if '-' in date and len(date.split('-', maxsplit=1)[0]) == 4: # yyyy-yyyy | yyyy-yy
        date_1, date_2 = date.split('-',  maxsplit=1)[0], date.split('-')[1]
    dates = sorted(list(set(re.findall(r'(17\d{2}|18\d{2}|19\d{2}|20\d{2})', date)))) # catchall
    if len(dates) == 0: #creating review flag
        return (0,'Review')
    if len(dates) == 1: #catching singular dates
        date_1, date_2 = dates[0], None
    else: #catching ranges
        date_1, date_2 = dates[0], dates[1]
    return int(date_1), date_2
