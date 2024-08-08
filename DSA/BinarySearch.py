class Binarysearch:
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
    beg = mid = 0
    end = self.n - 1
    while beg <= end:
      mid = (end - beg) // 2
      if self.arr[mid] == item:
        loc = mid + 1
        return f"Element at location {loc}"
      elif self.arr[mid] < item:
        beg = mid + 1
      elif self.arr[mid] > item:
        end = mid - 1
      else:
        return "No items found!" # Don't know if this 'else' is necessary.
      return "No items found!"
  
bs = Binarysearch()
bs.input()
print(bs.output())