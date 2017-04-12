def coroutine(func):    
  def start(*args,**kwargs):       
    cr = func(*args,**kwargs)        
    cr.__next__()        
    return cr    
  return start

class COR(object):  
  def __init__(self, pattern):       
    self.count=0       
    self.pattern=pattern       
    self.find=self._grep()  
    
    @coroutine  
    def _grep(self):        
      while True:           
        line=yield           
        if line in self.pattern:                
          print(self.count, line)               
          self.count+=1   
      
      def send(self, arg):       
            self.find.send(arg)   
      
      def close(self):        
           print("Closing Courtine after finding {} total count".format(self.count))       
          self.find.close()   
      
      def next(self):       
        self.find.__next__()
