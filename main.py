import os

from app import configure_app
from tornado import ioloop

def load_config_from_environment_variables():
    def __recursive_dictionary(output, keys_array, value):
        first_key = keys_array[0]

        if len(keys_array) == 1:
            output[first_key] = value
        else:
            if first_key not in output:
                output[first_key] = {}

            __recursive_dictionary(output[first_key], keys_array[1:], value)

    environment_variables = os.environ
    config = {}
    for variable in environment_variables:
        if variable.startswith("ANALYTICS_"):
            lower_case_variable = variable.lower()
            __recursive_dictionary(config, lower_case_variable[10:].split("_"), environment_variables[variable])

    if 'debug' in config:
        config['debug'] = (config['debug'].lower() == 'true')
    else:
        config['debug'] = False

    return config


if __name__ == '__main__':
    config = load_config_from_environment_variables()
    application = configure_app(config)

    application.listen(config['app']['port'])
    ioloop.IOLoop.instance().start()
