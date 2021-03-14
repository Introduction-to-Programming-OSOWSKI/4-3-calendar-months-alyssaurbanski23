def calendar(m):
    for i in range(0, len(month)):
        if m == month[i]:
            return i + 1
    return m + " is not a month" 

month = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
print (calendar("january"))
#print (calendar("george"))