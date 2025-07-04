# HTTP (Hypertext Transfer Protocol) Notes

**HTTP** (Hypertext Transfer Protocol) is the foundation of data communication on the World Wide Web. It is a protocol that enables the transfer of resources—like HTML documents, images, and other files—between a **client** (typically a web browser) and a **server** (a computer hosting the resources). Developed by Tim Berners-Lee in 1989, HTTP is essential to how the internet operates. This note covers HTTP's structure, methods, status codes, headers, and its role in web development, with examples for clarity.

---

## What is HTTP?

HTTP is a **client-server protocol**: a client (e.g., a browser) sends a **request** to a server, which responds with a **response**. It’s designed to fetch and deliver resources, making it the backbone of web browsing.

HTTP is **stateless**, meaning each request-response pair is independent—the server doesn’t retain memory of prior requests unless additional mechanisms (like cookies) are used.

**Key Characteristics**:
- **Client-Server**: Client initiates, server responds.
- **Stateless**: No inherent memory between requests.
- **Purpose**: Transfers hypertext and resources.

---

## How HTTP Works: Request and Response

HTTP communication involves a **request** from the client and a **response** from the server.

### Structure of an HTTP Request

An HTTP request has three parts:

1. **Request Line**:
   - Includes the **HTTP method**, **request URI** (resource path), and **HTTP version**.
   - Example: `GET /index.html HTTP/1.1`

2. **Headers**:
   - Metadata about the request (e.g., browser type).
   - Example: `User-Agent: Mozilla/5.0`

3. **Body** (optional):
   - Data sent to the server (e.g., form data).
   - Example: `username=john&password=1234`

**Sample Request**:
```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

### Structure of an HTTP Response

An HTTP response includes:

1. **Status Line**:
   - Contains the **HTTP version**, **status code**, and **status message**.
   - Example: `HTTP/1.1 200 OK`

2. **Headers**:
   - Metadata about the response (e.g., content type).
   - Example: `Content-Type: text/html`

3. **Body**:
   - The requested resource (e.g., HTML content).
   - Example: `<h1>Hello, World!</h1>`

**Sample Response**:
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 20

<html>
  <body>
    <h1>Hello, World!</h1>
  </body>
</html>
```

---

## HTTP Methods

HTTP methods define the client’s intended action:

- **GET**: Retrieves a resource (safe, no changes).
  - Example: `GET /about.html`
- **POST**: Sends data to the server (e.g., forms).
  - Example: `POST /submit-form`
- **PUT**: Updates a resource.
  - Example: `PUT /users/1`
- **DELETE**: Deletes a resource.
  - Example: `DELETE /users/1`
- **HEAD**: Retrieves headers only (no body).
  - Example: `HEAD /index.html`
- **OPTIONS**: Lists supported methods.
  - Example: `OPTIONS /api/users`

---

## HTTP Status Codes

Status codes indicate the request’s outcome:

- **1xx (Informational)**: Processing continues (e.g., `100 Continue`).
- **2xx (Successful)**: Request succeeded (e.g., `200 OK`, `201 Created`).
- **3xx (Redirection)**: Further action needed (e.g., `301 Moved Permanently`).
- **4xx (Client Error)**: Client issue (e.g., `404 Not Found`, `400 Bad Request`).
- **5xx (Server Error)**: Server issue (e.g., `500 Internal Server Error`).

**Common Examples**:
- `200 OK`: Success
- `404 Not Found`: Resource missing
- `500 Internal Server Error`: Server failed

---

## HTTP Headers

Headers are key-value pairs providing metadata:

- **Content-Type**: Resource type (e.g., `text/html`).
- **Content-Length**: Body size (e.g., `1024`).
- **User-Agent**: Client identifier (e.g., `Mozilla/5.0`).
- **Accept**: Preferred response type (e.g., `application/json`).
- **Authorization**: Credentials (e.g., `Bearer <token>`).

---

## HTTPS: Securing HTTP

**HTTPS** (HTTP Secure) adds **SSL/TLS** encryption to HTTP, ensuring:
- **Confidentiality**: Data is private.
- **Integrity**: Data isn’t tampered with.
- **Authentication**: Server identity is verified.

URLs use `https://` and port 443. It’s critical for secure data transfer (e.g., login forms).

---

## Evolution of HTTP

- **HTTP/1.0**: Basic, separate connections.
- **HTTP/1.1**: Persistent connections, caching.
- **HTTP/2**: Multiplexing, header compression.
- **HTTP/3**: QUIC over UDP (faster, in progress).

---

## HTTP in Action

- **Webpage Load**: `GET /index.html` → `200 OK`.
- **Form Submission**: `POST /login` → `302 Found`.
- **API Call**: `GET /api/users` → JSON response.

---

## Summary

HTTP is a stateless protocol driving web communication with:
- **Requests/Responses**: Structured exchanges.
- **Methods**: Actions like GET, POST.
- **Status Codes**: Outcome indicators.
- **Headers**: Metadata.
- **HTTPS**: Security layer.

It’s essential for web development and browsing!