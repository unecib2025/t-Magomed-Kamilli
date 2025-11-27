#1
list1=["10.0.0.1", "10.0.0.2", "10.0.0.1", "192.168.1.10"]
a=set(list1)
print(a)
#2
set1={"root", "admin", "test"}
set1.add("hacker")
set1.remove("test")
print(set1)
#3
ports={21, 22, 23, 25}
port=22
if port in ports:
    print("Unallowed port")
#4
known={"mal.com", "bad.net"}
new={"bad.net", "xevil.org"}
new=new.difference(known)
print(new)
#5
white={"alice", "bob", "root"}
black={"root","admin"}
wb=white.intersection(black)
print(wb)
#6
systemA={"CVE-1", "CVE-2"}
systemB={"CVE-2", "CVE-3"}
uni=systemB.union(systemA)
print(uni)
#7
Admin={"read", "write", "delete"}
User={"read", "download"}
dif=Admin.symmetric_difference(User)
print(dif)
#8
all_logs=["123", "qwerty", "test", "123", "qwerty", "admin"]
unique_logs=set(all_logs)
unique_logs.discard("test")
print(unique_logs)
#9
global_ip={"10.0.0.1","10.0.0.2","192.168.1.1"}
local_ip={"10.0.0.2","10.0.0.3"}
local_ip.intersection_update(global_ip)
print(local_ip)
#10
log_list=["scan", "debug_mode", "scan", "connect", "debug_info"]
log_set=set(log_list)
for item in list(log_set):
    if "debug" in item:
        log_set.discard(item)
print(log_set)
#Вопросы
#1. Элементы множеств бывают уникальными, неупорядоченными и неизменяемыми.
#2. Нет, так как они являются изменяемыми типами данных.
#3. Они оба удаляют элемент, но при отсутствии элемента remove выдает ошибку, а discard нет.
#4. В их функциях разницы нет, они оба объединяют два множества.
#5. Симметричную разность множества, то есть элементы, которые есть только в одном из множеств, но не в обоих.
#6. Изменяет исходное множество, оставляя только элементы, которые есть и в нём, и в другом множестве.
#7. Модифицируют: add(), remove(), discard(), pop(), clear(), intersection_update(), difference_update(). Возвращают: union(), intersection(), difference(), symmetric_difference().



