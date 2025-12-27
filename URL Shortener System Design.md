# URL Shortener System Design - Two‑Page Summary
## 1. Core Principles
- **Uniqueness** - each short code must map to exactly one long URL. 
- **Low Latency** - redirects must complete in a few milliseconds. 
- **Persistence & Durability** - mappings must survive failures for years.
- **Scalability** - billions of reads/writes; horizontal scaling required. 
- **Security & Trust** - block malicious URLs, prevent abuse.
- **Extensibility** - support analytics, custom domains, expiration, etc.

## 2. High‑Level Architecture

```mermaid
graph TB
    %% Client Layer - User Interaction Points
    subgraph "Client Layer"
        U[User Browser]
        M[Mobile Apps]
        API[API Clients]
    end
    
    %% Load Balancing & Edge Layer
    subgraph "Edge & Load Balancing"
        DNS[DNS]
        CDN[CDN Edge]
        LB[Load Balancer]
    end
    
    %% API Service Layer
    subgraph "API Service Layer"
        direction LR
        AS[API Gateway]
        RS[Redirect Service]
        SS[Shortening Service]
    end
    
    %% Core Business Logic
    subgraph "Core Services"
        CG[Code Generator]
        VD[Validator]
        NM[Normalizer]
    end
    
    %% Caching Layer
    subgraph "Caching Layer"
        RC[Redis Cluster]
        MC[Memcached]
        ECC[Edge Cache]
    end
    
    %% Storage Layer
    subgraph "Storage Layer"
        direction TB
        DB[(Primary DB)]
        RSDB[(Replica DB)]
        CS[(Cold Storage)]
        WAL[Write-ahead Log]
    end
    
    %% Analytics Pipeline
    subgraph "Analytics Pipeline"
        AL[Analytics Logger]
        KF[Kafka Stream]
        DW[Data Warehouse]
        ES[Elasticsearch]
    end
    
    %% Monitoring & Observability
    subgraph "Monitoring & Observability"
        MG[Monitoring]
        ALM[Alert Manager]
        LOG[Log Aggregation]
    end
    
    %% Security Layer
    subgraph "Security Layer"
        BL[Blacklist Service]
        RL[Rate Limiter]
        CAP[CAPTCHA]
        AUTH[Auth Service]
    end
    
    %% External Services
    subgraph "External Services"
        THREAT[Threat Intelligence]
        GEO[GeoIP Service]
    end
    
    %% ==================== FLOWS ====================
    
    %% Client to Edge Flow
    U --> DNS
    M --> DNS
    API --> DNS
    
    DNS --> CDN
    CDN --> LB
    
    %% API Request Flow
    LB --> AS
    
    %% Shortening Flow (Write Path)
    AS --> SS
    SS --> VD
    SS --> NM
    SS --> CG
    SS --> AUTH
    
    VD --> BL
    VD --> THREAT
    
    CG --> DB
    SS --> DB
    
    %% Redirect Flow (Read Path)
    RS --> RC
    RC -->|Cache Miss| DB
    RS --> ECC
    
    %% Analytics Flow
    RS --> AL
    SS --> AL
    AL --> KF
    KF --> DW
    KF --> ES
    
    %% Monitoring Flow
    MG --> DB
    MG --> RC
    MG --> AS
    MG --> RS
    MG --> AL
    
    %% Security Flow
    SS --> RL
    SS --> CAP
    RS --> RL
    
    %% Storage Replication
    DB --> RSDB
    DB --> CS
    DB --> WAL
    
    %% Geo Enrichment
    AL --> GEO
    
    %% Alerting
    MG --> ALM
    LOG --> ALM
    
    %% Styling for visual clarity
    style U fill:#e1f5fe
    style M fill:#e1f5fe
    style API fill:#e1f5fe
    
    style DNS fill:#e0f2f1
    style CDN fill:#e0f2f1
    style LB fill:#fff3e0
    
    style AS fill:#f3e5f5
    style RS fill:#f3e5f5
    style SS fill:#f3e5f5
    
    style CG fill:#fff9c4
    style VD fill:#fff9c4
    style NM fill:#fff9c4
    
    style RC fill:#e8f5e8
    style MC fill:#e8f5e8
    style ECC fill:#e8f5e8
    
    style DB fill:#fce4ec
    style RSDB fill:#fce4ec
    style CS fill:#f5f5f5
    style WAL fill:#fff3e0
    
    style AL fill:#ffe0b2
    style KF fill:#ffe0b2
    style DW fill:#ffe0b2
    style ES fill:#ffe0b2
    
    style MG fill:#e1f5fe
    style ALM fill:#ffccbc
    style LOG fill:#e1f5fe
    
    style BL fill:#ffcdd2
    style RL fill:#ffcdd2
    style CAP fill:#ffcdd2
    style AUTH fill:#ffcdd2
    
    style THREAT fill:#f5f5f5
    style GEO fill:#f5f5f5
```

### Architecture Components Breakdown

**Client & Edge Layer**
- **DNS**: Geo-routing and load distribution
- **CDN**: Global edge caching for static content
- **Load Balancer**: Distributes traffic across API servers

**API Service Layer**
- **API Gateway**: Single entry point with rate limiting
- **Redirect Service**: Optimized for high-throughput GET requests
- **Shortening Service**: Handles URL validation and code generation

**Core Business Logic**
- **Code Generator**: Creates unique short codes (Hash/ID/Random)
- **Validator**: Syntax checks, blacklist validation
- **Normalizer**: Canonicalizes URLs for consistency

**Caching Layer**
- **Redis Cluster**: Hot URL mappings (sub-millisecond)
- **Memcached**: Application-level cache for hot keys
- **Edge Cache**: CDN-level caching for global performance

**Storage Layer**
- **Primary DB**: Key-value store for mappings
- **Replica DB**: Multi-region failover
- **Cold Storage**: Archived inactive links
- **WAL**: Write-ahead logging for durability

**Analytics Pipeline**
- **Analytics Logger**: Async event collection
- **Kafka**: Event streaming queue
- **Data Warehouse**: Clickstream storage
- **Elasticsearch**: Query and search capabilities

**Monitoring & Observability**
- **Monitoring**: Metrics collection (Grafana/Prometheus)
- **Alert Manager**: PagerDuty integration
- **Log Aggregation**: ELK stack for troubleshooting

**Security Layer**
- **Blacklist Service**: Threat database integration
- **Rate Limiter**: IP-based abuse prevention
- **CAPTCHA**: Bot protection
- **Auth Service**: API keys and OAuth

**External Services**
- **Threat Intelligence**: Phishing/malware databases
- **GeoIP Service**: Location enrichment for analytics

## 6. Storage Layer
**Requirements** Fast reads/writes.Durability.High availability.Billions of rows.Efficient indexing

### Options
- **SQL** - simple, consistent, but harder to scale horizontally.
- **NoSQL** - Cassandra, DynamoDB, MongoDB; highly scalable.
- **Hybrid** - SQL for writes, NoSQL/cache for reads.

### Techniques
- Primary key = short code → O(1) lookups. Sharding by code prefix. Cold storage for inactive links. WAL, snapshots, multi‑region replication.

## 7. Caching Strategies
- **In‑Memory Cache** (Redis/Memcached) for hot URLs.
- **Application Cache** for ultra‑hot keys.
- **CDN Edge Caching** for global traffic.

### Eviction Policies 
LRU, LFU, TTL‑based.
### Challenges
Cache invalidation.Hot key overload → use consistent hashing

## 8. Scalability Challenges
- **Short Code Generation at Scale** - Avoid centralized bottlenecks; use distributed ID generators.
- **Database Scalability** - SQL limits → move to NoSQL or sharded clusters.
- **Caching Infrastructure** - Redis clustering, sharding.
- **Traffic Spikes** - Auto‑scaling redirect servers; pre‑cache viral links.
- **Multi‑Region Scaling** - Geo‑replication, Anycast routing, DNS load balancing.
- **Storage Growth** - Partitioning, cold storage, TTL for expired links.

## 9. Fault Tolerance & Reliability
- Replication across regions. Cache cluster failover. Load balancing across redirect servers. Graceful degradation (redirects still work even if analytics fail). Disaster recovery: snapshots, backups, hot standbys.

## 10. API & Service Design
### Essential Endpoints
- `POST /shorten` - create short link. 
- `GET /{shortCode}` - redirect. 
- `GET /stats/{shortCode}` - analytics. 
- `DELETE /{shortCode}` - expire/remove link.

### Principles
- RESTful design.Rate limiting.Authentication for bulk operations.Consistent error handling

### Microservices Split
- Shortening service.Redirect service.Analytics service

## 11. Security Considerations
- Block phishing/malware URLs. CAPTCHA for bot protection. Rate limiting abusive clients. User authentication for custom links. Protect analytics data.

## 12. Analytics & Monitoring
### Analytics
- Click counts.Geo distribution.Device type.Referrer tracking

### System Monitoring
- Latency.Error rates.Traffic spikes.Cache hit ratio
