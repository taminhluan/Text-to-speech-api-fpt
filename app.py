from lib import *
import sys

args = sys.argv
command = 'run_all'
short_direct = 'input'
voice = "female"
speed= "0"
prosody= "0"

try:
	command = args[1]
	short_direct = args[2]
	voice = args[3]
	speed= args[4]
	prosody= args[5]
except:
	pass

if command == 'help':
	print(open('help.txt', 'r').read())
elif command == 'backup':
	backup(short_direct)
elif command == 'remove_files':
	backup(short_direct)
elif command == 'download':
	download(short_direct, voice, speed, prosody)
elif command == 'merge_files':
	merge_files(short_direct)
else:
	run_all(short_direct, voice, speed, prosody)
        
