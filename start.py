#Text to speech use fpt api
import sys
import requests
#API Key của bạn
#00:  "7c1151e8d66146cc832ba10584a5333a"
#01:  "952acd5968644894b16e8b51e89bc165"
#02: "4957fc5ae67f476abdb44be1bf12c288"
#03: "1f7e191fe53947f6b5556ebc923f5cf4"
#04: "77c8f15ca85f4e558a00d61e0ce519b0"
#05: "77bdc6ff6e3b4b82bb1c094c0f3cd5a0"
keys = [
        '952acd5968644894b16e8b51e89bc165',
        '4957fc5ae67f476abdb44be1bf12c288',
  	'1f7e191fe53947f6b5556ebc923f5cf4',
	'77c8f15ca85f4e558a00d61e0ce519b0',
	'77bdc6ff6e3b4b82bb1c094c0f3cd5a0',
	'c517594f3b43478cbea61054effbcb36',
	'975822c502c3463cbcd6ab0e586ee3d1',
	'978b8d3f52694dd1a0336ba488fa092c',
	'64ec9036808d4d67afcd2801f6cd0599',
	'8ef86b3b16ed4fed8289703212d7c5ce',
	'eb901e9263eb4439bc1dc40fc22d86dd',
	'c4b0c091d2714e8d9e8144e1b4b75f5a',
	'b79ef1fe5dde49f9a03bda519f90b2c0',
	'3acd44b1bff241278038a82d08ad0710',
	'401c07c328b842628c8fe36a4066c16b',
	'4fa987ea27fc4005a27fcf32fbfbde48',
	'8570122a71dc4eccad1208176efd4bda',
	'5677496690e04a83b7feb8fd11339c51',
	'3126715bcfb14a01aa2a85314af8d882',
	'88b80aacc15d49f7816554bee7a0bce4',
	'7507eb5c685547f3932296c993962663',
	'056604c10e1241f984c7ad7e81a9a33c',
	'ec454c24dab74c77a619adb7539b5923',
	'f8642ed3aa5e4ecd9f5e19377b3cb359',
	'1fc0a5e8e22b4b91bb62b88f442fa167',
	'5703ada87d0c4d159fc432e9b4645aea',
	'49543fd413cd40f09ee3dfc9f7e9fa81',
	'689c80f862584f00b9fb1e491598aab4',
	'3f9528b4733b42c6b3a605223b9f3d01',
	'693afc409d684c4e88793868d45761b3'
]
api_key =  "7c1151e8d66146cc832ba10584a5333a"

#Xác định các giọng đọc, voice có các giá trị là leminh (giọng nam miền bắc), male (giọng nam miền bắc),
#female (giọng nữ miền bắc), hatieumai (giọng nữ miền nam), ngoclam (giọng nữ Huế)
voice = "leminh"
# Xác định các giọng đọc, voice có các giá trị là:
# leminh (giọng nam miền bắc nghe ấm ), 
# male (giọng nam miền bắc hơi già có tiếng thở),
# female (giọng nữ miền bắc trẻ, giọng trong đọc hơi chậm so với các giọng khác), 
# hatieumai (giọng nữ miền nam nghe đk), 
# ngoclam (giọng nữ Huế  đọc hơi bị ngắt nên cho chậm lại)
speed= "0"
#ngữ điệu 1 on. 0 off
prosody= "0"
args = sys.argv
if len(args) >= 1:
    short_direct = args[1]
    direc = '{}/'.format(args[1])
else:
    direc = ''
if direc == '-f/':
    direc = ''
import os
import datetime

#backup file full.mp3
if short_direct not in os.listdir():
    os.mkdir(short_direct)
if 'full.mp3' in os.listdir('{}'.format(direc)):
    #create folder backup if not exists
    if 'backup' not in os.listdir('{}'.format(direc)):
        os.mkdir('{}backup'.format(direc))
    
    now = str(datetime.datetime.now()).replace(" ", "_").replace(":", "_")
    os.rename("{}full.mp3".format(direc), "{}backup/{}.mp3".format(direc, now))
    print('backup file full mp3 to {}backup/{}.mp3'.format(direc, now))

# Remove all file mp3
for item in os.listdir('{}'.format(direc)):
    if item.endswith(".mp3"):
        os.remove(os.path.join(direc, item))
print('remove all file mp3')

from textwrap import wrap
import time
import wget
import random
file = open("{}.txt".format(short_direct), "r", encoding="utf-8") 
content = file.read()

wraptexts = wrap(content, 480)
    

for i in range(len(wraptexts)):
    while True:
        try:
            text = wraptexts[i]
            api_key = random.choice(keys)
            print('\n', api_key)
            url = "http://api.openfpt.vn/text2speech/v4?api_key={}&voice={}&speed={}&prosody={}".format(api_key, voice, speed, prosody)
            response = requests.post(url, data=text.encode('utf-8'), headers={'voice':voice, 'speed':speed, 'prosody':prosody})
            response = response.json()
            print('\n', response['async'])
            file = response['async']
            print("downloading file {}/{} ".format(i+1, len(wraptexts)), "{}{:03}.mp3".format(direc, i))
        except :
            time.sleep(0.01)
            print('Thu lai')
            continue
        break
    while True:
        try:
            wget.download(file, "{}{:03}.mp3".format(direc, i))
        except :
            time.sleep(0.1)
            print('Co loi. Thu lai', end='')
            continue
        break
    
print('\nCOMPLETE')

#create list for merge
import subprocess
f = open("{}create_list.bat".format(direc), "w")
f.write("(for %%i in (*.mp3) do @echo file '%%i') > list.txt")
f.close()
s = "{}create_list.bat".format(direc)
os.chdir(short_direct)
print(os.listdir())
print(s)

# os.system("create_list2.bat".format(direc))
subprocess.Popen("create_list.bat")
os.chdir('..')

#merge file for create 
#output: full.mp3
p = subprocess.run('ffmpeg -f concat -safe 0 -i {}list.txt -c copy {}full.mp3'.format(direc, direc))

