# python_parallel_command_execution
An example of using the asyncio library to write concurrent execution of Linux commands.


Before reading the code in this repo make sure you understand the code that explains the basic concepts of the asyncio library: https://github.com/Maverick2318/python_asyncio_examples


---


Example output of parallel_cmd.py. It demonstrates that running a sleep 1 and a sleep 2 command completes in two seconds due to running them concurrently:

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


---


Example output of parallel_then_decision.py. It demonstrates that you can capture the exit codes of the individual commands then make a decision based on those codes after all the commands have completed:


C02VQ1S6HTDD:python_parallel_command_execution nsiddiq$ ./parallel_then_decision.py

Started at 16:41:51

['sleep 1 && exit 0' exited with 0]

['sleep 1 && exit 2' exited with 2]

['sleep 1 && exit 0' exited with 0]

Finished at 16:41:52

Not all commands passed.
