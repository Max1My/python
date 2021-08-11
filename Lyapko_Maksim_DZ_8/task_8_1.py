import re

def email_parse(email):
    return CHECK_MAIL.match(email)

CHECK_MAIL = re.compile(r'(\w+)(\b@\w+[.]\w+)')

email = 'someone@geekbrainsru'
msg = f'wrong email: {email}'

if __name__ == '__main__':
    if CHECK_MAIL.match(email) is None:
        raise ValueError(msg)

RE_MAIL = re.search(r'(\w+)(\b@\w+[.]\w+)',email)

UserName = RE_MAIL.group(1)
domain = RE_MAIL.group(2)
email_list = {
    'username':UserName,
    'domain':domain
}
print(email_list)