import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Load the data
df = pd.read_csv('./data.csv')
df = df.dropna()

# Define the features and the target
features = ['PAC', 'SHO', 'PAS', 'DRI', 'DEF', 'PHY']
X = df[features]
y = df['Name']


# Create a KNN model    
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)


# Function to predict the player
def FIFA_player_predict(PAC, SHO, PAS, DRI, DEF, PHY):
    input_features = pd.DataFrame({'PAC': [PAC], 'SHO': [SHO], 'PAS': [PAS], 'DRI': [DRI], 'DEF': [DEF], 'PHY': [PHY]})
    result = model.predict(input_features)
    return result


if __name__ == '__main__':
    print(FIFA_player_predict(90, 80, 70, 90, 60, 80))


