def normalise(text):
    return text.replace(" ", "").replace("-", "").upper()def is_valid(reg):
    if len(reg) not in (9, 10):
        return False
    return (reg[:2].isalpha() and reg[2:4].isdigit() and
            reg[4:-4].isalpha() and 1 <= len(reg[4:-4]) <= 2 and
            reg[-4:].isdigit())def format_reg(reg):
    return f"{reg[:2]} {reg[2:4]} {reg[4:-4]} {reg[-4:]}"raw = "tn 09 ab 1234"reg = normalise(raw)print(reg, "valid" if is_valid(reg) else "INVALID")if is_valid(reg):
    print(format_reg(reg))
