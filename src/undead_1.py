from tool import tool
import win32con
import win32process
import win32api
import time

OFFSET = 0xEC
PROCESS_ALL_ACCESS = win32con.PROCESS_ALL_ACCESS

process_pid = tool.Getpid("ac_client")
process_base_addr = tool.get_base_addr("ac_client")

OpenProcess = win32api.OpenProcess
CloseHandle = win32api.CloseHandle
ReadProcessMemory = win32process.ReadProcessMemory
WritePocessMemory = win32process.WriteProcessMemory

process = OpenProcess(PROCESS_ALL_ACCESS, False, process_pid)

if process:
    hp = 100
    pointer_start = process_base_addr + 0x0017E0A8
    pointer_start : bytes = ReadProcessMemory(process, pointer_start, 4)
    pointer_start = int.from_bytes(pointer_start, "little")
    while True:
        WritePocessMemory(process, pointer_start + OFFSET, hp.to_bytes(4, "little"))
        time.sleep(0.5)
    CloseHandle(process)
else:
    print("프로세서 열기 실패함")