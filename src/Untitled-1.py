abc = [1, 2, 3, 4, 5]

def test(list):
    if len(list) == 0:
        return
    print(list[0])
    test(list[1:])

test(abc)