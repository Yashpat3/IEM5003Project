## Air Traffic Controller Scheduling System

### Overview
This project focuses on solving a simplified version of a scheduling problem for Air Traffic Controllers (ATCOs) employed by the Federal Aviation Authority. The objective is to efficiently assign ATCOs to shifts over a 2-week planning horizon, divided into 15-minute intervals.

### Problem Description
There are two main optimization problems addressed in this system:

#### Shift Distribution Problem
This problem aims to determine the minimum number of 8-hour and 10-hour shifts required to meet the staffing needs (rt) for each time period. It focuses solely on the distribution of shifts without building complete work schedules or permitting overtime extensions.

#### Shift Scheduling Problem
In this problem, the goal is to construct a minimum-cost collection of regular and compressed schedules to fulfill the coverage requirements for each time period. This involves creating fixed numbers of complete schedules (regular and compressed) with provisions for overtime as necessary.

### Constraints
- ATCOs can work either 10 × 8-hour shifts per schedule or 8 × 10-hour shifts per schedule.
- There must be a minimum 8-hour gap between consecutive shifts.
- Overtime can be integrated into a shift or assigned as a standalone extra shift.
- All ATCOs are assumed to be paid the same hourly rate, with overtime compensated at 1.5 times the standard rate.

### Usage
This system provides solutions for the shift distribution problem and the shift scheduling problem. Users can input staffing requirements for each time period and obtain optimal shift distributions or complete schedules that meet these requirements.

### Implementation
The system utilizes mathematical optimization techniques to solve the scheduling problems efficiently. It can be further extended to incorporate heuristic methods for generating comprehensive work schedules based on the optimal shift distributions provided.

### Note
This system focuses on optimizing shift distributions and scheduling while leaving the process of combining shifts into complete schedules to external heuristic methods.

### Contributors
- Yash J. Patel MS-IEM
- Yash Patel MS-BA&DS

### License
Gurobi Acadmic Licence

### Acknowledgments
Dr. Balasundaram Baski
Ms. Parisa Mohebbi

