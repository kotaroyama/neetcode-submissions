class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local = email.split("@")[0]
            domain = email.split("@")[1]
            dot_removed = local.replace(".", "")
            plus_removed = dot_removed.split("+")[0]

            unique_email = f"{plus_removed}@{domain}"
            unique_emails.add(unique_email)

        return len(unique_emails)
        
            