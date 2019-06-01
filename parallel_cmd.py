#!/usr/bin/env python3

import asyncio
import time

def print_time(word):
    print(f"{word} at {time.strftime('%X')}")

async def run_command(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

async def main():
    await asyncio.gather(
        run_command('sleep 1; echo "hello"'),
        run_command('sleep 2; echo "world"'))

asyncio.run(run_command('ls /zzz'))
print_time("Started")
asyncio.run(main())
print_time("Finished")
