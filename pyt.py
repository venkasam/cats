def now(text):
    f=open(text)
    wrds=0
    fi=f.readlines()
    for lines in fi:
       words=lines.split()
       wrds=wrds+len(words)
    print(wrds)

now(input("enter text file here"))
