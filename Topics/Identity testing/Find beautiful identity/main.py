def object_with_beautiful_identity():
    for i in range(10_000):
        # Change the next line
        istr = str(id(i))
        if istr[-3:] == "888":
            return i
