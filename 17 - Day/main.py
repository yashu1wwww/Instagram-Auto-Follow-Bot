class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Arunesh")
user_2 = User("002", "Ankesh")

user_1.follow(user_2)

print("ID : ", user_1.id)
print("Username : ", user_1.username)
print("Followers : ", user_1.followers)
print("Following : ", user_1.following)

print()

print("ID : ", user_2.id)
print("Username : ", user_2.username)
print("Followers : ", user_2.followers)
print("Following : ", user_2.following)
