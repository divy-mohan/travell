# Neem Karoli Travellers - Next.js Frontend Requirements & API Guide

## 1. Project Overview & Architecture
This project uses a decoupled **Headless Architecture**. 
- **Backend:** Django REST Framework (running on port `8000`)
- **Frontend:** Next.js (will run on port `3000`)

The goal of the Frontend Engineer is to consume the JSON endpoints provided by Django and render an extremely fast, SEO-optimized, and visually stunning UI using Next.js Server-Side Rendering (SSR).

## 2. Verification of APIs
✅ **STATUS: 100% VERIFIED** 
All APIs have been tested and configured with CORS allowing `http://localhost:3000` to bypass Cross-Origin restrictions. JWT Authentication and API rate limits are successfully active.

---

## 3. The API Endpoints (Data Consumption Dictionary)

### A. Dynamic Chat Agent (Page Contextual)
**Endpoint:** `GET http://127.0.0.1:8000/api/v1/home/agent/?page={page_slug}`
- **Purpose:** Fetches visual persona data (Avatar, Color, Suggestions) for the live chat bubble tailored to specific pages (e.g., `?page=jim-corbett` or `?page=home`).
- **Frontend Action:** Build a floating Chat component in global Next.js Layout. Use `usePathname()` to dynamically query this API. Apply the returned `theme_color` to the UI.

### B. Travel Packages & Safari Details
**Endpoint:** `GET http://127.0.0.1:8000/api/v1/packages/`
**Endpoint:** `GET http://127.0.0.1:8000/api/v1/home/safari-packages/`
- **Purpose:** Returns the array of available travel trips and safaris.
- **Frontend Action:** Map these arrays into beautiful `PackageCard` components. Use Next.js `<Link>` to dynamically route users to individual package pages based on the returned `slug` fields. Inject `meta_title` and `meta_description` from this payload directly into the Next.js `metadata` object for optimal SEO.

### C. Homepage Display Content
**Endpoint:** `GET http://127.0.0.1:8000/api/v1/home/hero-images/`
**Endpoint:** `GET http://127.0.0.1:8000/api/v1/home/gallery-images/`
- **Purpose:** Fetches the ultra-high resolution hero videos/images and the gallery grid.
- **Frontend Action:** Implement a dynamic Hero Carousel and a Masonry Grid layout. Ensure `<Image>` components use the returned `seo_caption` as the `alt` tag for accessibility and SEO scaling.

### D. Booking APIs (Secured)
**Endpoint:** `POST http://127.0.0.1:8000/api/v1/booking/submit/`
**Endpoint:** `POST http://127.0.0.1:8000/api/v1/booking/hotel/`
- **Purpose:** Allows users to submit their booking forms securely.
- **Status:** Rate-limited to max 5 requests per minute.
- **Frontend Action:** Create detailed booking form structures using React Hook Form or Formik. Post the JSON directly to these endpoints, catching and displaying specific field-level errors (like Invalid Email or Phone number) gracefully to the user.

---

## 4. Specific Responsibilities of the Next.js Frontend Engineer

To complete the Neen Karoli project effectively, the Frontend Engineer must build:

### 1. Server-Side Fetched Pages
All standard pages (Home, Jim Corbett, Chardham Yatra) should be Server Components (`page.tsx`) that `await fetch()` the APIs above. This guarantees that search-engine crawlers see the fully generated page instantly without waiting for JavaScript.

### 2. A Dynamic Floating Agent
You must design a floating chat bubble that lives in the master UI layout. It will hook into the `GET /agent/` API, dynamically morphing its Avatar, color, and popup messages based on which route the user navigates into.

### 3. SEO Integration
The Backend API payload now strictly includes: `slug`, `meta_title`, and `meta_description`. The frontend engineer **must** map these into Next.js's native `generateMetadata()` function on every single dynamic route layout. 

### 4. Interactive UI Elements
- Build beautiful, smooth skeleton loaders while client-side API requests pend.
- Build Toast Notifications (Green for Success, Red for failures) during booking submissions.
- Implement responsive masonry grids for the Photo Galleries fetched via the `/gallery-images/` API.
