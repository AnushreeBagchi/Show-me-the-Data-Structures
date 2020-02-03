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
    userList = return_users_in_group(group, list())
    if input_user in userList:
        return True
    return False

def return_users_in_group(group, user_list):
    group_users = group.get_users()
    child_groups = group.get_groups()
    if group_users != []:
        for group_user in group_users:
            user_list.append(group_user)
    if child_groups != []:
        child_groups = group.get_groups()
        for child_group in child_groups:
            return_users_in_group(child_group, user_list)
    return user_list

    
# Test cases
print("Pass" if is_user_in_group(sub_child_user, parent) == True else "Fail")
print("Pass" if is_user_in_group("Parent user", parent) == True else "Fail")
print("Pass" if is_user_in_group("Parent user", child) == False else "Fail")

print("Pass" if is_user_in_group("", child) == False else "Fail") #edge case when user is not provided

def test5():
    try:
        is_user_in_group("Parent user", None)
    except ValueError as err:
        print("Pass")

test5()