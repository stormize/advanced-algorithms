food = dict()
orders=[]
counter=0
round = input().split(' ')
requests=round[0]
payment=round[1]
for i in range(int(requests)):
    recipe=input().split(' ')
    food[recipe[0]]=int(recipe[1])
for j in range(int(payment)):
   order = input().split(' ')
   for x in order:
       if food.get(x):
         counter+=food[x]

   print(counter)

