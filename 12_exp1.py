try:
     with open("1.txt","r") as f:
          f1= f.read()
          print(f1)
        
     with open("2.txt","r") as f:
         f2 = f.read()
         print(f2)
         

     with open("3.txt","r") as f:
         f3 = f.read()
         print(f3)
         
except Exception as e:
     print(f" some file is missing {e}")
            

    