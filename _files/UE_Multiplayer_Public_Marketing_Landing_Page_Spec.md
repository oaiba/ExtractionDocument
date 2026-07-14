# Unreal Engine Multiplayer Public Marketing Landing Page Specification

## 1. Purpose and Status

This document defines the public marketing landing page for the game. It is the English-canonical design and content contract for a standalone website that introduces the game, explains its gameplay, presents approved media, and directs visitors to approved launch, wishlist, newsletter, and community destinations.

The page is a public marketing surface. It is not the Unreal in-game home screen, the Admin Web, a player portal, or a LiveOps control-plane client.

## 2. Goals, Audience, and Boundaries

### 2.1 Goals

- Communicate the game value proposition clearly to new visitors.
- Show approved gameplay features and media without making unverified product claims.
- Convert visitors through release-state-appropriate primary and secondary CTAs.
- Provide editorial links for news, events, roadmap updates, community channels, and legal information.

### 2.2 Audience

| Audience | Primary need | Expected outcome |
| --- | --- | --- |
| New player | Understand the game quickly | Wishlist, pre-register, download, or play |
| Returning prospect | See current news, events, and release status | Re-engage through CTA or community |
| Community member | Find official channels and roadmap | Join approved community destination |
| Press/creator | Find approved overview and media | Follow press/community contact link |

### 2.3 Non-goals

- Player sign-in, account management, profile, inventory, wallet, matchmaking, or game launch authentication.
- Admin functions, LiveOps configuration, operational dashboards, or direct database/API access.
- Real-time game status, queue status, personalized offers, or client-runtime event data.
- Unapproved release dates, platform availability, ratings, awards, gameplay claims, or store URLs.

## 3. Release States and CTA Contract

The page is built and deployed with one `releaseState`. It is an editorial build-time value, not a client-side call to a game service.

| `releaseState` | Hero primary CTA | Hero secondary CTA | Required destination behavior |
| --- | --- | --- | --- |
| `preLaunch` | `Wishlist` or `Pre-register` | `Get updates` | Primary opens approved store/registration URL; secondary opens approved newsletter URL or form |
| `launched` | `Download` or `Play now` | `Wishlist` or `Get updates` | Primary opens approved platform/download URL; secondary uses an approved available destination |

CTA labels and URLs are supplied by Marketing. The implementation must not render a CTA with a blank, placeholder, or unapproved destination. If the selected release state lacks a valid primary CTA, publication is blocked.

External destinations open in a new tab only when that is the approved user experience; any new tab uses `rel="noopener noreferrer"` and communicates that behavior accessibly.

## 4. Static Content Model

All values below are editorial build-time inputs. They may be held in a static content file, CMS export produced at build time, or page source, but they must never require the LiveServices runtime.

| Content group | Required fields | Rules |
| --- | --- | --- |
| Site identity | game title, short description, logo asset | Use approved brand assets only |
| Release | `releaseState`, primary CTA label/URL, secondary CTA label/URL | Must satisfy Section 3 |
| Hero | headline, supporting copy, hero image/video, alt/caption treatment | Video requires poster and accessible fallback |
| Features | title, short copy, approved image/video | Three to six feature cards recommended |
| Media | asset type, source, thumbnail/poster, alt text/caption, credit where required | No autoplay with sound |
| News/events | title, date, summary, image, canonical URL | Static cards link to an approved canonical post; no runtime feed |
| Roadmap | phase/title, status, description, optional date qualifier | Dates and commitments require Product approval |
| Community | channel name, icon, approved URL, optional community guideline URL | Only official channels |
| Legal | privacy, terms, cookies where applicable, copyright, contact | Required links must resolve before publication |

No PII is stored by the site except through an explicitly approved external newsletter/form provider. The page must link to the provider's applicable privacy notice at the point of submission.

## 5. Information Architecture

The landing page uses this order. A deployment may hide an optional section only when its content is unavailable and doing so does not leave a broken navigation link.

1. **Global header** — logo/home link, anchor navigation to Overview, Features, Media, News, Roadmap, Community, and a release-state primary CTA.
2. **Hero** — game identity, concise value proposition, approved hero media, primary CTA, and secondary CTA.
3. **Game overview** — short introduction that establishes setting or core experience using approved copy.
4. **Gameplay/features** — three to six scannable feature cards with supporting approved media.
5. **Media** — trailer and/or screenshots. A playable video has captions when speech is present and a poster/thumbnail fallback.
6. **News and events** — editorial cards for current announcements or public-facing events. Each card navigates to a canonical external or dedicated public article.
7. **Roadmap** — a high-level, non-binding view of approved milestones. It is not a service-status page.
8. **Community** — official social/community destinations and community-guideline link if one exists.
9. **Final CTA** — repeats the active primary and secondary release-state CTAs.
10. **Footer** — copyright, privacy, terms, cookie preferences/policy where applicable, contact/press route, and relevant platform/legal marks.

## 6. Layout and Responsive Behavior

### 6.1 Desktop wireframe

```text
+------------------------------------------------------------------+
| Logo | Overview Features Media News Roadmap Community | [CTA]    |
+------------------------------------------------------------------+
| HERO: headline + copy + [Primary CTA] [Secondary CTA] | visual   |
+------------------------------------------------------------------+
| Game overview                                                    |
+------------------------------------------------------------------+
| Feature cards (3-6)                                              |
+------------------------------------------------------------------+
| Trailer / screenshot gallery                                     |
+------------------------------------------------------------------+
| News & events cards                                              |
+------------------------------------------------------------------+
| Roadmap milestones                                               |
+------------------------------------------------------------------+
| Community links + final CTAs                                     |
+------------------------------------------------------------------+
| Legal footer                                                     |
+------------------------------------------------------------------+
```

### 6.2 Mobile behavior

- Collapse header navigation into an accessible menu; retain the primary CTA visibly or within the open menu without duplication ambiguity.
- Stack hero content before media and use responsive image/video crops that preserve the main subject.
- Present feature, media, news, and roadmap items as a single-column list or horizontally scrollable group only when keyboard controls and visible focus are available.
- Keep tap targets at least 44 by 44 CSS pixels where practical and ensure no horizontal page scrolling at common mobile widths.
- Do not rely on hover for content, controls, or CTA labels.

## 7. Interaction, States, and Failure Handling

### 7.1 Navigation and CTAs

- Anchor navigation scrolls to the named section and moves focus predictably when required for keyboard/screen-reader users.
- The active CTA appears in header, hero, and final CTA areas with consistent label and destination for the selected `releaseState`.
- Any external CTA or article link clearly identifies its destination when the label alone is insufficient.

### 7.2 Editorial states

| Section | Ready state | Empty or failed-asset behavior |
| --- | --- | --- |
| Hero | Approved media and CTA | Use approved static image fallback; block publish if primary CTA is invalid |
| Features | Approved cards | Hide an unavailable card; retain at least one overview path |
| Media | Gallery/trailer | Hide unavailable item; never show broken media control |
| News/events | One or more current cards | Hide section and its navigation item when no approved content exists |
| Roadmap | Approved milestones | Show approved high-level availability message or hide section and navigation item |
| Community | Official links | Hide unavailable channel; retain required legal/footer links |

The site must not display queue availability, maintenance status, player-specific content, or raw LiveOps event data as a substitute for missing editorial content.

## 8. Accessibility, SEO, Privacy, and Performance

### 8.1 Accessibility

- Use semantic landmarks, one `h1`, ordered heading hierarchy, visible keyboard focus, and a skip-to-content link.
- Provide meaningful alternative text for informative images; mark decorative images appropriately; provide captions/transcripts for spoken video content.
- Respect `prefers-reduced-motion`; motion must pause/stop where necessary and must not be required to understand the page.
- Maintain WCAG 2.2 AA color contrast for text and essential controls.

### 8.2 SEO and sharing

- Provide a unique title, meta description, canonical URL, Open Graph/Twitter title, description, and approved share image.
- Use structured data only for verified facts; do not emit unsupported product, review, event, or availability claims.
- Include robots and sitemap behavior in the web-hosting implementation, not in game runtime infrastructure.

### 8.3 Privacy and performance

- Load only approved analytics, consent, embed, and newsletter-provider scripts after required consent.
- Link privacy/terms/cookie information from the footer; expose cookie preferences where required by the selected jurisdiction and provider.
- Optimize responsive media, lazy-load below-the-fold images, defer nonessential third-party embeds, and provide posters for video.
- Target a fast first contentful render on mobile; the implementation must establish measurable performance budgets before production launch.

## 9. Ownership and Approval Workflow

| Area | Accountable owner | Required approval |
| --- | --- | --- |
| Copy, CTAs, news/events, roadmap, community URLs | Marketing | Product for game/release claims |
| Gameplay descriptions and product facts | Product / Game team | Product approval |
| Brand assets, screenshots, trailers | Brand / Marketing | Asset-rights approval |
| Privacy, terms, cookies, consent | Legal | Legal approval |
| Accessibility, SEO, performance, hosting | Web implementation owner | Web QA approval |

Content updates remain static editorial releases. A change to `releaseState`, CTA URL, platform availability, or dated roadmap claim requires Marketing and Product approval before deployment.

## 10. Acceptance Checklist

- [ ] `preLaunch` and `launched` builds show the correct primary and secondary CTAs with approved, reachable destinations.
- [ ] The page contains hero, overview, features, media, news/events, roadmap, community, final CTA, and legal footer, or deliberately hides an optional empty section and its navigation entry.
- [ ] No browser request targets authentication, player, inventory, matchmaking, Admin, or LiveOps runtime endpoints.
- [ ] Desktop, tablet, and mobile layouts have no clipped content, inaccessible controls, or unintended horizontal scrolling.
- [ ] Keyboard-only traversal, focus order, visible focus, menu behavior, headings, landmarks, text alternatives, captions, and reduced-motion handling pass accessibility review.
- [ ] All external links, approved media, share metadata, legal links, and community links are validated before publication.
- [ ] The page contains no placeholder URLs, unapproved claims, secrets, personal player data, or game-service credentials.
- [ ] Production performance, consent, analytics, and hosting checks meet the web project's approved deployment criteria.

## 11. Recommended Technical Baseline

The recommended implementation is a standalone Next.js application using TypeScript and React. This aligns with the proposed Admin Web frontend stack while preserving an independent build and deployment boundary.

| Concern | Recommendation | Boundary |
| --- | --- | --- |
| Framework | Next.js | Separate application under `marketing-web/` |
| Language | TypeScript | Strict type checking enabled |
| UI | React components | Do not import Admin Web screens or runtime state |
| Styling | Tailwind CSS or CSS Modules | Select one project-wide approach during bootstrap |
| Content | Static Markdown/JSON/TypeScript content | Build-time only; no LiveServices runtime dependency |
| Assets | Versioned files under `public/` | Approved media only; optimize before production |
| Rendering | Static export or equivalent static hosting output | No server session or player request required |
| Tests | Typecheck, lint, component/route checks, accessibility and link checks | Run in the marketing-web pipeline |

### 11.1 Recommended repository layout

```text
ob-multiplayer-live-services/
├── backend/
├── admin-web/
├── marketing-web/
│   ├── app/
│   ├── components/
│   ├── content/
│   │   ├── site.json
│   │   ├── news/
│   │   └── roadmap/
│   ├── public/
│   │   ├── images/
│   │   ├── videos/
│   │   └── social/
│   ├── tests/
│   ├── package.json
│   └── README.md
├── contracts/
├── db/
├── deployments/
└── docs/
```

`marketing-web/` is a sibling application to `admin-web/`. It may share repository tooling and review rules, but it has its own `package.json`, build command, test command, deployment configuration, and ownership.

### 11.2 Build-time content and configuration

- `releaseState` is selected at build time as `preLaunch` or `launched`.
- CTA labels and destinations, media, news/events, roadmap items, community URLs, legal URLs, and public metadata are static content inputs.
- Public build variables may select approved environment-independent values; secrets must never be placed in the page bundle.
- The app must not import backend packages, call Go APIs, reuse Admin Web authentication, or access PostgreSQL, Redis, object storage, player data, matchmaking, or LiveOps endpoints.

### 11.3 Git and CI/CD integration

The application remains in the `ob-multiplayer-live-services` Git repository but is deployed independently:

```text
Git push
  -> detect marketing-web changes
  -> install and validate marketing-web dependencies
  -> typecheck + lint + tests
  -> build static site
  -> accessibility, URL, SEO, and asset checks
  -> deploy to public hosting/CDN
```

Changes outside `marketing-web/` must not trigger a marketing deployment unless the shared toolchain or release workflow explicitly requires it. Changes to CTA destinations, release state, platform availability, or dated roadmap claims require Marketing and Product approval.

## 12. Implementation Handoff

The marketing website is an independently owned and deployed public web surface. It may live in the same Git monorepo for review and atomic documentation, but it must remain outside the `ob-multiplayer-live-services` runtime path and must not use the Admin Web as its frontend foundation.
