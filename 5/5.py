# def user(user_id, user_name):
#     return [user_id, [user_name]]

# def user_id(user):
#     return user[0]

# def user_name(user):
#     return user[1][0]

# addison = user(1, "Addison")
# print(user_name(addison)) # prints Addison

# Default definition
def tree(label, branches=[]):
    return [label] + branches

def label(t):
    return t[0]

def branches(t):
    return t[1:]

def is_leaf(t):
    return len(t) == 1

def tree(label, branches=[]):
    return {"label": label,
            "branches": branches}

def label(t):
    return t["label"]

def branches(t):
    return t["branches"]

def print_tree(t, level=0):
    print(" " * level, label(t))
    for b in branches(t):
        print_tree(b, level=level+1)

t = tree(1, [tree(2), tree(3)]) # tree from discussion
print_tree(t)

def height(t):
    # return max(0 if is_leaf(branches(t)) else 1 + height(branches(t)[i]) for i in range(len(branches(t))))
    return 0 if is_leaf(t) else 1 + max(height(b) for b in branches(t))
    return 0 if is_leaf(t) else 1 + max(height(b) for b in branches(t))
    return 1 + max(height(b) for b in branches(t))

def map(fn, seq):
    return [fn(elem) for elem in seq]

def filter(pred, seq):
    return [x for x in seq if pred(x)]

def reduce(combiner, seq):
    accumulate = seq[0]
    for elem in seq[1:]:
        accumulate = combiner(accumulate, elem)
    return accumulate
    # return seq[-1] if len(seq) == 1 else combiner(reduce(combiner, seq[:-1]), seq[-1])
    # return seq[0] if len(seq) == 1 else combiner(seq[0], reduce(combiner, seq[1:]))

