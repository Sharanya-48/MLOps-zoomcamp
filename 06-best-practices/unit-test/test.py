import sample
ride = {
    "PULocationID": 10,
    "DOLocationID": 50,
    "trip_distance": 40
}

features=sample.prepare_features(ride)
print(sample.predict(features))