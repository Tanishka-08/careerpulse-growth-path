---
name: Career Velocity
colors:
  surface: '#fcf8fa'
  surface-dim: '#dcd9db'
  surface-bright: '#fcf8fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f5'
  surface-container: '#f0edef'
  surface-container-high: '#eae7e9'
  surface-container-highest: '#e4e2e4'
  on-surface: '#1b1b1d'
  on-surface-variant: '#45464d'
  inverse-surface: '#303032'
  inverse-on-surface: '#f3f0f2'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#0051d5'
  on-secondary: '#ffffff'
  secondary-container: '#316bf3'
  on-secondary-container: '#fefcff'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#002113'
  on-tertiary-container: '#009668'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#dbe1ff'
  secondary-fixed-dim: '#b4c5ff'
  on-secondary-fixed: '#00174b'
  on-secondary-fixed-variant: '#003ea8'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#fcf8fa'
  on-background: '#1b1b1d'
  surface-variant: '#e4e2e4'
typography:
  h1:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  stat-number:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: -0.01em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin: 32px
  max_width: 1280px
---

## Brand & Style

The design system is built on the principles of **Corporate Modernism** with a heavy emphasis on **Minimalism**. It aims to evoke a sense of steady progress, professional reliability, and high-performance focus. The target audience consists of ambitious professionals who require a tool that feels more like an "executive dashboard" and less like a social media platform.

The UI should feel technical and precise but remain encouraging. This is achieved through generous whitespace (to reduce cognitive load in data-heavy views) and a "tech-forward" aesthetic characterized by crisp lines, subtle depth, and intentional accent colors that signify movement and completion.

## Colors

The palette is anchored in a deep navy for authority and stability, paired with a vibrant professional blue for interaction. 
- **Core Stability:** Deep Navy (#0F172A) is used for headers and primary navigation to ground the experience.
- **Action & Movement:** Professional Blue (#2563EB) directs the user’s eye toward interactive elements and primary calls to action.
- **Accents:** 'Success' Green (#10B981) is reserved strictly for milestone completions and positive progress indicators. 'Focus' Orange (#F59E0B) highlights active tasks or items requiring immediate professional attention.
- **Environment:** The workspace utilizes a light gray background (#F8FAFC) to separate the canvas from white (#FFFFFF) content cards, creating a clean, layered workspace.

## Typography

The design system utilizes **Inter** exclusively to achieve a systematic, utilitarian aesthetic. It is highly readable at small sizes, which is critical for complex roadmaps and data tables.

- **Headlines:** Use tighter letter spacing and heavier weights to create a sense of importance and "tech" precision.
- **Body:** Standard weights with comfortable line heights ensure that long-form career goals and descriptions are easy to digest.
- **Labels:** Uppercase styles with increased letter spacing are used for category tags and metadata to distinguish them from actionable content.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop views to maintain a professional, organized structure, transitioning to a fluid model for mobile.

- **Grid:** A 12-column grid with a 24px gutter provides the framework for the roadmap and dashboard widgets. 
- **Rhythm:** An 8pt spatial system (represented as `base * x`) governs all margins and padding to ensure mathematical consistency.
- **Dashboard Layout:** Use a sidebar-navigation pattern (collapsed by default or icons-only) to maximize the "workspace" area for the career tracker and data visualizations.

## Elevation & Depth

Visual hierarchy is managed through **Tonal Layers** and **Ambient Shadows**.

1.  **Background Layer:** The light gray (#F8FAFC) acts as the floor of the application.
2.  **Surface Layer:** Content cards and containers are pure white with a subtle 1px border (#E2E8F0) and a soft, diffused shadow (Offset: 0, 4px; Blur: 12px; Color: rgba(15, 23, 42, 0.05)).
3.  **Active/Floating Layer:** Modals and dropdowns use a more pronounced shadow to indicate temporary focus (Offset: 0, 10px; Blur: 25px; Color: rgba(15, 23, 42, 0.1)).

This approach avoids "heavy" interfaces, keeping the feel light and productive.

## Shapes

The design system uses a **Rounded** shape language to soften the "corporate" feel and make the tracker feel modern and accessible.

- **Standard Elements:** Buttons, input fields, and small cards use a 0.5rem (8px) radius.
- **Large Containers:** Dashboard widgets and main content areas use a 1rem (16px) radius to create clear visual containment.
- **Indicators:** Progress bars use fully rounded (pill-shaped) ends to emphasize movement and flow.

## Components

- **Buttons:** Primary buttons use a solid blue background with white text. Secondary buttons use a transparent background with a 1px navy border. All buttons have a subtle "lift" effect on hover.
- **Roadmap Cards:** Features a "Focus" orange border-left (4px) for active goals and a "Success" green check icon for completed milestones.
- **Chips/Badges:** Small, low-contrast background fills (e.g., light blue background with dark blue text) for tagging skills or industries.
- **Input Fields:** Clean white backgrounds with a light gray border that transitions to blue on focus. Label text is always positioned above the field in the `label-caps` style.
- **Progress Tracker:** A horizontal stepped indicator. Completed steps are solid green; current steps are outlined blue; future steps are light gray.
- **Data Tables:** Minimalist styling with no vertical lines; only horizontal dividers in light gray. The header row uses a light navy tint for subtle distinction.