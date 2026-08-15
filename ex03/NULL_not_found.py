def NULL_not_found(object: any) -> int:
    if type(object) is type(None):
        print(f"Nothing: {object} {type(object)}")
    elif type(object) is float:
        print(f"Cheese: {object} {type(object)}")
    elif type(object) is int:
        print(f"Zero: {object} {type(object)}")
    elif type(object) is str and object == "":
        print(f"Empty: {object} {type(object)}")
    elif type(object) is bool:
        print(f"Fake: {object} {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0