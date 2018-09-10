from models import Purchases

import telebot
from telebot import types

import PIL
from PIL import Image


# 
# TOKEN
TOKEN = '655462722:AAFgk2fEtpB7fkByuLEFTZ-Lx9rV8xxlCPI'
#username = os.environ['BOT_USERNAME']
# 
bot = telebot.TeleBot(TOKEN)
user = bot.get_me()



# 
# GLOBAL VARIABLES
PURCHASE_FROM = ''
NOT_PURCHASER_FROM = True
NAME_GIVEN = ''
PICTURE_GIVEN = ''
PRICE_GIVEN = ''
STORE_NAME_GIVEN = ''
STORE_LOCATION_GIVEN = ''
STORE_GPS_GIVEN = {}
CONDITION_GIVEN = ''
GENUINE_GIVEN = ''
RATING_GIVEN = ''
REVIEW_GIVEN = ''

# 
# DEFAULT GLOBAL VARIABLES
def default():
	# Set global variables to default
	global PURCHASE_FROM
	PURCHASE_FROM = ''
	global NOT_PURCHASER_FROM
	NOT_PURCHASER_FROM = True
	global NAME_GIVEN
	NAME_GIVEN = ''
	global PICTURE_GIVEN
	PICTURE_GIVEN = ''
	global PRICE_GIVEN
	PRICE_GIVEN = ''
	global STORE_NAME_GIVEN
	STORE_NAME_GIVEN = ''
	global STORE_LOCATION_GIVEN
	STORE_LOCATION_GIVEN = ''
	global STORE_GPS_GIVEN
	STORE_GPS_GIVEN = {}
	global CONDITION_GIVEN
	CONDITION_GIVEN = ''
	global GENUINE_GIVEN
	GENUINE_GIVEN = ''
	global RATING_GIVEN
	RATING_GIVEN = ''
	global REVIEW_GIVEN 
	REVIEW_GIVEN = ''



# 
# FLOAT TO STRING FUNCTION FOR PRICE
def price_str(price):
	price = str(price)
	birr = price.split('.')[0]
	cent = price.split('.')[1]

	if len(cent) > 2:
		cent = cent[:2]
	elif len(cent) == 1:
		cent = cent + '0'
	
	len_birr = len(birr)
	list_birr = list(birr)
	comm_birr = int((len(birr)-1)/3)

	for x in range(comm_birr):
		comm_place = len_birr - (x + 1) * 3
		list_birr.insert(comm_place, ',')
		birr = ''.join(list_birr)	

	return birr + '.' + cent




# 
# HELP MESSAGE HANDLER
@bot.message_handler(commands=['help'])
def help(message):
	pass





# 
# WILCOME MESSAGE HANDLER
@bot.message_handler(commands=['start'])
def send_welcome(message):
	try:
	    keyboard = types.InlineKeyboardMarkup()
	    default()
	    keyboard.add(types.InlineKeyboardButton("\U0001F3EA store", callback_data="store"))
	    keyboard.add(types.InlineKeyboardButton("\U0001F4F1 facebook", callback_data="facebook"))
	    keyboard.add(types.InlineKeyboardButton("\U0001F4F1 telegram", callback_data="telegram"))
	    bot.reply_to(message, "Hello {}. \U0001F600\nWhere did you buy your recent purchase?\n\n\U0001F449 From:".format(message.from_user.first_name), reply_markup=keyboard)
	except Exception as e:
		print(e)





# 
# CANCEL MESSAGE HANDLER
@bot.message_handler(commands=['cancel'])
def cancel_message(message):
	try:
		# Set global variables to default
		default()
		bot.reply_to(message, 'All the data you give is deleted ' + message.from_user.first_name + '.\nto startover /start.')
	except Exception as e:
		print(e)



# 
# CALLBACK QUERY HANDLERS FOR PURCHASE_FROM 
@bot.callback_query_handler(func=lambda call: call.data == 'store')
def give_choice_for_purchase_from(call):
    try:
    	if not call.from_user.is_bot:
	        bot.answer_callback_query(call.id, text='\U00002714 from: store')
	        default()
	        global PURCHASE_FROM
	        PURCHASE_FROM = 'store'
	        global NOT_PURCHASER_FROM
	        NOT_PURCHASER_FROM = False
	        bot.send_message(call.from_user.id, "\U00002611 from: store.\n\n\U0000270D send us the name of your purchase?")
    except Exception as e:
        print(e)


@bot.callback_query_handler(func=lambda call: call.data == 'facebook')
def give_choice_for_purchase_from(call):
    try:
    	if not call.from_user.is_bot:
	        bot.answer_callback_query(call.id, text='\U00002714 from: facebook')
	        default()
	        global PURCHASE_FROM
	        PURCHASE_FROM = 'facebook'
	        global NOT_PURCHASER_FROM
	        NOT_PURCHASER_FROM = False
	        bot.send_message(call.from_user.id, "\U00002611 from: facebook.\n\n\U0000270D send us the name of your purchase?")
    except Exception as e:
        print(e)


@bot.callback_query_handler(func=lambda call: call.data == 'telegram')
def give_choice_for_purchase_from(call):
    try:
    	if not call.from_user.is_bot:
	        bot.answer_callback_query(call.id, text='\U00002714 from: telegram')
	        default()
	        global PURCHASE_FROM
	        PURCHASE_FROM = 'telegram'
	        global NOT_PURCHASER_FROM
	        NOT_PURCHASER_FROM = False
	        bot.send_message(call.from_user.id, "\U00002611 from: telegram.\n\n\U0000270D send us the name of your purchase?")
    except Exception as e:
        print(e)




# 
# FOR USERS SENDING TEXT NOT CLICKING THE WHERE PURCHASE CHOICES. 
@bot.message_handler(content_types=['text'],
					 func=lambda m: NOT_PURCHASER_FROM
					)
def send_help_for_slow_users(message):
	try:
	    keyboard = types.InlineKeyboardMarkup()
	    default()
	    keyboard.add(types.InlineKeyboardButton("\U0001F3EA store", callback_data="store"))
	    keyboard.add(types.InlineKeyboardButton("\U0001F4F1 facebook", callback_data="facebook"))
	    keyboard.add(types.InlineKeyboardButton("\U0001F4F1 telegram", callback_data="telegram"))
	    bot.reply_to(message, "\U000026A0 Something went wrong starting over\n\nHello {}. \U0001F600\nWhere did you buy your recent purchase?\n\n\U0001F449 From:".format(message.from_user.first_name), reply_markup=keyboard)
	except:
		print(e)




# 
# ACCEPT NAME OF PURCHASE
@bot.message_handler(content_types=['text'],
					 func=lambda m: True if PURCHASE_FROM and not NAME_GIVEN and not PICTURE_GIVEN and not PRICE_GIVEN and not STORE_NAME_GIVEN and not STORE_LOCATION_GIVEN and not STORE_GPS_GIVEN and not CONDITION_GIVEN and not GENUINE_GIVEN and not RATING_GIVEN and not REVIEW_GIVEN else False
					)
def accept_name(message):
	try:
		global NAME_GIVEN
		if message.text[0] == '/':
			bot.reply_to(message, '\U000026A0 sorry product name dosen\'t start with "/".\n\n\U0000270D send us the name of your purchase?')
		elif len(message.text) > 31:
			bot.reply_to(message, '\U000026A0 sorry product name to long.\n\n\U0001F449 name should be less than "30" characters.\n\n\U0000270D send us the name of your purchase?')	
		else:
			NAME_GIVEN = message.text
			bot.reply_to(message, '\U00002611 product name: "' + NAME_GIVEN + '"\n\n\U0001F5BC send the picture of your \'{}\'.'.format(NAME_GIVEN))
	except Exception as e:
		print(e)




# 
# ACCEPT PICTURE OF PURCHASE
@bot.message_handler(content_types=['photo'],
					 func=lambda m: True if PURCHASE_FROM and NAME_GIVEN and not PICTURE_GIVEN and not PRICE_GIVEN and not STORE_NAME_GIVEN and not STORE_LOCATION_GIVEN and not STORE_GPS_GIVEN and not CONDITION_GIVEN and not GENUINE_GIVEN and not RATING_GIVEN and not REVIEW_GIVEN else False
					)
def accept_photo(message):
	try:
		global PICTURE_GIVEN

		fileID = message.photo[-1].file_id
		# print(fileID)
		file_info = bot.get_file(fileID)
		# print(file_info.file_path)
		downloaded_file = bot.download_file(file_info.file_path)

		PICTURE_GIVEN = NAME_GIVEN + '-' + str(message.from_user.id) + '-' + str(message.date) + '.jpg'
		uploaded_pic = open('img/uploaded/' + PICTURE_GIVEN, 'wb')
		uploaded_pic.write(downloaded_file)
		uploaded_pic.close()

		# BASEHIGHT OF PIC
		basehight = 950
		img = Image.open('img/uploaded/' + PICTURE_GIVEN)
		hpercent = (basehight / float(img.size[1]))
		wsize = int((float(img.size[0]) * float(hpercent)))
		img = img.resize((wsize, basehight), PIL.Image.ANTIALIAS)
		img.save('img/product/' + PICTURE_GIVEN)
		img.close()

		bot.reply_to(message, '\U00002611 Photo: recived\n\n\U0001F4B5 How much did you pay for it?\n\n\U0001F449 don\'t include \'birr\', \'cent\', etc... only number.')
	except Exception as e:
		print(e)
		bot.reply_to(message, '\U000026A0 Photo: is not recived\n\n\U0001F5BC Try again send the picture of your purchase.')
		



# 
# ANSWER FOR NON_IMAGE RESPONCES FOR IMAGE REQUEST
@bot.message_handler(content_types=['text'],
					 func=lambda m: True if PURCHASE_FROM and NAME_GIVEN and not PICTURE_GIVEN and not PRICE_GIVEN and not STORE_NAME_GIVEN and not STORE_LOCATION_GIVEN and not STORE_GPS_GIVEN and not CONDITION_GIVEN and not GENUINE_GIVEN and not RATING_GIVEN and not REVIEW_GIVEN else False
					)
def send_photo_please(message):
	if not message.text[0] == '/':
		bot.reply_to(message, '\U000026A0 Photo: not recived. \n\n\U0001F5BC please, send the picture of your \'{}\'.'.format(NAME_GIVEN))
	else:
		pass




# 
# ACCEPT PRICE OF PURCHASE
@bot.message_handler(content_types=['text'],
					 func=lambda m: True if PURCHASE_FROM and NAME_GIVEN and PICTURE_GIVEN and not PRICE_GIVEN and not STORE_NAME_GIVEN and not STORE_LOCATION_GIVEN and not STORE_GPS_GIVEN and not CONDITION_GIVEN and not GENUINE_GIVEN and not RATING_GIVEN and not REVIEW_GIVEN else False
					)
def accept_price(message):
	try:
		price = float(message.text)
		if price > 100000000 or price < 0:
			bot.reply_to(message, '\U000026A0 price must be between 0-100,000,000.\n\n\U0001F449 don\'t include \'birr\', \'cent\', etc... only number.\n\n\U0001F4B5 How much did you pay for your \'' + NAME_GIVEN + '\'?')
		else:
			global PRICE_GIVEN
			PRICE_GIVEN = price 
			if PURCHASE_FROM == 'store':
				keyboard = types.InlineKeyboardMarkup()
				keyboard.add(types.InlineKeyboardButton("\U00002757 i don't remember", callback_data="pass_name"))
				bot.reply_to(message, '\U00002611 price: ' + price_str(PRICE_GIVEN) + ' ETB\n\n\U0001F3EC Send us What is the name of the store?', reply_markup=keyboard)
			elif PURCHASE_FROM == 'facebook':	
				bot.reply_to(message, '\U00002611 price: ' + price_str(PRICE_GIVEN) + ' ETB\n\n\U0001F4F2 What is the name of the facebook \'group\' that you purchased your \'{}\'?'.format(NAME_GIVEN))
			elif PURCHASE_FROM == 'telegram':	
				bot.reply_to(message, '\U00002611 price: ' + price_str(PRICE_GIVEN) + ' ETB\n\n\U0001F4F2 What is the name of the telegram \'channel\' or \'group\' that you purchased your \'{}\'?'.format(NAME_GIVEN))
	except Exception as e:
		print(e)	
		bot.reply_to(message, '\U000026A0 price must be a number. \n\n\U0001F449 don\'t include \'birr\', \'cent\', \'$\', etc...\n\n\U0001F4B5 How much did you pay for your \'' + NAME_GIVEN + '\'?')




# 
# CALLBACK QUERY HANDLERS FOR NO STORE NAME
@bot.callback_query_handler(func=lambda call: call.data == 'pass_name')
def give_choice_for_purchase_from(call):
	try:
		global STORE_NAME_GIVEN
		STORE_NAME_GIVEN = '/$&pass'
		bot.answer_callback_query(call.id, text='\U00002714 store name undefined!')
		bot.send_message(call.from_user.id, '\U00002611 store: passed\n\n\U0001F4CD Where is the store?\n\n\U0001F449 Eg: Merkato yerga-hayele 2nd floor.')
	except Exception as e:
		print(e)




#
# ACCEPT STORE, FACEBOOK OR TELEGRAM NAME OF PURCHASE
@bot.message_handler(content_types=['text'],
				     func=lambda m: True if PURCHASE_FROM and NAME_GIVEN and PICTURE_GIVEN and PRICE_GIVEN and not STORE_NAME_GIVEN and not STORE_LOCATION_GIVEN and not STORE_GPS_GIVEN and not CONDITION_GIVEN and not GENUINE_GIVEN and not RATING_GIVEN and not REVIEW_GIVEN else False
					)
def accept_store_name(message):
	try:
		global STORE_NAME_GIVEN
		global STORE_GPS_GIVEN
		global STORE_LOCATION_GIVEN
		if PURCHASE_FROM == 'store': 
			if message.text[0] == '/':
				bot.reply_to(message, '\U000026A0 '+ message.text +' is not a store name.\n\n\U0001F449 please answer by texting for the questions the bot asks.\n\n\U0001F3EC What is the name of the store?')
			elif len(message.text) > 26:	
				bot.reply_to(message, '\U000026A0 store name to long.\n\n\U0001F449 store name should be less than 25 characters.\n\n\U0001F3EC What is the name of the store?')
			elif message.text.lower() == 'pass':
				STORE_NAME_GIVEN = '/$&pass'
				bot.reply_to(message, '\U00002611 store: passed\n\n\U0001F4CD Where is the store?\n\n\U0001F449 Eg: Merkato yerga-hayele 2nd floor.')
			else:
				STORE_NAME_GIVEN = message.text
				bot.reply_to(message, '\U00002611 store: \'' + STORE_NAME_GIVEN + '\'\n\n\U0001F4CDWhere is the store?\n\n\U0001F449 Eg: Merkato yerga-hayele 2nd floor.')
		elif PURCHASE_FROM == 'facebook':
			if message.text[0] == '/':
				bot.reply_to(message, '\U000026A0 \''+ message.text +'\' is not a facebook group name.\n\n\U0001F449 please answer by texting for the questions the bot asks.\n\n\U0001F4F2 What is the name of the facebook \'group\', that you purchased your \'{}\' from?'.format(NAME_GIVEN))
			elif len(message.text) > 26:	
				bot.reply_to(message, '\U000026A0 group name to long.\n\n\U0001F449 group name should be less than 25 characters.\n\n\U0001F4F2 What is the name of the facebook \'group\', that you purchased your \'{}\' from?'.format(NAME_GIVEN))
			else:
				STORE_NAME_GIVEN = message.text
				STORE_LOCATION_GIVEN = 'facebook'
				STORE_GPS_GIVEN['no_location'] = True
				keyboard = types.InlineKeyboardMarkup()
				keyboard.add(types.InlineKeyboardButton("\U0001F44C new", callback_data="new"))
				keyboard.add(types.InlineKeyboardButton("\U0000270C used", callback_data="used"))
				bot.reply_to(message, '\U00002611 facebook group: ' + STORE_NAME_GIVEN + '\n\n\U0001F449 What was the condition of your purchase?',  reply_markup=keyboard)
		elif PURCHASE_FROM == 'telegram':
			if message.text[0] == '/':
				bot.reply_to(message, '\U000026A0 \''+ message.text +'\' is not a telegram channel or group name.\n\n\U0001F449 please answer by texting for the questions the bot asks.\n\n\U0001F4F2 What is the name of the telegram \'channel\' or \'group\', that you purchased your \'{}\' from?'.format(NAME_GIVEN))
			elif len(message.text) > 26:	
				bot.reply_to(message, '\U000026A0 group or channel name to long.\n\n\U0001F449 group or channel name should be less than 25 characters.\n\n\U0001F4F2 What is the name of the telegram \'channel\' or \'group\', that you purchased your \'{}\' from?'.format(NAME_GIVEN))
			else:
				STORE_NAME_GIVEN = message.text
				STORE_LOCATION_GIVEN = 'telegram'
				STORE_GPS_GIVEN['no_location'] = True
				keyboard = types.InlineKeyboardMarkup()
				keyboard.add(types.InlineKeyboardButton("\U0001F44C new", callback_data="new"))
				keyboard.add(types.InlineKeyboardButton("\U0000270C used", callback_data="used"))
				bot.reply_to(message, '\U00002611 telegram channel: ' + STORE_NAME_GIVEN + '\n\n\U0001F449 What was the condition of your purchase?', reply_markup=keyboard)
	except Exception as e:
		print(e)	




# 
# ACCEPT THE STORE LOCATION 
@bot.message_handler(content_types=['text'],
				     func=lambda m: True if PURCHASE_FROM and NAME_GIVEN and PICTURE_GIVEN and PRICE_GIVEN and STORE_NAME_GIVEN and not STORE_LOCATION_GIVEN and not STORE_GPS_GIVEN and not CONDITION_GIVEN and not GENUINE_GIVEN and not RATING_GIVEN and not REVIEW_GIVEN else False
					)
def accept_store_location(message):
	try:
		global STORE_LOCATION_GIVEN
		if message.text[0] == '/':
			bot.reply_to(message, '\U000026A0 is not a store location.\n\n\U0001F449 Answer by texting for the questions the bot asks.\n\n\U0001F4CDWhere is the store?\n\n\U0001F449 Eg: Merkato yerga-hayele 2nd floor.')
		elif len(message.text) > 51:
			bot.reply_to(message, '\U000026A0 store location to long.\n\n\U0001F449 store location should be less than 50 characters.\'\n\n\U0001F4CDWhere is the store?\n\n\U0001F449 Eg: Merkato yerga-hayele 2nd floor.')	
		else:
			STORE_LOCATION_GIVEN = message.text
			keyboard = types.InlineKeyboardMarkup()
			keyboard.add(types.InlineKeyboardButton("\U00002757 i'm not at the store", callback_data="no_location"))
			bot.reply_to(message, '\U00002611 store location: \'' + STORE_LOCATION_GIVEN + '\'\n\n\U0001F5FA Send us the location if your are at the store.\n\n\U0001F449 touch \U0001F4CE on your keyboard and select location, then send location.', reply_markup=keyboard)
	except Exception as e:
		print(e)




# 
# CALLBACK QUERY HANDLERS FOR NO LOCATION 
@bot.callback_query_handler(func=lambda call: call.data == 'no_location')
def give_choice_for_purchase_from(call):
	try:
		global STORE_GPS_GIVEN
		STORE_GPS_GIVEN['no_location'] = True
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton("\U0001F44C new", callback_data="new"))
		keyboard.add(types.InlineKeyboardButton("\U0000270C used", callback_data="used"))
		bot.answer_callback_query(call.id, text='\U00002714 not at the store!')
		bot.send_message(call.from_user.id, '\U00002611 store gps location: Recived\n\n\U0001F449 What was the condition of your purchase?',  reply_markup=keyboard)
	except Exception as e:
		print(e)




# 
# ACCEPT GPS LOCATION OF STORE
@bot.message_handler(content_types=['location'],
				     func=lambda m: True if PURCHASE_FROM and NAME_GIVEN and PICTURE_GIVEN and PRICE_GIVEN and STORE_NAME_GIVEN and STORE_LOCATION_GIVEN and not STORE_GPS_GIVEN and not CONDITION_GIVEN and not GENUINE_GIVEN and not RATING_GIVEN and not REVIEW_GIVEN else False
					)
def accept_store_gps(message):
	try:
		global STORE_GPS_GIVEN
		STORE_GPS_GIVEN['longitude'] = message.location.longitude
		STORE_GPS_GIVEN['latitude'] = message.location.latitude
		STORE_GPS_GIVEN['no_location'] = False
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton("\U0001F44C new", callback_data="new"))
		keyboard.add(types.InlineKeyboardButton("\U0000270C used", callback_data="used"))
		bot.reply_to(message, '\U00002611 store gps location: Accepted\n\n\U0001F449 What was the condition of your purchase?',  reply_markup=keyboard)
	except Exception as e:
		bot.reply_to(message, '\U000026A0 store gps location: Not Recived\n\n\U0001F449 Try again. send us location of the store.')
	



# 
# CALLBACK QUERY HANDLERS FOR NEW CONDITION 
@bot.callback_query_handler(func=lambda call: call.data == 'new')
def accept_purchase_condition(call):
	try:
		global CONDITION_GIVEN
		CONDITION_GIVEN = 'new'
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton("\U0001F44D yes", callback_data="yes"))
		keyboard.add(types.InlineKeyboardButton("\U0001F44E no", callback_data="no"))
		bot.answer_callback_query(call.id, text='\U00002714 condition: new')
		bot.send_message(call.from_user.id, '\U00002611 condition: new\n\n\U0001F449 Is the product genuine?',  reply_markup=keyboard)
	except Exception as e:
		print(e)




# 
# CALLBACK QUERY HANDLERS FOR USED CONDITION 
@bot.callback_query_handler(func=lambda call: call.data == 'used')
def accept_purchase_condition(call):
	try:
		global CONDITION_GIVEN
		CONDITION_GIVEN = 'used'
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton("\U0001F44D yes", callback_data="yes"))
		keyboard.add(types.InlineKeyboardButton("\U0001F44E no", callback_data="no"))
		bot.answer_callback_query(call.id, text='\U00002714 condition: used')
		bot.send_message(call.from_user.id, '\U00002611 condition: used\n\n\U0001F449 Is the product genuine?',  reply_markup=keyboard)
	except Exception as e:
		print(e)




# 
# CALLBACK QUERY HANDLERS FOR YES GENUINE
@bot.callback_query_handler(func=lambda call: call.data == 'yes')
def accept_purchase_genuine(call):
	try:
		global GENUINE_GIVEN
		GENUINE_GIVEN = 'yes'
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton("\U00002B50", callback_data="one_rating"))
		keyboard.add(types.InlineKeyboardButton("\U00002B50\U00002B50", callback_data="two_rating"))
		keyboard.add(types.InlineKeyboardButton("\U00002B50\U00002B50\U00002B50", callback_data="three_rating"))
		keyboard.add(types.InlineKeyboardButton("\U00002B50\U00002B50\U00002B50\U00002B50", callback_data="four_rating"))
		keyboard.add(types.InlineKeyboardButton("\U00002B50\U00002B50\U00002B50\U00002B50\U00002B50", callback_data="five_rating"))
		bot.answer_callback_query(call.id, text='\U00002714 genuine: yes')
		bot.send_message(call.from_user.id, '\U00002611 genuine: yes\n\n\U0001F449 rate the product, from 1 to 5.', reply_markup=keyboard)
	except Exception as e:
		print(e)



# 
# CALLBACK QUERY HANDLERS FOR NO GENUINE
@bot.callback_query_handler(func=lambda call: call.data == 'no')
def accept_purchase_genuine(call):
	try:
		global GENUINE_GIVEN
		GENUINE_GIVEN = 'no'
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton("\U00002B50", callback_data="one_rating"))
		keyboard.add(types.InlineKeyboardButton("\U00002B50\U00002B50", callback_data="two_rating"))
		keyboard.add(types.InlineKeyboardButton("\U00002B50\U00002B50\U00002B50", callback_data="'three'_rating"))
		keyboard.add(types.InlineKeyboardButton("\U00002B50\U00002B50\U00002B50\U00002B50", callback_data="four_rating"))
		keyboard.add(types.InlineKeyboardButton("\U00002B50\U00002B50\U00002B50\U00002B50\U00002B50", callback_data="five_rating"))
		bot.answer_callback_query(call.id, text='\U00002714 genuine: no')
		bot.send_message(call.from_user.id, '\U00002611 genuine: yes\n\n\U0001F449 rate the product, from 1 to 5.', reply_markup=keyboard)
	except Exception as e:
		print(e)





# 
# CALLBACK QUERY HANDLERS FOR NO RATING
@bot.callback_query_handler(func=lambda call: call.data == 'one_rating')
def accept_purchase_genuine(call):
	try:
		global RATING_GIVEN
		RATING_GIVEN = 1
		bot.answer_callback_query(call.id, text='\U00002714 rating: \U00002B50')
		bot.send_message(call.from_user.id, '\U00002611 Rating: ' + str(RATING_GIVEN) + '\n\n\U0000270D Write your review of your \'{}\''.format(NAME_GIVEN))
	except Exception as e:
		print(e)



@bot.callback_query_handler(func=lambda call: call.data == 'two_rating')
def accept_purchase_genuine(call):
	try:
		global RATING_GIVEN
		RATING_GIVEN = 2
		bot.answer_callback_query(call.id, text='\U00002714 rating: \U00002B50\U00002B50')
		bot.send_message(call.from_user.id, '\U00002611 Rating: ' + str(RATING_GIVEN) + '\n\n\U0000270D Write your review of your \'{}\''.format(NAME_GIVEN))
	except Exception as e:
		print(e)



@bot.callback_query_handler(func=lambda call: call.data == 'three_rating')
def accept_purchase_genuine(call):
	try:
		global RATING_GIVEN
		RATING_GIVEN = 3
		bot.answer_callback_query(call.id, text='\U00002714 rating: \U00002B50\U00002B50\U00002B50')
		bot.send_message(call.from_user.id, '\U00002611 Rating: ' + str(RATING_GIVEN) + '\n\n\U0000270D Write your review of your \'{}\''.format(NAME_GIVEN))
	except Exception as e:
		print(e)


@bot.callback_query_handler(func=lambda call: call.data == 'four_rating')
def accept_purchase_genuine(call):
	try:
		global RATING_GIVEN
		RATING_GIVEN = 4
		bot.answer_callback_query(call.id, text='\U00002714 rating: \U00002B50\U00002B50\U00002B50\U00002B50')
		bot.send_message(call.from_user.id, '\U00002611 Rating: ' + str(RATING_GIVEN) + '\n\n\U0000270D Write your review of your \'{}\''.format(NAME_GIVEN))
	except Exception as e:
		print(e)


@bot.callback_query_handler(func=lambda call: call.data == 'five_rating')
def accept_purchase_genuine(call):
	try:
		global RATING_GIVEN
		RATING_GIVEN = 5
		bot.answer_callback_query(call.id, text='\U00002714 rating: \U00002B50\U00002B50\U00002B50\U00002B50\U00002B50')
		bot.send_message(call.from_user.id, '\U00002611 Rating: ' + str(RATING_GIVEN) + '\n\n\U0000270D Write your review of your \'{}\''.format(NAME_GIVEN))
	except Exception as e:
		print(e)



# 
# ACCEPT PURCHASE RATING
@bot.message_handler(content_types=['text'],
				     func=lambda m: True if PURCHASE_FROM and NAME_GIVEN and PICTURE_GIVEN and PRICE_GIVEN and STORE_NAME_GIVEN and STORE_LOCATION_GIVEN and STORE_GPS_GIVEN and CONDITION_GIVEN and GENUINE_GIVEN and not RATING_GIVEN and not REVIEW_GIVEN else False
					)
def accept_rating(message):
	try:
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton("\U00002B50", callback_data="one_rating"))
		keyboard.add(types.InlineKeyboardButton("\U00002B50\U00002B50", callback_data="two_rating"))
		keyboard.add(types.InlineKeyboardButton("\U00002B50\U00002B50\U00002B50", callback_data="'three'_rating"))
		keyboard.add(types.InlineKeyboardButton("\U00002B50\U00002B50\U00002B50\U00002B50", callback_data="four_rating"))
		keyboard.add(types.InlineKeyboardButton("\U00002B50\U00002B50\U00002B50\U00002B50\U00002B50", callback_data="five_rating"))
		bot.reply_to(message, '\U000026A0 please choose a rating from the choices bellow.', reply_markup=keyboard)
	except Exception as e:
		print(e)
		


# 
# ACCEPT PURCHASE REVIEW
@bot.message_handler(content_types=['text'],
				     func=lambda m: True if PURCHASE_FROM and NAME_GIVEN and PICTURE_GIVEN and PRICE_GIVEN and STORE_NAME_GIVEN and STORE_LOCATION_GIVEN and STORE_GPS_GIVEN and CONDITION_GIVEN and GENUINE_GIVEN and RATING_GIVEN and not REVIEW_GIVEN else False
					)
def accept_review(message):
	if len(message.text) < 3900 and not message.text[0] == '/':
		global REVIEW_GIVEN
		REVIEW_GIVEN = message.text
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton("\U0001F44D yes", callback_data="yes_recommend"))
		keyboard.add(types.InlineKeyboardButton("\U0001F44E no", callback_data="no_recommend"))
		bot.reply_to(message, '\U00002611 review: accepted\n\n\U0001F449 Do you recommend this to a friend?', reply_markup=keyboard)
	else:
		bot.reply_to(message, '\U000026A0 Review to long \n\n\U0000270D Write your review of your \'{}\''.format(NAME_GIVEN))




# 
# CALLBACK QUERY HANDLERS FOR YES RECOMMEND
@bot.callback_query_handler(func=lambda call: call.data == 'yes_recommend')
def give_choice_for_purchase_from(call):
	try:
		global RECOMMEND_GIVEN
		RECOMMEND_GIVEN = 'yes'
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton("\U0001F44D share", callback_data="share"))
		keyboard.add(types.InlineKeyboardButton("\U000026D4 cancel", callback_data="cancel"))
		bot.answer_callback_query(call.id, text='\U00002714 recommend: yes')
		bot.send_message(call.from_user.id, '\U00002611 recommend: yes\n\U0001F449 share?', reply_markup=keyboard)
	except Exception as e:
		print(e)



# 
# CALLBACK QUERY HANDLERS FOR NO RECOMMEND
@bot.callback_query_handler(func=lambda call: call.data == 'no_recommend')
def give_choice_for_purchase_from(call):
	try:
		global RECOMMEND_GIVEN
		RECOMMEND_GIVEN = 'no'
		keyboard = types.InlineKeyboardMarkup()
		keyboard.add(types.InlineKeyboardButton("\U0001F44D share", callback_data="share"))
		keyboard.add(types.InlineKeyboardButton("\U000026D4 cancel", callback_data="cancel"))
		bot.answer_callback_query(call.id, text='\U00002714 recommend: no')
		bot.send_message(call.from_user.id, '\U00002611 recommend: no\n\U0001F449 share?', reply_markup=keyboard)
	except Exception as e:
		print(e)



# 
# SHARE
@bot.callback_query_handler(func=lambda call: call.data == 'share')
def give_choice_for_purchase_from(call):
	try:
		if GENUINE_GIVEN.lower() == 'yes':
			genuine = True
		elif GENUINE_GIVEN.lower() == 'no':
			genuine = False
		if RECOMMEND_GIVEN.lower() == 'yes':
			recommend = True
		elif RECOMMEND_GIVEN.lower() == 'no':
			recommend = False 
		purchase = Purchases()
		if STORE_GPS_GIVEN['no_location']:
			purchase.create(purchase_from=PURCHASE_FROM,
						  name=NAME_GIVEN,
						  picture=PICTURE_GIVEN,
						  price=PRICE_GIVEN,
						  store_name=STORE_NAME_GIVEN,
						  store_location=STORE_LOCATION_GIVEN,
						  condition=CONDITION_GIVEN,
						  genuine=genuine,
						  rating=RATING_GIVEN,
						  review=REVIEW_GIVEN,
						  recommend=recommend,
						  gps=False,
						  latitude=0.0,
						  longitude=0.0,
						)
		else:
			purchase.create(purchase_from=PURCHASE_FROM,
							  name=NAME_GIVEN,
							  picture=PICTURE_GIVEN,
							  price=PRICE_GIVEN,
							  store_name=STORE_NAME_GIVEN,
							  store_location=STORE_LOCATION_GIVEN,
							  condition=CONDITION_GIVEN,
							  genuine=genuine,
							  rating=RATING_GIVEN,
							  review=REVIEW_GIVEN,
							  recommend=recommend,
							  gps=True,
							  latitude=STORE_GPS_GIVEN['latitude'],
							  longitude=STORE_GPS_GIVEN['longitude'],
							)
		genu= "\U00002705" if genuine else "\U0000274C"
		
		if PURCHASE_FROM == 'store':
			if STORE_NAME_GIVEN == "/$&pass":
				store_name_given = "store name \"not given\""
			else:
				store_name_given = STORE_NAME_GIVEN
			text = "\U0001F6CD  {} \n\U0001F4B0  {} ETB \n\U0001F449  condition:  {} \n\U00002757  genuine\U00002122   {}  \n\U0001F3EA  {} \n\U0001F4CD  {}  ".format(NAME_GIVEN,
																																							 price_str(PRICE_GIVEN),
																																							 CONDITION_GIVEN,
																																							 genu,
																																							 store_name_given,
																																							 STORE_LOCATION_GIVEN,
																																							)		
		else:
			if PURCHASE_FROM == "facebook":
				store_name_given = '"' +STORE_NAME_GIVEN + "\" from facebook-group"
			elif PURCHASE_FROM == "telegram":
				store_name_given = '"' +STORE_NAME_GIVEN + "\" from telegram-group"
			text = "\U0001F6CD  {} \n\U0001F4B0  {} ETB \n\U0001F449  condition:  {} \n\U00002757  genuine\U00002122   {}  \n\U0001F4F2  {} ".format(NAME_GIVEN,
																																					 price_str(PRICE_GIVEN),
																																					 CONDITION_GIVEN,
																																					 genu,
																																					 store_name_given,
																																					)		
		purchase.save()
		bot.send_message(call.from_user.id, '\U0001F600 Thanks for your time\nproduct name: \'' + NAME_GIVEN + '\' is shared. \n\n\U0001F44D we are sure many of us will learn from it.')
		bot.answer_callback_query(call.id, text='\U00002714 exprience: shared!')

		product_pic = open('img/product/' + PICTURE_GIVEN, 'rb')
		bot.send_photo('@aradabuyer', product_pic, text)
		product_pic.close()

		stars = '' 
		white_star = 5 - RATING_GIVEN
		for rating in range(RATING_GIVEN):
			stars += '\U00002B50'

		for rating in range(white_star):
			stars += '\U00002606'

		reco = '\U00002705' if recommend else '\U0000274C'     
		bot.send_message('@aradabuyer', 'REVIEW\n'+ stars + '\n--------------------------------------------------------------\n' + call.from_user.first_name + ':\n' + REVIEW_GIVEN + '\n--------------------------------------------------------------\n\nRecommend to a friend  ' + reco)


		if not STORE_GPS_GIVEN['no_location']:
			bot.send_location('@aradabuyer', STORE_GPS_GIVEN['latitude'], STORE_GPS_GIVEN['longitude'])
		
		default()

	except Exception as e:
		print(e)

# 
# CANCLE
@bot.callback_query_handler(func=lambda call: call.data == 'share')
def give_choice_for_purchase_from(call):
	try:
		# 
		default()
		bot.answer_callback_query(call.id, text='\U00002714 progress: canceled!')
		bot.send_message(call.from_user.id, 'All the data you give is deleted ' + message.from_user.first_name + '.\nto startover /start.')
	except Exception as e:
		print(e)





print("{} bot running....".format(user.first_name))


if __name__ == '__main__':
    bot.polling(none_stop=True)


print("{} bot stoped!!!!".format(user.first_name))
