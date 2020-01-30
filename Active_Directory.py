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
    group_users = group.get_users()
    child_groups = group.get_groups()
    if group_users != []:
        for group_user in group_users:
            if group_user == input_user:
                return True
    elif child_groups != []:
        child_groups = group.get_groups()
        for child_group in child_groups:
            is_user_in_group(input_user, child_group)
    return False

    

print("Pass" if is_user_in_group(sub_child_user, parent) == False else "Fail")
print("Pass" if is_user_in_group("Parent user", parent) == True else "Fail")
print("Pass" if is_user_in_group("Parent user", child) == False else "Fail")

