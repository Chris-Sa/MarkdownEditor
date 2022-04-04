# write your code here

class Editor:

    def __init__(self):

        self.content = []
        self.exits = False

        self.loop()

    def helps(self):
        print("Available formatters: plain bold italic header link inline-code new-line "
              "\nSpecial commands: !help !done")


    def done(self):

        file = open("output.md", 'w+')

        for line in self.content:
            file.write(line)

        file.close()
        exits = True

    def plain(self):

        text = input("Text:")
        self.content.append("{}".format(text))

    def bold(self):

        text = input("Text:")
        self.content.append("**{}**".format(text))

    def italic(self):
        text = input("Text:")
        self.content.append("*{}*".format(text))

    def inline_code(self):
        text = input("Text:")
        self.content.append("`{}`".format(text))

    def link(self):
        label = input("Label:")
        url = input("URL:")
        link = "[{}]({})".format(label, url)
        self.content.append(link)

    def header(self):

        level = int(input("Level:"))
        while level not in range(1, 7):

            print("The level should be within the range of 1 to 6.")
            level = int(input("Level:"))

        head = input("Text:")
        self.content.append("{} {}\n".format(level * "#", head))

    def new_line(self):

        self.content.append("\n")

    def lists(self, ordered):

        rows = 0
        text = []
        while rows <= 0:
            rows = int(input("Number of rows:"))
            if rows <= 0:
                print("The number of rows should be greater than zero")
            else: break

        for i in range(1, rows + 1):
            prompt = "Row #{}: ".format(i)
            text = input(prompt)
            if ordered:
                if i == 1:
                    self.content.append("{}. {}\n".format(i, text))
                else:
                    self.content.append("{}. {}\n".format(i, text))
            elif not ordered:
                self.content.append("* {}\n".format(text))



    def loop(self):

        while not self.exits:

            choice = input("Choose a formatter:")

            if choice == "!help":
                self.helps()
            elif choice == "!done":
                self.done()
                break
            elif choice == "plain":
                self.plain()
            elif choice == "bold":
                self.bold()
            elif choice == "italic":
                self.italic()
            elif choice == "inline-code":
                self.inline_code()
            elif choice == "link":
                self.link()
            elif choice == "header":
                self.header()
            elif choice == "new-line":
                self.new_line()
            elif choice == "ordered-list" or choice == "unordered-list":

                if choice == "ordered-list":
                    self.lists(ordered=True)
                elif choice == "unordered-list":
                    self.lists(ordered=False)
            else:
                print("Unknown formatter type or command")

            output = ""
            for i in self.content:
                output += i
            print(output)


write = Editor()



