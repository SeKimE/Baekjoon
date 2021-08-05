
# ----------- error 1
N = int(input('input N: '))

if N%5 == 0:
    result = int(N/5)
else:
    a = int(N/5)
    a_left = N%5
    if a_left%3 ==0:
        result = int(a_left/3) + a
    else:
        b = int(a_left/3)
        left = a_left%3
        while(1):
            if a ==0:
                result = -1
                break
            else:
                a = a-1
                left = left+5
                b = b+int(left/3)
                left = left%3
                if left ==0:
                    result = a+b
                    break
print(result)

# ---------------- error 2
N = int(input('input N: '))


result = []
maxi = int(N/5)
for am5 in range(maxi+1):
    left=N - 5*am5
    am3 = int(left/3)
    left  = left%3
    if left !=0:
        result.append(-1)
    else:
        result.append(am5+am3)
result = set(result)-{-1}
if len(result) == 0:
    print(-1)
else:
    print(min(result))


# 정답
sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)

