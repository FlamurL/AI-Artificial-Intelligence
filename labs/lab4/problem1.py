import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import math
from submission_script import *
from dataset_script import dataset

if __name__ == '__main__':
  p = int(input())
  crit = input().strip()
  n = len(dataset)
  k = math.ceil(n * p / 100)
  le = LabelEncoder()
  m = len(dataset[0]) - 1
  xe = [[] for _ in range(m)]
  ye = []
  for i in range(m):
    f = [r[i] for r in dataset]
    xe[i] = le.fit_transform(f)
  ye = le.fit_transform([r[-1] for r in dataset])
  xe = np.array(xe).T
  tr = xe[-k:]
  ts = xe[:-k]
  tr_y = ye[-k:]
  ts_y = ye[:-k]
  clf = DecisionTreeClassifier(criterion=crit, random_state=0)
  clf.fit(tr, tr_y)
  pred = clf.predict(ts)
  acc = accuracy_score(ts_y, pred)
  d = clf.get_depth()
  l = clf.get_n_leaves()
  imp = clf.feature_importances_
  mx = np.argmax(imp)
  mn = np.argmin(imp)
  tx = [r[:-1] for r in dataset[-k:]]
  ty = [r[-1] for r in dataset[-k:]]
  sx = [r[:-1] for r in dataset[:-k]]
  sy = [r[-1] for r in dataset[:-k]]
  submit_train_data(tx, ty)
  submit_test_data(sx, sy)
  submit_classifier(clf)
  submit_encoder(le)
  print(f"Accuracy: {acc}")
  print(f"Depth: {d}")
  print(f"Number of leaves: {l}")
  print(f"Most important feature: {mx}")
  print(f"Least important feature: {mn}")