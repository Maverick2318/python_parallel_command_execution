# python_parallel_command_execution
An example of using the asyncio library to write concurrent execution of Linux commands.


Example output:

C02VQ1S6HTDD:python_parallel_command_execution nsiddiq$ ./parallel_cmd.py

['ls /zzz' exited with 1]

[stderr]

ls: /zzz: No such file or directory


Started at 16:13:07

['sleep 1; echo "hello"' exited with 0]

[stdout]

hello

['sleep 2; echo "world"' exited with 0]

[stdout]

world


Finished at 16:13:09
