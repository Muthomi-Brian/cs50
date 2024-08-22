

def main():
  try:
    value =int(input("input mass:"))
    conversion(value)
  except ValueError:
    if value == "":
      print("input cant be an empty string")
      return main()
    
    else:
      print(f"{value}is not a number")
      return main()
  
  
def conversion(a):
  E = a * 3000000000*3000000000
  return print(E)

main()