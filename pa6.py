'''
hw 6
'''


# Problem 1
def make_change(total):
    '''
    gives all possible coin changes for total value
    '''
    coins = [1, 5, 10, 25, 100]
    combinations = []

    def change_combinations(total, combination, index):
        if total == 0:
            combinations.append(combination)
        else:
            for i in range(index, len(coins)):
                if total - coins[i] >= 0:
                    change_combinations(total - coins[i],
                                        combination + [coins[i]], i)
    change_combinations(total, [], 0)
    return combinations


# Problem 2
def dict_filter(f, d):
    '''
    filters dictionary values that return true for given function
    '''
    return_dict = {}
    for key, value in d.items():
        if f(key, value):
            return_dict[key] = value
    return return_dict


# Problem 3
def treemap(f, tree):
    '''
    apply function to all nodes
    '''
    new_key, new_value = f(tree.key, tree.value)
    tree.key = new_key
    tree.value = new_value
    for child in tree.children:
        treemap(f, child)


# Problem 4
class DTree:
    def __init__(self, variable, threshold, lessequal, greater, outcome):
        if outcome is None:
            if any([arg is None for arg in [variable,
                                            threshold, lessequal, greater]]):
                raise ValueError('If outcome is none, other\
                                  variables cannot be none')
        else:
            if any([arg is not None for arg in [variable,
                                                threshold,
                                                lessequal, greater]]):
                raise ValueError('If outcome is not none,\
                                  all first four arguments are none')
        self.variable = variable
        self.threshold = threshold
        self.lessequal = lessequal
        self.greater = greater
        self.outcome = outcome

    def tuple_atleast(self):
        '''
        find the minimum length of tuple
        '''
        def find_max(tree):
            if tree.variable is None:
                return -1
            max_var = tree.variable
            if isinstance(tree.lessequal, DTree):
                max_var = max(max_var, find_max(tree.lessequal))
            if isinstance(tree.greater, DTree):
                max_var = max(max_var, find_max(tree.greater))
            if max_var >= 0:
                return max_var
            else:
                return -1
        rv = find_max(self) + 1
        return rv

    def find_outcome(self, tup):
        '''
        find outcome based on given tuple
        '''
        if self.outcome is not None:
            return self.outcome
        if tup[self.variable] <= self.threshold:
            return self.lessequal.find_outcome(tup)
        else:
            return self.greater.find_outcome(tup)

    def no_repeats(self):
        '''
        find whether tree doesn't check same condition numerous times
        '''
        def repeat_tracker(self, vars_l):
            if self.outcome is not None:
                return True
            if self.variable in vars_l:
                return False
            vars_l.append(self.variable)
            return repeat_tracker(self.lessequal, vars_l) and\
                repeat_tracker(self.greater, vars_l)
        vars_l = []
        return repeat_tracker(self, vars_l)
