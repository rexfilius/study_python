class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def introduceYourself(self, guestName):
        print("Hi {}, I'm {}. Contact me at {}"
              .format(guestName, self.name, self.email))

    def __repr__(self):
        return "User(username={}, name={}, email={})" \
            .format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()


class UserDatabase:
    def __init__(self, ):
        self.users: list[User] = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            # find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email

    def listAll(self):
        return self.users
