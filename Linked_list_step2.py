from Linked_list_step1 import link_two_values

class add_a_link(link_two_values):
    def __init__(self, thisval, nextval, value_set):
        self.thisval = thisval
        self.nextval = nextval
        self.value_set = value_set
        super().__init__(thisval, nextval, value_set)


    def assign_the_neighbor(new_this, new_next=None):
        """
        requires input of one new value
        """
        super().__init__()
        new_this = link_two_values.nextval
        new_next = new_next
        new_value_set = [new_this, new_next]
        return new_value_set


if __name__ == '__main__':
    thisval_in, nextval_in, value_set_in, new_next_in = [1,2,[1,2],3]
    test = add_a_link(thisval=thisval_in, nextval=nextval_in, value_set=value_set_in)
    response = test.assign_the_neighbor(new_next=new_next_in)
    print (response.new_value_set)