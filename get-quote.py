import random
rand = random.randint(0,19)
rand2 = random.randint(0,19)
while rand == rand2:
  rand2 = random.randint(0,19)


def primary():
 # print("Keep it logically awesome.")
  f = open("quotes.txt")

  quotes = f.readlines()
  f.close()
  
  myQuotes = "\n" + quotes[rand] + quotes[rand2]
  print(myQuotes)

  

if __name__== "__main__":
  primary()
