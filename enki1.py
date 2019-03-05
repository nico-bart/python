# def say_hello(name):
#     return "Hello,{0}".format(name)
# def h2_decorate(string_function):
#     def func_wrapper(name):
#         return "<h2>{0}<h2>".format(string_function(name))
#     return func_wrapper
# hello_wrapper = h2_decorate(say_hello)
#
# say_hello("Nico")


# def counter_gen(n):
#     i = 0
#     while i<n:
#         yield i
#         i += 1
#
# scores = [0,1,4,5]
# newscores = []
# for i in scores:
#     newscores.append(i+2)
# print(newscores)
#
# scores = [0,1,4,5]
# newscores = list(map(lambda x: x+2, scores))
# print("--")
# print(newscores)

testlist1 = [-3,-2,1,2]
testlist2 = [7,-10]
print(max(testlist2,key=abs)) #prints highest absolute value in testlist2

print(max(testlist2,testlist1)) #prints list with highest value in it

print(max(testlist1,testlist2,key=len)) #prints the longer list

print(max(list(max(testlist1,testlist2))))

# Find the list with the highest average per entry
queue1 = [3,1,2,2,3,1]
queue2 = [3,7,6,9,8,4]
print(max(queue1,queue2,key=lambda x: sum(x)/len(x)))

#print the sum
queue3 = [1,2,3,4,5,6]
print(sum(queue3))
print(sum(queue3,5))
