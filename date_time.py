
from datetime import date, datetime, timedelta
import locale

locale.setlocale(locale.LC_ALL, "russian")

today = datetime.now()
yesterday = today - timedelta(days=1)
days_ago_30 = today - timedelta(days=30)

yesterday = yesterday.strftime('%d %B %Y')
today = today.strftime('%d %B %Y')
days_ago_30 = days_ago_30.strftime('%d %B %Y')
print(f'Вчера - {yesterday}\nСегодня - {today}\n30 дней назад - {days_ago_30}')


#Превратите строку "01/01/25 12:10:03.234567" в объект datetime
date_string = '01/01/25 12:10:03.234567'
string_date = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
print(string_date)

