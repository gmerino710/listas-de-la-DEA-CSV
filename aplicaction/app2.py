import re;
#este siurve para rgular expression

def separate_name(name):
    print(name);
    name = re.sub('-',' ',name);
    print(name);
    name = name.split(' ');
    print(name);
    print(len(name))
    if len(name) ==3:
        names = name[0]+' '+name[1];
        print(names)
        apellidos = name[2];
        print(apellidos)
    elif len(name)==2:
        names = name[0]
        print(names)
        apellidos=name[1];
        print(apellidos)
        print('{} {}'
        .format(names,apellidos));

name ='Steven Jefferson-Blenkhorn'

separate_name(name);
 