from Sequences.Simple import naturals

# Trying out sequences that are not numeric like Dyck words

def dyck_words_str(n):
    """
    All words consisting of n pairs of correctly matched parentheses
    """
    
    def dyck_recur(S):
        # Check how many of each parenthesis we have
        a = S.count("(")
        b = S.count(")")
        if len(S) > 2*n or b > a:
            return None
        elif a == b == n:
            yield S
        else:
            yield from dyck_recur(S+"(")
            yield from dyck_recur(S+")")
    
    yield from dyck_recur("")


def dyck_language_str():
    """
    All words consisting of correctly matched pairs of parentheses
    """
    
    for n in naturals(1):
        yield from dyck_words_str(n)




D = dyck_language_str()
for i in range(20):
    print(next(D))