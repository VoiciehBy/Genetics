
def start_json_file(filename):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("{\n\"horses\" : [ \n")


def jsonify_last_generation(filename, last_generation):
    with open(filename, "a", encoding="utf-8") as file:
        for i in last_generation:
            file.write(i.to_json() + str(",\n"))


def end_json_file(filename):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(']\n}')
    with open(filename, "r", encoding="utf-8") as file:
        txt = file.read()
        n = len(txt)
        txt = txt[:n - 5] + txt[n - 4:]
    with open(filename, "w", encoding="utf-8") as file:
        file.write(txt)
