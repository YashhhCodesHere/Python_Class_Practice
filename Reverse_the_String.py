s = "1234abcd"
n = len(s)
s_rev = []
for i in range(n):
    s_rev += s[n-i-1]

for i in range(len(s_rev)):
    print(s_rev[i], end="")



# Another Method:-

s = "1234abcd"
s_rev = s[::-1] # This will reverse the string
print(s_rev)
