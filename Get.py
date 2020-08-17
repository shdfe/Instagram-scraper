import re
import requests
from bs4 import BeautifulSoup
import json
'''
        This gets the instagram api data, like the follower count, etc.
        '''
class Get:
    def __init__(self):
        self.get()
    def get(acct):
        res = requests.get(acct).text
        soup = BeautifulSoup(res,'html.parser')
        script = soup.find('script',text=re.compile('window._sharedData'))
        script = str(script)
        script = script.replace('<script type="text/javascript">window._sharedData = ','')
        script = script.replace(';</script>','')
        script=json.loads(script)
        return script





        
        
        

        
        





