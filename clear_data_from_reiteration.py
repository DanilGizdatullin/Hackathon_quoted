import pandas as pd

with open('data/table_for_db_changed.csv', 'r') as f:
    cntr = 0
    raw_data = ''
    quote_ids = []
    quotes = []
    authors = []
    complexities = []
    for line in f:
        cntr += 1
        if cntr % 4 == 0:
            raw_data += line[0: -1]
            data = raw_data.split('####')
            quote_id, quote, author, complexity = int(data[0]), data[1], data[2], float(data[3])
            quote_ids.append(quote_id)
            quotes.append(quote)
            authors.append(author)
            complexities.append(complexity)
            raw_data = ''
        else:
            raw_data += line[0: -1]
            raw_data += '####'

data_for_df = {
    'quote': pd.Series(quotes, index=quote_ids),
    'author': pd.Series(authors, index=quote_ids),
    'complexity': pd.Series(complexities, index=quote_ids)
}
df = pd.DataFrame(data_for_df)
# d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
#    ....:      'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
print(df.shape)
print(len(df.index))
indexes = df.index
df = df.drop_duplicates(subset='quote')
print(df.shape)

print(len(df.index))
print(len(indexes))
f_write = open('data/table_for_db_changed_1.csv', 'w')
cntr = 0
for index in df.index:
    try:
        row = df.loc[index]
        f_write.write(str(index)+'\n')
        f_write.write(row['quote'] + '\n')
        f_write.write(row['author'] + '\n')
        f_write.write(str(row['complexity']) + '\n')
    except IndexError:
        cntr += 1
        continue
print(cntr)
f_write.close()
