###
# This is an interesting algorithm that compares two sets of data directly and returns a result. 
# It can be used to compare two sets quickly as long as there are no repeats within each set, and as long as the sets aren't large. 
# A good example would be comparing two lists of Social Security numbers to see if there are any matches 
# (in a list of different people's SSNs, there shouldn't be any repeats).
###

set1 = [111223333, 222334444, 333445555, 444556666]
set2 = [666778888, 888990000, 100112222, 444556666]

def direct_comparison_check(set1, set2):
    """
    Directly compares two sets of SSNs and returns the overlap.
    
    :param set1: List of SSNs (e.g., people earning a paycheck above $1,550)
    :param set2: List of SSNs (e.g., people receiving SSDI benefits)
    :return: List of SSNs found in both sets (flagged for further investigation)
    """
    
    flagged = []
    for ssn1 in set1:
        for ssn2 in set2:
            if ssn1 == ssn2:
                flagged.append(ssn1)
    return flagged

# Call the function and print the result
result = direct_comparison_check(set1, set2)
print(result)

# Output: [444556666]