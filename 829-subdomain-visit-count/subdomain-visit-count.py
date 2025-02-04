class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dicto = defaultdict(int)
        ans = []
        for pair in cpdomains:
            domains = pair.split()
            sub_doms = domains[1].split(".")
            dicto[sub_doms[-1]] += int(domains[0])
            dicto['.'.join(sub_doms[-2:])] += int(domains[0])
            if len(sub_doms)==3:
                dicto['.'.join(sub_doms)] += int(domains[0])
        for key, value in dicto.items():
            ans.append(' '.join([str(value), key]))
        return ans
            
            
