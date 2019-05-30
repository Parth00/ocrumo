from datetime import datetime

""" Library to implement LRU Cache with Cache expiration"""
class LRUItem(object):
    """ Creating a cache item object that contains a key, value and time validity"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.time = datetime.now()


class LRUCache(object):
    """ Creating a cache container that contains its size, list of elements and list of elements in the cache already"""
    def __init__(self, size, time_validity):
        self.time_validity = time_validity
        self.size = size
        self.cache = {}
        self.element_list = []

    #Deleting cache element
    def deleteItem(self, element):
        del self.cache[element.key]
        del self.element_list[self.element_list.index(element)]

    #Pushing cache element to the first if its empty and move to the top if it exists
    def pushElement(self, element):
        if element.key in self.cache:
            index = self.element_list.index(element)
            self.element_list[:] = self.element_list[:index] + self.element_list[index+1:]
            self.element_list.insert(0, element)
        else:
            if len(self.element_list) > self.size:
                self.deleteItem(self.element_list[-1])
            
            self.cache[element.key] = element
            self.element_list.insert(0, element)

    #Delete cache elements which are expired
    def deleteInvalidElements(self):
        now = datetime.now()
        for element in self.element_list:
            expiration_limit = now - element.time
            if expiration_limit.seconds > self.time_validity:
                self.deleteItem(element)

        
