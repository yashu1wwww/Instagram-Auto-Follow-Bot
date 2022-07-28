def format_name(firstName, lastName):
    f_name = firstName.lower()
    l_name = lastName.lower()

    f_name = f_name[0].upper() + f_name[1:]
    l_name = l_name[0].upper() + l_name[1:]

    fullName = f_name + " " + l_name

    return fullName


print(format_name("aRunEsH", "KuMaR"))
print(format_name("anKesH", "KuMaR"))
print(format_name("i'hv cAr", "hOMe"))


# angela formated name
def name_formate(f_name, l_name):
    """
        This is docstring
        :param f_name:
        :param l_name:
        :return: fullname
    """
    if f_name == "" or l_name == "":
        return "Please enter your firstname and lastname"
    fullName = f"{f_name.title()} {l_name.title()}"
    return fullName

print(name_formate("aRunEsH", "KuMaR"))

print(name_formate(input("Enter your firstname? "), input("Enter your lastname? ")))
