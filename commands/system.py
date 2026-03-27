import subprocess
import logging

logger = logging.getLogger("linux-monitor")

def show_stats():
    try:
        # Get CPU usage
        cpu_result = subprocess.run(["top", "-b", "-n", "1"], capture_output=True, text=True)
        cpu_usage = [line for line in cpu_result.stdout.splitlines()][:3] 
        
        # Get Memory usage
        mem_result = subprocess.run(["free", "-h"], capture_output=True, text=True)
        mem_usage = mem_result.stdout
        
        print("CPU Usage:")
        for line in cpu_usage:
            print(line)
        # print(cpu_usage)
        print("\nMemory Usage:")
        print(mem_usage)
        logger.info("Displayed system stats successfully.")
    except Exception as e:
        logger.error(f"Error retrieving system stats: {e}")
        print(f"Error retrieving system stats: {e}")