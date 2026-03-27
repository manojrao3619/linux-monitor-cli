import argparse
from commands import process, system
from utils.logger import setup_logger

logger = setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Linux Monitoring CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    #list processes
    list_parser = subparsers.add_parser("list", help="List all running processes")
    list_parser.add_argument("--limit", type=int, default=10, help="Number of processes to display")

    #system stats
    subparsers.add_parser("stats", help="Show CPU and Memory usage")

    #kill process
    kill_parser = subparsers.add_parser("kill", help="Kill a process by PID")
    kill_parser.add_argument("pid", type=int, help="Process ID to kill")

    args = parser.parse_args()

    if args.command == "list":
        process.list_processes(limit=args.limit)
    elif args.command == "stats":
        system.show_stats()
    elif args.command == "kill":
        process.kill_process(args.pid)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()