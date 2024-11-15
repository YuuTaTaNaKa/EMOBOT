from poster.encode import multipart_encode, MultipartParam
from poster.streaminghttp import register_openers
import urllib2

url="https://api.webempath.net/v2/analyzeWav"
register_openers()
items = []
items.append(MultipartParam('apikey', "YOUR_APIKEY"))
items.append(MultipartParam.from_file('wav', "/PATH/TO/WAVFILE.wav"))
datagen, headers = multipart_encode(items)
request = urllib2.Request(url, datagen, headers)
response = urllib2.urlopen(request)
if response.getcode() == 200:
    print(response.read())
else:
    print("HTTP status %d" % (response.getcode()))


# pip install poster==0.8.1