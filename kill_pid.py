import os, subprocess, signal

p = subprocess.Popen(['ps', '-elf'], stdout=subprocess.PIPE)
out, err = p.communicate()
for line in out.splitlines():
    if 'merge' in line:
        pid = int(line.split()[3])
        os.kill(pid, signal.SIGKILL)
        print('killed %d' % pid)