import telegram_send as ts
import json

""" data = {'sum' : 82500}
json.dump(data, open('balance.json', 'w')) """
with open ('balance.json', 'r+') as f:
    data = json.load(f)
    ts.send(messages=['Отправить Березу 6875 за гитару\nОсталось: {} rub.'.format(data['sum'])])
    data['sum'] -= 6875
    print(data['sum'])
    f.seek(0)
    json.dump(data, f)
    f.truncate()