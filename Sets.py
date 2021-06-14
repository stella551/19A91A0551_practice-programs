#Set .add()
N = int(input())
countries = set()
for i in range(N):
    countries.add(input())
print(len(countries))
"""
Input (stdin)
7
UK
China
USA
France
New Zealand
UK
France
Your Output (stdout)
5
Expected Output
5
"""
#Set .difference() Operation
E = int(input())
English = list(input().split())
F = int(input())
French = list(input().split())
print(len(set(English)-set(French)))

"""
Input (stdin)
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Your Output (stdout)
4
Expected Output
4
"""
#Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int,input().split()))
num = int(input())
for i in range(num):
    ip = input().split()
    if ip[0]=="remove":
        s.remove(int(ip[1]))
    elif ip[0]=="discard":
        s.discard(int(ip[1]))
    else :
        s.pop()
print(sum(list(s)))

"""
Input (stdin)
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
Your Output (stdout)
4
Expected Output
4
"""
#Set .intersection() Operation
E = int(input())
English = list(input().split())
F = int(input())
French = list(input().split())
print(len(set(English)&set(French)))
"""
Input (stdin)
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Your Output (stdout)
5
Expected Output
5
"""
#Set .symmetric_difference() Operation
E = int(input())
English = list(input().split())
F = int(input())
French = list(input().split())
print(len(set(English)^set(French))
"""
Input (stdin)
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Your Output (stdout)
8
Expected Output
8
"""
#Set .union() Operation
E = int(input())
English = list(input().split())
F = int(input())
French = list(input().split())
print(len(set(English)|(set(French))))
"""
Input (stdin)
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Your Output (stdout)
13
Expected Output
13
"""
#Symmetric Difference
#input
M=int(input())
m=input()
N=int(input())
n=input()

#splitting and mapping(string to int_list)
x=list(map(int,m.split()))
y=list(map(int,n.split()))

#creation of sets
a=set(x)
b=set(y)

#difference in each sets
c=a.difference(b)
d=b.difference(a)

#union of difference
e=c.union(d)

#converting set to a list
result=list(e)

#sorting
result.sort()

#iteration
for i in range(len(result)):
    print(result[i])
"""
Input (stdin)
4
2 4 5 9
4
2 4 11 12
Your Output (stdout)
5
9
11
12
Expected Output
5
9
11
12
"""
