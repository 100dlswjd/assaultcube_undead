import time

from class_gather.process_class import ProcessMemoryControl\

ac_clinet_process = ProcessMemoryControl("ac_client")

OFFSET = 0xEC

hp = 100
pointer_start = ac_clinet_process.base_addr + 0x0017E0A8
sig = ac_clinet_process.read(ac_clinet_process.base_addr, 2)

pointer_start : bytes = ac_clinet_process.read(pointer_start, 4)
pointer_start = int.from_bytes(pointer_start, "little")

while True:
    cur_hp = ac_clinet_process.read(pointer_start + OFFSET, 4)
    cur_hp = int.from_bytes(cur_hp, "little")
    print("현재 체력 : ", cur_hp)
    ac_clinet_process.write(pointer_start + OFFSET, hp.to_bytes(4, "little"))
    time.sleep(0.5)