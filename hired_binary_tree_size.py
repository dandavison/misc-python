def solution(arr):
    sums = {"left": 0, "right": 0}

    def result():
        if sums["left"] < sums["right"]:
            return "Right"
        elif sums["left"] == sums["right"]:
            return ""
        else:
            return "Left"


    level = 1
    i = 1
    while True:
        for side in ["left", "right"]:
            for _ in range(2 ** (level - 1)):
                if i == len(arr):
                    return result()
                if arr[i] > 0:
                    sums[side] += arr[i]
                i += 1
        level += 1
