from django.shortcuts import render

def usersmain(request):
 return render(request, 'usersmain/mainuser.html')

import requests
import datetime


# функция которая принивмает адрес кошелька и получает
# информацию от trongrid по последним 20ти транзакциям полльзователя
def get_request(adres):
    request = requests.get(f"https://api.trongrid.io/v1/accounts/{adres}/transactions/trc20",
                           headers={"acccept": "application/json"})
    return request


# функция которая достает нужную информацию из  ответа trongrida
def parsing_the_transaction(reuquest):
    for trans in reuquest.json().get('data', []):
        symbol = trans.get('token_info', {}).get('symbol')
        time_ = datetime.datetime.fromtimestamp(float(trans.get('block_timestamp', '')) / 1000)
        sender = trans.get('from', '')
        addressee = trans.get('to', '')
        value = trans.get('value', '')

        dec = -1 * int(trans.get('token_info', {}).get('decimals', ''))
        value = float(value[:dec] + '.' + value[dec:])

        transaction_tuple = (time_, value, symbol, sender, addressee)

        yield transaction_tuple


# функция которая вернет 1 если транзакция подходящая под заданные условия существует
# и ноль если нет
def checking_last_20_transactions(transaction, usdt_amount, usdt_sender, usdt_addressee, deltatime):
    # получаю время для сравнения с временем транзакций
    # Получаем текущее время
    now = datetime.datetime.now()
    # Вычисляем время сколько-то секунд назад
    time_30_seconds_ago = now - datetime.timedelta(seconds=deltatime)

    # получаю необходимую инфу из переданного функцией parsing_the_transaction списка
    time_ = transaction[0]
    value = transaction[1]
    symbol = transaction[2]
    sender = transaction[3]
    addressee = transaction[4]

    # длинный бллок с условием, должно быть время трранзакции в пределах того что нам надо,
    # отправитель и адресат должни совпадать с теми который нам нужны,
    # количество usdt должно быть тем что нам надо и это должен быть usdt
    if time_30_seconds_ago <= time_ <= now and float(
            value) >= usdt_amount and symbol == "USDT" and sender == usdt_sender and addressee == usdt_addressee:
        # print(f"{time_} | {value:>9.02f} {symbol} | {sender} --> {addressee}")
        return 1
    else:
        return 0


# основная функция которая должна вызываться
def chacking_transaction():
    response = get_request("TTkyAktX8DUVYvHvnWwNB4Dv6kfh5hyvRr")
    is_transaction = 0
    # проверяю есть ли в последних 20 транзакциях пользователя нужная мне транзакция
    # она была совершена в пределах 20ти дней от текущего времени,
    # отправитель: TTkyAktX8DUVYvHvnWwNB4Dv6kfh5hyvRr,
    # получатель: TAg3oyHwswaJjNTyximhvQpkZ2J3bdEGMo
    for i in range(21):
        is_transaction = checking_transaction(
            next(parsing_the_transaction(response)),
            1,
            "TTkyAktX8DUVYvHvnWwNB4Dv6kfh5hyvRr",
            "TAg3oyHwswaJjNTyximhvQpkZ2J3bdEGMo",
            1728000
        )
