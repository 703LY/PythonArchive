# definisikan vowels menjadi set dan kalimat input menjadi list, 
# lalu pake 2 pointer dari kiri dan kanan, 
# apabila bukan vowel, maka pointernya geser ke tengah. 
# kalo vowel, lakukan swap. 
# terakhir, list di append kembali menjadi string utuh.

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        sjadilist = list(s)

        vowels = set (['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O'])

        # ===cara two pointer===
        left = 0
        right = len(s) - 1

        while left < right:
            if sjadilist[left] not in vowels:
                left += 1
            elif sjadilist[right] not in vowels:
                right -= 1
            else:
                tempVowel = sjadilist[left]
                sjadilist[left] = sjadilist[right]
                sjadilist[right] = tempVowel
                left +=1
                right -=1
        return"".join(sjadilist)