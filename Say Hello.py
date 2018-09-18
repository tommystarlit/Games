def say_hello():
  name = input("Hello! What's your name?: ")
  if name == "Python" or name == "Py":
      print("Hello "+ name +"! "+"I love You <3")
      print("")
  else:
    print("Hello "+ name +".")
    print("")
  say_hello()
  
say_hello()