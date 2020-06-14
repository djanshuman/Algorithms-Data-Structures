// Create the below linked list:
// myLinkedList = {
//   head: {
//     value: 10
//     next: {
//       value: 5
//       next: {
//         value: 16
//         next: null
//       }
//     }
//   }
// };
//1->10->5->16
//1->10->99->5->16

class LinkedList {
  constructor(value) {
    this.head = {
      value: value,
      next: null
    };
    this.tail = this.head;
    this.length = 1;
  }
  append(value) {
    //Code here
    const newNode={
      value:value,
      next:null
    };
    this.tail.next=newNode;
    this.tail=newNode;
    this.length++;
    return this;
    
  }
  prepend(value){
    const newnode={
      value:value,
      next:null
    };
    newnode.next=this.head;
    this.head=newnode;
    this.length++;
    return this;
  }
  printList(){
    const array=[]
    let currentValue=this.head
    while(currentValue!= null ){
      array.push(currentValue.value);
      currentValue=currentValue.next;
    }
    return array;
  }
  insert(index,value){
    //Check
    if(index ===0){
      return this.prepend(value);
    }
    if(index >= this.length){
      return this.append(value);
    }
    const newnode={
      value:value,
      next:null
    };
    const leader= this.TraverseToIndex(index-1);
    let holdingPointer=leader.next;
    leader.next=newnode;
    newnode.next=holdingPointer;
    this.length++;
    return this.printList();
  }
  TraverseToIndex(index){
    let counter=0;
    let currentValue=this.head
    while(counter!=index){
      currentValue=currentValue.next;
      counter++;
    }
    return currentValue;
  }
  remove(index){
    const leader=this.TraverseToIndex(index-1);
    let holdingPointer=leader.next.next;
    leader.next=holdingPointer;
    this.length--;
    return this.printList();
  }
}
let myLinkedList = new LinkedList(10);
myLinkedList.append(5);
myLinkedList.append(16);
console.log(myLinkedList)
myLinkedList.prepend(1);
console.log(myLinkedList)
myLinkedList.printList();
myLinkedList.insert(2,99);
myLinkedList.insert(100,990);
myLinkedList.printList();
myLinkedList.remove(5);
myLinkedList.insert(0,69);
myLinkedList.printList();

