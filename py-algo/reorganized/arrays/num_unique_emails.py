"""
Unique Emails

"""
def numUniqueEmails(emails: list[str]) -> int:
def clean_email(email: str):
            local, domain = email.split("@")
            ignore_idx = local.find('+')
            if ignore_idx >= 0:
                local = local[:ignore_idx].replace('.', '')
            else:
                local = local.replace('.', '')

            return local, domain

        email_set = set()
        for email in emails:
            local, domain = clean_email(email)
            email_set.add((local, domain))
        print(email_set)
        return len(email_set)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to numUniqueEmails
    print(numUniqueEmails([]))
