# arr = [6, 12, 24, 8, 1]

class linearsearch:
  arr = []
  
  def __init__(self) -> None:
    # self.loc = -1
    self.n = 0
  def input(self):
    self.n = int(input("Enter the no. of elements in the array: "))
    for i in range(self.n):
      ele = int(input("Enter the elements of the array: "))
      self.arr.append(ele)

  def output(self):
    item = int(input("Enter the item to be searched: "))
    for i in range(self.n):
      if self.arr[i] == item:
        loc = i + 1
        return f"Element at location {loc}"
    return "No items found!"
  
ls = linearsearch()
ls.input()
print(ls.output())
