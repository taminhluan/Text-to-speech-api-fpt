#Text to speech created by luantm
FPT đã ra v5 với các giọng hay hơn các bạn có thể tham khảo từ https://fpt.ai/tts/
Nếu các bạn quan tâm có thể liên hệ với mình để mua v5
Uses:
	Cmd: app.exe [<<command>> <<direct>> <<voice>> <<speed>> <<prosody>>]

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
	
#Xác định các giọng đọc, voice có các giá trị là leminh (giọng nam miền bắc), male (giọng nam miền bắc),
#female (giọng nữ miền bắc), hatieumai (giọng nữ miền nam), ngoclam (giọng nữ Huế)
voice = "female"
# Xác định các giọng đọc, voice có các giá trị là:
# leminh (giọng nam miền bắc nghe ấm ), 
# male (giọng nam miền bắc hơi già có tiếng thở),
# female (giọng nữ miền bắc trẻ, giọng trong đọc hơi chậm so với các giọng khác), 
# hatieumai (giọng nữ miền nam nghe đk), 
# ngoclam (giọng nữ Huế  đọc hơi bị ngắt nên cho chậm lại)
speed= "0"
#ngữ điệu 1 on. 0 off
prosody= "0"

please add your api key in keys.txt
