##  Utility scripts used in PySnakie project  ##

# Parse a config file
def parse_config(path):
    import configparser

    config = configparser.ConfigParser()
    config.read(path)

    return config


# Set cofigured options
def patch_options(config, options):
    for section in config.sections():
        for option, value in config.items(section):
            if option in options:
                match type(options[option]).__name__:
                    case "str":
                        value = value.strip('"')
                    case "int":
                        value = int(value)

                options.update({option: value})

    return options
