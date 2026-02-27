  top shows you three numbers for the load average:
  load average: 1.15, 0.95, 0.75
  
  the key is understanding that load average is not a percentage.

  The "Bridge" Analogy

  The best way to understand load average is to think of your CPU as a single-lane bridge.


   * Load Average of 0.00: The bridge is empty. There are no cars (processes) wanting to cross.
   * Load Average of 1.00: The bridge is at full capacity. There's a car on the bridge at all times, but there's no traffic jam. As soon as one car
     leaves, another one immediately gets on. The system is perfectly utilized.
   * Load Average less than 1.00 (e.g., 0.50): The bridge is under-utilized. There is no traffic jam, and the bridge is empty 50% of the time.
   * Load Average greater than 1.00 (e.g., 2.00): The bridge is overloaded. There is one car on the bridge, and one car is waiting in line for the
     bridge to be free. The system is still at 100% CPU utilization, but now there is a queue of tasks that can't run.

  What Load Average Actually Measures


  The load average is a measure of the number of processes that are either currently running on the CPU or are in the run queue, ready and waiting for
  the CPU. It also includes processes stuck in an uninterruptible sleep state (usually waiting for slow disk I/O).

  So, a load average is a measure of demand for the CPU's attention.

  Answering Your Question: Can it be 100?

  Yes, absolutely.


  A load average of 100.00 on your single-core PC would mean that, on average, there is:
   * 1 process currently running on the CPU.
   * 99 other processes lined up in the queue, waiting for their turn to run.


  This indicates a system that is extremely overloaded. The "traffic jam" to use your CPU is 99 processes deep. The system would be incredibly slow
  and likely unresponsive because every process has to wait a very long time for a tiny slice of CPU time.

  The Three Numbers in top


  top shows you three numbers for the load average:
  load average: 1.15, 0.95, 0.75


  These represent the average load over the last 1 minute, 5 minutes, and 15 minutes, respectively. This helps you see trends:
   * In the example above, the load has recently increased (the 1-minute average is higher than the 15-minute average).

  A Note on Multi-Core Systems


  The interpretation of load average depends on the number of CPU cores. If you had a 4-core PC:
   * A load average of 4.00 would mean all four cores are perfectly utilized (all four "lanes" of your bridge are full).
   * A load average of 1.00 would mean the system is only 25% loaded.
   * A load average of 8.00 would mean all four cores are busy, and there are, on average, four other processes waiting in line.


  Rule of Thumb: For a healthy system, the load average should generally not exceed the number of CPU cores.
