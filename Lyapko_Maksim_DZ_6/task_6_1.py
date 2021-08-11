
req_list = []

IP_INDEX = 0
METHOD_INDEX = 5
URL_INDEX = 6
with open('nginx_log.txt','r',encoding='utf-8') as f:
       for line in f.readlines():
           line = line.split(' ')
           remote_addr = [line[IP_INDEX]]
           request_type = [line[METHOD_INDEX]]
           requested_resource = [line[URL_INDEX]]
           line_set = remote_addr + request_type + requested_resource
           line_set = tuple(line_set)
           req_list.append(line_set)
print(req_list)
