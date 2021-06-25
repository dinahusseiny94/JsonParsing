import pandas as pd

filepath = '/Users/dinaelhusseiny/Desktop/Parsing'
json_filename = 'parse.json'
json_filepath = filepath + '/' + json_filename

json_file = open(json_filepath, "r")
df = pd.read_json(json_file)

output = []
data = {}
output_df = []

for key in df.keys():
    filename = key + '.csv'
    output_filepath = filepath + '/' + filename
    data_key = pd.DataFrame(df[key].dropna())
    max_length = 0
    max_row = {}
    for index, row in data_key.iterrows():
        if key == 'countries':
            df_temp = pd.DataFrame.from_dict(row[0])
            df_temp.insert(0, 'Country Name', index)
            output.append(df_temp)
            output_df = pd.concat(output,sort=False)
        if key == 'plotting_dates':
            data[index] = row[0]
    if key == 'plotting_dates':
        output_df = pd.DataFrame.from_dict([data])

    output_df.to_csv(output_filepath, index=False)