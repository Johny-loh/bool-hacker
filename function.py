def dummy1(a):
    return True


def dummy2(a):
    return False


def simply(a, b, c, f):
    return a or not(a)


def easy1(a):
    return a


def easy2(a):
    return not a


def easy3(a, b):
    return a and b

def logic1(a, b, c):
    return a and b and c or a and b and not c
    #a ∧ b ∧ c ∨ a ∧ b ∧ ¬ c

def logic2(a, b, c):
    return (not a or b) and not (a or b) and (not a or c)
    #(not a ∨ b) ∧ ¬ (a ∨ b) ∧ (not a ∨ c)

def medium4(a, b, c, d, e, f):
    return a and not b or c and not d and e and f
    #a ∧ ¬ b ∨ c ∧ ¬ d ∧ e ∧ f

def medium5(a, b, c, d, e, f): 
    return (a and not b and not d) and (not f or e or not c and f) or (a and not b and not c and d) or (a and not b and c and d) or (c and not d and e and f) and (c or not e)
    #(a ∧ ¬b ∧ ¬d) ∧ (¬f ∨ e ∨ ¬c ∧ f) ∨ (a ∧ ¬b ∧ ¬c ∧ d) ∨ (a ∧ ¬b ∧ c ∧ d) ∨ (c ∧ ¬d ∧ e ∧ f) ∧ (c ∨ ¬e)

def long_running3(x, y, z, t, e, w, a, x1, x2, x4):
    return (x and y or z) or (t and w) or w and (e and x) or (e and a)