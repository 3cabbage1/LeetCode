class Solution:
    def minWindow(self, s: str, t: str) -> str:
        fast,slow = 0,0 # 滑动窗口快慢指针
        fast_move=True # fast指针是否移动了？
        left,right=-1,-1 # 结果子串[left,right]
        t_len,s_len=0,len(s) # 当前填上t的字符个数，当前子串最短长度
        true_t_len=len(t) # t的总字符个数
        dic={} # {t中字符:子串中还差的个数}
        for i in t:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        while fast<len(s) :
            if s[fast] in dic and fast_move:
                # fast指针移动了且fast字符在dic中
                if dic[s[fast]]>0:
                    # 差的个数>0才更新，填上一个
                    t_len+=1
                # 差的个数-1（有多的时候可以为负）
                dic[s[fast]]-=1

            if t_len==true_t_len:
                # 能填完t
                # print(f"fast:{fast},slow:{slow}")
                if fast-slow+1<=s_len:
                    s_len=fast-slow+1
                    left=slow
                    right=fast
                if s[slow] in dic:
                    # 下一步移动会导致子串中少一个当前s[slow]字符
                    # 所以dic中当前s[slow]字符差的个数先+1
                    dic[s[slow]]+=1
                    if dic[s[slow]]>0:
                        # 差的数+1后如果>0代表有缺的了，所以填上的长度-1
                        t_len-=1
                # 当前slow开头的最短子串已找到，+1找下个字符开头的最短子串
                slow+=1
                if slow>fast:
                    # fast前的都核对完了，fast前移（保证fast不可能慢于slow）
                    fast+=1
                    fast_move=True
                else:
                    # 只移了slow找当前有没有更短的，fast没移
                    # 故置false，避免下步以为fast变又置了dic值
                    fast_move = False
            else:
                fast+=1
                fast_move = True
        # fast移完后slow还没移完

        if t_len==true_t_len:
            # 还可继续前移slow判断有没有更短的
            fast -= 1 # 因为fast刚移出去了
            # print("true")
            while slow<len(s):
                if t_len == true_t_len:
                    # print(f"fast:{fast},slow:{slow}")
                    if fast - slow + 1 <= s_len:
                        s_len = fast - slow + 1
                        left = slow
                        right = fast
                    if s[slow] in dic:
                        dic[s[slow]] += 1
                        if dic[s[slow]] > 0:
                            t_len -= 1
                slow += 1

        return s[left:right+1]


if __name__=="__main__":
    s=Solution()
    print(s.minWindow("ADOBECODEBANC","ABC"))
    # s.minWindow("acebbca", "abc")