def prob_a_or_b (a,b, all_possible_outcome):
    prob_a = len(a)/len(all_possible_outcome)

    prob_b = len(a)/len(all_possible_outcome)

    inter = a.intersection(b)

    prob_inter = len(inter)/len(all_possible_outcome)

    return (prob_a + prob_b - prob_inter)


evens = {2 , 4 , 6}
greater_than_two = {2 , 4 , 5 , 6}
all_possible_rolls = {1 , 2 , 3 , 4 , 5 , 6}

print(prob_a_or_b(evens , greater_than_two , all_possible_rolls))