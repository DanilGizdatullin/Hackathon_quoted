import pandas as pd
import matplotlib.pyplot as plt
import pickle

with open('data/table_for_db_changed_1.csv', 'r') as f:
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
complexity = df['complexity'].values.copy()
print(df.columns)
# map(lambda x: 0.03 if x>0.022 else x, complexity)
# big_complexity = filter(lambda x: x>0.022, complexity)
print(len(set(complexity)))
(n, bins, patches) = plt.hist(complexity, bins=len(set(complexity)))
print(n)
plt.show()
# print(n)
# print(bins)
# print(len(n))
# print(len(bins))


def give_a_borders(n_id):
    return [bins[n_id], bins[n_id + 1]]
for _ in xrange(5):
    for i in xrange(len(n)-1, 0, -1):
        if n[i] == 0:
            left_border, right_border = give_a_borders(i)
            shift = (right_border - left_border)*0.9
            complexity = map(lambda x: x - shift if x > left_border else x, complexity)
    # pickle.dump(complexity, open('complexity', 'wb'))
    # complexity = pickle.load(open('complexity', 'rb'))
    (n, bins, patches) = plt.hist(complexity, bins=len(set(complexity)))
    # plt.show()
    print(n)
df_new = df.copy()
df_new['complexity'] = pd.Series(complexity, index=df_new.index)

df_new = df_new.sort(['complexity'], ascending=[1])
print(df_new.index)
print(df.sort(['complexity'], ascending=[1]).index)
print(list(df_new.index))
if list(df_new.index) == list(df.sort(['complexity'], ascending=[1]).index):
    print True
else:
    print False

if list(df_new.index) == list(df.index):
    print True
else:
    print False
#
# print(df.index)
big_complexity = df_new['complexity']
min_val = min(big_complexity)
max_val = max(big_complexity)

print min_val
print max_val

new_complexity = map(lambda x: (x - min_val) / (max_val - min_val), big_complexity)

df_new['complexity'] = pd.Series(new_complexity, index=df_new.index)

f_write = open('data/table_for_db_normalized.csv', 'w')
cntr = 0
for index in df_new.index:
    try:
        row = df_new.loc[index]
        f_write.write(str(index)+'\n')
        f_write.write(row['quote'] + '\n')
        f_write.write(row['author'] + '\n')
        f_write.write(str(row['complexity']) + '\n')
    except IndexError:
        cntr += 1
        continue
print(cntr)
f_write.close()

big_complexity = df_new['complexity']
min_val = min(big_complexity)
max_val = max(big_complexity)
# plt.hist(new_complexity, bins=len(set(new_complexity)))
plt.hist(new_complexity, bins=100)
plt.show()
print min_val
print max_val
