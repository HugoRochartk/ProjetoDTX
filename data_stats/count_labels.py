import pandas as pd



df2 = pd.read_csv('C:\\Users\\HugoRocha\\Desktop\\ProjetoDTX\dataframes\\multi_labeled_dataframe.csv', sep=';')


counter = {}


for s in list(df2['possible_labels']):

    splitted = s.split('/')
    for label in splitted:
        if label not in counter:
            counter[label] = 1
        else:
            counter[label] += 1


print(sorted(list(counter.items()), key = lambda x: -x[1]))
