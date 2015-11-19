import wikiquote
import json
from oauth2client.client import SignedJwtAssertionCredentials
import gspread

json_key = json.load(open('../Weekly Reports-bd2b424c9654.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], bytes(json_key['private_key'], 'UTF-8'), scope)
gc = gspread.authorize(credentials)
wks = gc.open_by_key('15vnTQwm68NnE6CaFpUMfQkKO0w2ab98spE2MuYvkAwI').worksheet('Nonfiction Classic')
i = 1
quotes = []
while i <= 100:
    try:
        a = wikiquote.quotes(wks.cell(i, 1).value, max_quotes=5000)
        print(a)
        quotes.append(a)
        i += 1
    except:
        i += 1
i = 0
with open('quotes5.csv', 'w') as out_file:
  for row in quotes:
      for q in row:
        i += 1
        print(q, file=out_file)
