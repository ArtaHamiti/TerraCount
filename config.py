from configparser import ConfigParser


def config(filename="database.ini", section="postgresql"):
    # crate a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db_dict = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_dict[param[0]] = param[1]
    else:
        raise Exception(f'Section{section} in not found in the {filename}')
    print(db_dict)


config()