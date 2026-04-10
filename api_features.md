# API Conversion Opportunities for Neem Karoli Travellers

After analyzing the codebase, here are the core functionalities that can be transitioned into a RESTful API form. This would allow for a more dynamic frontend, mobile app integration, or a headless CMS approach.

## 1. Safari & Travel Packages (`packages` & `home` apps)
- **GET `/api/packages/`**: List all available safari and travel packages.
- **GET `/api/packages/{id}/`**: Get full details, pricing, and duration for a specific package.
- **GET `/api/packages/search/?q=...`**: Search and filter packages dynamically without full page reloads.

## 2. Booking System (`booking` app)
- **POST `/api/bookings/safari/`**: Submit a safari booking form.
- **POST `/api/bookings/hotel/`**: Submit a hotel booking form.
- **GET `/api/bookings/status/{id}/`**: Track the status of a specific booking (if tracking is added/stored).
- **GET `/api/package-options/`**: Fetch the list of available package categories for form dropdowns.

## 3. Media & Gallery (`home` app)
- **GET `/api/gallery/`**: Fetch all gallery images with titles and descriptions.
- **GET `/api/carousel/`**: Fetch images specifically for the homepage hero/carousel.
- **GET `/api/hero-images/`**: Fetch high-resolution background/hero visuals.

## 4. User Account & Management (if implemented)
- **POST `/api/auth/login/`**: User authentication.
- **POST `/api/auth/register/`**: New traveller registration.
- **GET `/api/user/profile/`**: User's past bookings and preferences.

## 5. Contact & Support
- **POST `/api/contact/`**: Submit general enquiries or contact forms via AJAX.

## Why use an API?
1. **Faster UI**: Updates the page without refreshing (SPA behavior).
2. **Mobile Support**: The same backend can serve both the website and a future mobile app.
3. **Decoupling**: Allows using modern frontend frameworks like React, Vue, or Next.js.
4. **Improved Validation**: Provides real-time feedback on form inputs.

---
**Suggested Technology**: [Django REST Framework (DRF)](https://www.django-rest-framework.org/) is the standard way to implement this in your current Django project.
