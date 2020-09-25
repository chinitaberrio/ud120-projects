#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    error = net_worths - predictions
    abs_error = abs(error)
    index = sorted(range(len(abs_error)), key=lambda k: abs_error[k])
   
    cleaned_data = []
    ### your code goes here
    for i in range(81): 
        cleaned_data += ((ages[index[i]], net_worths[index[i]], error[index[i]]),)
        
    return cleaned_data

