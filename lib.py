import sys
import requests
import os
import datetime
from textwrap import wrap
import time
import wget
import random
import subprocess

keys = open('keys.txt', 'r').read().split()
voice = "female"
speed= "0"
prosody= "0"

#backup file full.mp3
def backup(short_direct):
	direc = '{}/'.format(short_direct)
	
	if short_direct not in os.listdir():
		os.mkdir(short_direct)
	if 'full.mp3' in os.listdir('{}'.format(direc)):
		#create folder backup if not exists
		if 'backup' not in os.listdir('{}'.format(direc)):
			os.mkdir('{}backup'.format(direc))
		
		now = str(datetime.datetime.now()).replace(" ", "_").replace(":", "_")
		os.rename("{}full.mp3".format(direc), "{}backup/{}.mp3".format(direc, now))
		print('backup file full mp3 to {}backup/{}.mp3'.format(direc, now))
		
def remove_files(short_direct):
	direc = '{}/'.format(short_direct)
	for item in os.listdir('{}'.format(direc)):
		if item.endswith(".mp3"):
			os.remove(os.path.join(direc, item))
	print('remove all file mp3')
	
def download(short_direct, voice=voice, speed=speed, prosody=prosody):
	direc = '{}/'.format(short_direct)
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
				print('Waiting...', end='')
				continue
			break
	print('\nCOMPLETE')
	
def merge_files(short_direct):
	direc = '{}/'.format(short_direct)
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
	
def run_all(short_direct, voice=voice, speed=speed, prosody=prosody):
	backup(short_direct)
	remove_files(short_direct)
	download(short_direct, voice, speed, prosody)
	merge_files(short_direct)

	