from typing import List, Any
from functools import reduce, cmp_to_key



def triplets_with_sum(num:int) -> List[int]:
    triplets = []

    for t in range(1, num + 1):
        for s in range(t + 1, num + 1, 2):
            c = s * s + t * t
            if c > num: break

            a, b =  s * s - t * t, 2 * s * t
            a, b = (a, b) if a < b else (b, a)

            if a + b + c == num:
                triplets.append((a, b, c))

            for k in range(2, num + 1):
                if k * (a + b + c) > num: break
                if k * (a + b + c) == num:
                    triplets.append((k * a, k * b, k * c))
    #
    return sorted(unique(triplets),
                  key=cmp_to_key(lambda t1, t2: 1 if t1[0] <= t2[0] else -1)
)


def unique(lst: List[Any]) -> List[Any]:
    return reduce(lambda nl, x: [*nl, x] if x not in nl else nl,
                  lst,
                  [])

#
# def triplets_with_sum(num:int) -> List[int]:
#     """
#     Naive version which does not scale well....
#     """
#     triplets = []

#     for a in range(1, num):
#         if a > num // 3: break

#         for b in range(a + 1, num):
#             if a + b > num: break

#             for c in range(b + 1, num):
#                 if a + b + c == num and a * a + b * b == c * c:
#                     triplets.append([a, b, c])
#                     continue
#                 if a + b + c > num: break
#     return triplets


# def unique(lst: List[Any]) -> List[Any]:
#     nlst = []
#     for x in lst:
#         if x not in nlst:
#             nlst.append(x)
#     return nlst
