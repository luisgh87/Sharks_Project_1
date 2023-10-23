def age(x):
    if x.isdigit():
        return int(x)
    else:
        return np.nan
    
def sex(x):
    if x == "m":
        return "m"
    elif x == "f":
        return "f"
    else:
        return np.nan
    
.applymap(lambda x: x.strip().lower() if isinstance(x, str) else x)