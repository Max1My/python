import re

from task_6_1 import read_logs

def get_raw(raw):
    RE_RAW = re.search(r'(?P<remote_addr>\d{1,3}[\.]\d{1,3}[\.]\d{1,3}[\.]\d{1,3})\S+\s+\S+\s+\S+\s+\S[[](?P<request_datetime>\d{2}[\/]\w+[\/]\d{4}[\:]\d{2}[\:]\d{2}[\:]\d{2}\S+\s+\S[+]\d{4})[]]\S+\s+\S{2}(?P<request_type>\w{3})\S+\s+\S(?P<requested_resource>[\/]\w+[\/]\w+)\S+\s\S+\s\S(?P<response_code>\d{3})\S+\s\S(?P<response_size>\d+)',raw)
    remote_addr = RE_RAW.group('remote_addr')
    request_datetime = RE_RAW.group('request_datetime')
    request_type = RE_RAW.group('request_type')
    requested_resource = RE_RAW.group('requested_resource')
    response_code = RE_RAW.group('response_code')
    response_size = RE_RAW.group('response_size')
    all_raw = f'{remote_addr} {request_datetime} {request_type} {requested_resource} {response_code} {response_size}'
    return all_raw

logs = read_logs('nginx_log.txt')

raw_parse = []

gen = (x for x in range(len(logs)))
while True:
    try:
        for i in range(len(logs)):
            raw = str(logs[next(gen)])
            raw_parse.append(get_raw(raw))
    except AttributeError:
        continue
    except StopIteration:
        break
print(raw_parse)