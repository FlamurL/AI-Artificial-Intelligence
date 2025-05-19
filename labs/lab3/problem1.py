import os
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from dataset_script import dataset
from submission_script import submit_train_data, submit_test_data, submit_classifier, submit_encoder

if __name__ == '__main__':

    encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
    encoder.fit([row[:-1] for row in dataset])


    train_set = dataset[:int(0.75 * len(dataset))]
    train_X = [row[:-1] for row in train_set]
    train_Y = [str(row[-1]) for row in train_set]
    train_X_encoded = encoder.transform(train_X)

    test_set = dataset[int(0.75 * len(dataset)):]
    test_X = [row[:-1] for row in test_set]
    test_Y = [str(row[-1]) for row in test_set]
    test_X_encoded = encoder.transform(test_X)

    classifier = CategoricalNB()
    classifier.fit(train_X_encoded, train_Y)


    accuracy = 0
    for sample_x, sample_y in zip(test_X_encoded, test_Y):
        prediction = classifier.predict([sample_x])[0]
        if prediction == sample_y:
            accuracy += 1
    accuracy = accuracy / len(test_X)
    print(f"{accuracy:.16f}")


    input_test = input().strip().split()

    input_test_x_encoded = encoder.transform([input_test])


    prediction_input = classifier.predict(input_test_x_encoded)[0]
    predictions_input_probabilities = classifier.predict_proba(input_test_x_encoded)
    print(prediction_input)
    print(predictions_input_probabilities)


    submit_train_data(train_X_encoded, train_Y)
    submit_test_data(test_X_encoded, test_Y)
    submit_classifier(classifier)
    submit_encoder(encoder)