from random import choice

class CustomDataStructure:
    def __init__(self):
        self.index_map = {}
        self.values = []

    def custom_insert(self, val):
        if val in self.index_map:
            return print(f"Error: {val} already exists in data structure")
        
        self.values.append(val)
        max_len = len(self.values)-1
        self.index_map[val] = max_len
        return print(f"Value {val} inserted at index {max_len}")
        

    def custom_delete(self, val):
        '''
        retrieve last value from the list self.values and swap it with the value that will be popped.
        pop list and remove the key in dict
        '''
        if val in self.index_map:
            index = self.index_map[val]
            last_val = self.values[-1]
            self.values[index] = last_val
            self.values.pop()
            self.index_map[last_val] = index
            del(self.index_map[val])
            return print(f"Value {val} deleted from data structure.")

        return print(f"Error: {val} not found when trying to delete")

    def custom_search(self, val):
        if val in self.index_map:
            return print(f"Found value {val} at index {self.index_map[val]}")
        
        return print(f"Error: {val} not found during search")

    def get_random(self):
        random_value = choice(self.values)
        return print(f"Value {random_value} found in data structure at index {self.index_map[random_value]}")

cds = CustomDataStructure()

cds.custom_insert(11) # insert 11
cds.custom_insert(32) # insert 32
cds.custom_insert(4444) # insert 4444
cds.get_random() # get random number from list
cds.custom_search(32) # get 32 from dict
cds.custom_delete(32) # delete 32 from dict and list
cds.custom_search(32) # 32 no longer exists so error is thrown on search
cds.custom_delete(32) # 32 no longer exists so error is thrown on delete
cds.custom_insert(4444) # error should be thrown for inserting duplicate