ns = list(range(5))

# for i in range(len(ns)):
#     for j in range(i + 1, len(ns)):
#         print(i, j, "---", ns[i], ns[j])

# for i, ni in enumerate(ns):
#     for j in range(i + 1, len(ns)):
#         print(i, j, "---", ns[i], ns[j])

for i, ni in enumerate(ns):
    for j, nj in enumerate(ns[i + 1 :], i + 1):
        print(i, j, "---", ni, nj)
