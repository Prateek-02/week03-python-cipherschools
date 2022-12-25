def func(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")
        
d = {'name':'Prateek','age':19}        
func(**d)    