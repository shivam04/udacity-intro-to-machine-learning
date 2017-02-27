#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import sys
import pickle
import re
import numpy as np
sys.path.append("../tools/")
from feature_format import featureFormat
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#total person
print len(enron_data)
#total features
print len(enron_data[enron_data.keys()[0]])

#poi
poi = 0
for k in enron_data.keys():
	if enron_data[k]["poi"]==1:
		poi+=1
print poi

#total poi in text
poi_a = 0
with open("../final_project/poi_names.txt") as f:
	lines = f.readlines()
	for line in lines:
		if re.match(r'\((y|n)\)',line):
			poi_a+=1
print poi_a

#James Prentice total value
print enron_data['PRENTICE JAMES']['total_stock_value']

#Wesley Colwell to POI emails
print enron_data["COLWELL WESLEY"]['from_this_person_to_poi']

#value of stock option exercised by Jeffrey K Skilling

print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

#max total payment
max_total_payment = -1
person = ""
for k in ("LAY KENNETH L", "SKILLING JEFFREY K", "FASTOW ANDREW S"):
	if enron_data[k]['total_payments'] > max_total_payment:
		max_total_payment = enron_data[k]['total_payments']
		person = k

print person,max_total_payment

#How many folks in this dataset have a quantified salary? What about a known email address?
salaries_available = 0
email_available = 0
for k in enron_data.keys():
	if enron_data[k]['salary']!='NaN':
		salaries_available+=1
	if enron_data[k]['email_address']!='NaN':
		email_available+=1
print salaries_available,email_available

#How many people in the E+F dataset have NaN for their payments?
# What percentage of people in the dataset as a whole is this?

total_payments_unavailable = 0
total_payments_unavailable_poi = 0
for k in enron_data.keys():
	if enron_data[k]['total_payments']=='NaN':
		total_payments_unavailable+=1
print total_payments_unavailable,float(total_payments_unavailable)/len(enron_data)*100


# HOw may POIs in the E+F dataset have Nan for their total payments?
# What percentage of POIs as a whole is this?

total_payments_unavailable_poi = 0
for k in enron_data.keys():
	if enron_data[k]['total_payments']=='NaN':
		if enron_data[k]['poi']:
			total_payments_unavailable_poi+=1
print total_payments_unavailable_poi,float(total_payments_unavailable_poi)/len(enron_data)*100