def draw_new(k): # pays if k successes in q sequence

    payoff = 0
    count = 0

    for i in range(10):
        U = uniform()
        count = count + ( 1 if U  < o.5 else 0 )
        print(count)
        if count == k:
            payoff = 1
    return payoff

draw_new(3)
