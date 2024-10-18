class ListNode {
    constructor(val) {
        this.val = val;
        this.next = null;
    }
}

// recursive
const mergeLists = (head1, head2) => {
    if (head1 == null && head2 == null) return null;
    if (head1 == null) return head2;
    if (head2 == null) return head1;

    if (head1.val < head2.val) {
        let next1 = head1.next;
        head1.next = mergeLists(next1, head2);
        return head1;
    } else {
        let next2 = head2.next;
        head2.next = mergeLists(head1, next2);
        return head2;
    }
};

// iterative
// const mergeLists = (head1, head2) => {
//     let dummyHead = new ListNode(null);
//     let tail = dummyHead;
//     let current1 = head1;
//     let current2 = head2;

//     while (current1 != null && current2 != null) {
//         if (current1.val < current2.val) {
//             tail.next = current1;
//             current1 = current1.next;
//         } else {
//             tail.next = current2;
//             current2 = current2.next;
//         }
//         tail = tail.next;
//     }

//     if (current1 == null) tail.next = current2;
//     if (current2 == null) tail.next = current1;

//     return dummyHead.next;
// };

// test_00

const a = new Node(5);
const b = new Node(7);
const c = new Node(10);
const d = new Node(12);
const e = new Node(20);
const f = new Node(28);
a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;
// 5 -> 7 -> 10 -> 12 -> 20 -> 28


const q = new Node(6);
const r = new Node(8);
const s = new Node(9);
const t = new Node(25);
q.next = r;
r.next = s;
s.next = t;
// 6 -> 8 -> 9 -> 25

console.log(
    mergeLists(a, q)
);

// 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28
