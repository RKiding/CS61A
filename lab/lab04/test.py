from ucb import trace

@trace
def max_subseq(n, t):
    if t == 0:
        return 0
    elif n < 10:
        return n
    else:
        all_but_last, last = n //10, n % 10
        use_digit = max_subseq(all_but_last, t-1) * 10 + last
        not_use_digit = max_subseq(all_but_last, t)
        return max(use_digit, not_use_digit)
