
# q1

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
  if num % 5 != 0:
    continue
  if num > 500:
    break
  if num > 150:
    continue
  print(num)




  
# q2
for var in range(10):
    print(var)
else:
    print("Done!")




# q3    
num = 76542
print(str(num)[::-1])





# q4
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
x = {}
for key in keys:
    for value in values:
        x[key] = value
        values.remove(value)
        break
print("dictionary is" + str(x))





# q5
sample_dict ={
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]
for x in keys:
    sample_dict.pop(x)
print(sample_dict)




# q6
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
for x in sample_list:
    sample_set.add(x)
print(sample_set)



# q7
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))



# q8
tuple1 = (10, 20, 30, 40, 50)
new_tuple = tuple1[::-1]
print(new_tuple)



# q9
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])



# q10
tuple1 = (10, 20, 30, 40)
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)

