def sum_of_multiples(limit, multiples):
    return sum({p for m in multiples if m for p in range(m, limit, m)})
