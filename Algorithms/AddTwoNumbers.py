################### Question ########################

# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

################### SOLUTION 1 ########################

# In this solution we will retrieve each number from the linkedlists, add them, and then change the sum to a linkedlist format
# since we are only traversing the linkedlists one time in all the steps,
# Time Complexity = O(n)
# And for the space complexity we are again only storing one linkedlist per number so,
# Space Complexity = O(n)

class Solution:
    def addTwoNumbers(self, num1_node, num2_node):
        num1 = self.retrieveNumber(num1_node)
        num2 = self.retrieveNumber(num2_node)
        ans = num1+num2
        ans_node = self.retrieveLinkedListHead(ans)
        return ans_node
    
    def retrieveNumber(self, num_node):
        # While traversing the linked list, keep track of the power
        power = 0
        number = 0
        # For each node, multiply it accordingly and sum it
        while num_node!=None:
            number+=num_node.val*10**power
            power+=1
            num_node = num_node.next
        return number
    
    def retrieveLinkedListHead(self, num):
        if num<10:
            head = ListNode(num%10, None)
        else:
            node = ListNode()
            head = ListNode(num%10, node)
            num = num//10
            # This flag is gonna tell us if the last digit that's left
            # is comming from a two digit number or a larger number
            less_than_100 = True
            while num//10!=0:
                less_than_100 = False
                next_node = ListNode()
                node.val = num%10
                # trunkating the number
                num = num//10
                # Only change node to next_node if more than one digit is left
                # otherwise we don't want to lose track of the node
                if num>=10:
                    node.next = next_node
                    node = next_node
            
            # the last digit
            if less_than_100:
                node.val = num
            else:
                node.next = next_node
                next_node.val = num
            
        return head

################### SOLUTION 2 ########################

# In this solution we are not retrieving the number. We will work our way through the linkedlist
# add each two digit and the borrow from the last addition and so on
# the key with linkedlist to look one slot ahead. check if the next is None or not to continue.
# since we are only traversing through the linkedlist:
# Time Complexity = O(n)
# Space Complexity = O(n)

class Solution:
    def addTwoNumbers(self, num1_node, num2_node):
        sum = num1_node.val+num2_node.val
        digit = sum%10
        borrow = sum//10
        ans_head = ListNode(digit, None)
        node = ans_head
        
        # There is at least two more digits left in both numbers
        while num1_node.next!=None and num2_node.next!=None:
            # Move to current digits to work with
            num1_node = num1_node.next
            num2_node = num2_node.next
            # Calculate the new digit
            sum = num1_node.val+num2_node.val+borrow
            digit = sum%10
            borrow = sum//10
            # Form the linkedlist
            new_node = ListNode(digit, None)
            node.next = new_node
            node = new_node

        # both numbers only have one more digit left
        if num1_node.next==None and num2_node.next==None:
            if borrow!=0:
                new_node = ListNode(borrow, None)
                node.next = new_node
        
        # num1 has only one digit left to work with
        elif num1_node.next==None:
            while num2_node.next!=None:
                # Move to current digit to work with
                num2_node = num2_node.next
                # Calculate the new digit
                sum = num2_node.val+borrow
                digit = sum%10
                borrow = sum//10
                # Form the linkedlist
                new_node = ListNode(digit, None)
                node.next = new_node
                node = new_node
            if borrow!=0:
                new_node = ListNode(borrow, None)
                node.next = new_node  
        
        # num2 has only one digit left
        else:
            while num1_node.next!=None:
                # Move to current digit to work with
                num1_node = num1_node.next
                # Calculate the new digit
                sum = num1_node.val+borrow
                digit = sum%10
                borrow = sum//10
                # Form the linkedlist
                new_node = ListNode(digit, None)
                node.next = new_node
                node = new_node
            if borrow!=0:
                new_node = ListNode(borrow, None)
                node.next = new_node 

        return ans_head
    
################### SOLUTION 2 BUT BETTER ########################

# This ones logic is the same as solution 2 but cleaner code
# It's not confusing itself with different scenarios. But "makes" them all looking like one scenario
# by adding imaginary 0s to the short number -- not literally adding.
# when it comes to it and there is no more digit, adds it with 0!

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        # Delete dummyHead
        dummyHead.next = None
        return result