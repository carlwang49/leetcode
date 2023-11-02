from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        s = ""
        while i < len(chars):
            current_char = chars[i]
            j = i + 1
            count = 1
            while j < len(chars):
                if chars[j] == current_char:
                    count += 1
                    j += 1
                else:
                    break
            s += chars[i]
            if count > 1:
                s += str(count)
            i += count

        chars.clear()
        for char in s:
            chars.append(char)

        return len(chars)
