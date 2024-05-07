#higher order functions
lit = [1,2,3,4]
list(map(lambda x: x**3, lit))
list(filter((lambda x: x<3), lit))                                    