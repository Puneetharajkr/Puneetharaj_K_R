a = int(input("Enter a number: "))
result = []

limit = 1
if a%2==1:
    limit = a
else:
    limit=a-1

for i in range(limit):
    result.append(2*i + 1)

print("Output:")
print(", ".join(map(str, result)))
