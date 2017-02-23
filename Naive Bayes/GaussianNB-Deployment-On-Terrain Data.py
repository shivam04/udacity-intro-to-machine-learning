def classify(features_train, labels_train):   
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(features_train, labels_train)
    return clf
    
    
    ### your code goes here!
    
    #pred = clf.predict(features_test) 