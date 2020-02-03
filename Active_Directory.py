class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
    def add_group(self, group):
        self.groups.append(group)
    def add_user(self, user):
        self.users.append(user)
    def get_groups(self):
        return self.groups
    def get_users(self):
        return self.users
    def get_name(self):
        return self.name



parent = Group("Parent")
child = Group("Child")
sub_child = Group("Subchild")

sub_child_user = "Sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
parent.add_user("Parent user")
child.add_user("Child user")

def is_user_in_group(input_user, group):
    if group is None:
        raise ValueError('Please enter a valid group')
    return return_is_user_in_group(input_user, group, bool())

def return_is_user_in_group(input_user, group, is_present):
    group_users = group.get_users()
    if input_user in group_users:
        return True
    else: 
        child_groups = group.get_groups()
        for child_group in child_groups:
            is_present = return_is_user_in_group(input_user, child_group, is_present )
            return is_present
    return False        
    
# Test cases
print("Pass" if is_user_in_group(sub_child_user, parent) == True else "Fail")
print("Pass" if is_user_in_group("Parent user", parent) == True else "Fail")
print("Pass" if is_user_in_group("Parent user", child) == False else "Fail")
print("Pass" if is_user_in_group("Child user", parent) == True else "Fail")

print("Pass" if is_user_in_group("", child) == False else "Fail") #edge case when user is not provided
def test5(): # edge case when None group is provided
    try:
        is_user_in_group("Parent user", None)
    except ValueError as err:
        print("Pass")

test5()