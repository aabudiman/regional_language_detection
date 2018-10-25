from _json import make_encoder

import tweepy
from tweepy import *
import json
import pre_process

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        json_load = json.loads(data)
        texts = json_load['text']
        coded = texts.encode('utf-8')
        coded = coded.decode('unicode_escape').encode('ascii', 'ignore')
        s = str(coded)
        teks = '\"'+s[2:-1]+'\"'+'\n'
        # print(s[2:-1])
        return True

    def on_error(self, status):
        print(status)

def write(namaFile, bahasa, data):
    text_file = open(namaFile+".txt", "a+")
    text_file.write(data + "/" + bahasa+"\n")

def getData(akun):
    auth = tweepy.OAuthHandler('xxxxxxxxxxxxxxxxxx', 
'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    
auth.set_access_token('xxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
                          'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    client = tweepy.API(auth)

    testing = client.user_timeline(screen_name=akun, count=10)
    return testing


auth = tweepy.OAuthHandler('Gc2VIMAWHO7bLC27argnz7CAS', 'zvFlbyCmyBCsiGZyRY0SkKEX80UFEkqOk0gulGLrqUCsdBXMfh')
auth.set_access_token('378438981-a36Tgu9PKsQsSqbSTKTRfixVMKm6PfKgQfDldNd7', 'AnF2N3VyeqVLDiImRRraaCviOGdjjnMAWlOg4xlDzpLqT')
client = tweepy.API(auth)

testing = client.user_timeline(screen_name = "TheKakek",count = 10000)

teks = []
# for status in testing:
#     print(status.text)
#     data = pre_process.tokenize1(pre_process.tokenize2(status.text))
#     write('indonesia', 'indonesia', str(data))
