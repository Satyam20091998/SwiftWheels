# SwiftWheels
A platform to connect riders with drivers, similar to Uber
# Ride Sharing Website Project (Uber-like)

## Overview
This project aims to create a ride-sharing website, connecting riders with drivers. It allows users to register, book rides, and drivers to accept rides. The system will integrate Google Maps API for location tracking and routing.

## Project Goals
- Develop a website similar to Uber, connecting riders with drivers.
- Use Python (Flask/Django), Docker, and SQL databases.
- Integrate Google Maps for route tracking and distance calculation.
- Create a scalable backend with RESTful APIs for future mobile app development.

## Technologies Used
- **Backend**: Python (Flask/Django)
- **Frontend**: HTML, CSS, JavaScript (React.js/Angular.js)
- **Database**: PostgreSQL/MySQL
- **Containerization**: Docker
- **Mapping**: Google Maps API
- **Version Control**: GitHub

## Roadmap

### 1. Research
- Choose appropriate backend and frontend technologies.
- Investigate OAuth/JWT for authentication.
- Research Stripe/PayPal for potential future payment integration.

### 2. Initial Setup
- Set up a GitHub repository for collaboration.
- Set up Docker with Python, Flask/Django, and the database.
- Write a `Dockerfile` and `docker-compose.yml` for the app.

### 3. System Design
- **User Management**: Registration and login for riders and drivers.
- **Ride Booking System**: Book and manage rides.
- **Location Services**: Google Maps API for location tracking.
- **Ride Matching Algorithm**: Basic logic for matching drivers with riders.
- **Database**: Users, Rides, Transactions, Vehicles, Location logs.
  
### 4. Project Phases
1. **Phase 1**: Setup backend and database with Docker.
2. **Phase 2**: Implement ride booking and Google Maps integration.
3. **Phase 3**: Testing and optimization.
4. **Phase 4**: Collaboration using GitHub branches.
5. **Phase 5**: Future expansion into mobile apps.

### 5. Database and Backend Storage
- Use SQL with Docker to manage user and ride data.
- Implement RESTful APIs for interaction with the frontend.

### 6. Git Workflow
- Use `feature` branches for development.
- Regular code reviews to ensure quality and prevent bugs.

## Week-by-Week Plan

### Week 1-2: Backend Setup
- Set up Docker and Python backend.
- Create RESTful API endpoints for user management.
- Design the database schema.

### Week 3-4: Google Maps Integration
- Add Google Maps for location and routes.
- Implement ride-matching logic.

### Week 5-6: Frontend & Testing
- Create the frontend for ride booking.
- Conduct full tests on user flows.
- Use Docker for local deployment and testing.

## How to Run the Project
1. Clone the repository.
2. Set up Docker.
3. Use `docker-compose up` to start the backend and database.
4. Access the frontend on `localhost`.

## Future Plans
- Add a mobile app using Flutter or React Native.
- Integrate payment options for seamless transactions.

