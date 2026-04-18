# Memory Bank

> Project context extracted from AI conversations.

---

## Session — 2026-04-18 18:36

## Architecture Decisions
### Made
#### Frontend Framework: React
#### Styling Library: Tailwind CSS
#### Backend Framework: Node.js with Express
#### Database: MongoDB

## Technologies Chosen and Why
### Frontend
*   React: Familiarity and ecosystem strength make it an ideal choice for the team.
*   Tailwind CSS: Quick development speed and ease of use ensure a smooth user experience.
### Backend
*   Node.js with Express: Simple, straightforward approach to meet project needs.
*   Auth0: Provides an out-of-the-box solution for authentication, reducing maintenance overhead.
*   Zustand: Suitable for the project's scale, offering a more lightweight alternative to Redux.
### Database
*   MongoDB: Flexible data model and document-based structure make it a better fit for the project's requirements.
*   Socket.io: Confirmed as necessary for real-time updates.

## Things Tried and Rejected
#### Tried
*   Redux vs. Zustand
*   Real-time Updates (polling considered)
*   Handling JWT manually
*   Using Redis as a caching layer
#### Rejected
*   PostgreSQL

## Naming Conventions Established
#### Renamed useTaskData to useTasks

## Open Questions Remaining
#### Whether or not a caching layer is necessary
#### Currently undecided, with Redis being mentioned as an option
