class Heap:
  def __init__(self):
    self.contents = []
  
  def insert(self, item):
    idx = len(self.contents)
    self.contents.append(item)
    # [11,10,9,5]
    while()


if __name__ == '__main__':
  heap = Heap()

  heap.insert(10)
  heap.insert(9)
  heap.insert(11)
  heap.insert(5)
  heap.insert(22)
  heap.insert(3)

  assert(heap.size() == 6)
  assert(heap.pop() == 22)
  assert(heap.pop() == 11)
  assert(heap.pop() == 10)
  assert(heap.size() == 3)
  print('Success!')
