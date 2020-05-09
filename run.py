import requests
import time
import os

token = os.environ['TELEGRAM_BOT_TOKEN'] #Telegram bot token
url = "https://api.telegram.org/bot%s/" %(token)
n = 0
active_users = {}

monikers_tuple  = [
	("sandwich","sandwiches",21),
	("coffee", "coffees",7),
	("tea", "teas",5),
	("lunch", "lunches",49)
]
monikers_dict = {n[i]: n[2] for n in monikers_tuple for i in range(2)}
monikers_flat = [monikers_tuple[i][j] for i in range(len(monikers_tuple)) for j in range(3)]
monikers_str  = '\n'.join(f"{i[0]}: {i[2]} doge" for i in monikers_tuple)

def getCount(chatid):
	n = []
	t = time.time()
	chat_users = active_users[chatid]
	for i in chat_users:
		if t - chat_users[i] <= 600:
			n.append(i)
	return n

def sendMsg(message,chatid):
	requests.get(url + "sendMessage", data={"chat_id":chatid,"text":message})

def process(message,username,chatid):
	message = message.split(" ")
	for i in range(message.count(' ')):
		message.remove(' ')
		
	if "/register" in message[0]:
		#try:
			#block_io.get_new_address(label=username)
			sendMsg("@"+username+" you are now registered.",chatid)
		#except:
			sendMsg("@"+username+" you are already registered.",chatid)
	elif "/start" in message:
		    sendMsg("Welcoe the tipper bot",chatid)
	elif "/balance" in message[0]:
		#try:
		#	(balance, pending_balance) = returnBal(username)
			sendMsg("@"+username+" Balance : Doge",chatid)
		#except:
			sendMsg("@"+username+" you are not registered yet. use /register to register.",chatid)
	elif "/tip" in message[0]:
		#try:
			#person = message[1].replace('@','')
			#amount_msg = 1 if message[2] in ('a', 'an', '1') else message[2]
			#amount = abs(float(amount_msg)) * monikers_dict.get(message[3], 1)

			#if monikers_dict.get(message[3], 0) == 0:
			#	sin_plu = "doge"
			#elif amount_msg == 1:
			#	sin_plu = monikers_tuple[monikers_flat.index(message[3])//3][0]
			#else:
			#	sin_plu = monikers_tuple[monikers_flat.index(message[3])//3][1]

			#block_io.withdraw_from_labels(amounts=str(amount), from_labels=username, to_labels=person)
			#sendMsg("@"+username+" tipped "+ str(amount_msg) + " " + sin_plu +
					#("" if monikers_dict.get(message[3], 0) == 0 else f" ({str(amount)} doge)") +
					#" to @"+person+"",chatid)
			#(balance, pending_balance) = returnBal(person)
			#sendMsg("@"+person+" Balance : "+balance+ "Doge ("+pending_balance+" Doge)",chatid)
		#except ValueError:
			sendMsg("@"+username+" invalid amount.",chatid)
		#except:
			sendMsg("@"+username+" insufficient balance or @ is not registered yet.",chatid)
	elif "/address" in message[0]:
		#try:
			#data = block_io.get_address_by_label(label=username)
			#sendMsg("@"+username+" your address is "+data['data']['address']+"",chatid)
		#except:
			sendMsg("@"+username+" you are not registered yet. use /register to register.",chatid)
	elif "/withdraw" in message[0]:
		#try:
			amount = abs(float(message[1]))
			address = message[2]
			#data = block_io.withdraw_from_labels(amounts=str(amount), from_labels=username, to_addresses=address)
		#except ValueError:
			sendMsg("@"+username+" invalid amount.",chatid)
		#except:
			sendMsg("@"+username+" insufficient balance or you are not registered yet.",chatid)

	elif "/rain" in message[0]:
	     sendMsg("UNDER MAINTAINCE",chatid)
	    
	elif "/monikers" in message:
		 sendMsg("--MONIKERS--\n" +
			monikers_str,chatid)

	elif "/active" in message:
		 try:
			 
			sendMsg("Current active : %d shibes" %(len(getCount(chatid))),chatid)
	     except
		     sendMsg("UNDER MAINTAINCE",chatid)
	     pass 
	else:
		global active_users
		try:
				active_users[chatid][username] = time.time()
		except KeyError:
			active_users[chatid] = {}
			active_users[chatid][username] = time.time()

while True:
	try:
		print("such dogeshift. much running.")
		data = requests.get(url+"getUpdates", data={"offset":n}).json()
		n = data["result"][0]["update_id"] + 1
		username = data["result"][0]["message"]["from"]['username']
		chatid = data["result"][0]["message"]["chat"]["id"]
		message = data["result"][0]["message"]["text"]
		process(message,username,chatid)
	except:
		pass
