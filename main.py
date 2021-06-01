#import modules
from win10toast import ToastNotifier
from pushbullet import Pushbullet
import requests
import time
import os

#set variables
url = 'NOMICS-API-HERE'
pb = Pushbullet('PUSHBULLET-API-HERE')
toast = ToastNotifier()
start = 35787.96
capital = 500
goal = 10
os.system('cls')

#get live crypto price
def get_price():
	try:
		raw_data = requests.get(url).json()
		p = float(raw_data[0]['price'])
		#check for profit
		if p >= start:
			percent = p - start
			percent = percent / start
			percent = percent * 100
			profit = capital * percent / 100
			print('↑ +%' + str(percent) + ' | Capital: ' + str(capital) + ' | Profit: ' + str(profit) + ' | Price: $' + str(p))
			#notify if goal profit is reached
			if profit >= goal:
				notify_win('Goal profit reached!', 'You have now reached your goal profit you may now withdraw it.', 2)
				notify_android('Goal profit reached!', 'You have now reached your goal profit you may now withdraw it.')
				exit()	
		#check for loss
		else:
			percent = start - p
			percent = percent / start
			percent = percent * 100
			print('↓ -%' + str(percent) + ' | Capital: ' + str(capital) + ' | Price: $' + str(p))
		time.sleep(5)
	except KeyboardInterrupt:
		print('exit...')
		exit()

#notification
def notify_win(header, body, duration):
	toast.show_toast(header, body, duration=duration)	

def notify_android(header, body):
	pb.push_note(header, body)

while True:
	get_price()