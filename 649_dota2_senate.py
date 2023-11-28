class Solution:
    """
    author: hongpei
    date: 2023/11/25
    """
    def predictPartyVictory(self, senate: str) -> str:
        
        ss = list(senate)

        r_cnt = 0
        d_cnt = 0
        while(len(ss) > 1):
            cur_len = len(ss)
            i = 0
            while i < cur_len:
                if r_cnt and ss[i] == "D":
                    ss.pop(i)
                    r_cnt -= 1
                    cur_len -= 1
                    continue
                
                if d_cnt and ss[i] == "R":
                    ss.pop(i)
                    d_cnt -= 1
                    cur_len -= 1
                    continue

                if ss[i] == "R":
                    r_cnt += 1

                elif ss[i] == "D":
                    d_cnt += 1

                if r_cnt == len(ss) or d_cnt == len(ss):
                    return "Radiant" if ss[0] == 'R' else "Dire"
                    
                i += 1
                
        return "Radiant" if ss[0] == 'R' else "Dire"