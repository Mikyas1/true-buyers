# import telebot
# from telebot import types


# TOKEN = '********'
# #username = os.environ['BOT_USERNAME']
# bot = telebot.TeleBot(TOKEN)
# user = bot.get_me()



# k = types.InlineKeyboardMarkup()
# k.add(types.InlineKeyboardButton("test", callback_data="test"))
# bot.send_location('@shemachet', 0.0, 0.0, reply_markup=k)
# text = "\U0001F464 REVIEW\n\U00002B50\U00002B50\U00002B50\U00002606\U00002606\n________________________________________\n\nMike:\njjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj\U0000274C\U0000274C\U0000274C\U0000274C"
# print(len(text))
# bot.send_message('@shemachet', text)#\U000026C4
# bot.send_location('@aradabuyer', '38.752402', '38.752402', 'location')

# @bot.message_handler(content_types=['text'])
# def x(message):
# 	print(message)
# 	bot.reply_to(message, '!Recommend')





# from models import Purchases


# purchase = Purchases()

# purchase.create(user_id="user.id",
# 		      user_name= "first_name",
# 		      purchase_from='PURCHASE_FROM',
# 			  name='NAME_GIVEN',
# 			  picture='PICTURE_GIVEN',
# 			  price=5,
# 			  store_name='STORE_NAME_GIVEN',
# 			  store_location='STORE_LOCATION_GIVEN',
# 			  condition='CONDITION_GIVEN',
# 			  genuine=True,
# 			  rating=4,
# 			  review='REVIEW_GIVEN',
# 			  recommend=True,
# 			  gps=True,
# 			  latitude=12.12,
# 			  longitude=23.23,
# 			  shared=False,
# 			  supercategory='asdf',
# 			  category='asdf',
# 			  reactors=(),
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
# @bot.message_handler(func=lambda msg: True)
# def search_book(message):
#     text = 'test123'
#     keyboard = types.InlineKeyboardMarkup()
#     keyboard.add(types.InlineKeyboardButton("See Bookstores", callback_data="vendor"))
#     markup = types.ReplyKeyboardMarkup(row_width=2)
#     itembtn1 = types.KeyboardButton('/start')
#     itembtn2 = types.KeyboardButton('v')
#     itembtn3 = types.KeyboardButton('d')
#     markup.add(itembtn1, itembtn2, itembtn3)
#     bot.reply_to(message, "Choose one letter:", reply_markup=markup)
#     bot.reply_to(message, text, reply_markup=keyboard)





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







# print("{} bot running....".format(user.first_name))
# bot.polling()
# print("{} bot stoped!!!!".format(user.first_name))


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

# @bot.message_handler(content_types=['text'])
# def private_message(msg):
# 	k = types.InlineKeyboardMarkup()
# 	k.add(types.InlineKeyboardButton("test", callback_data="test"))
# 	bot.reply_to(msg, "test", reply_markup=k)


# @bot.callback_query_handler(func=lambda call: call.data == 'test')
# def private_query(query):
# 	k = types.InlineKeyboardMarkup()
# 	k.add(types.InlineKeyboardButton("test1", callback_data="test"))
# 	bot.edit_message_reply_markup(query.message.chat.id, query.message.message_id, reply_markup=k)



# print("{} bot running....".format(user.first_name))
# bot.polling()
# print("{} bot stoped!!!!".format(user.first_name))

# a = [1,2,3]
# print(len(a))

# import datetime

# def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
# def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
# def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
# def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
# def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
# def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
# def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
# def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))

# prRed("Hello world")
# prGreen("Hello world")
# prYellow("Hello world")
# prLightPurple("Hello world")
# prPurple("Hello world")
# prCyan("Hello world")
# prLightGray("Hello world")
# prBlack("Hello world")


# prGreen('======================================================================================================================================================================')
# prYellow('======================================================================================================================================================================')
# prRed('======================================================================================================================================================================')


# SHEMACH_LOGO = """
#               \033[92m|]]]]]]]]]]]]      ||        ||      ||]]]]]]]]]]      ||]]]]]]]]||[[[[[[[[||           //\\\\              //]]]]]]]]      ||        ||\033[00m
#               \033[92m||                 ||        ||      ||                ||        ||        ||          //  \\\\            //               ||        ||\033[00m
#               \033[92m||                 ||        ||      ||                ||        ||        ||         //    \\\\          //                ||        ||\033[00m
#               \033[92m||                 ||        ||      ||                ||        ||        ||        //      \\\\        ||                 ||        ||\033[00m
#               \033[93m||                 ||        ||      ||                ||        ||        ||       //        \\\\       ||                 ||        ||\033[00m
#               \033[93m||                 ||        ||      ||                ||        ||        ||      //          \\\\      ||                 ||        ||\033[00m
#               \033[93m||]]]]]]]]]]]      ||]]]][[[[||      ||]]]]]]]]]]      ||        ||        ||      ||[[[[[]]]]]||      ||                 ||]]]][[[[||\033[00m
#               \033[93m           ||      ||        ||      ||                ||        ||        ||      ||          ||      ||                 ||        ||\033[00m
#               \033[93m           ||      ||        ||      ||                ||        ||        ||      ||          ||      ||                 ||        ||\033[00m
#               \033[91m           ||      ||        ||      ||                ||        ||        ||      ||          ||      ||                 ||        ||\033[00m
#               \033[91m           ||      ||        ||      ||                ||        ||        ||      ||          ||       \\\\                ||        ||\033[00m
#               \033[91m           ||      ||        ||      ||                ||        ||        ||      ||          ||        \\\\               ||        ||\033[00m
#               \033[91m[[[[[[[[[[[[|      ||        ||      ||]]]]]]]]]]      ||        ||        ||      ||          ||         \\\\]]]]]]]]]     ||        ||\033[00m
# 	"""

# BOT_LOGO = """  
#                                                             \033[92m||]]]]]]]]\\\\          //]]]\\\\        [[[[[[]]]]]]\033[00m   
#                                                             \033[92m||	       ||        //     \\\\            ||\033[00m
#                                                             \033[92m||	       ||       //       \\\\           ||\033[00m
#                                                             \033[92m||         ||      ||         ||          ||\033[00m
#                                                             \033[93m||	       ||      ||         ||          ||\033[00m
#                                                             \033[93m||	      //       ||         ||          ||\033[00m
#                                                             \033[93m||]]]]]]]]]        ||         ||          ||\033[00m
#                                                             \033[93m||        \\\\       ||         ||          ||\033[00m
#                                                             \033[93m||         ||      ||         ||          ||\033[00m
#                                                             \033[91m||         ||      ||         ||          ||\033[00m
#                                                             \033[91m||         ||       \\\\       //           ||\033[00m
#                                                             \033[91m||         ||        \\\\     //            ||\033[00m
#                                                             \033[91m||]]]]]]]]//          \\\\[[[//             ||\033[00m
# 	"""
# print(SHEMACH_LOGO)
# prLightPurple(BOT_LOGO)

# prGreen('======================================================================================================================================================================')
# prYellow('======================================================================================================================================================================')
# prRed('======================================================================================================================================================================')


# prLightPurple('PROCESS STATUS:\n\n')
# prLightPurple('           DATE TIME                PROCESS PROGRESS\n')


# prLightPurple("---> \"{}\" ---> starting \"{}\" bot....\n\n".format(str(datetime.datetime.utcnow()).split('.')[0], "Shemach"))
# prLightPurple("---> \"{}\" ---> \"{}\" bot running....\n\n".format(str(datetime.datetime.utcnow()).split('.')[0], "Shemach"))
# prRed("---> \"{}\" ---> \"{}\" bot stoped !!!!\n\n".format(str(datetime.datetime.utcnow()).split('.')[0], "Shemach"))


# text = """"
# 		This phone is amazing. A huge upgrade from my iPhone 6. The camera is unbelievable. Amazing quality, the screen is so clear i think it bits iPhone 10. It got 1 tb sd and 500 gb internal storage, this phone is very powerful 8 gb ram. Sound quality is best I heard in phones. The os runs perfectly on the hardware 👍.I wasn't sure about buying Samsung product but the quality and feel is 👌🏻superb.

# 		"""
# print(len(text))
