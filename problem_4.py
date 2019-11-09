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
    if len(group.get_users()) > 0:
        return user in group.get_users()

    if len(group.get_groups()) == 1:
        return is_user_in_group(user, group.get_groups()[0])
    else:
        for g in group.get_groups():
            return is_user_in_group(user, g)
    
    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# More user to test
sub_child_child = Group("subchild_child")
alien = "alien"
sub_child_child.add_user(alien)
sub_child.add_group(sub_child_child)

print(is_user_in_group("sub_child_user", parent))