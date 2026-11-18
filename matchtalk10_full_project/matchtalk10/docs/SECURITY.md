# Security before production
- Hash passwords with Argon2id/bcrypt; never store plaintext.
- Implement session/token rotation, revocation, recovery and MFA for admins.
- Enforce RBAC server-side on every privileged endpoint.
- Validate DTOs; rate-limit; restrict CORS; use security headers.
- Use parameterized DB access; protect cookie flows against CSRF and pages against XSS.
- Keep provider/API secrets server-side and rotate them.
- Use TLS, encrypted backups, least privilege and tested restores.
- Provide privacy notice, consent, opt-out, retention, export and deletion for personalization activity.
- Add dependency scanning, SAST/DAST, penetration tests and incident response.
