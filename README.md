# Bazar.com Online Book Store Project

## Project Goals
- Explore multi-tier web design and micro-services.
- Teach Replication, Caching, Consistency concepts.
- Introduce basics of containerization and Docker.

## The Problem
Bazar.com experienced a surge in demand after introducing three new books during a spring break sale. However, the increasing popularity led to complaints about processing delays. The task is to re-architect Bazar.com's online store to handle higher workloads.

### Part 1: Build Servers as shown:
![image](https://github.com/NoorAldeenAbuShehadeh/Multi-tier-Online-Book-Store/assets/102482887/05ec868d-8095-44d1-95c6-d09cf26554ac)

### Part 2: Replication and Caching
- Add replication and caching to enhance request processing latency.
- Implement an in-memory cache at the front-end node to store recent request results.
- Assume replication of order and catalog servers with load balancing algorithms.
- Address cache consistency by implementing server-push techniques.
- Use REST APIs for communication between components.

### Part 3: Dockerize Your Application
- Package each application component as a Docker container.
- Components include front-end server, cache server (if separate), catalog, and backend server.
- Use tools available to create Docker container images.
- Upload Docker version of the application to GitHub for easy deployment.

## Implementation Details
- **Caching**: In-memory cache integrated into the front-end server or as a separate micro-service.
- **Replication**: Assume replication of order and catalog servers with load balancing algorithms.
- **Cache Consistency**: Implement server-push techniques for cache consistency.
- **Communication**: All components use REST APIs for communication.
- **Dockerization**: Package each component as a Docker container for portability and easy deployment.
