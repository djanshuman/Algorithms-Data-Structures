class DoublyLinkedList{
  constructor(value){
    this.head={
      value: value,
      next: null,
      prev: null
    };
    this.tail=this.head;
    this.length=1;
  }
  append(value){
    const newnode={
      value:value,
      next:null,
      prev:null
    };
    newnode.prev=this.tail;
    this.tail.next=newnode;
    this.tail=newnode;
    this.length++;
  }
  prepend(value){
    const newnode={
      value:value,
      next:null,
      prev:null
    };
  
    newnode.next=this.head;
    this.head.prev=newnode;
    this.head=newnode;
    this.length++;
  }
  printList(){
    let currentValue=this.head;
    let array=[]
    while(currentValue!=null){
      array.push(currentValue.value);
      currentValue=currentValue.next;
    }
    return array;
  }
  insert(index,value){
    if(index===0){
      return this.prepend(value);
    }
    if(index >=this.length){
      return this.append(value);
    }
    const newnode={
      value:value,
      next:null,
      prev:null
    };
    const leader=this.traverseToIndex(index-1);
    const follower=leader.next;
    newnode.prev=leader;
    leader.next=newnode;
    newnode.next=follower;
    follower.prev=newnode;
    this.length++;
    return this.printList();
  }
  traverseToIndex(index){
    let i=0;
    let currentValue=this.head;
    while(i!=index){
      currentValue=currentValue.next;
      i++;
    }
    return currentValue;
  }
  remove(index){
    if(index===0){
      let tempHolder=this.head.next;
      this.head=tempHolder;
      this.head.prev=null;
      this.length--;
      return this.printList();
    }
    if(index ==(this.length)-1){
      const leader=this.traverseToIndex(index-1);
      this.tail=leader;
      leader.next=null;
      this.length--;
      return this.printList();
    }

    const leader=this.traverseToIndex(index-1);
    let tempHolder=leader.next.next;
    leader.next=tempHolder;
    tempHolder.prev=leader;
    this.length--;
    return this.printList();
  }

}
let myLinkedList=new DoublyLinkedList(10);
//console.log(myLinkedList)
//myLinkedList.append(20);
//myLinkedList.append(9)
myLinkedList.append(20)
myLinkedList.append(30)
myLinkedList.append(66)
myLinkedList.append(89)
//myLinkedList.append(309)
//console.log(myLinkedList)
//myLinkedList.prepend(200);
//console.log(myLinkedList)
//myLinkedList.printList();
myLinkedList.insert(1,98);
//myLinkedList.printList();
//myLinkedList.insert(2,8);
//myLinkedList.append(60)
//myLinkedList.printList();
//console.log(myLinkedList);
//myLinkedList.printList();
//console.log(myLinkedList);
//myLinkedList.prepend(100);
//myLinkedList.remove(2);
//myLinkedList.printList();
//myLinkedList.remove(0);
//myLinkedList.remove(3);
console.log(myLinkedList);
myLinkedList.remove(5);
console.log(myLinkedList);
myLinkedList.printList();
