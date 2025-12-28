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
graph LR
    %% User Layer
    subgraph Users[Users]
        U[User Browser]
        M[Mobile Apps]
    end
    
    %% Edge & Delivery Layer
    subgraph EdgeLayer[Edge Layer]
        DNS[DNS]
        CDN[CDN Edge]
        LB[Load Balancer]
    end
    
    %% API Services
    subgraph "API Services"
        API[API Gateway]
        RS[Redirect Service]
        SS[Shortening Service]
    end
    
    %% Core Storage & Cache
    subgraph DataLayer[Data Layer]
        RC[Redis Cache]
        DB[(Database)]
    end
    
    %% Supporting Services
    subgraph SupportingServices[Supporting Services]
        CG[Code Generator]
        AL[Analytics]
        SEC[Security]
    end
    
    %% Monitoring
    Monitoring[Monitoring]
    
    %% Main Flow
    Users --> EdgeLayer
    DNS --> CDN
    CDN --> LB
    LB --> API
    
    %% Shortening Flow
    API --> SS
    SS --> CG
    SS --> SEC
    SS --> DB
    
    %% Redirect Flow
    API --> RS
    RS --> RC
    RC -->|Cache Miss| DB
    
    %% Analytics Flow
    RS --> AL
    SS --> AL
    
    DataLayer --> Monitoring
    SupportingServices --> Monitoring
    API --> SEC 
    
    %% Styling
    style U fill:#e1f5fe
    style M fill:#e1f5fe
    style DNS fill:#e0f2f1
    style CDN fill:#e0f2f1
    style LB fill:#fff3e0
    style API fill:#f3e5f5
    style RS fill:#f3e5f5
    style SS fill:#f3e5f5
    style RC fill:#e8f5e8
    style DB fill:#fce4ec
    style CG fill:#fff9c4
    style AL fill:#ffe0b2
    style SEC fill:#ffcdd2
    style Monitoring fill:#e1f5fe
```


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
