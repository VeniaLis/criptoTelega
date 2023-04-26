import requests
from datetime import datetime
import telebot
from criptoken import token


def get_data():
    req = requests.get('https://yobit.net/api/3/ticker/eth_usd/')
    req2 = requests.get('https://yobit.net/api/3/ticker/xrp_usd/')
    req3 = requests.get('https://yobit.net/api/3/ticker/btc_usd/')
    req4 = requests.get('https://yobit.net/api/3/ticker/usdt_usd/')
    req5 = requests.get('https://yobit.net/api/3/ticker/ltc_usd/')
    response = req.json()
    response2 = req2.json()
    response3 = req3.json()
    response4 = req4.json()
    response5 = req5.json()
    sell_price = response['eth_usd']['sell']
    buy_price = response['eth_usd']['buy']
    sell_price2 = response2['xrp_usd']['sell']
    buy_price2 = response2['xrp_usd']['buy']
    sell_price3 = response3['btc_usd']['sell']
    buy_price3 = response3['btc_usd']['buy']
    sell_price4 = response4['usdt_usd']['sell']
    buy_price4 = response4['usdt_usd']['buy']
    sell_price5 = response5['ltc_usd']['sell']
    buy_price5 = response5['ltc_usd']['buy']
    print(f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nsell ETH price: {sell_price}\nbuy ETH price: {buy_price}\n'
          f'sell XRP price: {sell_price2}\nbuy XRP price: {buy_price2}',
          f'\nsell BTC price: {sell_price3}\nbuy BTC price: {buy_price3}',
          f'\nsell USDT price: {sell_price4}\nbuy USDT price: {buy_price4}',
          f'\nsell LTC price: {sell_price5}\nbuy LTC price: {buy_price5}')

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id,'Привет друг, если хочешь узнать о курсах крипты напиши "eth", "xrp", "btc", "usdt", "ltc" в телеге!')

    @bot.message_handler(content_types=['text'])
    def send_message(message):
        if message.text.lower() == 'eth':
            try:
                req = requests.get('https://yobit.net/api/3/ticker/eth_usd/')
                response = req.json()
                sell_price = response['eth_usd']['sell']
                buy_price = response['eth_usd']['buy']
                bot.send_message(
                    message.chat.id,
                    f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nцена продажи ETH: {sell_price}\nцена покупки ETH: {buy_price}'
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id, 'Что-то пошло не так! Попробуй еще раз!'
                )
        elif message.text.lower() == 'xrp':
            try:
                req2 = requests.get('https://yobit.net/api/3/ticker/xrp_usd/')
                response2 = req2.json()
                sell_price2 = response2['xrp_usd']['sell']
                buy_price2 = response2['xrp_usd']['buy']
                bot.send_message(
                    message.chat.id,
                    f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nцена продажи XRP: {sell_price2}\nцена покупки XRP: {buy_price2}')

            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id, 'Что-то пошло не так! Попробуй еще раз!'
                )

        elif message.text.lower() == 'btc':
            try:
                req3 = requests.get('https://yobit.net/api/3/ticker/btc_usd/')
                response3 = req3.json()
                sell_price3 = response3['btc_usd']['sell']
                buy_price3 = response3['btc_usd']['buy']
                bot.send_message(
                    message.chat.id,
                    f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nцена продажи BTC: {sell_price3}\nцена покупки BTC: {buy_price3}'
                )

            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id, 'Что-то пошло не так! Попробуй еще раз!'
                )
        elif message.text.lower() == 'usdt':
            try:
                req4 = requests.get('https://yobit.net/api/3/ticker/usdt_usd/')
                response4 = req4.json()
                sell_price4 = response4['usdt_usd']['sell']
                buy_price4 = response4['usdt_usd']['buy']
                bot.send_message(
                    message.chat.id,
                    f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nцена продажи USDT: {sell_price4}\nцена покупки USDT: {buy_price4}'
                )

            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id, 'Что-то пошло не так! Попробуй еще раз!'
                )
        elif message.text.lower() == 'ltc':
            try:
                req5 = requests.get('https://yobit.net/api/3/ticker/ltc_usd/')
                response5 = req5.json()
                sell_price5 = response5['ltc_usd']['sell']
                buy_price5 = response5['ltc_usd']['buy']
                bot.send_message(
                    message.chat.id,
                    f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nцена продажи LTC: {sell_price5}\nцена покупки LTC: {buy_price5}'
                )

            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id, 'Что-то пошло не так! Попробуй еще раз!'
                )

        else:
            bot.send_message(message.chat.id,'Не не не только XRP BTC ETH USDT LTC')

    bot.polling()



if __name__ == '__main__':
    get_data()
    telegram_bot(token)