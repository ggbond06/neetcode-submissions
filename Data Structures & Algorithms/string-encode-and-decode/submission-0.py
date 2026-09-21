class Solution:

    def encode(self, strs: List[str]) -> str:

        output = ""

        for item in strs:
            output += f'{len(item)}#{item}'

        return output

    def decode(self, s: str) -> List[str]:
        if s == "0#":
            return [""]

        output = []

        while len(s) > 0:
            j = 0
            while s[j] != "#":
                j+=1

            n = int(s[0:j])
            start = j+1
            end = start + n

            output.append(s[start:end])
            s = s[end:]

        return output




        
