from fastapi import HTTPException, Request

DDOS_THRESHOLD = 1000
ip_requests = {}


def ddos_protection(request: Request):
    client_ip = request.client.host
    if client_ip not in ip_requests:
        ip_requests[client_ip] = 0
    ip_requests[client_ip] += 1

    if ip_requests[client_ip] > DDOS_THRESHOLD:
        raise HTTPException(status_code=429, detail="Too many requests")
