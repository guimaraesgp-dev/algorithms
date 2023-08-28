def merge(left, right):
    array = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            array.append(left[0])
            left = left[1:]
        else:
            array.append(right[0])
            right = right[1:]

    array += left
    array += right

    return array


def is_anagram(first_string, second_string):
    fss = sort_list(list(first_string.lower()))
    sso = sort_list(list(second_string.lower()))
    return (
        "".join(fss),
        "".join(sso),
        words(
            "".join(fss),
            "".join(sso),
        ),
    )


def words(words1, words2):
    return bool(words1 and words2 and words1 == words2)


def sort_list(letter):
    if len(letter) <= 1:
        return letter

    mid = len(letter) // 2
    left = letter[:mid]
    right = letter[mid:]
    left = sort_list(left)
    right = sort_list(right)

    return merge(left, right)
