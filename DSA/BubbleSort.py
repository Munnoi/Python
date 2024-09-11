class BubbleSort:
  arr = []

  def __init__(self) -> None:
    self.n = 0

  def input(self):
    self.n = int(input("Enter the size of the array: "))
    print("Enter the elements of the array: ")
    for i in range(self.n):
      ele = int(input())
      self.arr.append(ele)

  def output(self):
    for i in range(self.n):
      for j in range(self.n - i - 1):
        if self.arr[j] > self.arr[j + 1]:
          self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j] # Swapping
  
  def display(self):
    for x in self.arr:
      print(x, end=' ')
    print()

bs = BubbleSort()
bs.input()
bs.output()
bs.display()