from functools import wraps


def topic(*args, **kwargs):
    if len(args) != 1:
        return
    topic_str = args[0]

    def print_topic(func):

        @wraps(func)
        def decorated(*args, **kwargs):
            print(f"\033[32m********** {topic_str} ***********\033[0m")
            func_call = func(*args, **kwargs)
            print("\n\n\n")
            return func_call

        return decorated

    return print_topic
