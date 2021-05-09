from string import Template


def main():
    str1 = "You are my buddy, {0} and {1}".format("Carlos", "Ana")
    print(str1)

    templ = Template("You are doing this {activity} done by {author}.")
    str2 = templ.substitute(activity="jogging", author="Dibbie")
    print(str2)
    data = {
        "author": "Joe Marini",
        "title": "Advanced Python"
    }
    str3 = templ.substitute(data)
    print(str3)
if __name__ == "__main__":
    main()