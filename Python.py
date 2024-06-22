import ping
import time

def monitor_network(hostname, interval=5):
  """Monitors network performance to a given hostname with specified interval.

  Args:
    hostname: The hostname or IP address of the target device.
    interval: The time interval (in seconds) between pings.

  Returns:
    A dictionary containing information about the latest ping:
      - success: True if ping was successful, False otherwise.
      - latency: Round-trip time of the ping in milliseconds (ms).
  """

  while True:
    response = ping.quiet_ping(hostname, timeout=1)  # Set a timeout to avoid hanging

    if response.success:
      latency = response.rtt_avg  # Get average round-trip time
      print(f"Ping to {hostname} successful! Average latency: {latency:.2f} ms")
    else:
      print(f"Ping to {hostname} failed!")

    time.sleep(interval)  # Wait before next ping

if __name__ == "__main__":
  # Example usage
  hostname = "www.google.com"  # Replace with the hostname you want to monitor
  monitor_network(hostname)

** Explanation:

Imports:
ping: This module is used to send ping requests to a host and measure response times.
time: This module is used for scheduling the time intervals between pings.

** monitor_network function:
This function takes a hostname and an optional interval parameter.
It enters an infinite loop (while True) to continuously monitor the network.

** Inside the loop:
ping.quiet_ping sends a ping request to the hostname with a one-second timeout.

** the ping is successful:
response.success is True, and response.rtt_avg provides the average round-trip time (latency) in milliseconds (ms).
The success message and latency are printed.

** If the ping fails:
A message indicating the failed ping is printed.
time.sleep(interval) pauses the loop for the specified interval before the next ping.
__main__ block (executed only when the script is run directly):

Sets the hostname variable to the target you want to monitor (replace with your desired hostname).
Calls the monitor_network function with the hostname.
