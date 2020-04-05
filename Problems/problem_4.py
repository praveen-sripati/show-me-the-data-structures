#!/usr/bin/env python
# coding: utf-8

# # Problem 4: Active Directory

# In[1]:


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


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

child_user = "child_user"
child.add_user(child_user)

sub_child_user_one = "sub_child_user_one"
sub_child.add_user(sub_child_user_one)

sub_child_user_two = "sub_child_user_two"
sub_child.add_user(sub_child_user_two)

child.add_group(sub_child)
parent.add_group(child)
print(sub_child.get_users())


# In[2]:


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.
    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    has_user = find_user(user, group)
    if has_user:
        return True
    else:
        return False

# Helper function to find user in the group
def find_user(user, group):
    users = group.get_users()
    if len(users):
        if user in users:
            return True
    else:
        groups = group.get_groups()
        for group in groups:
            return find_user(user, group)


# # Test Cases

# In[3]:


print(is_user_in_group("sub_child_user_one", sub_child))
#True


# In[4]:


print(is_user_in_group('parent_user', parent))
#False


# In[5]:


print(is_user_in_group('child_user', child))
#True


# In[6]:


print(is_user_in_group('', child))
#False


# In[7]:


print(is_user_in_group('child_user', parent))
#True


# In[8]:


print(is_user_in_group('child_user', sub_child))
#False

