class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = {}
        domains_count = []
        for line in cpdomains:
            count = int(line.split(' ')[0])
            domain_name = line.split(' ')[1]
            split_domain_names = domain_name.split('.')
            for i in range(len(split_domain_names)):
                domain = '.'.join(split_domain_names[i:])
                d[domain] = d.get(domain, 0) + count
        for domain_name, count in d.items():
            domains_count.append(str(count) + ' ' + domain_name.encode('ascii'))
        return domains_count
        
"""
Input: 
["900 gmail.mail.com", "50 yah.com", "1 inteli.mail.com", "5 wikipedia.org"]
Output: 
["901 mail.com","50 yah.com","900 gmail.mail.com","5 wikipedia.org","5 org","1 inteli.mail.com","951 com"]
Explanation: 
We will visit "gmail.mail.com" 900 times, "yah.com" 50 times, "inteli.mail.com" once and "wiki.org" 5 times. 
For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.
"""
