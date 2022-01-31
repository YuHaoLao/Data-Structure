import sys 

class CDLLNode:

    def __init__(self, time="", tweet="", next_node=None, prev_node=None):
        self.time: str = time
        self.tweet: str = tweet
        self.next_node: CDLLNode = next_node
        self.prev_node: CDLLNode = prev_node
class CDLL:

    def __init__(self):
        self.head: CDLLNode = None
        self.current: CDLLNode = None
        self.numnodes: int = 0
    

    def find (self,k:str):
        
        
        for i in range (self.numnodes):
            
            if k.lower() in self. current.tweet.lower():
                self.print_current()
                # self.current=self.head
                break
                
            if self.current==self.current.prev_node :
                return
            else :

                self.go_next()
        return 

        
 # makes an insertion based on the 'current' node
    def insert(self,time: str, tweet: str):
        new_node=CDLLNode(time, tweet, None, None)
        if self.head==None:

            self.head=new_node
            
        
        elif self.head.next_node==None:
            if self.head.time>time:

                self.head.next_node = new_node
                self.head.prev_node = new_node
                new_node.next_node = self.head
                new_node.prev_node = self.head
                self.head=new_node
            else:
                
                self.head.next_node = new_node
                self.head.prev_node = new_node
                new_node.next_node = self.head
                new_node.prev_node = self.head

        elif self.head.time>time:
            self.head.prev_node.next_node=new_node
            new_node.prev_node=self.head.prev_node
            new_node.next_node=self.head
            self.head.prev_node=new_node
            self.head=new_node

        elif self.head.prev_node.time<time:
            self.head.prev_node.next_node=new_node
            new_node.prev_node=self.head.prev_node
            new_node.next_node=self.head
            self.head.prev_node=new_node
            

        else:
            self.current=self.head

            while self.current.time<time:
                self.current=self.current.next_node
               
            self.current.prev_node.next_node=new_node
            new_node.next_node=self.current
            new_node.prev_node=self.current.prev_node
            self.current.prev_node=new_node

           
        self.current=self.head
            
 
        self.numnodes += 1

    def go_next(self):
        
        self.current = self.current.next_node

    
    def go_prev(self):
        self.current=self.current.prev_node

    def go_first(self):
        self.current=self.head

    def go_last(self):
        self.current=self.head.prev_node

    def skip(self,n:int):
        for i in range (n):

            self.current = self.current.next_node
        
            


    def print_current(self):
        print(self.current.time)
        print(self.current.tweet)

    

            
def main():

    obj1= CDLL()
    name =sys.argv[1]

    with open(name,'r') as f:
        for line in f.readlines():
            s=line.split('|')
            time=s[1].split()[3]
            tweet=s[2].strip()
            obj1.insert(time,tweet)

    obj1.print_current()
    while True:
        command = input()
        if command == "n":
            obj1.go_next()
            obj1.print_current()
        elif command[0:2]=="s ":

            n,word=command.split(" ")
            obj1.find(word)

        elif command=="p":
            obj1.go_prev()
            obj1.print_current()
        elif command == "f":
            obj1.go_first()
            obj1.print_current()
        elif command == "l":
            obj1.go_last()
            obj1.print_current()
        elif command == "num":
            print(obj1.numnodes)

        elif command.isnumeric():
            aa=int(command)
            obj1.skip(aa)
            obj1.print_current()
           

        elif command == "q":
            return 

    	   
if __name__ == "__main__":

    main() 