import subprocess
import logging

logger = logging.getLogger("linux-monitor")

def list_processes(limit=10):
    try:
        result = subprocess.run(["ps", "aux"], capture_output=True, text=True)
        lines = result.stdout.splitlines()
        # print(f"{'USER':<10} {'PID':<10} {'%CPU':<10} {'%MEM':<10} {'COMMAND'}")
        print(f"TOP {limit} PROCESSES:")
        for line in lines[:limit+1]:  # +1 to account for the header
            print(line)
        logger.info("Listed processes successfully.")
    except Exception as e:
        logger.error(f"Error listing processes: {e}")
        print(f"Error listing processes: {e}")

def kill_process(pid):
    try:
        subprocess.run(["kill", str(pid)], check=True)
        logger.info(f"Killed process with PID {pid}.")
        print(f"Process with PID {pid} has been killed.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error killing process with PID {pid}: {e}")
        print(f"Error killing process with PID {pid}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")