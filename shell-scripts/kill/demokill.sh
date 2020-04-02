
# To look for the process runnign in linux
ps -ef



killall [process name]


The kill command terminates individual processes as specified by their PID.

kill [PID]


 ps aux | grep "emacs"



sudo kill -9 process_id_1 process_id_2 process_id_3

You can also combine the kill command the pidof command to kill all the process of a program.



Of course, you have to replace the program_name with the name of the program you want to kill.
sudo kill -9 `pidof programe_name`


if you know the name of the process, you can use the command pidof in this fashion:
$ pidof firefox
16723 16574 16445 16086 14833 14778 14476 14378


ps aux | grep -i “name of your desired program”

ps aux command returns all the running process on the system. And the grep afterwards shows the line which matches with the program name. 



From the terminal, ps -ef will list all the processes. See man ps. See man kill, man 2 kill, man  killall, man nice, man pkill, man renice, man 7 signal, and man skill to mess with processes. However, simply killing a process that you think is useless may be a mistake. The system might restart the process, or something you depend on might depend on the process you killed. Learn what the processes do, and look at /etc/init/ and /etc/init.d, /etc/rc?.d, man service to see how processes are started by the system.

Or from terminal you can use

ps aux | less

To view every process:

ps -A or ps -e

All processes running by a user:

ps -u username

To kill a process, either find the process name and type:

kill -9 processname

or kill the process ID (PID):

kill pid

Stop/suspend a process:

ctrl-z






There is also the tool "htop". It is like "top", but has lots of other capabilities.

In a terminal enter:

sudo apt install htop



My main tool here is top

type top at the command line in a terminal window

You'll get a list of the process that are running, listed by cpu usage. Wait a few seconds for it to gather more stats before proceeding.



