#max points [6]
def UsernameValidation(strParam):
  """
  Have the function UsernameValidation(str) take the str parameter being passed 
  and determine if the string is a valid username according to the following rules: 

  1. The username is between 4 and 25 characters.
  2. It must start with a letter. 
  3. It can only contain letters, numbers, and the underscore character. 
  4. It cannot end with an underscore character. 

  If the username is valid then your program should return the string true, otherwise return the string false.

  #Examples

  Input: "aa_" 
  Output: false

  Input: "u__hello_world123" 
  Output: true
  """

  # code goes here
  if (len(strParam) <= 25 and len(strParam)  >= 4):
      return False
  elif strParam[0].isLiteral():
      return False
  elif strParam[24] == "_":
    return False
  elif onlyValidCharacter(strParam,"_") or onlyValidCharacter(strParam,"0123456789") or :
     return False
  else:
    return True

if __name__ == "__main__":
  # keep this function call here 
  print(UsernameValidation(input("input: ")))
