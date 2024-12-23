def first_puzzle():
    with open("input.txt", "r") as f:
        content = f.read().strip()
        length = len(content)
        i = 0
        floor_count = 0

        while (i < length):
            match content[i]:
                case "(":
                    print("1+ floor")
                    floor_count += 1
                    i += 1
                case ")":
                    print("1- floor")
                    floor_count -= 1
                    i += 1
                case _:
                    print("Invalid")
                    print(f"Problem {content[i]}")
                    break
            print(f"Total floor: {floor_count}")
            f.close()

def second_puzzle():
    with open("input.txt", "r") as f:
        content = f.read().strip()
        length = len(content)
        i = 0
        floor_count = 0

        while (i < length):
            match content[i]:
                case "(":
                    floor_count += 1
                    i += 1
                    if (floor_count == -1):
                        print(i)
                        break;
                case ")":
                    floor_count -= 1
                    i += 1
                    if (floor_count == -1):
                        print(i)
                        break;
                case _:
                    print("Invalid")
                    break
            print(f"total floor: {floor_count}")
            f.close()

second_puzzle()

