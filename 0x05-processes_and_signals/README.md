# 0x05. Processes and signals

This project delves into the realm of processes and signals in Bash scripting. The tasks encompass understanding and manipulating processes, PIDs, signals, and signal handling. The following scripts address specific requirements:

| Filename | Description |
| -------- | ----------- |
| `0-what-is-my-pid` | Displays its own PID |
| `1-list_your_processes` | Displays a list of currently running processes, showing process hierarchy |
| `2-show_your_bash_pid` | Displays lines containing the word "bash" to get the PID of your Bash process |
| `3-show_your_bash_pid_made_easy` | Displays the PID and process name of processes containing the word "bash" without using ps |
| `4-to_infinity_and_beyond` | Displays "To infinity and beyond" indefinitely with a sleep between each iteration |
| `5-dont_stop_me_now` | Stops the 4-to_infinity_and_beyond process using kill |
| `6-stop_me_if_you_can` | Stops the 4-to_infinity_and_beyond process without using kill or killall |
| `7-highlander` | Displays "To infinity and beyond" with "I am invincible!!!" on SIGTERM signal |
| `8-beheaded_process` | Kills the 7-highlander process |
| `100-process_and_pid_file` | Manages processes and PID files.                                                                         |
| `manage_my_process`        | Indefinitely writes "I am alive!" to a file |
| `101-manage_my_process`    | Bash (init) script to manage `manage_my_process`.                                                        |
| `102-zombie.c`             | Creates 5 zombie processes.                                                                             |
