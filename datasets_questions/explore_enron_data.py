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

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
#lenght of the dataset
print('number of people ', len(enron_data)) 
#number of features
print('number of features', len(enron_data['GLISAN JR BEN F'])) 

names = enron_data.keys() 
n_poi = 0
for i in range(len(enron_data)):
	n_poi += enron_data[names[i]]["poi"]

print('number of persons of interest', n_poi)

print('James Prentice value of stock', enron_data['PRENTICE JAMES']['total_stock_value'])

print('Email messages from Wesley Colwell to persons of interest', enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

print('Value of stock options exercised by Jeffrey K Skilling', enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

print('Lay, Skillin, Fastow took home ', enron_data['LAY KENNETH L']['total_payments'], enron_data['SKILLING JEFFREY K']['total_payments'], enron_data['FASTOW ANDREW S']['total_payments'])

q_salary = 0
email = 0
not_payment = 0
poi_not_payment = 0
for person in enron_data:
	for key, value in enron_data[person].items():
		if (key == 'salary' and value != 'NaN'):
			q_salary +=1
		if (key == 'email_address' and value != 'NaN'):
			email +=1
		if (key == 'total_payments' and value == 'NaN'):
			not_payment +=1
		if (key == 'poi' and value == 1 and enron_data[person]['total_payments'] == 'NaN'):
			poi_not_payment +=1
	

print('number of folks in this dataset which have a quantified salary and email', q_salary, email)

percentage = not_payment*100/len(enron_data)

print(' number people in the E+F dataset (as it currently exists) have NaN for their total payments', not_payment, percentage )

print('percentage of pois in the dataset with NaN in their total payments ', poi_not_payment*100/len(enron_data))


