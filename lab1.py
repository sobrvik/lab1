# task 1
x = 1
y = 1.1
text = "text"
plus = True
minus = False
print ("x =", x, type(x),"\n",
       "y =", y, type(y),"\n", 
       "text =", text,type(text), "\n",
       "plus =", plus, type(plus),"\n",
       "minus =", minus, type(minus))

#task 2

x = 5
y = 7
z = 9
print("x =",x, "y =",y, "z =",z,"\n",
      "x + y =",x + y,"\n",
      "x - y =",x - y,"abs =",abs(x-y),"\n",
      "x * y =",x * y,"\n",
      "x / y =",x / y,"round =",round(x/y),"modulo =",(x%y),"\n",
      "x ** y =",x ** y)
res=(x+y+z)/3
print("середнє арифметичне чисел", x, y, z,"=", res)

#task3

first_name = "viktor "
last_name = "sOBORAICHUK"
full_name = first_name.capitalize()+last_name.swapcase()
age = "38"
print (f"My name is {full_name} and I am {age} years old.")

#task4

input_num = input("Введіть число: ")
num = int(input_num)
if num % 2 == 0:
      print(f"{num} - парне число")
else:
      print(f"{num} - не парне число")
      
num = float(input("Введіть число: "))
range1 = float(input("Введіть число початку діапазону: "))
range2 = float(input("Введіть число кінця діапазону: "))
    
if range1 <= num <= range2:
      print(f"Число {num} входить в діапазон [{range1}, {range2}].")
elif range1 >= num >= range2:
      print(f"Число {num} входить в діапазон [{range1}, {range2}].")    
else:
      print(f"Число {num} не входить в діапазон [{range1}, {range2}].")
        
#task5
   
for i in range(1, 11):
    print(i)
    
sum=0
cur_num=1
while cur_num <= 100:
      sum += cur_num
      cur_num += 1
print(f" сума чисел від 1 до 100 = {sum}")
       
#task6

def sum_num(a, b):
    return a + b    
res = sum_num(3, 8)
print(res)

def revers(str):
    res=''
    for i in range(len(str)-1,-1,-1):
        res+=str[i]
    return res

test = revers(input("введіть строку : "))
print("строка у звороті : ",  test)

#task 7

nums = [1, 2, 3, 4, 5]
for element in nums:
    print(element)
nums.insert(0, 0)
nums.pop()
print(nums)


#task8

student = {
"name": "Віктор",
"age": 100,
"faculty": "КН-2/1"
}
print("ім'я: ", student["name"], "вік: ", student["age"], "факульет: ", student["faculty"])
student["year"] = 2024
print(student)

#task9

def nums(a,b):
      try:
            res=a/b
            print(f"Результат ділення: {res}")
      except ZeroDivisionError:
            print ("Ділення на нуль неможливе")
      
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
nums(a, b)
