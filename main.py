#!/usr/bin/python
# -*- coding:utf8 -*-

def main001():
    from ans import q001
    a = q001.Solution()
    print a.twoSum([2, 7, 11, 15], 9)


def main002():
    from ans import q002
    a = q002.Solution()
    print a.addTwoNumbers([2, 4, 3], [5, 6, 4])


def main007():
    from ans import q007
    print q007.Solution().reverse(-122230)


def main009():
    from ans import q009
    print q009.Solution().isPalindrome(12000021)


def main013():
    import ans.q013
    print ans.q013.Solution().romanToInt("MCMXCIV")


def main118():
    import ans.q118
    print ans.q118.Solution().generate(19)


def main136():
    import ans.q136
    print ans.q136.Solution().singleNumber([4, 1, 2, 1, 2])


def main771():
    import ans.q771
    print ans.q771.Solution().numJewelsInStones("z", "ZZ")


def main709():
    import ans.q709
    print ans.q709.Solution().toLowerCase("LOVELY")


def main807():
    import ans.q807
    print ans.q807.Solution().maxIncreaseKeepingSkyline([[3, 0, 8, 4],
                                                         [2, 4, 5, 7],
                                                         [9, 2, 6, 3],
                                                         [0, 3, 1, 0]])


def main535():
    import ans.q535
    url = "https://leetcode.com/problems/design-tinyurl"
    codec = ans.q535.Codec()
    print codec.decode(codec.encode(url))


def main832():
    import ans.q832
    print ans.q832.Solution().flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]])


def main461():
    import ans.q461
    print ans.q461.Solution().hammingDistance(1, 4)


def main804():
    import ans.q804
    print ans.q804.Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])


def main476():
    import ans.q476
    print ans.q476.Solution().findComplement(5)


def main500():
    import ans.q500
    print ans.q500.Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])


def main557():
    import ans.q557
    print ans.q557.Solution().reverseWords("Let's take LeetCode contest")


def main867():
    import ans.q867
    print ans.q867.Solution().transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def main811():
    import ans.q811
    print ans.q811.Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com",
                                               "1 intel.mail.com", "5 wiki.org"])


def main171():
    import ans.q171
    print ans.q171.Solution().titleToNumber("ZY")


def main821():
    import ans.q821
    print ans.q821.Solution().shortestToChar("loveleetcode", "e")


def main806():
    import ans.q806
    print ans.q806.Solution().numberOfLines(
        [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        , "bbbcccdddaaa")
    print ans.q806.Solution().numberOfLines(
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        "abcdefghijklmnopqrstuvwxyz"
    )


def main463():
    import ans.q463
    print ans.q463.Solution().islandPerimeter([[0, 1, 0, 0],
                                               [1, 1, 1, 0],
                                               [0, 1, 0, 0],
                                               [1, 1, 0, 0]]
                                              )


def main561():
    import ans.q561
    print ans.q561.Solution().arrayPairSum([1, 4, 3, 2])


def main693():
    #打表
    import ans.q693
    print ans.q693.Solution().hasAlternatingBits(5)
    for i in range(1, 100):
        print int(("01" * i)[1:], 2)
        print int(("10" * i), 2)
    print ([int(("01" * i)[1:], 2) for i in range(1, 20)] +
           [int(("10" * i), 2) for i in range(1, 20)])

def main258():
    import ans.q258
    print ans.q258.Solution().addDigits(123)
    import matplotlib.pyplot as plt
    x=range(1000)
    y=[]
    for i in x:
        y.append(ans.q258.Solution().addDigits(i))
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    main258()
