import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from submission_script import *
from dataset_script import dataset

if __name__ == '__main__':
  c = int(input())
  t = int(input())
  crit = input().strip()
  new = list(map(float, input().split()))
  n = len(dataset)
  k = int(n * 0.85)
  x = [r[:c] + r[c+1:-1] for r in dataset]
  y = [r[-1] for r in dataset]
  tr_x = x[:k]
  tr_y = y[:k]
  ts_x = x[k:]
  ts_y = y[k:]
  new = new[:c] + new[c+1:] if c < len(new) else new
  clf = RandomForestClassifier(n_estimators=t, criterion=crit, random_state=0)
  clf.fit(tr_x, tr_y)
  pred = clf.predict(ts_x)
  acc = accuracy_score(ts_y, pred)
  new_pred = clf.predict([new])[0]
  probs = clf.predict_proba([new])[0]
  submit_train_data(tr_x, tr_y)
  submit_test_data(ts_x, ts_y)
  submit_classifier(clf)
  print(f"Accuracy: {acc}")
  print(new_pred)
  print(probs)