class Division(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


if __name__ == "__main__":
    from sys import exit
    a = 0
    b = 0
    try:
        a = float(input("input a: "))
        b = float(input("input b: "))
    except:
        print("Incorrect value!")
        exit(1)

    try:
        if b == 0:
            raise Division("Сan't divide by zero")
        print(f"{a}/{b} = {a/b}")
    except Division as result:
        print(result)