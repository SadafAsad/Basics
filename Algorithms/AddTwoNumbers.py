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