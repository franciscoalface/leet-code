# def majority_element(nums):
#     m = {}
#     number = ""
#     appearances = 0
#     for num in nums:
#         if num in m:
#             m[num] += 1
#         else:
#             m[num] = 1

#     for key, value in m.items():
#         if value > appearances:
#             number = key
#             appearances = value

#     return number


def majority_element(nums):
    m = {}
    size = len(nums)

    for num in nums:
        m[num] = m.get(num, 0) + 1

    for key, value in m.items():
        if value > size // 2:
            return key
