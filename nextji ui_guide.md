Frontend UI/UX Implementation Guide (Next.js)
1. Design Philosophy

The UI must reflect:

Spiritual + Premium Travel Feel
Clean, airy, minimal clutter
Focus on nature, peace, and luxury
Fast loading + SEO-first rendering
Core Principles:
Performance > Animations
Readability > Decoration
Mobile-first responsive design
Visual hierarchy must guide booking decisions
2. Global Theme System
🎨 Color Palette

Use a nature + spiritual palette:

Primary Color: #6B4F3B (Earth Brown)
Secondary Color: #D4AF37 (Golden Accent)
Background: #F9F7F3 (Soft Cream)
Text Dark: #1A1A1A
Text Light: #6B6B6B
Success: #28A745
Error: #DC3545
Dynamic Theme (IMPORTANT)
Override primary color using /agent/ API
Apply theme_color dynamically:
Buttons
Chat bubble
Highlights
3. Typography System
Heading Font: Playfair Display (Elegant / Spiritual)
Body Font: Inter (Clean / Modern)
Font Sizes:
H1: 48px
H2: 36px
H3: 28px
Body: 16px
Small: 14px
4. Layout Structure (Next.js App Router)
Structure:
app/
 ├── layout.tsx (Global Layout)
 ├── page.tsx (Homepage)
 ├── [slug]/
 │    └── page.tsx (Dynamic Pages)
 ├── components/
 │    ├── HeroCarousel
 │    ├── PackageCard
 │    ├── GalleryGrid
 │    ├── BookingForm
 │    ├── ChatAgent
 │    └── SkeletonLoader
5. Global Components
5.1 Header
Sticky top navigation
Transparent → solid on scroll
Include:
Logo (left)
Nav links (center)
CTA button: "Book Now"
CTA Button Style:
Background: Primary
Text: White
Border Radius: 8px
Hover: Darker shade + slight scale
5.2 Footer
3 column layout:
About
Quick Links
Contact Info
Social icons (Bootstrap Icons)
Copyright
6. Homepage UI (SSR Page)
6.1 Hero Section
Data Source:

/hero-images/

Implementation:
Full-screen carousel
Overlay gradient (dark fade)
Text on top:
Heading: Large (H1)
Subtext: Calm descriptive line
CTA: "Explore Packages"
Behavior:
Auto-slide
Lazy loading images
Use Next <Image />
6.2 Travel Packages Section
Data Source:

/packages/

UI: Grid Layout
Package Card Design:
Image (Top)
Title
Short Description
Price / Badge
CTA: View Details
Interaction:
Hover:
Image zoom
Shadow increase
Click:
Route to /[slug]
6.3 Safari Packages Section

Same as above but horizontal scroll layout for better UX.

6.4 Gallery Section
Data Source:

/gallery-images/

Layout:
Masonry Grid (Responsive)
Behavior:
Hover overlay
Lightbox preview
7. Dynamic Pages (Slug-based SSR)
Example:

/jim-corbett

Data Usage:
slug
meta_title
meta_description
MUST IMPLEMENT:
generateMetadata():
export async function generateMetadata({ params }) {
  const data = await fetch(API);
  return {
    title: data.meta_title,
    description: data.meta_description,
  };
}
8. Chat Agent (Floating Component)
Data Source:

/agent/?page={slug}

UI Requirements:
Floating Bubble:
Bottom-right corner
Circular button
Dynamic color from API
On Click:
Expand panel:
Avatar
Suggestions
Quick replies
Behavior:
Auto-update on route change
Smooth open/close animation
9. Booking Form UI
APIs:
/booking/submit/
/booking/hotel/
Form Fields:
Name
Email
Phone
Date
Package Selection
UX Requirements:
Validation:
Real-time validation
Show errors below inputs
Submission:
Disable button during request
Show loader
Response:
Success → Green Toast
Error → Red Toast
10. Skeleton Loaders
Use While:
Fetching packages
Loading gallery
Page transitions
Style:
Grey shimmer animation
Match actual layout
11. Responsiveness
Breakpoints:
Mobile: < 768px
Tablet: 768px - 1024px
Desktop: > 1024px
Rules:
Stack layouts on mobile
Use horizontal scroll for cards
Touch-friendly buttons
12. Animations & Micro Interactions

Use minimal, smooth animations:

Fade-in sections on scroll
Hover effects on cards
Button click ripple

Avoid:

Heavy animations
Delays affecting performance
13. Icons

Use Bootstrap Icons

Examples:

bi-geo-alt (location)
bi-calendar
bi-telephone
bi-chat-dots
14. Performance Optimization
Use Next.js <Image />
Enable lazy loading
Use SSR for all pages
Avoid unnecessary client-side JS
15. Accessibility
Use proper alt tags (from seo_caption)
Buttons must be clickable and visible
Good contrast ratios
Keyboard navigation support
16. Developer Notes
Use fetch() inside Server Components
Use use client only where needed (forms, chat)
Use environment variables for API base URL
Handle API errors gracefully
17. Final UX Goal

The final product should feel:

Fast like a static website
Premium like a travel brand
Calm like a spiritual journey
Simple enough for any user to book easily