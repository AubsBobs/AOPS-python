def anagram_rec(str1):
    if len(str1) == 1:
        return str1
    list1 = []
    for i in range(len(str1)):
        for p in anagram_rec(str1[:i]+str1[i+1:]):
            list1.append(str1[i]+p)
            list1.append(p)
    return list1


def anagram(str1):
    list1 = anagram_rec(str1)
    with open("wordlist.txt") as file:
        words = [line.rstrip() for line in file]
    list2 = []
    for word in list1:
        if word in words:
            if word not in list2:
                if len(word) >= 3:
                    list2.append(word)
    for i in range(len(list2)):
        list3 = sorted(list2, key=len)
        list3.reverse()
    return list3

print(anagram(input('Type Letters Here: ')))