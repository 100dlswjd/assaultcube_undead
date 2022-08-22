import time
import win32api
import win32con

from class_gather.process_class import ProcessMemoryControl\

nop_code = b'\x90\x90\x90\x90\x90\x90'
org_code = None

ac_clinet_process = ProcessMemoryControl("ac_client")
target_addr = ac_clinet_process.base_addr + 0x00084499
org_code = ac_clinet_process.read(target_addr, 6)

flag = False
while True:
    if win32api.GetAsyncKeyState(win32con.VK_F8) & 0x8000:
        flag = not flag
        if flag:
            ac_clinet_process.write(target_addr, nop_code)
            print("적용")
        else:
            ac_clinet_process.write(target_addr, org_code)
            print("해제")
        time.sleep(0.5)
    if win32api.GetAsyncKeyState(win32con.VK_F9) & 0x8000:
        break
