class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

# MY SOLUTION
#   def append(self, item):
#     self.storage.pop(self.current)
#     self.storage.insert(self.current, item)
#     if self.current < self.capacity -1:
#         self.current += 1
#     else: 
#         self.current = 0

#   def get(self):
#     return [i for i in self.storage if i != None]

# solution from TL Jon Simmons
  def append(self, item):
    self.storage[self.current] = item
    self.current = (self.current+1) % self.capacity

  def get(self):
    if self.current > self.capacity:
      return self.storage
    else:
       return list(filter(None.__ne__, self.storage))