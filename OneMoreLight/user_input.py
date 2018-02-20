def clean_user_input(dirty_string):
    # TODO some magic
    clean_string = ''.join(e for e in dirty_string if e.isalnum())

    return clean_string
