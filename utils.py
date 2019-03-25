# check if the user has permission to use this command
def check_roles(allowed_role, author_roles):
    return(bool(set(author_roles) & set(allowed_role)))
