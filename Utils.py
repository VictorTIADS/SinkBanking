import re


def is_yes_or_no(text):
    if text.upper() == "S" or text.upper() == "N":
        return True
    else:
        return False


def is_valid_input(text):
    textValidation = str(text)
    if textValidation is not None and bool(textValidation and not textValidation.isspace()):
        return True
    else:
        return False


def is_valid_cpf(cpf):
    if len(cpf) == 0 or cpf.replace(" ", "") == "":
        return False
    clean_cpf = clean_cpf_if_contains_dash_or_dot(cpf)
    if len(clean_cpf) != 11:
        return False
    cpf_with_mask = apply_cpf_format(clean_cpf)
    pattern = r"^(\d{3}.){2}\d{3}-\d{2}$"
    return bool(re.match(pattern, cpf_with_mask))


def clean_cpf_if_contains_dash_or_dot(cpf):
    return cpf.replace("-", "").replace(".", "").replace(" ", "")


def apply_cpf_format(cpf):
    return "%s.%s.%s-%s" % (cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11])
