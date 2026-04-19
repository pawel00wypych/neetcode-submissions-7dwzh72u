class Solution:

    def encode(self, strs: List[str]) -> str:
       encoded = ''
       for s in strs:
          encoded += '#' + str(len(s)) + '#'+ s
       return encoded
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            if s[i] == '#' and s[i+1].isdigit():
                i += 1
                len_str = ''
                while s[i] != '#':
                   len_str += s[i]
                   i += 1
                len_str = int(len_str)
                i += 1
                new_str = ''
                while len_str > 0:
                    new_str += s[i]
                    i += 1
                    len_str -= 1
                strs.append(new_str)

        return strs
                    
