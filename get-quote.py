import random
def one():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 16
  rnd = random.randint(0,last)
  print(quotes[rnd], end=' ', sep='\n')
  print(quotes[rnd+1])

  file = open("quotes.txt", "a")
  file.write("\nHello Word")
  file.close()

if __name__== "__main__":
  one()
