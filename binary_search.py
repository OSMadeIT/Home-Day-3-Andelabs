class BinarySearch(list): # create a BinarySearch class that inherits from the list class
    def __init__(self,a,b): # __init__() takes two integers as parameters, a and b
      data = []
      data.append(b)
      list_len = 1
      while list_len < a:
        data.append(data[list_len -1] + b)
        list_len +=  1
      super(BinarySearch,self).__init__(data)
      self.length = len(data)

    def search(self,value_to_find): #Method, search, it takes just one argument
        count  = 0
        first  = 0
        self.length = len(self)
        last  = self.length - 1
        mid_point = int((last) / 2)
        obj_location = {'count':'','index':''}
        while first < mid_point:
            
            if (first == mid_point) and (self[first] > value_to_find):
                index = -1 
                obj_location["count"] = self.length
                obj_location["index"] = index
                return obj_location
            
            elif self[first] == value_to_find:
                index = first
                obj_location["count"] = count
                obj_location["index"] = index
                return obj_location
            elif self[last] == value_to_find:
                index = last
                obj_location["count"] = count
                obj_location["index"] = index
                return obj_location
            elif self[mid_point] == value_to_find:
                index = mid_point
                obj_location["count"] = count
                obj_location["index"] = index
                return obj_location
            else:
                if self[mid_point] > value_to_find:
                    last = mid_point - 1
                    first = first + 1
                    mid_point = (last + first)//2
                else:
                    first = mid_point + 1
                    last = last - 1
                    mid_point = ((last + first)//2) + 1
            count += 1
        obj_location = {'count':count,'index':-1}       
        return obj_location
