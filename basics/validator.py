# Example of a custom module to be imported

import re #imported a core module


def validate_email(email): # function takes in an email --> then validates it
    if len(email) > 7:
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email))
