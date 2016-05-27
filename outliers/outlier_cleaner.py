#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    residual_erros = [ (abs(x-y), i) for i,(x,y) in enumerate(zip(predictions, net_worths))]
    residual_erros.sort()
    new_total_length =  int(len(residual_erros) * 0.9 ) # 10% removed 
    residual_erros = residual_erros[ : new_total_length]
    for err, i in residual_erros:
        cleaned_data.append((ages[i], net_worths[i], err))
    return cleaned_data

