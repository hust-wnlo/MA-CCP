





# # TODO xxxxxxx模版



# ID_list = ["bert_p.trace", "gapbs_page_rank_p.trace", "splash_radiosity_p.trace", "xz_p.trace", "ycsb_f_p.trace"]
# # ID_list = ["bert_p_small.trace"]


# for ID_value in ID_list:
#     ID = ID_value
    
#     path = "/home/zy/data/Trace/memory_traces/%s" % (ID)
#     fp = open(path, "r")
    

    
#     for eachline in fp:
#         line = eachline[:-1].split(" ")
#         time = int(line[0])  # ns
#         id = int(line[1])  # ID of the trace
#         lba = int(line[2]) // 64  # bytes
#         size = int(line[3])  # *8 bytes
#         RW = int(line[4])  # 0 is write, 1 is read



#     fp.close()














# for ID_value in ID_list:
#     ID = ID_value
    
#     path = "/home/zy/data/Trace/memory_traces/%s" % (ID)
#     fp = open(path, "r")

#     id_set, size_set, RW_set = set(), set(), set()
#     num, num_R, num_W = 0, 0, 0

#     print(ID)
#     for eachline in fp:
#         line = eachline[:-1].split(" ")
#         lba = int(line[2])  # bytes
#         size = int(line[3])  # *8 bytes
#         RW = int(line[4])  # 0 is write, 1 is read
        
#         num += 1
#         if RW == 1:
#             num_R += 1
#         elif RW == 0:
#             num_W += 1
        
#         id_set.add(id)
#         if lba % 64 != 0:
#             print("lba: ", lba)
#         size_set.add(size)
#         RW_set.add(RW)
    
#     print(num, num_R, num_W, round(num_W / num * 100, 6))
#     print(id_set)
#     print(size_set)
#     print(RW_set)
        
        
        
        
        
        

# ID_list = ["bert_p.trace", "gapbs_page_rank_p.trace", "splash_radiosity_p.trace", "xz_p.trace", "ycsb_f_p.trace"]
# # ID_list = ["bert_p_small.trace"]


# for ID_value in ID_list:
#     ID = ID_value
    
#     path = "/home/zy/data/Trace/memory_traces/%s" % (ID)
#     fp = open(path, "r")
    
#     rand_request_num = 32
#     all_list, R_list, W_list = [0 for _ in range(rand_request_num)], [0 for _ in range(rand_request_num)], [0 for _ in range(rand_request_num)]
#     num_all, num_R, num_W = 0, 0, 0
#     rand_all, rand_R, rand_W = 0, 0, 0
#     delta = 16  # *64   8对应于512B  16对应于1024B
    
#     for eachline in fp:
#         line = eachline[:-1].split(" ")
#         lba = int(line[2]) // 64  # bytes
#         # size = int(line[3])  # *8 bytes
#         RW = int(line[4])  # 0 is write, 1 is read
        
#         num_all += 1
#         if RW == 1: num_R += 1
#         else: num_W += 1

#         flag_rand = True        
#         for i in all_list:
#             if ee <= delta:
#                 flag_rand = False
#                 break
#         if flag_rand == True:
#             rand_all += 1
#         del all_list[0]
#         all_list.append(lba)
        
#         if RW == 1:
#             flag_rand = True        
#             for i in R_list:
#                 if ee <= delta:
#                     flag_rand = False
#                     break
#             if flag_rand == True:
#                 rand_R += 1
#             del R_list[0]
#             R_list.append(lba)
#         else:
#             flag_rand = True        
#             for i in W_list:
#                 ee = abs(i - lba)
#                 if ee <= delta:
#                     flag_rand = False
#                     break
#             if flag_rand == True:
#                 rand_W += 1
#             del W_list[0]
#             W_list.append(lba)
#     fp.close()
#     print(ID, str(round(rand_all / num_all, 6)), str(round(rand_R / num_R, 6)), str(round(rand_W / num_W, 6)))







# file = open("Result.csv", "a+")

# import numpy as np
# import math

# ID_list = ["bert_p.trace", "gapbs_page_rank_p.trace", "splash_radiosity_p.trace", "xz_p.trace", "ycsb_f_p.trace"]
# ID_list = ["gapbs_page_rank_p.trace"]

# cdf_time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 
#             1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000,
#             100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 
#             1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 
#             10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 80000000, 90000000, 
#             100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000, 
#             1000000000, 2000000000, 3000000000, 4000000000, 5000000000, 6000000000, 7000000000, 8000000000, 9000000000, 
#             10000000000, 20000000000, 30000000000, 40000000000, 50000000000, 60000000000, 70000000000, 80000000000, 90000000000, 
#             100000000000, 200000000000, 300000000000, 400000000000, 500000000000, 600000000000, 700000000000, 800000000000, 900000000000]  # max=900s
# cdf_time = cdf_time[::-1]
# cdf_RR = [0 for _ in range(len(cdf_time))]
# cdf_RW = [0 for _ in range(len(cdf_time))]

# for ID_value in ID_list:
#     ID = ID_value
#     path = "/home/zy/data/Trace/memory_traces/%s" % (ID)
#     fp = open(path, "r")

#     obj = dict()
#     rw = {'RR': 0, 'RW': 0, 'WW': 0, 'WR': 0}

#     for eachline in fp:
#         line = eachline[:-1].split(" ")
#         address = int(line[2]) // 64  # bytes
#         time = int(line[0])  # ns


        
#         if address in obj:
#             flag = RW + obj[address][0]
#             rw[flag] += 1

#             if flag == 'RR':
#                 tt = (time - obj[address][1])
#                 for i, data in enumerate(cdf_time):
#                     if tt < data:
#                         cdf_RR[i] += 1
#                     else:
#                         break
#             elif flag == 'RW':
#                 for i, data in enumerate(cdf_time):
#                     if tt < data:
#                         cdf_RW[i] += 1
#                     else:
#                         break
#             elif flag == 'WW':
#                 tt = (time - obj[address][1])
#                 for i, data in enumerate(cdf_time):
#                     if tt < data:
#                         cdf_WW[i] += 1
#                     else:
#                         break
#             elif flag == 'WR':
#                 for i, data in enumerate(cdf_time):
#                     if tt < data:
#                         cdf_WR[i] += 1
#                     else:
#                         break

#         obj[address] = (RW, time)

#     fp.close()

#     print(ID, rw['RR'], rw['RW'], rw['WW'], rw['WR'])

#     file.write(str(ID) + ',' + str(rw['RR']) + ',' + str(rw['RW']) + ',' + str(rw['WW']) + ',' + str(rw['WR']) + "\n")
#     file.flush()

# ss = ""

# print(cdf_RR[::-1])
# print(cdf_RW[::-1])
# print(cdf_WW[::-1])
# print(cdf_WR[::-1])


# ss = ss[:-1] + "\n"
# for i in cdf_RW[::-1]:
#     ss += str(i) + ","
# ss = ss[:-1] + "\n"
# for i in cdf_WW[::-1]:
#     ss += str(i) + ","
# ss = ss[:-1] + "\n"
# for i in cdf_WR[::-1]:
#     ss += str(i) + ","
# ss = ss[:-1] + "\n"

# file.write(ss)
# file.flush()

# file.close()
        
        
        
        
        











ID_list = ["ycsb_f_p.trace"]


for ID_value in ID_list:
    ID = ID_value
    
    path = "/home/zy/data/Trace/memory_traces/%s" % (ID)
    fp = open(path, "r")
    
    obj = dict()
    obj_R, obj_W = dict(), dict()
    fre = [0 for _ in range(500000)]
    R_fre, W_fre = [0 for _ in range(500000)], [0 for _ in range(500000)]

    
    for eachline in fp:
        line = eachline[:-1].split(" ")
        # time = int(line[0])  # ns
        # id = int(line[1])  # ID of the trace
        lba = int(line[2]) // 64  # bytes
        # size = int(line[3])  # *8 bytes
        RW = int(line[4])  # 0 is write, 1 is read
        
        if lba in obj.keys():
            obj[lba] += 1
        else: obj[lba] = 1
        
        if RW == 1:
            if lba in obj_R.keys():
                obj_R[lba] += 1
            else: obj_R[lba] = 1
        else:
            if lba in obj_W.keys():
                obj_W[lba] += 1
            else: obj_W[lba] = 1
    
    for i in obj.keys():
        fre[obj[i]] += 1
    for i in obj_R.keys():
        R_fre[obj_R[i]] += 1
        
        
    for i, data in enumerate(fre):
        if data != 0:
            print(i, data)
    print('*' * 30)
    
    for i, data in enumerate(R_fre):
        if data != 0:
            print(i, data)
    print('*' * 30)
    
    for i, data in enumerate(W_fre):
        if data != 0:
            print(i, data)
    print('*' * 30)

    fp.close()













