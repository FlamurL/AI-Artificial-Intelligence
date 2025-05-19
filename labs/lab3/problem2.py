import os
from sklearn.naive_bayes import GaussianNB

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from dataset_script import dataset

if __name__ == '__main__':

    dataset = [[float(i) for i in row] for row in dataset]


    train_set = dataset[:int(0.85 * len(dataset))]
    train_X = [row[:-1] for row in train_set]
    train_Y = [int(row[-1]) for row in train_set]

    test_set = dataset[int(0.85 * len(dataset)):]
    test_X = [row[:-1] for row in test_set]
    test_Y = [int(row[-1]) for row in test_set]


    classifier = GaussianNB(var_smoothing=1e-9)
    classifier.fit(train_X, train_Y)


    accuracy = 0
    for test_x, test_y in zip(test_X, test_Y):
        predicted = int(classifier.predict([test_x])[0])
        if predicted == int(test_y):
            accuracy += 1
    accuracy = accuracy / len(test_set)
    print(f"{accuracy:.16f}")


    input_test = [float(i) for i in input().strip().split()]

    prediction_from_input = int(classifier.predict([input_test])[0])
    print(prediction_from_input)
    print(classifier.predict_proba([input_test]))

