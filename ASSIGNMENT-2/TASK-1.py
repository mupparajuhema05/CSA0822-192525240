def subsidy(units, ration=False, senior=False):
    if units <= 100:
        return "Full subsidy"
    elif 101 <= units <= 200:
        return "Partial subsidy" + (" + ration" if ration else "")
    elif senior:
        return "Full subsidy (senior)"
    else:
        return "No subsidy"print(subsidy(100))print(subsidy(150, ration=True))print(subsidy(250, senior=True))print(subsidy(250))
