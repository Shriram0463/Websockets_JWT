# WebSocket Communication with JWT Authentication

This project demonstrates a secure WebSocket communication setup between a Spring Boot backend and a FastAPI server, leveraging JWT (JSON Web Tokens) for authentication and message encryption.


## Overview

This application facilitates real-time messaging between Java (Spring Boot) and Python (FastAPI) applications using WebSockets. It showcases:

**JWT Implementation**: Utilizes JWT tokens with HS256 algorithm for secure message encoding and decoding.

**WebSocket Communication**: Establishes a bidirectional communication channel where Spring Boot sends encrypted messages as JWT tokens to FastAPI.

**Authentication**: Ensures secure message transfer by verifying JWT tokens on FastAPI using a shared secret key.


## Components

### Spring Boot Backend:
Generates JWT tokens containing message payloads.

Establishes WebSocket connections with FastAPI.

Sends JWT tokens over WebSocket for real-time communication.

### FastAPI Server:
Runs WebSocket endpoints to receive encrypted JWT tokens.

Decodes and verifies JWT tokens to extract message payloads.

Sends decoded messages back to Spring Boot for confirmation.


## Security

**JWT Tokens**: Signed with a shared secret key (HS256) for secure encoding and decoding of messages.

**Message Integrity**: Ensures that messages remain confidential and tamper-proof during transmission over WebSocket.


## Code Structure

    WS_JWT/
    ├── spring-boot/
    │   ├── src/
    │   │   ├── main/
    │   │   │   ├── java/
    │   │   │   │   └── com/
    │   │   │   │       └── example/
    │   │   │   │           └── jwtwebsocket/
    │   │   │   │               ├── controller/
    │   │   │   │               │   └── MessageController.java
    │   │   │   │               ├── service/
    │   │   │   │               │   └── JwtService.java
    │   │   │   │               ├── model/
    │   │   │   │               │   └── Message.java
    │   │   │   │               └── JwtWebsocketApplication.java
    │   │   │   └── resources/
    │   │   │       └── application.properties
    │   │   └── pom.xml
    └ ── fastapi/
        ├── main.py
        ├── jwt_service.py


## Files Overview

1. **MessageController.java**

    Handles incoming requests and sends JWT tokens over WebSocket.

2. **JwtService.java**

    Provides JWT token generation and verification services.

3. **Message.java**

    Defines the data model for messages exchanged over WebSocket.

4. **JwtWebsocketApplication.java**

    Main entry point for the Spring Boot application.

5. **application.properties**

    Configuration properties for the Spring Boot application.

6. **pom.xml**

    Maven configuration file for managing dependencies and build process.

7. **main.py**

    Defines WebSocket endpoint and JWT token decoding logic in FastAPI.

8. **jwt_service.py**

    Provides functions for decoding JWT tokens in FastAPI.


## Requirements

Java Development Kit (JDK)

Maven

Python 3.x

FastAPI

Uvicorn


## License

This project is licensed under the MIT License.
