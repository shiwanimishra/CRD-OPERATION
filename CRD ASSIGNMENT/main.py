
import code as x 

x.create("shiwani",21)

x.create("mishra",70,3600) 

x.read("shiwani")

x.read("mishra")

x.create("shiwani",50)
x.delete("shiwani")
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t2.start()
t2.sleep()

