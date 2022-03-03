/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) 
    {
        int carry = 0;
        ListNode* temp = new ListNode(0);
        ListNode* head = temp;
        while(l1!=NULL || l2!=NULL)
        {
            int p1 = l1 == NULL ? 0 : l1->val;
            int p2 = l2 == NULL ? 0 : l2->val;
            int val = (p1 + p2 + carry) % 10;
            carry = (int)(p1 + p2 + carry) / 10;
            temp->next = new ListNode(val);
            temp = temp->next;
            l1 = l1 == NULL ? NULL : l1->next;
            l2 = l2 == NULL ? NULL : l2->next;
        }
        if(carry)
        {
            temp->next = new ListNode(1);
        }
        
        return head->next;
    }
};