# Linux Monitor CLI

A modular Python-based command-line tool for monitoring Linux system
processes, analyzing resource usage, and managing processes efficiently.

## 🚀 Features

-   📊 View running processes
-   ⚡ Monitor CPU and memory usage
-   🛑 Kill processes by PID
-   🧩 Modular CLI architecture
-   📝 File-based logging for debugging

## 🧰 Tech Stack

-   Python
-   argparse
-   subprocess / psutil
-   Linux system utilities

## 📦 Project Structure

linux-monitor-cli/ │── main.py │── commands/ │ ├── process.py │ ├──
system.py │── utils/ │ ├── logger.py

## ▶️ Usage

python main.py list --limit 5\
python main.py stats\
python main.py kill `<pid>`{=html}

## 🧠 Learning Outcome

-   Built modular CLI architecture using Python
-   Interacted with Linux system processes and commands
-   Implemented structured logging and error handling
-   Designed reusable command-based modules

## 🔮 Future Improvements

-   Advanced filtering (CPU, memory thresholds)
-   Docker container monitoring
-   Parallel execution for faster processing
