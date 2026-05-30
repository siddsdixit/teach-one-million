# Security Audit Checklist

This skill provides the security audit checklist for the guard agent.

## OWASP Top 10 Quick Reference

| # | Category | Key Check |
|---|----------|-----------|
| A01 | Broken Access Control | Auth on every protected route, ownership checks |
| A02 | Cryptographic Failures | Argon2 passwords, 256-bit JWT secret, token expiry |
| A03 | Injection | Pydantic on all inputs, no raw query construction |
| A04 | Insecure Design | Rate limiting auth (10/min), no user enumeration |
| A05 | Security Misconfiguration | CORS restricted, debug=False in prod |
| A06 | Vulnerable Components | pip-audit + npm audit clean |
| A07 | Auth Failures | Token rotation, logout invalidation |
| A08 | Software Integrity | Lock files committed, no dynamic imports |
| A09 | Security Logging | Auth events logged, no PII in logs |
| A10 | SSRF | URL input validated against allowlist |

## Secret Scanning Patterns

```bash
# Grep for hardcoded secrets
grep -rnE '(password|secret|api_key|token)\s*[:=]\s*["\x27][^"\x27]{8,}' \
  --include='*.py' --include='*.ts' --include='*.tsx' --include='*.json' .

# Check git history
git log --all -p | grep -iE '(password|secret|api_key)\s*[:=]\s*["\x27][^"\x27]{8,}'
```

## Required Security Headers

- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Content-Security-Policy: default-src 'self'`

## Security Tools

```bash
pip install trufflehog3 pip-audit bandit semgrep
npm audit
```
