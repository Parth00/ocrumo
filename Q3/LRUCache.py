from datetime import datetime


class LRUItem(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.time = datetime.now()


class LRUCache(object):
    def __init__(self, size, time_validity):
        self.time_validity = time_validity
        self.size = size
        self.cache = {}
        self.element_list = []

    def deleteItem(self, element):
        del self.cache[element.key]
        del self.element_list[self.element_list.index(element)]

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

    def deleteInvalidElements(self):
        now = datetime.now()
        for element in self.element_list:
            expiration_limit = now - element.time
            if expiration_limit.seconds > self.time_validity:
                self.deleteItem(element)

    def showCacheElements(self, cache):
        for key, value in enumerate(cache.element_list):
            print("Key -> {}, Value -> {}, Time -> {}".format(value.key,value.element,value.time))


        