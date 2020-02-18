import pyshark as pys

# capFile = pys.FileCapture('test.pcapng')
capIf = pys.LiveCapture(interface='6', display_filter='icmp')

# print(capFile[0])
# capFile.close()

# 抓封包的時間
# capIf.sniff(timeout=60)
# 或使用抓封包數量
capIf.sniff(packet_count=3)

print(capIf[0])
print("*" * 50, "\n")


# 使用dir查看封包內的參數或可以使用的物件
print(dir(capIf[0]['IP']))
print("*" * 50, "\n")

print('Source IP:', capIf[0]['IP'].addr)
print(type(capIf[0]['IP'].addr))
print('Destination IP:', capIf[0]['IP'].dst)
capIf.close()
