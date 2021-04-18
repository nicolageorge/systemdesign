# systemdesign
System Design points to consider

# Distributed message queue

## Requirements

### Functional Requirements
`good place to add functional requirements`
- create_topic(name)
- publish_message(topic)
- subscribe(topic)

### Non functional requirements ( SLA - Service level agreements )
- Scalable - must handle load increase
- Highly Available - survives hardware fails and network partitioning
- Performant - single digit latency
- Durable - once submitted, data is not lost
- Extra
    - Maximum throughtput
    - Optimise costs

## Tradeofs

### Synchronous Communication
++ easy

++ faster to implement

-- hard to deal with errors

-- hard to deal with multiple requests

-- hard to deal with failing consumers

==> must have async communication

## High Level Design

# Im4 Placeholder

## Components

### DNS and Load Balancer

# Im2 Placeholder

TODO: Virtual IP Partitioning
DNS Resolves to load balancer

Load balancing techniques - Active - Passive Failover

To achieve DNS load balancing - Assign multiple A records to the same DNS name for the service

=> Requests are partitioned over several Load Balancers, over several Data Centers

=> Increase Availability

=> Increase Performance


### FrontEnd Service
- A lighweight web service
- Stateless service deployed across several data centers

#### Actions
- Request Validation
    - Ensure Required Parameters are present
    - Ensure data is not larger then permitted
    - Other Constraints

-  Authentication/Authorization
    - AUTHENTICATE -> Validate the identity of a user or a service
    - AUTHORIZE -> Determine whether or not the actor has permissions to do certain actions

- TLS(SSL) Termination
    - TLS -> Ensure data privacy and integrity
    - TLS Termination -> decrypt a request and pass unqncrypted request to the BackEnd
    - TODO: SSL on Load Balancer is Expensive
    - Termination usually handled by a TLS HTTP Proxy process that runs on the same host, not the FrontEnd service

- Server-side Encryption
    - Messages are encrypted as soon as FrontEnd receives them
    - Messages are stored in encrypted form and FrontEnd decrypts messages only when they are sent to the consumer

- Caching
    - Stores copies of source data
    - Helps reduce load on backend services
    - Increase overall system throutput and availability
    - Decrease latency
    - Stores metadata information about most used queues
    - Stores user identity information to save on calls to authentication services 

- Rate limiting (Throttling)
    - Limiting the number of requests per time unit
    - Protect the web service from being overwhelmed with requests
    - TODO: Leaky bucket algorithm

- Request dispatching
    - Responsible for all the activities associated with sending requests to backend services
        - Clients management
        - Response handling
        - Resources Isolation
    - TODO: Blukhead Pattern helps to isolate elements of application into pools so that if one fails, other will not be affected
    - TODO: Circuit Breaker pattern prevents an application from repeatedly trying to execute an operation that's likey to fail

- Request deduplication
    - May occur when a response from successful send_message request failed to reach a client
    - TODO: Lesser issue for 'At least once' delivery schematics, bigger issue for 'Exactly Once' or 'At most once' delivery semantics when we need to guarantee the message was processed at most once
    - Caching usually used to store previously seen request ids

- Usage data collection
    - Gather real-time information that can be used for audit

#### Components

# Im5 Placeholder
 
- Reverse Proxy
    - SSL Termination
        - Requests that come over HTTPS are decrypted and passed
        - Encrypting responses
    - Compression
        - gzip - compress respones before returning them back to clients(not in scope, in this case we have short messages)
            - may be usefull when dealing with large messages
    - Handles FrontEnd service slowness
        - return HTTP 503 - Service Unavailable if FrontEnd service is slow or unresponsive
- FrontEnd Service
    - can use local cache to decrease load on Metadata Service, e.g. LRU Cache
    - Responsible for writing log data to local data, other components listed below handle processing
        - Who, when made requests to specific API
        - number of requests, errors, successes

- Service logs agent
    - aggregate service logs
- Metrics Agent
    - aggregate metrics
- Audit logs agent
    - analyze audit trail



### Metadata Service

- A caching layer between FrontEnd and persistent storage
- Many Reads, little writes
- Strong consistency is prefered but not required
- provides separation of concerns
- simplifies maintenance and ability to make changes
- provides easy access through an API

# Im3 Placeholder

# Im 6 Placeholder

### Temporary Storage
- Fast, Highly Available, Scalable
- Guarantees data persistance, can store messages for days to handle unavailable subscriber

# Im7

- Can we use a database?
    - Yes, SQL or NoSQL? ( talk about tradeofs )
        - no complex queries/datamodel
        - no ACID
        - do not use storage for analytics/data warehousing
        - easily scaled for writes and reads
        - highly available
        - tolerate network partitions
            - NoSQL
    - Choosing specific NoSQL type?
        - Messages are short
        - do not need relationships between messages
            - do not need document store
        - -> Column or key-value database types ( Cassandra, DynamoDB )

- In Memory Storage
    - Yes, as long as persistance is suported
        - redis

- Message queues
    - Yes, kind of exactly what we need
    - Apache Kafka, Amazon SQS

- Stream processing platforms
    - pros / cons
    - Apache Kafka, Amazon Kinesis


### Sender Component
- Data retrieval
- Processing
- Sending Results in a fan-out manner ( Messages are sent to multiple destinations in parallel )






### What else is important
- Queue creation and deletion
    - API
    - Carefull with deletion, maybe only CLI
- Message deletion
    - Do not delete right after consumation
    - Keep track of offset / Have cleaning job - Apache Kafka
    - Mark messages as invisible, they can not be seen. Client needs to call DeleteMessage. If message is not deleted, it will become visible again - Amazon SQS
- Message Replication -> Achieve Message durability
    - Syncronously
        - When backend host receives new message, it blocks the request untill all duplication is done
        - ++ Has high durability
        - -- Has high latency 
    - Async
        - Response returned as soon as message is stored on first host, replication is done afterwards
        - ++ Has low latency
        - -- Does not guarantee that message survives backend host failures
- Message Delivery Semantics
    - At least once
        - Messages are never lost and can be redelivered
        - Basically the way to go
    - At most once
        - Messages can be lost and are never redelivered
    - Exactly once
        - Message delivered once and exactly once
        - Harder to implement because of failures to deliver, replication fail, consumers may fail to retrieve the message
- Push VS Pull
    - Pull easier to implement
- FIFO
    - Oldest message always processed first
    - Hard to maintain a certain order
- Security
    - Messages are encrypted over SSL/TLS to protect messages in transit
    - Encrypt messages on backend host
- Monitoring
    - Monitor components
    - Provide visibility into customer experience
    - Monitor health of queue system
    - Emit metrics and log data
    - setup alerts
    - customers can setup dashboards

SLA Reevaluation
- Scalable
    - Yes, all components are scalable, when load increases -> scale horizontally
- Highly Available
    - Yes, no single points of failures
    - Components deployed over several data centers
    - Individual hosts may die, partitions can happen
- Performant
    - Depends on implementation, hardware, network setup
- Durable
    - Replicate data while storing
    - Messages are not lost


