# Backend Overview

This folder contains the backend API logic.

## Architecture

```mermaid
graph LR
    A[Client] --> B[API Gateway]
    B --> C[Auth Service]
    B --> D[Database Service]
    D --> E[(PostgreSQL)]
