import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB

X_train = np.array([1.4, 1.0, 1.3, 1.9, 2.0, 1.8, 3.0, 3.8, 4.1, 3.9, 4.2, 3.4]).reshape(-1, 1)
y_train = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

classifier = GaussianNB()
clf = classifier.fit(X_train, y_train)

# predict
X_test = [[3.4]]

prob = clf.predict_proba(X_test)

print("P(Class = 0 | X) =", prob[0, 0])
print("P(Class = 1 | X) =", prob[0, 1])