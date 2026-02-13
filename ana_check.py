class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        class Solution(object):
            def isAnagram(self, s, t):
                """
                :type s: str
                :type t: str
                :rtype: bool
                """
                dict_a = {}
                dict_b = {}
                key = 0
                value = -1

                if len(s) != len(t):
                    print("string is bug")

                for i in range(len(s)):
                    key = s[i]
                    if key not in dict_a:
                        dict_a[key] = 1
                    else:
                        dict_a[key] += 1

                    value = dict_a[key]

                print(dict_a.keys(), dict_a.values())

                for j in range(len(t)):
                    key = t[j]
                    if key not in dict_b:
                        dict_b[key] = 1
                    else:
                        dict_b[key] += 1
                        value = dict_b[key]

                if (dict_a != dict_b):
                    return False
                else:
                    return True

        # s, t = string of lower case
        # return true/false
        print(dict_a[key], dict_a[value])

        # for j in range(len(t)):
        #     key = t[j]
        #     if key not in dict_a:
        #         dict_b[key] = 1
        #     else:
        #         dict_b[key] = 1 + dict_b[key]
        #     value = dict_b[key]

# s, t = string of lower case
# return true/false