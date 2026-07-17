#Exercise 01
names = ['Rakshitha','Poojitha','Yashwanth','Siddharth','Dhanveer']
print("good morning", names[0])
print("good morning", names[1])
print("good morning", names[2])
print("good morning", names[3])
print("good morning", names[4])

#Exercise 02
Guest_list = ['Kai', 'Isabella', 'Slaone', 'Xavier', 'Sebastian', 'Maya']
print(len(Guest_list))

#Exercise 03
Guest_list = ['Kai', 'Isabella', 'Slaone', 'Xavier', 'Sebastian', 'Maya']
print(f"Hey i have arranged a party in the account of my birthday, i will be looking forward to you", Guest_list[0])
print(f"Hey i have arranged a party in the account of my birthday, i will be looking forward to you", Guest_list[1])
print(f"Hey i have arranged a party in the account of my birthday, i will be looking forward to you", Guest_list[2])
print(f"Hey i have arranged a party in the account of my birthday, i will be looking forward to you", Guest_list[3])
print(f"Hey i have arranged a party in the account of my birthday, i will be looking forward to you", Guest_list[4])
print(f"Hey i have arranged a party in the account of my birthday, i will be looking forward to you", Guest_list[5])
print("Unfortunately", Guest_list[4], "cannot make it to the party ")
print("Unfortunately", Guest_list[5], "cannot make it to the party")
del Guest_list[5]
del Guest_list[4]
print("see you soon guys", Guest_list)

print("No worries guys i have got a bigger table")
Guest_list.insert(0, 'Mr and Mrs Volkov')
Guest_list.insert(3, 'Mr and Mrs Harper')
Guest_list.append('Mr and Mrs Donovan')  
print(Guest_list)   

Guest_list.pop (1)
print("Im so sorry kai, i promise we will soon catch up")
print (Guest_list)
Guest_list.pop (2)
print("im sorry mr and mrs harper we will mwwt some other time")
print(Guest_list)
Guest_list.pop (1)
print("sorry isa we will meet some other time")
print(Guest_list)
Guest_list.pop (1)
print("sorry sloane lets meet up somr other time")
print(Guest_list)
Guest_list.pop (1)
print("sorry xav lets meet up somr other time")
print(Guest_list)
Guest_list.pop (1)
print("sorry mr and mrs donovan lets meet up somr other time")
print(Guest_list)


print("Mr and Mrs Volkov we can meet today")
print("see you at dinner")

del Guest_list[0]
print(Guest_list)


#Exercise 04
favourite_cars = ['limousine','audi','red_ferrari','mclaren','bugatti']
print("one day i will have my own", favourite_cars[0])
print("one day i will have my own", favourite_cars[1])
print("one day i will have my own", favourite_cars[2])
print("one day i will have my own", favourite_cars[3])
print("one day i will have my own", favourite_cars[4])

#Exercise 05
Bucket_list = ['Italy', 'Paris', 'Greece', 'Fiji', 'Finland']
print(("list length is:",len(Bucket_list)))

print(Bucket_list)
print(sorted (Bucket_list))
print(Bucket_list)
Bucket_list.reverse()
print(Bucket_list)
Bucket_list.reverse()
print(Bucket_list)
Bucket_list.sort()
print(Bucket_list)
Bucket_list.sort(reverse=True)
print(Bucket_list)
