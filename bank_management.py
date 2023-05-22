from math import ceil
import uuid
import datetime
year = datetime.date.today().year
month=datetime.date.today().month
day=datetime.date.today().day
#Linked List
class Node(object):

    def __init__ (self, d, n = None):
        self.data = d
        self.next_node = n

    def get_next (self):
        return self.next_node

    def set_next (self, n):
        self.next_node = n
        
    def get_data (self):
        return self.data

    def set_data (self, d):
        self.data = d
        
    def has_next (self):
        if self.get_next() is None:
            return False
        return True
        
    def to_string (self):
        return  self.data
        
class LinkedList (object):

    def __init__ (self, r = None):
        self.root = r
        self.size = 0

    def get_size (self):
        return self.size

    def add (self, d):
        new_node = Node (d, self.root)
        self.root = new_node
        self.size += 1

    def add_node (self, n):
        n.set_next(self.root)
        self.root = n
        self.size += 1
        
    def remove (self, d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.get_data() == d:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True     # data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False  # data not found

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == d:
                return d
            elif this_node.get_next() == None:
                return False
            else:
                this_node = this_node.get_next()
                
    def print_list(self):
        v=[]
        if self.root is None:
            return
        this_node = self.root
        v.append(this_node.to_string())
        while this_node.has_next():
            this_node = this_node.get_next()
            v.append(this_node.to_string())
        return v
            
    def sort (self):
        if self.size > 1:
            newlist = [];
            current = self.root;
            newlist.append(self.root);
            while current.has_next():
                current = current.get_next();
                newlist.append(current);
            newlist = sorted(newlist, key = lambda node: node.get_data(), reverse = True);
            newll = LinkedList();
            for node in newlist:
                newll.add_node(node);
            return newll;
        return self;
myylist=LinkedList()
def alaki():
 print('### Main Menu ###\nChoose one item:\n1.Create new account\n2.Update your account information\n3.Transactions\n4.Check details of your account\n5.Remove existing account\n6.Most and Least balence\n7.Median of balence list\n8.Total number of accounts in this bank\n9.Search by name\n10.Sort ages and get Mean of ages\n11.Exit')
print('WELCOME TO OUR BANK MANAGEMENT SYSTEM')
 
myList=LinkedList()
alaki()

#heap sort

def heapify(arr, n, i): 
    largest = i  
    l = 2 * i + 1    
    r = 2 * i + 2   
    if l < n and arr[i] < arr[l]: 
        largest = l 
    if r < n and arr[largest] < arr[r]: 
        largest = r
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  
        heapify(arr, n, largest) 
def heapSort(arr): 
    n = len(arr) 
    for i in range(n // 2 - 1, -1, -1): 
        heapify(arr, n, i) 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   
        heapify(arr, i, 0) 


ages=LinkedList()
#Binary tree
class Nodee:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Nodee(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Nodee(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Nodee(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)

tree=Tree()
namee = LinkedList()
def birth(a):
  yu=year-140 #140 is the max of human age
  while True:
      if a.count('-')==2:
          try:
              aa=[int(i) for i in a.split('-')]
              if yu<aa[0]<=year and 0<aa[1]<=12 and 0<aa[2]<=31:
                  break
              else:
                  print('Wrong numbers')
          except ValueError:
              print('Wrong format')
      else:
          print('Wrong format')
      a=input('enter your year of birthday in AD(e.x. : 2002-1-13): ')
  i[k]=a

  
  noo=uuid.uuid4()
  a1= str(noo).split('-')
  no=a1[2]
def moneyy(a):
  try:
      xx=a
      xx=int(xx)
      i[k]=xx
  except ValueError:
      print('Warning! it should be only digits.')
      while True:
          a=input('Enter your account balance: ')
          try:
              x=a
              xx=int(x)
              i[k]=xx
              break
          except ValueError:
              print('Warning! it should be only digits.')
  
a=int(input('Operation Number: '))
while a!=11:
 if a==1:
  name=input('enter your full name: ')
  date=input('enter your year of birthday in AD(e.x. : 2002-1-13): ')
  yu=year-140 #140 is the max of human age
  while True:
      if date.count('-')==2:
          try:
              a=[int(i) for i in date.split('-')]
              if yu<a[0]<=year and 0<a[1]<=12 and 0<a[2]<=31:
                  break
              else:
                  print('Wrong numbers')
          except ValueError:
              print('Wrong format')
      else:
          print('Wrong format')
      date=input('enter your year of birthday in AD(e.x. : 2002-1-13): ')

  
  noo=uuid.uuid4()
  a1= str(noo).split('-')
  no=a1[2]
#   print(f'Your full id is: {noo}\nBut you have only use: {no}\nSo your account id is: {no}')
          
  password=input('password(At least 4 letters or numbers): ')
  if len(password)<4:
      while len(password)<4:
          print('Warning: At least you should use 4 charecters or digits for password')
          password=input('password(At least 4 letters or numbers): ')
  money=input('enter your account balance: ')
  try:
      xx=money
      xx=int(xx)
  except ValueError:
      print('Warning! it should be only digits.')
      while True:
          money=input('Enter your account balance: ')
          try:
              x=money
              x=int(x)
              break
          except ValueError:
              print('Warning! it should be only digits.')
  print('Creating your account...')
  print(f'Your Account ID is: {no}')
  print('Done')
  kol=[name,date,no,password,money]
  myList.add(kol) 
  namee.add(name) 
  s2=date.split('-')
  myylist.add(int(money)) 
  gg=int(year)-int(s2[0])
  ages.add(gg)
 elif a==2:
  try:
   if len(myList.print_list())!=0:
    num=input('enter your account id: ')
    for i in myList.print_list():
     if i[2]==num:
      passwo=input('enter the password: ')
      if passwo==i[3]:
       k=int(input('What do you want to change from your account?\n0.name\n1.birthday\n2.account ID\n3.password\n4.balance\n'))
    #    a=input('enter new data: ')
       if k==0:
           a=input('Enter your new Data: ')
           i[k]=a
           break
       elif k==1:
           a = input('Enter New Data: ')
           tt = i[1].split('-')
           u = int(year)-int(tt[0])
           birth(a)
           t = i[k].split('-')
           gg=int(year)-int(t[0])
           ages.remove(u)
           ages.add(gg)
           
           break

       elif k==2:
           a=input('Enter New Data: ')
           while len(a)!=4:
               a =('Lenght of Account ID shoud be 4\nEnter New Data:')
           i[k]=a
           break
       elif k==3:
           a = input('New Data: ')
           while len(a)<4:
               a =('Lenght of Password shoud be grater or equal to 4\nEnter New Data:')
           i[k]=a
           break
       elif k==4:
           p = i[k]
           a =input('Enter New Data: ')
           moneyy(a)
           print(p)
           myylist.remove(int(p))
           myylist.add(i[k])
           break

                       
       
     else:
         print('Wrong password!')
    else:
        print('Unknown ID.')
  except TypeError:
      print('No account founded.\nPress 1 to create an account')
 elif a== 3:
  try:
   if len(myList.print_list())!=0:
    num=input('enter your account id: ')
    for i in myList.print_list():
     if i[2]==num:
      passwo=input('enter the password: ')
      if passwo==i[3]:
       maghsad=input('the account id you want to add money to: ')
       for j in myList.print_list():
        if j[2]==maghsad:
         pool=int(input('enter the number of the money: '))
         oo=int(i[4])
         ok= oo-pool
         if ok>=0:
          i[4]=str(ok)
          pp=int(j[4])
          pp+=pool
          j[4]=str(pp)
          print('Done')
          break
         else:
             print('Not enough money in your account!')
        else:
            b=int(input('Warning! This account is unknown!\nDo you want to continue?\n1.Yes\n2.No\n'))
            if b ==1:
                pool=int(input('enter the number of the money: '))
                oo=int(i[4])
                ok= oo-pool
                if ok>=0:
                    i[4]=str(ok)
                    print('Done')
                else:
                    print('Not enough money in your account!')
            else:
                pass

     
      else:
          print('Wrong password!')
  except TypeError:
      print('No account founded.\nPress 1 to create an account')
 elif a ==4:
  try:
   if len(myList.print_list())!=0:
    num=input('enter your account id: ')
    for i in myList.print_list():
        if i[2]==num:
            passwo= input('Enter The password: ')
            if passwo==i[3]:
                print(f'Name:{i[0]}\nBD:{i[1]}\nAccount id:{i[2]}\nPassword:{i[3]}\nBalence:{i[4]}')
            else:
                print('Wrong password! ')
        else:
            print('Unknown ID.')
  except TypeError:
      print('No account founded.\nPress 1 to create an account')

  
 elif a==5:
    try:
       if len(myList.print_list())!=0:
           num=input('Enter your account id:')
           for i in myList.print_list():
               if i[2]==num:
                   passwor=input('Enter your password: ')
                   if passwor==i[3]:
                       s=int(input('Are you sure that you want to delete your account?(press 0 for yes and 1 for no)\n0.Yes\n1.No\n'))
                       if s==0:
                           myList.remove(i)
                           myylist.remove(int(i[4]))
                           print('account with number %s deleted'%num)
                           break
                       else:
                           break
                   else:
                       print('Wrong password!')
                       break
           else:
                   print('Not found.')
                   break
    except TypeError:
        print('No account founded.\nPress 1 to create an account')
                 

 elif a ==6:
     try:
         if len(myylist.print_list())>=2:
             aa = myylist.print_list()
             heapSort(aa)
             print(f'The most balence is: {aa[-1]}')
             print(f'The least balance is: {aa[0]}')


     except TypeError:
         print('You need at least 2 account for this part.\nPress 1 to create an account')
 elif a ==7:
     n = myylist.print_list()
     try:
         if len(n)>=1:
             heapSort(n)
             if len(n)%2!=0:
                 m = int(len(n)/2)
                 print(f'Median is : {n[m]}')
             else:
                 dd = len(n)//2
                 bb =dd+1
                 print(f'Median is :{n[dd-1]} and {n[bb-1]}')


     except TypeError:
         print('No account founded.\nPress 1 to create an account')
 elif a ==8:
     print('Total number of accounts: ',myList.get_size())
 elif a == 9:
     h = namee.print_list()
     ppp= myList.print_list()
     try:
         if len(h)!=0:
             vk = input('Enter the full name (e.x: Ali Hashemi): ')
             if namee.find(vk)==vk:
                 passwo=input('Enter the password: ')
                 jadid=ppp[h.index(vk)]
                 if passwo==jadid[3]:
                    print(f'Name:{jadid[0]}\nBD:{jadid[1]}\nAccount id:{jadid[2]}\nPassword:{jadid[3]}\nBalence:{jadid[4]}')
                 else:
                     print('Wrong password! ')
             else:
                 print(f'{vk} dose not have an account in this bank.')
     except TypeError:
         print('No account founded.\nPress 1 to create an account')
 elif a==10:
     try:
         if len(myList.print_list())!=0:
             g=ages.print_list()
             print('Sorted list for customers age: ')
             sum=0
             for i in g:
                 tree.add(i)
                 sum+=i
             tree.printTree()
             mean=sum/len(g)
             print(f'Mean is : {mean}')
     except TypeError:
         print('No account founded.\nPress 1 to create an account')
 alaki()
 a=int(input('Operation Number: '))
