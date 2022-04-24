import telegram_send as ts
import json

""" data = {'sum' : 82500}
json.dump(data, open('balance.json', 'w')) """
with open ('/Users/dboldin/Python/Telegram/SendMessage/balance.json', 'r+') as f:
    data = json.load(f)
    data['sum'] -= 6875
    ts.send(messages=['Отправить Березу 6875 за гитару\nОсталось: {} rub.'.format(data['sum'])])
    print(data['sum'])
    f.seek(0)
    json.dump(data, f)
    f.truncate()