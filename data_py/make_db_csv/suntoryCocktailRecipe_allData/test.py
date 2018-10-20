def get_str(*args):
    flg = 1
    for obj in args:
        for k, v in globals().items():
            if id(v) == id(obj):
                target = k
                break
        return target
        # if flg == 1:
        #     out = target+' = '+str(obj)
        #     flg = 0
        # else:
        #     out += ', '+target+' = '+str(obj)            

a = 1
print(type(chkprint(a)))