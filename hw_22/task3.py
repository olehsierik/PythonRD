def create_class(class_name: str, *args, **kwargs):
    class_base: tuple = tuple([item for item in args])
    print(class_base)

    attribute: dict = {key: value for key, value in kwargs.items()}
    print(attribute)

    return type(class_name, class_base, attribute)
