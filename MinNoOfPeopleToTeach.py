QUESTION:On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

You are given an integer n, an array languages, and an array friendships where:

There are n languages numbered 1 through n,
languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.

class Solution:
    def common(self, languages, u, v):
        for a in languages[u]:
            for b in languages[v]:
                if a == b:
                    return True
        return False

    def minimumTeachings(self, n, languages, friendships):
        st = set()
        for u, v in friendships:
            if not self.common(languages, u - 1, v - 1):
                st.add(u)
                st.add(v)

        if not st:
            return 0

        mpp = {}
        maxi = float("-inf")
        for person in st:
            for lang in languages[person - 1]:
                mpp[lang] = mpp.get(lang, 0) + 1
                maxi = max(maxi, mpp[lang])

        return len(st) - maxi

if __name__ == "__main__":
    sol = Solution()

    n = 3
    languages = [[2], [1, 3], [1, 2]]
    friendships = [[1, 2], [1, 3], [2, 3]]

    print("Minimum Teachings:", sol.minimumTeachings(n, languages, friendships))
