#!/usr/bin/env python

import os
import errno


def write_pid_file(pid_file):
    pid = os.getpid()
    with open(pid_file, "w") as f:
        f.write(str(pid))
    return pid


def pid_exists(pid):
    """Check whether pid exists in the current process table."""
    if pid == 0:
        return True
    try:
        os.kill(pid, 0)
    except OSError as err:
        if err.errno == errno.ESRCH:
            # ESRCH means no such process
            return False
        elif err.errno == errno.EPERM:
            # EPERM means there is a process you can't talk to
            return True
        else:
            # Meh
            raise err
    else:
        return True


def destroy_pid_file(pid_file):
    # Clean up the PID_FILE
    if os.path.isfile(pid_file):
        os.remove(pid_file)


def ensure_pid_file(pid_file):
    return ensure_pid_file_and_start(pid_file, True)


def ensure_pid_file_and_start(pid_file, should_start):
    if os.path.isfile(pid_file):
        with open(pid_file, "r") as f:
            pid = int(f.readline())
        if not pid_exists(pid) and should_start:
            new_pid = write_pid_file(pid_file)
            print("Old pid (" + str(pid) + ") does not exist -- starting a new process with pid: " + str(new_pid))
            return new_pid
        else:
            # Return the currently running PID
            return pid
    elif should_start:
        """New Process, since there is no pid file"""
        return write_pid_file(pid_file)
    return None
