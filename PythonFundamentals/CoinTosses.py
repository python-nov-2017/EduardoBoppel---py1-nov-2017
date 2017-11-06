import random


def coin_toss(rounds):
    
    heads = 0
    tails = 0
    this_round = ""

    for i in range(1, rounds+1):
        
        toss = round(random.random())
        if toss <= 0.5:
            this_round = "tail"
            tails += 1
        else:
            this_round = "head"
            heads += 1
        
        print "Attempt {}: Throwing a coin... It's a {}! ... Got {} head(s) and {} tail(s) so far".format(i, this_round, heads, tails)
        
        
    print "-------------------"
    print "Ending the program.  Thank you!"



coin_toss(5000)