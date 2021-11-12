import pandas as pd
import itertools
from collections import Counter

#filename= "C:\\Users\\14088\\Documents\\Books\\CS410 - TIS\\documents_utf8_filtered_20pageviews.csv"
#chunksize = 10 ** 8
#for chunk in pd.read_csv(filename, chunksize=chunksize):
#    process(chunk)

filename= "C:\\Users\\14088\\Documents\\Books\\CS410 - TIS\\documents_utf8_filtered_20pageviews.csv"
df = pd.read_csv(filename, header = None)

#### to view the column content ####
#  df[df.columns[1]][8]

#### Extracting the Title of the page ####
title_list = []
def find_index(vec):
    for i in range(len(vec)):
        index_ptr = vec[i][1:].index('')
        title_list.append(vec[i][1:(index_ptr + 1)])



df1 = df[df.columns[1]].str.split(' ')
find_index(df1)
title_flat_list = list(itertools.chain.from_iterable(title_list))

counts = Counter(title_flat_list)
print(counts)
x = counts.most_common(100)




