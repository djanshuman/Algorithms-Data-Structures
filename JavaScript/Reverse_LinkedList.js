class LinkedList{
  constructor(value){
    this.head={
      value: value,
      next: null
    };
    this.tail=this.head;
    this.length=1;
  }
  append(value){
    const newnode={
      value:value,
      next:null
    };
    this.tail.next=newnode;
    this.tail=newnode;
    this.length++;
  }
  prepend(value){
    const newnode={
      value:value,
      next:null
    };
    newnode.next=this.head;
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
      next:null
    };
    const leader=this.traverseToIndex(index-1);
    let holdingPointer=leader.next;
    leader.next=newnode;
    newnode.next=holdingPointer;
    this.length++;
    return this.printList();
  }
  traverseToIndex(index){
    let i=0;
    let currentValue=this.head;
    while(i!=index){
      currentValue=currentValue.next
      i++;
    }
    return currentValue;
  }
  remove(index){
    if(index===0){
      let tempHolder=this.head.next;
      this.head=tempHolder;
      this.length--;
      return this.printList();
    }
    if(index==this.length){
      const leader=this.traverseToIndex(index-1);
      leader.next=null;
      this.length--;
      return this.printList();
    }

    const leader=this.traverseToIndex(index-1);
    let tempHolder=leader.next.next;
    leader.next=tempHolder;
    this.length--;
    return this.printList();
  }
  reverse(){

    if(!this.head.next){
      return this.head;
    }
    let first=this.head;
    this.tail=this.head;
    let second=first.next;
    
    while(second){
      const temp=second.next;
      second.next=first;
      first=second
      second=temp;
    }
    this.head.next=null;
    this.head=first;
    return this.printList();
    //return this;
  }

}
let myLinkedList=new LinkedList(1);
//console.log(myLinkedList)
myLinkedList.append(10);
myLinkedList.append(16)
myLinkedList.append(88)
//console.log(myLinkedList)
//myLinkedList.prepend(200);
//console.log(myLinkedList)
//myLinkedList.printList();
//myLinkedList.insert(2,98);
//myLinkedList.printList();
//myLinkedList.insert(4,8);
//myLinkedList.printList();
//console.log(myLinkedList);
//myLinkedList.printList();
myLinkedList.reverse();
//myLinkedList.remove(2);
