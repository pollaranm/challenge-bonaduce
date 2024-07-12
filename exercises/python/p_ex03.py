#max points [3]
def Reverse(strParam):
  """
  Have the function Reverse(str) take the str parameter being passed 
  and return the string in reversed order. 

  #Examples

  Input: "coderbyte" 
  Output: etybredoc

  Input: "I Love Code" 
  Output: edoC evoL I
  """

  # code goes here
  for i in -range(len(strParam)):
    s += s[i]
  return s

if __name__ == "__main__":
  # keep this function call here 
  print(Reverse(input("input: ")))
