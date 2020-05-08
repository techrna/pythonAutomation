f=open("inputFile.txt","r")

pf=open("PassFile.txt","w")
ff=open("FailFile.txt","w")


for x in f:
    if x.split()[2]=="P":
        print(x)
        pf.write(x)
    else:
         ff.write(x)
f.close()
pf.close()
ff.close()