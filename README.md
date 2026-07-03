# MA-CCP
This file contains three components of the MA-CCP design: analysis of memory workload, design of cache management policy, and parallelism design for the backend flash storage.
The analysis of memory workloads is performed by analyzing a series of trace files using Python code. The content of the workload is as follows:
Column      | Type     | Example            | Description
------------|----------|--------------------|-----------------------
`timestamp` | `uint64` | `6613017` | Timestamp of this operation received by server, in nanosecond
`device_id` | `uint32` | `0`                | ID of the trace
`offset`    | `uint64` | `126703644672`     | Offset of this operation, in bytes
`length`    | `uint32` | `8`             | Length of this operation, in *8 bytes
`opcode`    | `char`   | `1`                | Either of 'R' or 'W', 0 is write, 1 is read

The cache management policy is designed and implemented using a list-based approach.
The design of the flash memory backend is based on the TSU architecture implemented in MQSim.

