#necessary things
import time
import youtube_dl

#check if the url is valid or not
def valid_checking(url):
	extractors = youtube_dl.extractor.gen_extractors()
	for e in extractors:
		if e.suitable(url) and e.IE_NAME != 'generic':
			return True
	return False

#welcome message
print("Youtube video downloader v0.1 (ALPHA STAGE) | Coded by _NooberrUwU#7048")
print("This program helps you to download videos on Youtube easier.")
print("Available commands: download, stop, source, info, version")
print("\n")

#main function
while True:
	cmd = input("Enter a command: ")

	if cmd == "":
		print("Hmmm... You didn't type in anything!")
		print("\n")
	elif cmd == "stop":
		print("Thanks for using my programme! Press ENTER to quit...")
		input()
		break
	elif cmd == "source":
		print("This is my open-source for this project: https://github.com/NooberrUwU/YoutubeDLer-python")
		print("\n")
	elif cmd == "info":
		print("Youtube video downloader v0.1 (ALPHA STAGE) | Coded by _NooberrUwU#7048")
		print("This program helps you to download videos on Youtube easier.")
		print("Available commands: download, help, stop, source, info, version")
		print("\n")
	elif cmd == "version":
		print("v0.1 - Alpha stage")
		print("\n")
	elif cmd == "download":
		url = input("Enter the URL: ")
		if valid_checking(url) == True:
			print("Your download progress will start in 3 seconds... Please wait!")
			
			#time for the module ready (reduce lagging and errors)
			time.sleep(3)
			
			#option (btw video downloaded is gonna put in video folder)
			ydl_opts = {
				'outtmpl': 'video/%(title)s.%(ext)s'
			}
			
			#download progress
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				ydl.download([url])
			
			print("\n")
		elif valid_checking(url) == False:
			print("Your URL doesn't exist or isn't supported. Please try again!")
			print("\n")
		else:
			print("An error occurred while executing the command! This problem will be automatically reported to staffs!")
			print("\n")
	else:
		print("Seems there's no command \"" + cmd + "\" !")