import pandas as pd
import re

def parse_artist(input: str) -> str:
    ''''
    Takes in URLs from WikiArt and extracts & returns formatted artist names.
    '''
    artist = re.findall('\/(.+)_',input)[0]
    artist_cap = [i.capitalize() for i in artist.split('-')]
    output = artist_cap[0]
    output = ' '.join(artist_cap)
    
    return output