import random
rand = random.randint(0,19)
def primary():
 # print("Keep it logically awesome.")
  f = open("quotes.txt")

  quotes = f.readlines()
  f.close()

  print(quotes[rand])

if __name__== "__main__":
  primary()
