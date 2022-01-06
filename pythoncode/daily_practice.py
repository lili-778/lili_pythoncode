'''
1、我们今天的任务就是编写一个函数，接收一个整数n，然后打印出回升三角形形状。
规则：
数字之间需要一个空格；
每行结束后不需要空格；
示例：
输入：5， 输出：
1 1 1 1 1
 2 2 2 2
  3 3 3
   4 4
    5
'''
"""
# n为三角形的行高
import re
def triangle_2021_1215(n:int):
    m=1
    y=n
    while m<=y:
        print(' ' * (m - 1), end='')
        for i in range(n):
            print(m,end=' ')
        n-=1
        m+=1
        print()
# triangle_2021_1215(8)

'''
2、请编写一个函数，接收两个字符串a和b，请判断他们是否是字母且大小写是否一致。
如果一致则返回1，不一致则返回0。如果其中任意一个不是字母，则返回-1。
示例：
输入：“a” 和 “g”，返回：1。
输入：“A” 和 “G”， 返回：1。
输入：“a” 和 “G”， 返回：0。
输入：“A” 和 “?”， 返回：-1。
'''
def check_s(ss:str):
    # 匹配除了字母以外的任意字符
    my_re=re.compile(r'[^A-Za-z]')
    res=re.findall(my_re,ss)
    # print(res)
    if len(res):
        # print('字符串存在任意一个不是字母')
        return -1
    else:
        if ss.isupper():
            # print('字符串都是大写字母')
            return 11
        elif ss.islower():
            # print('字符串都是小写字母')
            return 12
        else:
            # print('字符串包含大小写字母')
            return 0
def solution(a:str,b:str):
    if check_s(a) ==check_s(b) == 11:
        return 1
    elif check_s(a) ==check_s(b) == 12:
        return 1
    elif check_s(a)==-1 or check_s(b)==-1:
        return -1
    else:
        return 0
# assert solution("a","g")==1
# assert solution("A","G")==1
# assert solution("a","G")==0
# assert solution("0","?")==-1

'''
3、给定一个字符串，请编写一个函数，统计所有字符对应的ASCII码数值的总和。
示例：
输入：“a”，返回：97。
输入：“aaa”，返回：291。
'''

def solution_3(a:str):
    numic=0
    for i in a:
        numic+=ord(i)
    return numic
# print(solution_3('Mary had a little lamb'))
assert solution_3("a") == 97
assert solution_3("aaa") == 291
assert solution_3("Mary had a little lamb") == 2001

'''
4、已知一个数字列表nums和一个目标数字target，请编写一个函数，从左往右，找出其中任意两个连续且和值刚好等于target的数字，
一旦找到，需要从移除其中的第二个数字。以此类推，最终返回处理后的列表。

示例：
输入：nums=[1, 2, 3, 4, 5]，target=3。
返回：[1, 3, 4, 5]。
解释：因为1+2=3，所以移除2；最终剩下[1,3,4,5]。
'''

def solution(nums:list,target):
    i=0
    while True:
        sum1=nums[i]+nums[i+1]
        # 判断连续两个值是否等于目标值
        if sum1==target:
            # 相等的话就删除该值
            nums.pop(i+1)
            # 判断列表的长度-1是否与循环次数相等，相等则整个列表已经遍历一遍，终止循环
            if i==len(nums)-1:
                break
            # 跳出当前循环，继续下一次循环
            continue
        # 连续两个值不等于目标值
        else:
            i+=1
            # 判断列表的长度-1是否与循环次数相等，相等则整个列表已经遍历一遍，终止循环
            if i==len(nums)-1:
                break
    return nums

# assert solution([1, 3, 5, 6, 7, 4, 3], 7) == [1, 3, 5, 6, 7, 4]
# assert solution([4, 1, 1, 1, 4], 2) == [4, 1, 4]
# assert solution([2, 6, 2], 8) == [2, 2]
# assert solution([2, 2, 2, 2, 2, 2], 4) == [2]

'''
5、相信你一眼就能看出 210和 215 哪个数字更大，以及210和 310 的比较结果。但是对于一些底数和指数都不相同的两个数字，
例如39和 56，该如何比较它们的大小呢？
请编写一个函数，接收两个由[底数, 指数] 格式表示的数字，比较它们之间的大小。如果第一个数字较大则返回-1，如果它们相等则返回0，否则返回1。
'''
import  math
def solution5(x:list,y:list):
    if x[0]>0 and y[0]>0:
        if math.pow(x[0],x[1])>math.pow(y[0],y[1]):
            return -1
        elif math.pow(x[0],x[1])<math.pow(y[0],y[1]):
            return 1
        elif math.pow(x[0],x[1])==math.pow(y[0],y[1]):
            return 0
    else:
        raise ValueError

# assert solution5([2,10], [2,15]) == 1
# assert solution5([2,10], [2,10]) == 0
# assert solution5([3,9],[5,6]) == -1

'''
6、给定一个整数n（n>=0），请编写一个函数，找出这个数字之后的最近一个素数。
素数 的定义：只有两个正因数（1和自身）的自然数即为素数 。
'''
def solution6(n):
    x=0
    if n>1:
        while x<2:
            m=n+1
            for i in range(1,m):
                if m%i==0:
                    x+=1
            if x==1:
               return m
            else:
                x=0
                n+=1
    elif n==0:
        return 2
    elif n==1:
        return "1不是素数"
    else:
        return "请输入自然数"
# assert solution6(0) == 2
# assert solution6(2) == 3
# assert solution6(5) == 7
# assert solution6(181) == 191

'''
7、知欧姆定律公式：V = IR，其中V表示电压，单位是V；I表示电流，单位是A；R表示电阻，单位是R。
给定一个字符串，其中包含带有V，A或者R描述的任意两个单位信息，并且使用空格相隔。例如"2R 10V"和"1V 1A"。
请编写一个函数，计算出欧姆定律公式中缺少的单位和值，最多保留6位小数。
示例：
输入：“2200R 5V”，输出：“0.002273A”。
输入：“25V 1e-2A”，输出：“2500.0R”。
'''

def solution7(ss:str):
    try:
        R,V,A='','',''
        for i in ss.split(' '):
            if 'R'in i:
                R=float(i.replace('R',''))
            elif 'V' in i:
                V=float(i.replace('V',''))
            elif 'A' in i:
                A=float(i.replace('A',''))
        if R=='':
            return str(round(V/A,6))+'R'
        elif V=='':
            return str(round(A*R,6)) + 'V'
        elif A=='':
            return str(round(V/R,6)) + 'A'
    except:
        raise ValueError
# assert solution7("2200R 5V") == "0.002273A"
# assert solution7("0.005A 30V") == "6000.0R"
# assert solution7("30V 5000R") == "0.006A"
# assert solution7("0R 0A") == "0.0V"


def solution8(n):
    # lyer为圣诞树层数
    layer=int(n/3)
    y=1
    christmas=''
    while y<=layer:
        for i in range((2*y-1),2*y+4,2):
            ss='*'*i
            christmas=(christmas+ss.center(2*layer+3)).rstrip()+'\r\n'
            # print(ss.center(2*layer+3))
        y+=1
    return (christmas+'###'.center(2*layer+3)).rstrip()

assert solution8(5) == "  *\r\n ***\r\n*****\r\n ###"
assert solution8(8) == "   *\r\n  ***\r\n *****\r\n  ***\r\n *****\r\n*******\r\n  ###"

'''
9、已知一个包含表示年龄的数字列表，它至少会包含2个元素，并且是无序的。请编写一个函数，
返回其中最大的两个年龄列表，并且按照生序排列。
示例：
输入：[1, 3, 10, 0]，返回：[3, 10]
'''
def solution9(ll:list):
    ll.sort(reverse=True)
    return [ll[1],ll[0]]
# assert solution9([1, 5, 87, 45, 8, 8]) == [45, 87]
# assert solution9([6, 5, 83, 5, 3, 18]) == [18, 83]
# assert solution9([10, 1]) == [1, 10]

'''
10、给定一个3位数的数字，请编写一个函数，将它重新排列，并找出其中值最大的形式。
示例：
输入：123，输出：321。
'''
def solution10(num:int):
    ll=list(str(num))
    ll.sort(reverse=True)
    ss_num=''
    for i in ll:
        ss_num+=i
    return int(ss_num)

# assert solution10(123) == 321
# assert solution10(666) == 666
# assert solution10(109) == 910

'''
# 11、给定一个数字列表nums，请编写一个函数，将它们中的每个元素加上自己的位置编号（从1开始）。
# 例如第一个元素加1，第二个元素加2，以此类推。并且，如果增量结果是多位数，则只保留末尾数字。
# 示例：
# 输入：[1, 2, 3]，输出：[2, 4, 6]。因为[1+1, 2+2, 3+3]
# 输入：[3, 6, 9, 8, 9]，输出：[4, 8, 2, 2, 4]。
'''
def solution11(ll_in:list):
    ll_out=[]
    i=0
    while i < len(ll_in):
        num=ll_in[i]+(i+1)
        if num >=10:
            ll_out.append(int(str(num)[-1]))
        else:
            ll_out.append(num)
        i+=1
    return ll_out

# assert solution11([1, 2, 3]) == [2, 4, 6]
# assert solution11([4, 6, 7, 1, 3]) == [5, 8, 0, 5, 8]
# assert solution11([3, 6, 9, 8, 9]) == [4, 8, 2, 2, 4]

def solution12(ll: list):
    return len(set([i for n in ll for i in range(*n)]))

# assert solution12([(1, 4), (7, 10), (3, 5)]) == 7


def solution13(nums:list):
    nums_1=[i for i in str(nums[0])]
    nums_2=[i for i in str(nums[1])]
    nums_1[0],nums_2[0]=nums_2[0],nums_1[0]
    int1=''.join(nums_1)
    int2=''.join(nums_2)
    return abs((int(int1)-int(int2)))
assert solution13([12, 34]) == 18
assert solution13([55, 63]) == 12
assert solution13([357, 579]) == 178
assert solution13([1, 1]) == 0


# num=1
# print(num//2)
def solution14(num:int):
    sum=0
    for i in range(0,num):
        sum+=i
        if num==1:
            return 1
        elif sum == num:
            return i
        elif sum > num:
            return i-1

assert solution14(1) == 1
assert solution14(4) == 2
assert solution14(20) == 5
assert solution14(2211) == 66
assert solution14(9999) == 140
"""


