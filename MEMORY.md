# Memory Bank

> Project context extracted from AI conversations.

---

## Session — 2026-04-18 17:37

**Project Architecture**
========================

### **Architecture Decisions Made**

* Real-time updates are prioritized, leading to the selection of Firebase as the database solution.
* PostgreSQL is considered overkill due to the need for server management.

### **Technologies Chosen and Why**

| Technology | Reason |
| --- | --- |
| Firebase | Real-time updates, simplicity, and ease of use. |
| TypeScript | Already set up and will save debugging time in the future. |

### **Things Tried and Rejected and Why**

* PostgreSQL was considered but rejected due to the need for server management.
* Self-built authentication is left open for now, prioritizing core feature development.

### **Naming Conventions Established**

* The main component has been named `DashboardView` to maintain consistency with existing naming conventions.

### **Open Questions Remaining**

* Authentication implementation: Should self-built authentication be pursued or leave it for later?

---

## Session — 2026-04-18 17:40

**Project Planning**
=====================

### Architecture Decisions Made

* Real-time updates: Firebase is chosen to handle this requirement efficiently.
* Server management: PostgreSQL was considered but ultimately rejected due to the need for server management, which adds unnecessary complexity.

### Technologies Chosen and Why

* **Firebase**: Suitable for real-time updates and simple queries. Reduces the need for server management and provides a scalable solution.
* **TypeScript**: Already set up in the project, using it will save debugging time later on.

### Things Tried and Rejected

* **PostgreSQL**: Overkill for this project due to the need for server management. Firebase is chosen instead for its scalability and ease of use.
* **Self-built authentication**: Left open for now, focusing on the core feature first. Authentication can be implemented later when needed.

### Naming Conventions Established

* **DashboardView**: Main component name, consistent with existing naming conventions in the project.

### Open Questions Remaining

* **Authentication implementation**: Should implement authentication system once the core feature is complete.
* **Additional features and scalability**: Will consider adding more features or scaling Firebase as the project grows.
