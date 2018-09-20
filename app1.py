import telebot
from telebot import types


TOKEN = '655462722:AAFgk2fEtpB7fkByuLEFTZ-Lx9rV8xxlCPI'
#username = os.environ['BOT_USERNAME']
bot = telebot.TeleBot(TOKEN)
user = bot.get_me()

# text = "\U00002B06 REVIEW\n\U00002B50\U00002B50\U00002B50\U00002606\U00002606\n________________________________________\n\nMike:\njjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj\U0000274C\U0000274C\U0000274C\U0000274C"
# # # print(len(text))
# bot.send_message('https://t.me/joinchat/AAAAAEjUTBtpeh_EsT9D_A', text)#\U000026C4
# bot.send_location('@aradabuyer', '38.752402', '38.752402', 'location')

# @bot.message_handler(content_types=['text'])
# def x(message):
# 	print(message)
# 	bot.reply_to(message, '!Recommend')





# from models import Purchases


# purchase = Purchases()

# purchase.create(name="name_given",
# 			  picture="picture_given",
# 			  price=3,
# 			  store_name='store_name_given',
# 			  store_location='store_location_given',
# 			  condition='condition_given',
# 			  genuine=True,
# 			  rating=3,
# 			  review='review_given',
# 			  recommend=False,
# 			  gps=True,
# 			  latitude=23,
# 			  longitude=34,
# 			)

# purchase.save()

# import PIL
# from PIL import Image

# basewidth = 960
# img = Image.open('test/photo.jpg')
# wpercent = (basewidth / float(img.size[0]))
# hsize = int((float(img.size[1]) * float(wpercent)))
# img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
# img.save('test/resized_photo.jpg')

# search book
@bot.message_handler(func=lambda msg: True)
def search_book(message):
    text = 'test123'
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton("See Bookstores", callback_data="vendor"))
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('/start')
    itembtn2 = types.KeyboardButton('v')
    itembtn3 = types.KeyboardButton('d')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Choose one letter:", reply_markup=markup)
    bot.reply_to(message, text, reply_markup=keyboard)





# 
# GLOBAL VARIABLES
# USER = {}


# # 
# # WELCOME MESSAGE HANDLER
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
# 	try:
# 	    global USER 
# 	    USER[str(message.from_user.id)] = {}
# 	    USER[str(message.from_user.id)]['NOT_PURCHASER_FROM'] = True
# 	    print(USER)
# 	    bot.reply_to(message, "to cancle /cancle")
# 	except Exception as e:
# 		print(e)



# # 
# # WELCOME MESSAGE HANDLER
# @bot.message_handler(commands=['cancle'])
# def send_welcome(message):
# 	try:
# 	    global USER 
# 	    USER[str(message.from_user.id)] = {}
# 	    print(USER)
# 	    bot.reply_to(message, "to start /start")
# 	except Exception as e:
# 		print(e)







print("{} bot running....".format(user.first_name))
bot.polling()
print("{} bot stoped!!!!".format(user.first_name))


# USER = {}

# USER['12'] = {}

# if '12' not in USER:
# 	print('YES')

# print(USER)

# import pymongo

# uri = "mongodb://127.0.0.1:27017"

# client = pymongo.MongoClient(uri)

# database = client['fullstack']

# collection = database['students']

# collection.update_one({
# 	'name': "mike"
# },{
# 	'$set': {
# 	'mark': 4
# 	}
# }, upsert=False)


# x = collection.find_one({"name": "mike"})

# print(x)

