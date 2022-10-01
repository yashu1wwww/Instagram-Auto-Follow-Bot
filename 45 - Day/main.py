from bs4 import BeautifulSoup
import lxml


with open("website.html", mode="r", encoding="utf8") as file:
    content = file.read()


# soup = BeautifulSoup(content, 'html.parser')
soup = BeautifulSoup(content, "lxml")


# #   all content print
# print(soup)
# print(soup.prettify())


# #   title
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)


# #   print elements
# print(soup.p)
# print(soup.ul)
# print(soup.ul.li)
# print(soup.ul.li.name)
# print(soup.ul.li.string)
# print(soup.head)
# print(soup.head.title)
# print(soup.head.meta)


# #   get all elements
# print(soup.find_all("p"))
# print(soup.find_all("title"))
# print(soup.find_all("li"))
# print(soup.find_all("li")[0].string)


# for li in soup.find_all("li"):
#     # print(li)
#     # print(li.string)
#     print(li.getText())

# for a in soup.find_all("a"):
#     # print(a)
#     print(a.get("href"))

# for meta in soup.find_all("meta"):
#     # print(meta.get("name"))
#     print(meta.get("content"))


# #   find element by id
# heading = soup.find(name="h1", id="name")
# print(heading)
# print(heading.string)
# print(heading.name)

# #   find element by class name
# h3 = soup.find(name="h3", class_="heading")
# print(h3)
# print(h3.name)
# print(h3.string)
# print(h3.get("class"))

# all_h3 = soup.find_all(name="h3", class_="heading")
# print(all_h3)
#
# print()
#
# for h3 in all_h3:
#     # print(h3)
#     # print(h3.string)
#     print(h3.get("class"))


# #   selector
# p_a = soup.select_one(selector="p a")
# print(p_a)
# print(p_a.name)
# print(p_a.string)
# print(p_a.get("href"))
#
# name = soup.select_one(selector="#name")
# print(name)
#
# h3 = soup.select(selector=".heading")
# print(h3)
#   this is also working well
# a = soup.find_all(name="a")
# print(a)


form = soup.find("input")

print(form.get("maxlength"))
















