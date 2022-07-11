class List_includes(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

if __name__ == "__main__":
    list_of_nums = []
    while True:
        try:

            if input() == "stop":
                break
            elif not input().isdigit():
                raise List_includes()
            else:
                list_of_nums.append(int(input()))
        except List_includes:
            print("Incorrect value!")

print(*list_of_nums)


