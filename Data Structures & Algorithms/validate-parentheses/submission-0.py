class Solution:
    def isValid(self, s: str) -> bool:
        '''
        1. create an empty stack
        2. loop through each character
        3. if its an opening bracket .append() it
        4. if its a closing bracket
            - if the stack is empty, return False
            - else, .pop() the most recent opener
            - compare with the assumed opener from the dictionary
            - if there no match return False
        5. after looping through the string check if the stack is empty
        '''

        st = []
        dict_paren = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for char in s:
            if char in "({[":
                st.append(char)
            elif char in "]})":
                if not st:
                    return False
                else:
                    last_open = st.pop()
                    if last_open != dict_paren[char]:
                        return False

        if not st:
            return True
        else:
            return False