import telebot
import pandas as pd
import pickle
from Preproccesing import clean_text
from Preproccesing import lemma_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

bot = telebot.TeleBot('')

def check(text: str)->bool:
    '''Какие-то действия с текстом, если новость правда выводи True, неправда- False'''

    with open("Tf-idf.pkl", "rb") as f:
        tf = pickle.load(f)

    with open("SVM.pkl", "rb") as f:
        model = pickle.load(f)

    text = clean_text(text)
    text = lemma_text(text)
    text_tf = tf.transform(pd.Series(text))

    prediction = model.predict(text_tf)[0]

    if prediction == 1:
        return True
    else:
        return False

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Приветствую, я бот для проверки честности новостей на испанском языке\nПросто отправьте мне новость и я дам ответ')

@bot.message_handler(content_types=['text'])
def news(message):
    bot.send_message(message.chat.id, 'Данная новость правдивая' if check(message.text) else 'Данная новость фейк')

bot.polling(none_stop=True)


