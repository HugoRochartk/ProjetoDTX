import pandas as pd

df = pd.read_csv('C:\\Users\\HugoRocha\\Desktop\\ProjetoDTX\dataframes\\binary_labeled_dataframe.csv', sep=';')

print(df['label'])

h_c = 0
nh_c = 0

for i, elem in enumerate(df['label']):
    if elem == 'Highlight':
        h_c += 1

    else:
        nh_c += 1


print(f'Highlights: {h_c}\nNon-Highlights: {nh_c}')
