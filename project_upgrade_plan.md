# Detailed Project Upgrade: Decoupled Architecture (Django + Next.js)

This document provides a technical roadmap for upgrading the **Neem Karoli Travellers** website from a monolithic Django application to a modern, high-performance decoupled stack with a **Django REST API** and a **Next.js** frontend.

---

## 1. Architecture Overview

- **Backend (API)**: Django + Django REST Framework (DRF)
  - Responsibilities: Data storage, authentication logic, business rules, booking processing, and media management.
- **Frontend (UI)**: Next.js (React Framework)
  - Responsibilities: Fast page loads (SSR/SSG), smooth user experience, dynamic interactions, and SEO optimization.
- **Communication**: REST API (JSON) over HTTPs.

---

## 2. Backend Migration (Django to DRF)

### Step A: Install Dependencies
Install essential tools for building a secure API:
```bash
pip install djangorestframework django-cors-headers djangorestframework-simplejwt
```

### Step B: Create Serializers
Convert your existing models into JSON format. Example for `SafariPackage`:
```python
# Create serializers.py in each app
from rest_framework import serializers
from .models import SafariPackage

class SafariPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafariPackage
        fields = '__all__'
```

### Step C: API Viewsets & Routes
Convert existing views to `ViewSets` for cleaner code and standard REST endpoints:
- `GET /api/v1/packages/` (List packages)
- `POST /api/v1/bookings/` (Submit booking)

---

## 3. Frontend Implementation (Next.js)

### Step A: Project Initialization
Initialize the Next.js project using the latest App Router architecture:
```bash
npx create-next-app@latest frontend --typescript --tailwind --eslint
```

### Step B: Data Fetching (Server Components)
Leverage **Server-Side Rendering (SSR)** for fast loading and perfect SEO:
```javascript
// Example: fetching packages in Next.js
export default async function Page() {
  const res = await fetch('http://localhost:8000/api/v1/packages/');
  const packages = await res.json();
  
  return (
    <div className="grid grid-cols-3 gap-4">
      {packages.map(p => <PackageCard key={p.id} data={p} />)}
    </div>
  );
}
```

---

## 4. Advanced Security Implementation

### Layer 1: Authentication (JWT)
Use **SimpleJWT** for secure, stateless login.
- Store the access token in memory or a Secure Cookie (HttpOnly).
- Never store sensitive tokens in `localStorage` to prevent XSS attacks.

### Layer 2: CORS (Cross-Origin Resource Sharing)
Restrict who can talk to your API.
- Only allow your Next.js domain (e.g., `https://neemkarolitravellers.com`) to request data from the backend.

### Layer 3: Rate Limiting & Throttling
Prevent automated bots from spamming your booking system.
- Implement DRF Throttling to limit requests per IP (e.g., max 5 bookings per hour per user).

### Layer 4: Data Validation & Sanitization
- Ensure all inputs (phone numbers, ages) are strictly validated on the backend.
- Use Next.js built-in sanitization to prevent injection attacks.

---

## 5. Deployment Strategy

### Development
- Run Django on port `8000`.
- Run Next.js on port `3000`.

### Production
- **Reverse Proxy (Nginx)**: Use Nginx to route `/api/` requests to Django and everything else to Next.js.
- **SSL**: Force HTTPS everywhere using Let's Encrypt.
- **Docker**: Containerize both apps for easy scaling and consistent environments.

---

## 6. Key Benefits of this Upgrade
- **Speed**: Next.js uses Static Site Generation (SSG) to pre-render pages for near-instant loads.
- **Scalability**: You can host the frontend on **Vercel** and the backend on a fast **VPS** or Cloud provider independently.
- **Security**: Stateless JWT auth is more robust for modern web applications and mobile apps.
- **SEO**: Next.js handles metadata and social sharing previews significantly better than standard Django templates.

---

**Final Recommendation**: Start by installing `djangorestframework` and creating your first API endpoint for the `SafariPackage` model to test the data flow to a fresh Next.js app.
