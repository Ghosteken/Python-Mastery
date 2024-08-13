

# # # # # name = input("what is your name")
# # # # # if name == 'harry':
# # # # #     print("hermonie")
# # # # # elif name == 'draco':
# # # # #     print("sly")

# # # # # #match keyword
# # # # # match name:
# # # # #     case 'harryo' | 'bgood':
# # # # #         print("good")
# # # # #     case 'food':
# # # # #         print("tinumbu") 
# # # # #     case _:
# # # # #         print("who??")         
        
# # # # #loop
# # # # i = 0
# # # # while i<=2:
# # # #     print("meow")
# # # #     i +=1  
           
# # # print("good\n"*3,end="")


# # # for _ in range(3):
# # #     print("meow")           

# # n = int(input('what is n: '))
# # for n in range(n):
# #     print('meow')   
    
# while True:
#     n = int(input('what is n: '))
#     if n < 0 :
#         break
# for _ in range(n):
#     print("meow")             
def main():
    number = get_number()
    meow(number)
    
    
def get_number():
    while True:
        n = int(input('what is n: '))
        if n > 0 :
            break
    return n             
    
def meow(n):
    for _ in range(n):
        print('meow ')   

main()

#list
