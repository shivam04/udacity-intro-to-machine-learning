predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
true_positives = 0
false_positives = 0
false_negatives = 0
true_negatives = 0
for pred, actual in zip(predictions, labels):
	if pred == actual and actual == 1:
		true_positives += 1
	elif pred == 1 and actual == 0:
		false_positives += 1
	elif pred == 0 and actual == 1:
		false_negatives += 1
	else:
		true_negatives += 1
print "True Positives:", true_positives
print "False Positives", false_positives
print "False Negatives", false_negatives
print "True Negatives", true_negatives

print "\nPrecision (POIs):", true_positives/(true_positives + false_positives)
print "Recall (POIs)", true_positives/(true_positives + false_negatives)