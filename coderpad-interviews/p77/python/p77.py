from collections import OrderedDict


def solution(li: []):
    stack = []

    # 오름차순 정렬 O(log(n))
    for each in sorted(li):  # iter O(n)
        if not stack:
            stack.append(each)
        elif stack and stack[-1][0] <= each[0] and stack[-1][1] >= each[1]:
          # 스택 맨 위 범위에 포함되는 경우 스택에 올리지 않음
            continue
        elif stack and stack[-1][0] <= each[0] and stack[-1][1] > each[0]:
            temp = list(stack.pop())
            temp[1] = max(temp[1], each[1])
            stack.append(tuple(temp))
        else:  # 범위 포함 안되면 스택에 올림
            stack.append(each)

    return stack


def solution2(li: []):
    db, mergedDB = OrderedDict(), OrderedDict()
    for start, end in li:  # 순서 저장 O(n)
        db[start] = end
        mergedDB[start] = end

    for s1, e1 in db.items():  # O(n^2)
        for s2, e2 in db.items():
            if (s1 != s2 and e1 != e2) and s1 <= s2 and s2 <= e1:
                mergedDB[s1] = max(e1, e2)
                if s2 in mergedDB:
                    del mergedDB[s2]

    result = [(K, V) for K, V in mergedDB.items()]
    return result
