def create_class(class_name: str, *args, **kwargs):
    return type(class_name, args, kwargs)


new_class = create_class('String', str, some='1')

print(new_class)
