def fifty_thirty_twenty(n):

    d = dict()
    d['needs'] = n * (50/100)
    d['wants'] = n * (30/100)
    d['savings'] = n * (20/100)
    return d


print(fifty_thirty_twenty(10000) )# { "Needs": 5000, "Wants": 3000, "Savings": 2000 }

print(fifty_thirty_twenty(50000)) # { "Needs": 25000, "Wants": 15000, "Savings": 10000 }

print(fifty_thirty_twenty(13450)) # { "Needs": 6725, "Wants": 4035, "Savings": 2690 }