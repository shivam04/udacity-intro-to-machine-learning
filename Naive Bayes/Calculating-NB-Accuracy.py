def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB

    ### create classifier
    clf = GaussianNB()

    ### fit the classifier on the training features and labels
    clf.fit(features_train,labels_train)

    ### use the trained classifier to predict labels for the test features
    pred = clf.predict(features_test)


    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example, 
    ### where we just print the accuracy
    ### you might need to import an sklearn module
    #method 1
    c = 0
    t = len(labels_test)
    for i in range(0,t):
        if float(pred[i])==float(labels_test[i]):
            c+=1
    #print float(c)/float(t)
    accuracy = float(c)/float(t)
    #method 2
    accuracy =  clf.score(features_test, labels_test)
    return accuracy