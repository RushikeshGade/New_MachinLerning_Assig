import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def MarvellousPlayPredictor(data_path):
    # Step 1: Load data
    data = pd.read_csv(data_path, index_col=0)

    print("Size of Actual dataset:", len(data))

    # Step 2: Clean, Prepare and manipulate data
    feature_names = ['Whether', 'Temperature']
    print("Feature Names:", feature_names)

    whether = data['Whether']
    temperature = data['Temperature']
    play = data['Play']

    # Creating label encoder
    le = preprocessing.LabelEncoder()

    # Convert string labels into numeric values
    weather_encoded = le.fit_transform(whether)
    print("Weather Encoded:", weather_encoded)

    temp_encoded = le.fit_transform(temperature)
    print("Temperature Encoded:", temp_encoded)

    label = le.fit_transform(play)

    # Combine weather and temperature into a single list of tuples
    features = list(zip(weather_encoded, temp_encoded))

    # Step 3: Train the model
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(features, label)

    # Step 4: Test prediction
    predicted = model.predict([[0, 2]])  # 0: Overcast, 2: Mild
    print("Prediction for [Overcast, Mild]:", predicted)

def main():
    print("Machine Learning Application")
    print("Play Predictor using K Nearest Neighbors Algorithm")

    MarvellousPlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()


# OR


# def main():
#     # Load data
#     data = pd.read_csv("PlayPredictor.csv")


#     # Clean, Prepare and manipulate data
#     feature_nm = ['Whether', 'Temperature']
#     print("Feature names:", feature_nm)

#     # Creating labelEncoder
#     label_encoder = preprocessing.LabelEncoder()

#     data['Play'] = label_encoder.fit_transform(data['Play'])
#     data['Whether'] = label_encoder.fit_transform(data['Whether'])
#     data['Temperature'] = label_encoder.fit_transform(data['Temperature'])


#     # Combining weather and temp into single listof tuples
#     features = list(zip(data['Whether'], data['Temperature']))
#     labels = data['Play']

#     # Split into train and test sets (70% train, 30% test)
#     X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)


#     # train the model
#     classifier = KNeighborsClassifier(n_neighbors=3)
#     classifier.fit(X_train, y_train)

#     # Predict on Test data data_test
#     predictions = classifier.predict(X_test) # 0:Overcast, 2: Mild
#     print(predictions)

#     # Evaluate accuracy
#     accuracy = accuracy_score(y_test, predictions)
#     print("Model Accuracy:", round(accuracy * 100, 2), "%")

#     # Predict for a custom input: [0: Overcast, 2: Mild]
#     sample_prediction = classifier.predict([[0, 2]])
#     print("Prediction for [Overcast, Mild]:", label_encoder.inverse_transform(sample_prediction))

# if __name__ =="__main__":
#     main()
