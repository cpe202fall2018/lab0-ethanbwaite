def weight_on_planets():
   # write your code here
   
   earthWeight = float(input("How much do you weigh on Earth? "))
   print("\nOn Mars you would weigh %g pounds. \nOn Jupiter you would weigh %g pounds." % ((earthWeight*0.38),(earthWeight*2.34)))
   
   
if __name__ == '__main__':
   weight_on_planets()