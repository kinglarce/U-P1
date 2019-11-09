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


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user is not None or group is not None:

        if len(group.get_users()) > 0:
            if user in group.get_users():
                return True
        
        if len(group.get_groups()) == 1:
            return is_user_in_group(user, group.get_groups()[0])
        else:
            for g in group.get_groups():
                return is_user_in_group(user, g)
    
    return False

# Test case 1
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Expected: True
print(is_user_in_group("sub_child_user", parent))

# More user to test
cousins = 'cousins'
sub_child.add_user(cousins)
sub_child_child = Group("sub_child_child")
grand_child = 'grandchild'
sub_child_child.add_user(grand_child)
sub_child.add_group(sub_child_child)

# Expected: True
print(is_user_in_group("grandchild", parent))

# Test case 2
# Expected: False
print(is_user_in_group("alien", parent))
# Expected: False
print(is_user_in_group(cousins, sub_child_child))

# Test case 3
# Expected: False
print(is_user_in_group(None, parent))
# Expected: False
print(is_user_in_group(None, None))
