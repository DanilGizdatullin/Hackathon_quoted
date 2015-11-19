# -​*- coding: utf-8 -*​-
# import complexity_and_check

from complexity_and_check import check_quote
from complexity_and_check import sentence_complexity

sentence_id = 1
# cntr = 0
f_write = open('data/table_for_db.csv', 'w')
with open('data/all_quotes.csv', 'r') as f_read:
    for line in f_read:
        sentence = line[0: -1]
        try:
            if check_quote(sentence):
                try:
                    complexity = sentence_complexity(sentence)
                    f_write.write(str(sentence_id)+'\n'+sentence+'\n'+'authors'+'\n'+str(complexity)+'\n')
                    # cntr += 1
                except:
                    print('Type 1')
                    print(sentence)
        except:
            print('Type 2')
            print(sentence)
        # if cntr == 100:
        #     break
        sentence_id += 1
        # if sentence_id == 87:
        #     break
f_write.close()
