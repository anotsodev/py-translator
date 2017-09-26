# == Interactive Python Translator ==
# 
# This simple python program will translate the words or sentence that you entered.
# Usage: python py-translate.py
# 
# The purpose of this program is to translate words without opening the web browser and typing translate.google.com on the url bar, 
# well it basically saves time for the user ;).
# Requirements:
# 	1. requests
# 	2. urllib
# 
# Unlimited request to the google translate api, thanks to this: https://ctrlq.org/code/19909-google-translate-api

import requests
import urllib
import sys
import json

langs = [
    'auto','af','sq','am','ar','hy','az','eu','be','bn','bs','bg','ca','ceb','ny','zh-cn','zh-tw','co','hr','cs','da','nl','en','eo','et','tl','fi','fr','fy','gl','ka','de','el','gu','ht','ha','haw','iw','hi','hmn','hu','is','ig','id','ga','it','ja','jw','kn','kk','km','ko','ku','ky','lo','la','lv','lt','lb','mk','mg','ms','ml','mt','mi','mr','mn','my','ne','no','ps','fa','pl','pt','ma','ro','ru','sm','gd','sr','st','sn','sd','si','sk','sl','so','es','su','sw','sv','tg','ta','te','th','tr','uk','ur','uz','vi','cy','xh','yi','yo','zu'
]

def print_langs():
	print("Languages: ")
	with open('languages.json') as data_file:    
	    data = json.load(data_file)
	    for lang in langs:
	    	print(lang+" - "+data[lang])

def start_translator():
	print("\nInteractive Python Translator\n")
	while True:
		print("Available Commands: ")
		print("(1) Translate")
		print("(2) Quit")

		option = raw_input("\nPlease select a command to perform: ")
		if str(option) == '1':
			original_word = raw_input("\nEnter the word(s) that you need to translate: ")
			if original_word == '':
				print("You have entered an empty string.\n")
			else:
				# While input == list, repeat action
				while True:
					sl = raw_input("\nEnter the SOURCE language (Default = auto - Type 'list' to list all the languages): ")
					if sl in langs:
						break
					elif sl == 'list':
						print_langs()
						continue
					else:
						sl = 'auto'
						break
				print("\nSource Language: "+sl)
				while True:
					tl = raw_input("\nEnter the TARGET language (Type 'list' to list all the languages): ")
					if tl in langs:
						break
					elif tl == 'list':
						print_langs()
						continue
					else:
						tl = 'en'
						break
				print("\nTarget Language: "+tl)
				# API Request
				url = requests.get("https://translate.googleapis.com/translate_a/single?client=gtx&sl=" + sl + "&tl=" + tl + "&dt=t&q=" + urllib.quote_plus(original_word))
				print(" ")
				# Print the translated word
				print("Original Word(s) ("+sl+"): "+ original_word + "\nTranslated Word(s) ("+tl+"): " +url.json()[0][0][0].encode('utf-8')+"\n")
		elif option == '':
			continue
		else:
			print("Program is quitting...")
			sys.exit(1)

if __name__ == "__main__":
	start_translator()
			
