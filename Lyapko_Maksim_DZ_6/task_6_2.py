req_list = []
with open('nginx_log.txt','r',encoding='utf-8') as f:
       for line in f.readlines():
           line = line.split(' ')
           remote_addr = [line[0]]
           request_type = [line[5]]
           requested_resource = [line[6]]
           line_set = remote_addr + request_type + requested_resource
           line_set = tuple(line_set)
           req_list.append(line_set)
print(sorted(req_list))
