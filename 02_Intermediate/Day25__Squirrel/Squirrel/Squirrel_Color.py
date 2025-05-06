import pandas as pd

data = pd.read_csv("Day25/Squirrel/Squirrel_Census.csv")
data = data.rename(columns={'Primary Fur Color': 'Color'})
gray = len(data[data['Color'] == 'Gray'])
red = len(data[data['Color'] == 'Cinnamon'])
black = len(data[data['Color'] == 'Black'])

data_dict = {
    'Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray, red, black]
}

new_data = pd.DataFrame(data_dict)
new_data.to_csv("Day25/Squirrel/new_data.csv")
