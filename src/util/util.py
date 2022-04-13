def us_string_to_real(value, decimal_separator=','):
    return value.replace('R$', '').replace(',', '').replace('.', decimal_separator)


def ensure_path(path_dir):
    from pathlib import Path
    Path(path_dir).mkdir(parents=True, exist_ok=True)


def clear_folder(path_dir):
    import shutil
    shutil.rmtree(path_dir, ignore_errors=True)


def remove_if_exists(file_path):
    import os
    if os.path.exists(file_path):
        os.remove(file_path)


def optional_bool(param):
    if param is None:
        return False

    return bool(param)


def optional_str(param):
    if param is None:
        return ''

    return str(param)


def optional_int(param):
    if param is None:
        return 1

    return int(param)


def only_numbers(value):
    import re
    return re.sub(r'^([\s\d]+)$', '', value)
