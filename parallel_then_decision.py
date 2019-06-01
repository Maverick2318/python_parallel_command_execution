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

    return proc.returncode

async def main():
    return await asyncio.gather(
        run_command('sleep 1 && exit 0'),
        run_command('sleep 1 && exit 2'),
        run_command('sleep 1 && exit 0'),
        return_exceptions=True)

print_time("Started")
ec_one,ec_two,ec_three=asyncio.run(main())
print_time("Finished")

if not ec_one == 0 or not ec_two == 0 or not ec_three == 0:
    print("Not all commands passed.")
