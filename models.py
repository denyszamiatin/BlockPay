class User:
    """
    Class that represent user in system
    """
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return 'User(%s, %s, %s)' % (self.first_name, self.last_name, self.email)