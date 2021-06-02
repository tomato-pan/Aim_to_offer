# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def up_adjust(array:list):
    child_index = len(array)-1
    parent_index = (child_index-1)//2
    temp = array[child_index]
    while child_index>0 and temp<array[parent_index]:
        # 当小于父节点时替换子节点的值
        print(child_index,parent_index)
        array[child_index]=array[parent_index]
        child_index = parent_index
        parent_index = (parent_index-1)//2
    # 最后替换该值
    array[child_index]=temp

def down_adjust(p_index,length,array:list):
    pass

my_array = [1,3,2,6,5,7,8,9,10,0]
print(up_adjust(my_array))
print(my_array)
if __name__ == '__main__':
    list1 = [1,3,2,6,5,7,8,9,10,0]
    list1.pop(0)
    print(list1)