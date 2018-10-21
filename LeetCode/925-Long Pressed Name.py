class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        last = ""
        while typed:
            if name and name[0] == typed[0]:
                last = name[0]
                name = name[1:]
                typed = typed[1:]
            elif typed[0] == last:
                typed = typed[1:]
            else:
                return False
        return not name
