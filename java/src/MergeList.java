class ListNode{
    int val;
    ListNode next;
    ListNode(int x){
        val = x;
    }
}


public class MergeList {
    public static ListNode mergeTwoLists(ListNode l1, ListNode l2){
        if(l1 == null && l2 == null){
            return null;
        }else if(l1 == null){
            return l2;
        }else if(l2 == null){
            return l1;
        }
        ListNode head;
        ListNode tail;
        if(l1.val <= l2.val){
            head = l1;
            tail = l1;
            l1 = l1.next;
        }else{
            head = l2;
            tail = l2;
            l2 = l2.next;
        }

        while(l1 != null && l2 != null){
            //ListNode tmp;
            if(l1.val < l2.val){
                tail.next = l1;
                tail = l1;
                l1 = l1.next;
                //continue;
            }else{
                tail.next = l2;
                tail = l2;
                l2 = l2.next;
                //continue;
            }
        }

        while(l1 != null){
            tail.next = l1;
            tail = l1;
            l1 = l1.next;
        }

        while(l2 != null){
            tail.next = l2;
            tail = l2;
            l2 = l2.next;
        }

        return head;
    }

    public ListNode deleteDuplicates(ListNode head){
        while(head!=null) {
            if (head.next.val == head.val) {
                head.next = head.next.next;
            }
            head = head.next;
        }

        return head;
    }
    public static void main(String[] args) {


    }
}
