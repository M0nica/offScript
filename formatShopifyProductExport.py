import pandas as pd;

import csv  
pathname = "products_export_1-1.csv"
original_file = pd.read_csv(pathname,sep=",")
df = pd.DataFrame(original_file)

# only keep Title and Body (HTML) column,
# drop blank rows, 
# remove HTML tags
#  and rename Body (HTML to Body)
formatted_file = df[df.columns[df.columns.isin(['Title', 'Body (HTML)'])]].dropna(how='all').replace('<[^<]+?>', '', regex=True).rename(columns={"Body (HTML)": "Body"})

# save formattef file to a csv
save_path = r'product_titles_and_body.csv'
formatted_file.to_csv(save_path, index=False)



