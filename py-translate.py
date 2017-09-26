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

langs = [
    'auto','af','sq','am','ar','hy','az','eu','be','bn','bs','bg','ca','ceb','ny','zh-cn','zh-tw','co','hr','cs','da','nl','en','eo','et','tl','fi','fr','fy','gl','ka','de','el','gu','ht','ha','haw','iw','hi','hmn','hu','is','ig','id','ga','it','ja','jw','kn','kk','km','ko','ku','ky','lo','la','lv','lt','lb','mk','mg','ms','ml','mt','mi','mr','mn','my','ne','no','ps','fa','pl','pt','ma','ro','ru','sm','gd','sr','st','sn','sd','si','sk','sl','so','es','su','sw','sv','tg','ta','te','th','tr','uk','ur','uz','vi','cy','xh','yi','yo','zu'
]

def print_langs():
	print("\
'auto': 'Automatic'\n\
'af': 'Afrikaans'\n\
'sq': 'Albanian'\n\
'am': 'Amharic'\n\
'ar': 'Arabic'\n\
'hy': 'Armenian'\n\
'az': 'Azerbaijani'\n\
'eu': 'Basque'\n\
'be': 'Belarusian'\n\
'bn': 'Bengali'\n\
'bs': 'Bosnian'\n\
'bg': 'Bulgarian'\n\
'ca': 'Catalan'\n\
'ceb': 'Cebuano'\n\
'ny': 'Chichewa'\n\
'zh-cn': 'Chinese Simplified'\n\
'zh-tw': 'Chinese Traditional'\n\
'co': 'Corsican'\n\
'hr': 'Croatian'\n\
'cs': 'Czech'\n\
'da': 'Danish'\n\
'nl': 'Dutch'\n\
'en': 'English'\n\
'eo': 'Esperanto'\n\
'et': 'Estonian'\n\
'tl': 'Filipino'\n\
'fi': 'Finnish'\n\
'fr': 'French'\n\
'fy': 'Frisian'\n\
'gl': 'Galician'\n\
'ka': 'Georgian'\n\
'de': 'German'\n\
'el': 'Greek'\n\
'gu': 'Gujarati'\n\
'ht': 'Haitian Creole'\n\
'ha': 'Hausa'\n\
'haw': 'Hawaiian'\n\
'iw': 'Hebrew'\n\
'hi': 'Hindi'\n\
'hmn': 'Hmong'\n\
'hu': 'Hungarian'\n\
'is': 'Icelandic'\n\
'ig': 'Igbo'\n\
'id': 'Indonesian'\n\
'ga': 'Irish'\n\
'it': 'Italian'\n\
'ja': 'Japanese'\n\
'jw': 'Javanese'\n\
'kn': 'Kannada'\n\
'kk': 'Kazakh'\n\
'km': 'Khmer'\n\
'ko': 'Korean'\n\
'ku': 'Kurdish (Kurmanji)'\n\
'ky': 'Kyrgyz'\n\
'lo': 'Lao'\n\
'la': 'Latin'\n\
'lv': 'Latvian'\n\
'lt': 'Lithuanian'\n\
'lb': 'Luxembourgish'\n\
'mk': 'Macedonian'\n\
'mg': 'Malagasy'\n\
'ms': 'Malay'\n\
'ml': 'Malayalam'\n\
'mt': 'Maltese'\n\
'mi': 'Maori'\n\
'mr': 'Marathi'\n\
'mn': 'Mongolian'\n\
'my': 'Myanmar (Burmese)'\n\
'ne': 'Nepali'\n\
'no': 'Norwegian'\n\
'ps': 'Pashto'\n\
'fa': 'Persian'\n\
'pl': 'Polish'\n\
'pt': 'Portuguese'\n\
'ma': 'Punjabi'\n\
'ro': 'Romanian'\n\
'ru': 'Russian'\n\
'sm': 'Samoan'\n\
'gd': 'Scots Gaelic'\n\
'sr': 'Serbian'\n\
'st': 'Sesotho'\n\
'sn': 'Shona'\n\
'sd': 'Sindhi'\n\
'si': 'Sinhala'\n\
'sk': 'Slovak'\n\
'sl': 'Slovenian'\n\
'so': 'Somali'\n\
'es': 'Spanish'\n\
'su': 'Sundanese'\n\
'sw': 'Swahili'\n\
'sv': 'Swedish'\n\
'tg': 'Tajik'\n\
'ta': 'Tamil'\n\
'te': 'Telugu'\n\
'th': 'Thai'\n\
'tr': 'Turkish'\n\
'uk': 'Ukrainian'\n\
'ur': 'Urdu'\n\
'uz': 'Uzbek'\n\
'vi': 'Vietnamese'\n\
'cy': 'Welsh'\n\
'xh': 'Xhosa'\n\
'yi': 'Yiddish'\n\
'yo': 'Yoruba'\n\
'zu': 'Zulu'")

def start_translator():
	start = True
	option = ''
	print("\nInteractive Python Translator\n")
	while option == '' or start:
		print("Actions: ")
		print("(1) Translate")
		print("(2) Quit")

		option = raw_input("\nWhat do you want to do?: ")
		if str(option) == '2':
			sys.exit(1)
		elif str(option) == '1':
			original_word = raw_input("\nEnter the word(s) that you need to translate: ")
			if original_word == '':
				print("You have entered an empty string.\n")
			else:
				# While input == list, repeat action
				sl = 'list'
				while sl == 'list':
					sl = raw_input("\nEnter the SOURCE language (Default = auto - Type 'list' to list all the languages): ")
					if sl == 'list':
						print_langs()
					elif sl == '':
						sl = 'auto'
					elif sl not in langs:
						sl = 'auto'
					print("\nSource Language: "+sl)
				# While input == list, repeat action
				tl = 'list'
				while tl == 'list':
					tl = raw_input("\nEnter the TARGET language (Type 'list' to list all the languages): ")
					if tl == 'list':
						print_langs()
					elif tl == '':
						tl = 'en'
					elif tl not in langs:
						tl = 'en'
					print("\nTarget Language: "+tl)

				url = requests.get("https://translate.googleapis.com/translate_a/single?client=gtx&sl=" + sl + "&tl=" + tl + "&dt=t&q=" + urllib.quote_plus(original_word))
				print(" ")
				# Print the translated word
				print("Original Word(s) ("+sl+"): "+ original_word + "\nTranslated Word(s) ("+tl+"): " +url.json()[0][0][0].encode('utf-8')+"\n")
		else:
			print("Invalid choice, quitting...")
			sys.exit(1)

if __name__ == "__main__":
	start_translator()
			
