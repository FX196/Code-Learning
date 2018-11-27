class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.replace(".", "")
            if "+" in local:
                local = local[:local.find("+") + 1]
            unique.add(local + "@" + domain)
        return len(unique)
