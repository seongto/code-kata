# linked list를 만들 수 있는 MyLinkedList 클래스를 설계해봅시다.
# singly linked list 로 해도 되고, doubly linked list 로 구현하셔도 됩니다.
# 
# singly linked list를 구현하려면 val과 next라는 속성이 있어야 합니다.
# val: 현재 node의 value
# next: 다음 node를 가르키는 pointer(reference)
# 
# doubly linked list를 구현하려면 prev라는 속성이 하나 더 있어야 합니다.
# prev: 이전 node를 가르키는 pointer(reference)
# 
# MyLinkedList 클래스에는 5가지 method가 있습니다.
# 아래의 설명을 참고하여 구현해주세요.
# 
# get(index) : linked list 의 index 번째 node의 value를 return해주세요. 값이 없으면 -1을 return해주세요.
# addAtHead(val) : linked list 의 첫 번째 요소 전에 value가 val인 node를 추가해주세요. val이 추가되면 이 node는 linked list의 첫 번째 노드가 되는 것입니다.
# addAtTail(val) : value가 val인 node를 linked list의 마지막에 추가해주세요.
# addAtIndex(index, val) : value가 val인 node를 linked list의 index node 바로 전에 추가해주세요. 만약 index가 linked list의 길이와 같다면 제일 마지막에 추가하면 됩니다. 만약 index가 길이보다 길다면, node를 추가하지 말아주세요.
# deleteAtIndex(index) : linked list의 index 번째 node를 삭제해주세요.


class Node:
  def __init__(self, value):
    self.val = value
    self.next = self.pre = None
        
  def getNext(self):
    return self.next
  

class MyLinkedList():
  
  def __init__(self):
    self.head = None
  
      
  def get(self, index):
    current = self.head
    while index > 0 :
      current = current.getNext()
      index -= 1
    return current.val
  
  
  def addAtHead(self, val):
    newNode = Node(val)
    newNode.next = self.head
    self.head = newNode
      
      
  def addAtTail(self, val):
    newNode = Node(val)
    current = self.head
    while current.next != None :
      current = current.getNext()
    
    current.next = newNode
      
  
  def addAtIndex(self, index, val):
    newNode = Node(val)
    current = self.head
    while index > 1 :
      current = current.getNext()
      index -= 1

    newNode.next = current.getNext()
    current.next = newNode
    
  
  def deleteAtIndex(self, index):
    current = self.head
    while index > 1 :
      current = current.getNext()
      index -= 1
    
    current.next = current.getNext().getNext()
