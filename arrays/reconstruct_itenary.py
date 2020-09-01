import collections


class Solution:
    def visit(self, airport, targets, route):
        while targets[airport]:
            self.visit(targets[airport].pop(), targets, route)

        route.append(airport)

    # def findItinerary(self, tickets):
    #     targets = collections.defaultdict(list)
    #     for a, b in sorted(tickets)[::-1]:
    #         targets[a] += b,
    #     route = []
    #     print(targets)

    #     def visit(airport):
    #         while targets[airport]:
    #             visit(targets[airport].pop())
    #         route.append(airport)

    #     visit('JFK')
    #     return route[::-1]

    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        reversed_sorted_tickets = sorted(tickets, reverse=True)
        print(reversed_sorted_tickets)

        for a, b in reversed_sorted_tickets:
            targets[a].append(b)

        route = []
        self.visit("JFK", targets, route)
        return route[::-1]

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        ans = i = j = 0

        while j < n:

            if s[j] not in seen:
                seen.add(s[j])
                j += 1
                ans = max(ans, j-i)

            else:
                seen.remove(s[i])
                i += 1

        return ans


a = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
b = [["JFK", "SFO"], ["JFK", "ATL"], [
    "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]

c = "pwwkew"
print(Solution().lengthOfLongestSubstring(c))
