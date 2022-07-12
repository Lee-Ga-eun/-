# 가로 길이가 n, 세로 길이가 m인 직사각형 형태로 별찍기

# 나의 풀이
a,b= map(int, input().split(" "))
for _ in range(b):
    print("*"*a)


# 다른 풀이
a, b= map(int, input.split(" "))
print(("*"*a + "\n")*b)