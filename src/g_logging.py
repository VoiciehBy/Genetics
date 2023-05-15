from constants import HORSES_JSON_FILE_NAME, AI_HORSES_JSON_FILE_NAME


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


def start_horses_json_file():
    start_json_file(HORSES_JSON_FILE_NAME)


def start_ai_horses_json_file():
    start_json_file(AI_HORSES_JSON_FILE_NAME)


def start_json_files():
    start_horses_json_file()
    start_ai_horses_json_file()


def end_horses_json_file():
    end_json_file(HORSES_JSON_FILE_NAME)


def end_ai_horses_json_file():
    end_json_file(AI_HORSES_JSON_FILE_NAME)


def end_json_files():
    end_horses_json_file()
    end_ai_horses_json_file()
