class MyList(list):
    def sum(self):
        return sum(self)

nums = MyList([1, 2, 3, 4, 5])
print(nums.sum())  # 15
print(nums)        # [1, 2, 3, 4, 5]

my_list = MyList([1, 2, 3, 4, 5])
print(my_list)