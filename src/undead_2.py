from tool import tool
import win32con
import win32process
import win32api
import time

PROCESS_ALL_ACCESS = win32con.PROCESS_ALL_ACCESS

nop_code = b'\x90\x90\x90\x90\x90\x90'
org_code = None

process_name = "ac_client"

process_pid = tool.Getpid(process_name)
process_base_addr = tool.get_base_addr(process_name)

OpenProcess = win32api.OpenProcess
CloseHandle = win32api.CloseHandle
ReadProcessMemory = win32process.ReadProcessMemory
WritePocessMemory = win32process.WriteProcessMemory

# 0x00084499
process = OpenProcess(PROCESS_ALL_ACCESS, False, process_pid)
if process:
    target_addr = process_base_addr + 0x00084499
    org_code : bytes = ReadProcessMemory(process, target_addr, 6)
    flag = False
    while True:
        if win32api.GetAsyncKeyState(win32con.VK_F8) & 0x8000:
            flag = not flag
            if flag:
                WritePocessMemory(process, target_addr, nop_code)
                print("적용")
            else:
                WritePocessMemory(process, target_addr, org_code)
                print("해제")
            time.sleep(1)
        if win32api.GetAsyncKeyState(win32con.VK_F9) & 0x8000:
            print("종료")
            CloseHandle(process)
            break


