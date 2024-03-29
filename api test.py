import json
with open('qqqq.json', encoding="utf8") as f:       # <- документ формата json из папки  , расшифруем
 templates = json.load(f)
 #конверт ДЖСОН B  ПАЙТОН
 #  json_example.json "любой документ  на джейсон иначе не работает"

def CheckInt(item):
 return isinstance(item, int)

def Checkstr(item):
 return isinstance(item, str)
                                   #определяем тип данных
def CheckBool (item):
 return isinstance(item, bool)

def Checkurl(item):
 if isinstance(item, str):
  return item.startswith("http://") or item.startswith("https://")
 else:                         #вернут шттп если тип стр
  return False

def CheckStrvalue(item, val):
 if isinstance(item, str):
  return item in val #вернуть вал или фолс
 else:
  return False

def ErrorLog(item, value, string):


      Error.append({item: f'{value}, {string}'})

listofItems = {'timestamp': 'int', 'item_price': 'int', 'referer': 'url', 'location': 'url', 'item_url': 'url',
'remoteHost': 'str', 'partyId': 'str', 'sessionId': 'str', 'pageViewId': 'str', 'item_id': 'str',
'basket_price': 'str', 'userAgentName': 'str', 'eventType': 'val', 'detectedDuplicate': 'bool',
'detectedCorruption': 'bool', 'firstInSession': 'bool'} # вводим словарь

Error = []        # вводим варианты ошибок
for items in templates:
 for item in items:
  if item in listofItems:
   if listofItems[item] == 'int':
    if not CheckInt(items[item]):
     ErrorLog(item, items[item], f'ожидали типа {listofItems[item]}')
  elif listofItems[item] == 'str':
    if not CheckStr(items[item]):
     ErrorLog(item, items[item], f'ожидали типа {listofItems[item]}')
  elif listofItems[item] == 'bool':
    if not CheckBool(items[item]):
     ErrorLog(item, items[item], f'ожидали типа {listofItems[item]}')
  elif listofItems[item] == 'url':
   if not CheckUrl(items[item]):
      ErrorLog(item, items[item], f'ожидали типа {listofItems[item]}')
  elif listofItems[item] == 'val':
   if not CheckStrValue(items[item], ['itemBuyEvent', 'itemViewEvent']):

     ErrorLog(item, items[item], 'ожидали значение itemBuyEvent или itemViewEvent')

  else:
     ErrorLog(item, items[item], 'невалидное значение')
 else:
     ErrorLog(item, items[item], 'неизвестная переменная')

if Error == []:     # выводим результат проверки апи
 print('Pass')
else:
 print('Fail')
print(Error)
# спасибо что дочитал до конца <3 для меня важен любой фидбек