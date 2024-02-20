def name_valid(name):
    return name.isalpha()


def cpf_valid(cpf):
    return len(cpf) == 11


def rg_valid(rg):
    return len(rg) == 9


def phone_valid(phone):
    return phone > 11
