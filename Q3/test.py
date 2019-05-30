import LRUCache
from time import sleep

def displayCache(cacheList):
    for key, value in enumerate(cacheList.element_list):
        print("Key -> {}, Value -> {}, Time -> {}".format(value.key,value.value,value.time))    

parth = LRUCache.LRUItem(1, "Parth")
alpesh = LRUCache.LRUItem(2, "Alpesh")
dubal = LRUCache.LRUItem(3, "Dubal")
heena = LRUCache.LRUItem(4, "Heena")
vijay = LRUCache.LRUItem(5, "Vijay")

start_cache = LRUCache.LRUCache(5,10)
start_cache.pushElement(parth)
start_cache.pushElement(alpesh)
start_cache.pushElement(dubal)
start_cache.pushElement(heena)
start_cache.pushElement(vijay)
print("SHOWING CACHE")
displayCache(start_cache)

start_cache.deleteItem(parth)
print("SHOWING CACHE AFTER DELETION - PARTH")
displayCache(start_cache)

start_cache.pushElement(parth)
print("SHOWING CACHE AFTER PUSHING - PARTH")
displayCache(start_cache)

sleep(15)
start_cache.deleteInvalidElements()
print("SHOWING CACHE AFTER EXPIRATION")
displayCache(start_cache)