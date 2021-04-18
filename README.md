# systemdesign
System Design points to consider

## Distributed message queue

### Functional Requirements
`good place to add functional requirements`

### Non functional requirements ( SLA - Service level agreements )
* Scalable - must handle load increase
* Highly Available - survives hardware fails and network partitioning
* Performant - single digit latency
* Durable - once submitted, data is not lost
Extra
** Maximum throughtput
** Optimise costs


### Synchronous Communication
++ easy

++ faster to implement

-- hard to deal with errors

-- hard to deal with multiple requests

-- hard to deal with failing consumers

==> must have async communication

## IMAGE 1 PLACEHOLDER

### DNS and Load Balancer
TODO: Virtual IP Partitioning
DNS Resolves to load balancer

Load balancing techniques - Active - Passive Failover

To achieve DNS load balancing - Assign multiple A records to the same DNS name for the service

=> Requests are partitioned over several Load Balancers, over several Data Centers

	=> Increase Availability

	=> Increase Performance