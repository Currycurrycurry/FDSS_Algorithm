class Solution:
    def isNumber(self, s: str) -> bool:
        import re
        return re.match(r'^[\s]*[\+-]?(\.[\d]+|[\d]+(|\.[\d]*))([Ee][\+-]?[\d]+|)?[\s]*$', s) is not None