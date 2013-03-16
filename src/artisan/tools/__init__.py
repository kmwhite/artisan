def is_attr_set(check_instance, attrib_name):
    ''' Checks to see if the attribute is set '''

    if hasattr(check_instance, attrib_name):
        return getattr(check_instance, attrib_name) is not None

    return False
