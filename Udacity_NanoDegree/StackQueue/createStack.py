class Stack:
    def __init__(self,num_of_elements = 10):
        self.arr = [None for _ in range(num_of_elements)]
        self.next_elem = 0
        self.total_elements = 0

    def push(self,value):
        if self.next_elem == len(self.arr):
            print("Increasing stack size...")
            self._handle_stack_full_capacity()
        self.arr[self.next_elem] = value
        self.next_elem += 1
        self.total_elements += 1

    def size(self):
        return self.total_elements

    def is_empty(self):
        if self.size() == 0:
            return True
        return False

    def _handle_stack_full_capacity(self):
        old_stack = self.arr
        self.arr = [0 for _ in range(len(old_stack) * 2)]

        for index,value in enumerate(old_stack):
            self.arr[index] = value

foo = Stack()
print(foo.arr)
print(foo.is_empty())
print(foo.size())
print("\n"+"\n")
foo.push(0)
print(foo.arr)
foo.push("Hello")
foo.push("Done")
foo.push("Hello")
foo.push("Done")
foo.push("Hello")
foo.push("Done")
foo.push("Hello")
foo.push("Done")
foo.push("Hello")
foo.push("Done")
foo.push("Hello")
foo.push("Done")
foo.push("Hello")
foo.push("Done")
foo.push("Hello")
foo.push("Done")
foo.push("Hello")
foo.push("Done")
foo.push("Hello")
foo.push("Done")


print(foo.arr)
print("\n"+"\n")
print(foo.is_empty())
print(foo.size())
