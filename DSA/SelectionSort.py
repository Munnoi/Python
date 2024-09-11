class SelectionSort:
  arr = []

  def __init__(self) -> None:
    self.n = 0

  def input(self):
    self.n = int(input("Enter the size of the array: "))

    print("Enter the elements of the array:") 
    for i in range(self.n):
      ele = int(input())
      self.arr.append(ele)

  def output(self):
    for i in range(self.n - 1):
      for j in range(i + 1, self.n):
        if self.arr[i] > self.arr[j]:
          self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

  def display(self):
    for x in self.arr:
      print(x, end=' ')
    print()


ss = SelectionSort()
ss.input()
ss.output()
ss.display()