numbers = []
n = int(input("Enter Length of List :"))

for i in range (1, n+1):
    num = int(input("Enter the Number :"))
    numbers.append(num)

numbers.sort()
sorted_list=(sorted(numbers))
print("The Second Largest Number is :",sorted_list[-2])
