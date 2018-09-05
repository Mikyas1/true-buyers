from models import Purchases

import telebot
from telebot import types

import PIL
from PIL import Image

# bot = telegram.Bot(token=T)
# x = Purchases()
# x.objects.insert({'name': 'mike'})

# x.create(name='iphone 8',
# 		picture='.jpg',
#  		price=23000.00,
#  		store_name='gebeya', 
#  		store_location='lancha, in fornt of greek emabssy chilallo building 5 floor iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii',
# 		condition = 'new-used',
# 		genuine = True,
#  		rating = 4,
#  		review='This product is genuine.',
#  		recommend = False,
#  		latitude = 9.035862,
#  		longitude = 38.752402,
# 	)
# x.save()
# print('{} === {}'.format(type(x.recommend), x.recommend))
# print(type(False))

TOKEN = '655462722:AAFgk2fEtpB7fkByuLEFTZ-Lx9rV8xxlCPI'
#username = os.environ['BOT_USERNAME']
bot = telebot.TeleBot(TOKEN)
user = bot.get_me()





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





share_purchase = True
not_purchaser = True
purchaser_sending = {}
name_given = ''
picture_given = ''
price_given = ''
store_name_given = ''
store_location_given = ''
store_gps_given = {}
condition_given = ''
genuine_given = ''
rating_given = ''
review_given = ''
recommend_given = ''

# bot.send_message('@aradabuyer', 'first message form Arada Buyer Bot. click t.me/aradabuyerbot to intract with it.')

# photo = open('IMG.jpg', 'rb')
# bot.send_photo('@aradabuyer', photo, '''Lorem ipsum ''')
# photo.close()

# print(str(user))
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("\U0001F3EA store", callback_data="store"))
    keyboard.add(types.InlineKeyboardButton("\U0001F4F1 facebook", callback_data="facebook"))
    keyboard.add(types.InlineKeyboardButton("\U0001F4F1 telegram", callback_data="telegram"))
    bot.reply_to(message, "Hello {}. \U0001F600\nWhere did you buy your recent purchase?\nFrom:".format(message.from_user.first_name), reply_markup=keyboard)

@bot.message_handler(commands=['cancel'])
def cancel(message):
	# Set global variables to default
	global share_purchase
	share_purchase = True
	global not_purchaser
	not_purchaser = True
	global purchaser_sending
	purchaser_sending = {}
	global name_given
	name_given = ''
	global picture_given
	picture_given = ''
	global price_given
	price_given = ''
	global store_name_given
	store_name_given = ''
	global store_location_given
	store_location_given = ''
	global store_gps_given
	store_gps_given = {}
	global condition_given
	condition_given = ''
	global genuine_given
	genuine_given = ''
	global rating_given
	rating_given = ''
	global review_given
	review_given = ''
	global recommend_given
	recommend_given = ''

	bot.reply_to(message, 'All the data you give us is deleted ' + message.from_user.first_name + '.\nto startover /share_purchase.')

@bot.message_handler(commands=['share_purchase'], func=lambda m: share_purchase)
def start_registering(message):
	if not message.from_user.is_bot:
		global share_purchase
		share_purchase = False
		global purchaser_sending
		purchaser_sending = {'first_name': message.from_user.first_name, 'id': message.from_user.id} 
		global not_purchaser
		not_purchaser = False
		bot.reply_to(message, "What is the name of your purchase?")
	else:
		pass


@bot.callback_query_handler(func=lambda call: call.data == 'store')
def get_book_vendors_from_button(call):
    try:
    	if not call.from_user.is_bot:
	        bot.answer_callback_query(call.id, text='Searching Bookstores')
	        print(call)
    except Exception as e:
        print(e)


@bot.message_handler(content_types=['text'],
					 func=lambda m: not_purchaser
					)
def send_help_for_slow_users(message):
	bot.reply_to(message, "Howdy, how are you doing {}?\nWhy don't you share your exprince with your recent purchase?\n\t/share_purchase".format(message.from_user.first_name))






@bot.message_handler(content_types=['text'],
					 func=lambda m: True if purchaser_sending and not name_given and not picture_given and not price_given and not store_name_given and not store_location_given and not store_gps_given and not condition_given and not genuine_given and not rating_given and not review_given and not recommend_given else False
					)
def accept_name(message):
	global name_given
	if message.text[0] == '/':
		bot.reply_to(message, '!is not a product name.\nAnswer by texting for the questions the bot asks.\nWhat is the name of your purchase?\n/cancel')
	elif len(message.text) > 31:
		bot.reply_to(message, '!product name to long.\nname should be less than 30 characters.\nWhat is the name of your purchase?\n/cancel')	
	else:
		name_given = message.text
		bot.reply_to(message, 'product name: ' + name_given + '\nsend the picture of your purchase.\n/cancel')







@bot.message_handler(content_types=['photo'],
					 func=lambda m: True if purchaser_sending and name_given and not picture_given and not price_given and not store_name_given and not store_location_given and not store_gps_given and not condition_given and not genuine_given and not rating_given and not review_given and not recommend_given else False
					)
def accept_photo(message):
	try:
		global picture_given

		fileID = message.photo[-1].file_id
		# print(fileID)
		file_info = bot.get_file(fileID)
		# print(file_info.file_path)
		downloaded_file = bot.download_file(file_info.file_path)

		picture_given = name_given + '-' + str(message.from_user.id) + '-' + str(message.date) + '.jpg'
		uploaded_pic = open('img/uploaded/' + picture_given, 'wb')
		uploaded_pic.write(downloaded_file)
		uploaded_pic.close()

		basehight = 950
		img = Image.open('img/uploaded/' + picture_given)
		hpercent = (basehight / float(img.size[1]))
		wsize = int((float(img.size[0]) * float(hpercent)))
		img = img.resize((wsize, basehight), PIL.Image.ANTIALIAS)
		img.save('img/product/' + picture_given)
		img.close()

		bot.reply_to(message, 'product name: ' + name_given + '\nPhoto: recived\nHow much did you pay for it?\n!don\'t include birr, $, etc...\n/cancel')
	except:
		bot.reply_to(message, '!Photo: is not recived\nTry again send the picture of your purchase. \n/cancel')
		






@bot.message_handler(content_types=['text'],
					 func=lambda m: True if purchaser_sending and name_given and not picture_given and not price_given and not store_name_given and not store_location_given and not store_gps_given and not condition_given and not genuine_given and not rating_given and not review_given and not recommend_given else False
					)
def send_photo_please(message):
	if not message.text[0] == '/':
		bot.reply_to(message, 'send the picture of your purchase.')
	else:
		pass






@bot.message_handler(content_types=['text'],
					 func=lambda m: True if purchaser_sending and name_given and picture_given and not price_given and not store_name_given and not store_location_given and not store_gps_given and not condition_given and not genuine_given and not rating_given and not review_given and not recommend_given else False
					)
def accept_price(message):
	try:
		price = float(message.text)
		if price > 100000000 or price < 0:
			bot.reply_to(message, '!price must be between 0-100,000,000\nHow much did you pay for your:\n' + name_given + '?\n/cancel')
		else:
			global price_given
			price_given = price 
			bot.reply_to(message, 'product name: ' + name_given + '\nprice: ' + str(price_given) + '\nWhat is the name of the store?\n/cancel')
	except:	
		bot.reply_to(message, '!price must be a number \ndon\'t include birr, $, etc...\nHow much did you pay for your:\n' + name_given + '?\n/cancel')







@bot.message_handler(content_types=['text'],
				     func=lambda m: True if purchaser_sending and name_given and picture_given and price_given and not store_name_given and not store_location_given and not store_gps_given and not condition_given and not genuine_given and not rating_given and not review_given and not recommend_given else False
				    )
def accept_store_name(message):
	global store_name_given
	if message.text[0] == '/':
		bot.reply_to(message, '!is not a store name.\nAnswer by texting for the questions the bot asks.\nWhat is the name of the store?\n/cancel')
	elif len(message.text) > 26:	
		bot.reply_to(message, '!store name to long.\nstore name should be less than 25 characters.\nWhat is the name of the store?\n/cancel')
	else:
		store_name_given = message.text
		bot.reply_to(message, 'product name: ' + name_given + '\nstore: ' + store_name_given + '\nWhere is the store?\nEg: Merkato yerga-hayele 2nd floor.\n/cancel')






	
@bot.message_handler(content_types=['text'],
					 func=lambda m: True if purchaser_sending and name_given and picture_given and price_given and store_name_given and not store_location_given and not store_gps_given and not condition_given and not genuine_given and not rating_given and not review_given and not recommend_given else False
					)
def accept_store_location(message):
	global store_location_given
	if message.text[0] == '/':
		bot.reply_to(message, '!is not a store location.\nAnswer by texting for the questions the bot asks.\nWhere is the store?\nEg: Merkato yerga-hayele 2nd floor.\n/cancel')
	elif len(message.text) > 51:
		bot.reply_to(message, '!store location to long.\nstore location should be less than 50 characters.\nWhere is the store?\nEg: Merkato yerga-hayele 2nd floor.\n/cancel')	
	else:
		store_location_given = message.text
		bot.reply_to(message, 'product name: ' + name_given + '\nstore location:' + store_location_given + '\nIf you can give us the location or if you are at the store please turn on your location and send us the store location. If not just send "no location".\n/cancel')







@bot.message_handler(content_types=['location'],
					 func=lambda m: True if purchaser_sending and name_given and picture_given and price_given and store_name_given and store_location_given and not store_gps_given and not condition_given and not genuine_given and not rating_given and not review_given and not recommend_given else False
					)
def accept_store_gps(message):
	try:
		global store_gps_given
		store_gps_given['longitude']=message.location.longitude
		store_gps_given['latitude']=message.location.latitude
		store_gps_given['no_location']=False
		bot.reply_to(message, 'product name: ' + name_given + '\nstore gps location: Recived\nWhat was the condition of your purchase, new or used?\n/cancel')
	except:
		bot.reply_to(message, 'product name: ' + name_given + '\nstore gps location: Not Recived\nTry again. send us location of the store.\n/cancel')
	






@bot.message_handler(content_types=['text'],
					 func=lambda m: True if purchaser_sending and name_given and picture_given and price_given and store_name_given and store_location_given and not store_gps_given and not condition_given and not genuine_given and not rating_given and not review_given and not recommend_given else False
					)
def accept_store_gps_with_no_location(message):
	if not message.text[0] == '/' and message.text.lower() == 'no location':
		global store_gps_given
		store_gps_given['no_location']= True
		bot.reply_to(message, 'product name: ' + name_given + '\nstore gps location: Passed\nWhat was the condition of your purchase, new or used?\n/cancel')
	else:
		bot.reply_to(message, 'send "no location" to pass this step or send us the location of the store.\n/cancel')







@bot.message_handler(content_types=['text'],
					 func=lambda m: True if purchaser_sending and name_given and picture_given and price_given and store_name_given and store_location_given and store_gps_given and not condition_given and not genuine_given and not rating_given and not review_given and not recommend_given else False
					)
def accept_condition(message):
	global condition_given
	if message.text.lower() == 'new' or message.text.lower() == 'used':
		condition_given = message.text
		bot.reply_to(message, 'product name: ' + name_given + '\ncondition: ' + condition_given + '\nIs the product genuine or not?send "yes" or "no:\n/cancel')
	else:
		bot.reply_to(message, '!condition must be, "new" or "used".\nWhat was the condition of your purchase?\n/cancel')








@bot.message_handler(content_types=['text'],
					 func=lambda m: True if purchaser_sending and name_given and picture_given and price_given and store_name_given and store_location_given and store_gps_given and condition_given and not genuine_given and not rating_given and not review_given and not recommend_given else False
					)
def accept_genuine(message):
	global genuine_given
	if message.text.lower() == 'yes' or message.text.lower() == 'no':
		genuine_given = message.text
		bot.reply_to(message, 'product name: ' + name_given + '\ngenuine: ' + genuine_given + '\nHow many stars from 1 to 5 would you give your purchase?\n/cancel')
	else:
		bot.reply_to(message, '!genuine must be, "yes" or "no".\nIs the product genuine or not?\n/cancel')






		

@bot.message_handler(content_types=['text'],
					 func=lambda m: True if purchaser_sending and name_given and picture_given and price_given and store_name_given and store_location_given and store_gps_given and condition_given and genuine_given and not rating_given and not review_given and not recommend_given else False
					)
def accept_rating(message):
	try:
		rating = int(message.text)
		if rating > 6 or rating < 0:
			bot.reply_to(message, 'product name:' + name_given +'\nRating must between 1 to 5\nHow many stars would you give your purchase?\n/cancel')
		else:
			global rating_given
			rating_given = rating
			bot.reply_to(message, 'product name: ' + name_given + '\nRating: ' + str(rating_given) + '\nWrite your review with less than 150 characters?\n/cancel')
	except:
		bot.reply_to(message, '!Rating must be a number and between 1 to 5.\nHow many stars would you give your purchase?\n/cancel')
		






@bot.message_handler(content_types=['text'],
					 func=lambda m: True if purchaser_sending and name_given and picture_given and price_given and store_name_given and store_location_given and store_gps_given and condition_given and genuine_given and rating_given and not review_given and not recommend_given else False
					)
def accept_review(message):
	if len(message.text) < 151 and not message.text[0] == '/':
		global review_given
		review_given = message.text
		bot.reply_to(message, 'product name: ' + name_given + '\nreview: accepted\nDo you recommend this to a friend? Yes or No\n/cancel')
	else:
		bot.reply_to(message, '!Review to long \nWrite your review with less than 150 characters?\n/cancel')
		





@bot.message_handler(content_types=['text'],
					 func=lambda m: True if purchaser_sending and name_given and picture_given and price_given and store_name_given and store_location_given and store_gps_given and condition_given and genuine_given and rating_given and review_given and not recommend_given else False
					)
def accept_recommend(message):
	global recommend_given
	if message.text.lower() == 'yes' or message.text.lower() == 'no':
		recommend_given = message.text
		bot.reply_to(message, 'product name: ' + name_given + '\nrecommend: ' + recommend_given + '\nTo share your purchase send "share"?\nto cancel /cancel')
	else:
		bot.reply_to(message, '!Recommend must be, "yes" or "no".\nDo you recommend this to a friend? Yes or No\n/cancel')






@bot.message_handler(content_types=['text'],
					 func=lambda m: True if purchaser_sending and name_given and picture_given and price_given and store_name_given and store_location_given and store_gps_given and condition_given and genuine_given and rating_given and review_given and  recommend_given else False
					)
def share_purchase(message):
	if message.text.lower() == 'share' and not message.text[0] == '/':
		if genuine_given.lower() == 'yes':
			genuine = True
		elif genuine_given.lower() == 'no':
			genuine = False
		if recommend_given.lower() == 'yes':
			recommend = True
		elif recommend_given.lower() == 'no':
			recommend = False 
		purchase = Purchases()
		if store_gps_given['no_location']:
			purchase.create(name=name_given,
						  picture=picture_given,
						  price=price_given,
						  store_name=store_name_given,
						  store_location=store_location_given,
						  condition=condition_given,
						  genuine=genuine,
						  rating=rating_given,
						  review=review_given,
						  recommend=recommend,
						  gps=False,
						  latitude=0.0,
						  longitude=0.0,
						)
		else:
			purchase.create(name=name_given,
							  picture=picture_given,
							  price=price_given,
							  store_name=store_name_given,
							  store_location=store_location_given,
							  condition=condition_given,
							  genuine=genuine,
							  rating=rating_given,
							  review=review_given,
							  recommend=recommend,
							  gps=True,
							  latitude=store_gps_given['latitude'],
							  longitude=store_gps_given['longitude'],
							)
		#\U0001F6CD == shopping bags
		#\U0001F4B0 == $ bag
		#\U0001F3EA == department store
		#\U0001F4CD == pin	
		#\U00002757 == exclamation mark
		#\U00002122 == TM	
		#\U0001F449 == point right
		#U\00002B50 == star
		genu= "\U00002705" if genuine else "\U0000274C"
		text = "\U0001F6CD  {} \n\U0001F4B0  {} ETB \n\U0001F449  condition:  {} \n\U00002757  genuine\U00002122   {}  \n\U0001F3EA  {} \n\U0001F4CD  {}  ".format(name_given,
																																							 price_str(price_given),
																																							 condition_given,
																																							 genu,
																																							 store_name_given,
																																							 store_location_given,
																																							)
		purchase.save()
		# bot.send_message('@aradabuyer', 'first message form Arada Buyer Bot. click t.me/aradabuyerbot to intract with it.')
	
		bot.reply_to(message, 'Thanks for your time\nproduct name: ' + name_given + '\nis shared. i am sure many of us will learn from it.')
		
		product_pic = open('img/product/' + picture_given, 'rb')
		bot.send_photo('@aradabuyer', product_pic, text)
		product_pic.close()

		stars = '' 
		white_star = 5 - rating_given
		for rating in range(rating_given):
			stars += '\U00002B50'

		for rating in range(white_star):
			stars += '\U00002606'

		reco = '\U00002705' if recommend else '\U0000274C'
		bot.send_message('@aradabuyer', 'REVIEW\n'+ stars + '\n' + review_given + '\nRecommend to a friend  ' + reco)
	

		if not store_gps_given['no_location']:
			bot.send_location('@aradabuyer', store_gps_given['latitude'], store_gps_given['longitude'])
       
	else:
		bot.reply_to(message, '!To share send "share"\nto cancel /cancel')













print("{} bot running....".format(user.first_name))
bot.polling()
print("{} bot stoped!!!!".format(user.first_name))
