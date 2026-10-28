class Solution:
    def getAnagramsToStr(self, str):
        # char_list=[]
        # for i in range(26):
        #     char_list.append(0)
        # for i in str:
        #     char_list[ord(i)-ord('a')]+=1 # ord 返回字符character的真实值
        # final_str=""
        # for i in range(26):
        #     while char_list[i]!=0:
        #         final_str+=chr(ord('a')+i) # chr 将一个字符char值转为str
        #         char_list[i]-=1
        final_str = "".join(sorted(str))  # 直接对str中的字符排序再拼回顺序后的str就行，上面做的是一样的事情
        # 就是想让不同异位的str都返回同样按字母升序排序的统一字符串
        return final_str

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic = {}
        index_count = 0
        result = []
        for str in strs:
            tem_str = self.getAnagramsToStr(str)
            if tem_str in dic:
                # print(f"dic[tem_str]:{dic[tem_str]},str:{str}")
                result[dic[tem_str]].append(str)
            else:
                # print(f"index_count:{index_count},str:{str},{[str]}")
                result.append([str])
                # print(f"result:{result}")
                dic[tem_str] = index_count  # python dict字典键key只能选不可变对象做
                index_count += 1
        return result


if __name__ == '__main__':
    # print(Solution().getAnagramsToStr("eat"))
    print(Solution().groupAnagrams(["ddddddddddg", "dgggggggggg"]))
