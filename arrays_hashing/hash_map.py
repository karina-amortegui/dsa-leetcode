class MyHashMap() :
    #create init array with capacity of 10 buckets to start
    # [ [], [], [], [], [], [], [], [], [], [] ]
    def __init__(self, capacity=10):
        self.data = [[] for _ in range(capacity)]
        
    def hash(self, value):
        return
    
    def put(self, key, value):
        return

    def get(self, key):
        return  
    
    def delete(self, key):
        return
    
    def to_string(self):
        for bucket in self.data:
            for value in bucket:
                print(value)

if __name__ == "__main__":
    hashmap = MyHashMap()
    hashmap.to_string()