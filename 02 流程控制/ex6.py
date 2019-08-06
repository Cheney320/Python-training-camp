# 练习六：
# 使用while循环输出1 2 3 4 5 6 8 9 10
i = 1
while i <= 10:
    if i == 7:
        i += 1
        continue
    print(i,end=" ")
    i += 1
print()

# 求1-100所有数的和
s = sum([i for i in range(1,101)])
print(s)

# 输出1-100内所有奇数
odd = [i for i in range(1,101) if i%2==1]
print(odd)

# 输出1-100内所有偶数
even = [i for i in range(1,101) if i%2==0]
print(even)

# 求1-2+3-4+5...99所有数的和
s1 = [i for i in range(1,100,2)]
s2 = [-i for i in range(2,99,2)]
print(sum(s1)+sum(s2))
