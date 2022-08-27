class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_logged_in(function):
    def wrapper(*args):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper


@is_logged_in
def create_post(user):
    print(f"This is new blog post from {user.name}")


new_user = User("Arunesh")

# print(new_user.name)
# print(new_user.is_logged_in)

new_user.is_logged_in = True

create_post(new_user)
