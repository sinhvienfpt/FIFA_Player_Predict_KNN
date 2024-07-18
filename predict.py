import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Load the data
df = pd.read_csv('./data/data.csv')
df = df.dropna()
df
# Define the features and the target
features = ['PAC', 'SHO', 'PAS', 'DRI', 'DEF', 'PHY']
X = df[features]
y = df['Id']


# Create a KNN model    
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)


# Function to predict the player
def FIFA_player_predict(PAC, SHO, PAS, DRI, DEF, PHY):
    input_features = pd.DataFrame({'PAC': [PAC], 'SHO': [SHO], 'PAS': [PAS], 'DRI': [DRI], 'DEF': [DEF], 'PHY': [PHY]})
    result_id = model.predict(input_features)
    
    name,version = df[df['Id'] == result_id[0]][['Name', 'Version']].values[0]
    return "Player: {} - Version: {}".format(name, version)


if __name__ == '__main__':
    print(df.iloc[FIFA_player_predict(97,98,93,98,61,78)])