def hide_sensitive(file_name: str) -> None:
    import re

    with open(file_name, 'r+') as file:
        content = file.read()

        content_censor = re.sub('\S+@\S+', '<SENSITIVE_INFORMATION>', content)

        file.seek(0)

        file.write(content_censor)
