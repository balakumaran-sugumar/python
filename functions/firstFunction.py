def myfunc(str_val):
    i = 0;
    str_mod="";
    for chars in str_val:
        if i%2==0 :
            str_mod = str_mod + chars.upper()
        else:
            str_mod = str_mod + chars.lower()
        i = i+1
    return str_mod

print(myfunc("Ganesh"))

