def write_file(file_name, file_content):
    file_path = file_name.with_suffix(".txt")
    with open(file_path, "w") as file:
        file.write(file_content)

def append_file(file_name, file_content):
    file_path = file_name.with_suffix(".txt")
    with open(file_path, "a") as file:
        file.write(file_content)

def read_file(file_name):
    file_path = file_name.with_suffix(".txt")
    with open(file_path, "r") as file:
        return file.read()
