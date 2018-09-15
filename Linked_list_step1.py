class link_two_values:
    """
    input requires two values and the input set
    """

    def __init__(self, thisval=None, nextval=None, value_set=None):
        self.thisval = thisval
        self.nextval = nextval
        self.value_set= value_set

    def get_values(self, thisval, nextval):
        value_set = [thisval, nextval]
        return value_set


if __name__ == '__main__':
    link_two_values()