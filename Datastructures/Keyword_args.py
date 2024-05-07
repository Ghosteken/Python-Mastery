def complicated_methods(*args, **kwargs):
    print(args,kwargs)
    pass


complicated_methods(1,2,3, x =1, y ='hello world', z = True)


#def complicated_methods2(a,b,c = True, d = False):
 #   print(a,b,c,d)
   #  pass

#complicated_methods2(*[1, 2],**{"c":"hello","d" :"goodbye"}) # type: ignore