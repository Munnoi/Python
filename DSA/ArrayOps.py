# Array Operations

class ArrOps:
  arr = []
  item = pos = n = 0

  def read(self):
    self.n = int(input("Enter the size of the array: "))
    print("Enter the elements: ")
    for i in range(self.n):
      self.item = int(input())
      self.arr.append(self.item)
  
  def print(self):
    print("The array elements are: ")
    for ele in self.arr:
      print(ele, end=' ')
    print()
  
  def insert(self):
    self.pos = int(input("Enter the position of insertion: "))
    self.item = int(input("Enter the item to be inserted: "))
    self.pos = self.pos - 1
    self.arr.insert(self.pos, self.item)

  def delete(self):
    self.pos = int(input("Enter the position to be deleted: "))
    self.pos = self.pos - 1
    del self.arr[self.pos]
    

def main():
  ao = ArrOps()


  while True:
    print("1.Read")
    print("2.Insert")
    print("3.Delete")
    print("4.Print")

    choice = int(input("Enter your choice: "))

    if choice == 1:
      ao.read()
    elif choice == 2:
      ao.insert()
    elif choice == 3:
      ao.delete()
    elif choice == 4:
      ao.print()
    else:
      print("Invalid choice!")

    repeat = input("Do you want to continue(y/n)?")
    if repeat.lower() == 'n':
      break

if __name__ == "__main__":
  main()