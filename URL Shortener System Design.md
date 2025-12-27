# URL Shortener System Design - Two‑Page Summary
## 1. Core Principles
- **Uniqueness** - each short code must map to exactly one long URL. 
- **Low Latency** - redirects must complete in a few milliseconds. 
- **Persistence & Durability** - mappings must survive failures for years.
- **Scalability** - billions of reads/writes; horizontal scaling required. 
- **Security & Trust** - block malicious URLs, prevent abuse.
- **Extensibility** - support analytics, custom domains, expiration, etc.

## 2. High‑Level Architecture
- **Client & API Layer** - POST /shorten, GET /{code}.
- **Short Code Generation Service** - hashing, sequential IDs, or random Base62.
- **Storage Layer** - SQL or NoSQL; must support fast lookups.
- **Redirect Service** - handles billions of GETs; must be ultra‑fast.
- **Cache Layer** - Redis/Memcached for hot URLs.
- **Analytics Pipeline** - optional; logs clicks, geos, devices, referrers.

## 3. System Flow Example (Mermaid Diagram)

```mermaid
sequenceDiagram
    participant User
    participant API as API Server
    participant Gen as Code Generator
    participant DB as Database
    participant Cache as Cache
    participant R as Redirect Service

    User->>API: Submit long URL
    API->>Gen: Generate short code
    Gen-->>API: Return code
    API->>DB: Store (code → long URL)
    API-->>User: Return short URL

    User->>R: Access short URL
    R->>Cache: Lookup code
    Cache-->>R: Hit or miss
    R->>DB: Lookup if cache miss
    DB-->>R: Return long URL
    R->>Cache: Update cache
    R-->>User: Redirect (301/302)
```

## 4. Shortening Process
- **Input Validation** - Syntax check, reachability, blacklist filtering.
- **Normalization** - Lowercase domain, remove redundant params, canonicalize URL.
- **Short Code Generation**  - **Hashing** (MD5/SHA‑256 → Base62).  - **Sequential IDs** (ID → Base62).  - **Random Strings** (fixed‑length Base62). Must avoid collisions at scale.
- **Store Mapping** - Save code → URL + metadata (created_at, expiration, user_id).
- **Return Short URL**     - Example: `https://short.ly/abc123`.


## 5. Redirect Flow
- **Receive Request** for `/abc123`.  
- **Cache Lookup** - hot URLs must be served from Redis.  
- **DB Lookup** if cache miss.  
- **Analytics Logging** (async).  
- **Redirect** with 301 or 302.

**Performance Targets:**  Sub‑50ms end‑to‑end.  95%+ cache hit ratio.  Edge servers for global latency reduction.
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
