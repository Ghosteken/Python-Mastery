# # students = ['hermonie', 'ron', 'harry']
# # print(students[0])

# # num = (len(students))

# # # for student in students:
# # #     print(student)
# # for i in range(num):
# #     print(i + 1 ,students[i])    
    
    
# from sqlalchemy import Null


# students = {"   herminoe":"griffnidor",
#                 "harry":"gifitn",
#                 "ron":"giff",
#             }   

# for student in students:
#     print(student, students[student], sep=",")

# for _ in range(3):
#     print('#')
    
# def print_gods():
#     print_gods(size)
    
# # for each row in squre
# for i in range(size):
#     for j in range(size)    
# print("hellow")

def main():
    x = get_int("what is x?? ")
    print(f"x is {x}")



def get_int(promt):
    while True:
        try:
            return int(input(promt)) 
        except ValueError:
            print("x is not an integer")
                
 
main()