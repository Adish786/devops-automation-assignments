import psutil  # Library to access system and process utilities like CPU usage
import time    # Provides time-related functions (used for delay/sleep)

# Define the CPU usage threshold (in percentage) above which alerts will be triggered
CPU_THRESHOLD = 80  # percentage

def monitor_cpu():
    """
    Continuously monitor the CPU usage.
    If the CPU usage exceeds the predefined threshold,
    display an alert message.
    """
    print("Monitoring CPU usage...")
    try:
        while True:
            # Measure the CPU usage over a 1-second interval
            cpu_usage = psutil.cpu_percent(interval=1)

            # Check if CPU usage exceeds the defined threshold
            if cpu_usage > CPU_THRESHOLD:
                print(f"⚠️  Alert! CPU usage exceeds threshold: {cpu_usage}%")

            # Wait for 1 second before checking again
            time.sleep(1)

    except KeyboardInterrupt:
        # Handle user interruption (Ctrl+C)
        print("\n⏹️ Monitoring stopped by user.")

    except Exception as e:
        # Catch and report any other unexpected exceptions
        print(f"❌ Error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    monitor_cpu()
