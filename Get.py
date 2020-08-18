import re
import requests
from bs4 import BeautifulSoup
import json

def getVeri(acct):
        res = requests.get(acct).text
        soup = BeautifulSoup(res,'html.parser')
        script = soup.find('script',text=re.compile('window._sharedData'))
        script = str(script)
        script = script.replace('<script type="text/javascript">window._sharedData = ','')
        script = script.replace(';</script>','')
        script=json.loads(script)
        verified = script['entry_data']['ProfilePage'][0]['graphql']['user']['is_verified']
        r = 'Verified' if verified==True else 'Unverified'
        return r

def followers(acct):
    res = requests.get(acct).text
    soup = BeautifulSoup(res,'html.parser')
    follow = soup.find('meta',property='og:description').get('content')
    threshold = str(follow)
    thr = threshold.lower()
    r = thr.index('followers')
    e= r+len('followers')
    poo = thr[0:e]
    return poo

def postNum(acct):
    res = requests.get(acct).text
    soup = BeautifulSoup(res,'html.parser')
    follow = soup.find('meta',property='og:description').get('content')
    threshold = str(follow)
    thr = threshold.lower()
    thr = thr\
          .split()
    r = thr[4],thr[5]
    pee = ' '.join(r)
    return pee
def following(acct):
    res = requests.get(acct).text
    soup = BeautifulSoup(res,'html.parser')
    follow = soup.find('meta',property='og:description').get('content')
    threshold = str(follow)
    thr = threshold.lower()
    thr = thr\
          .split()
    r = thr[2],thr[3]
    r = ' '.join(r)\
        .replace(',','')

    
    return r

def mutual(acct):
    res = requests.get(acct).text
    soup = BeautifulSoup(res,'html.parser')
    script = soup.find('script',text=re.compile('window._sharedData'))
    script = str(script)
    script = script.replace('<script type="text/javascript">window._sharedData = ','')
    script = script.replace(';</script>','')
    script=json.loads(script)
    # returns an error, will fix later: script['entry_data']['ProfilePage'][0]['graphql']['user']['edge_mutual_followed_by']['edges'][1]['node']['username']

    
    


#print(getVeri('https://www.instagram.com/leomessi')) returns 'Verified'
