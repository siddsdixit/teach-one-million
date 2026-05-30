# Deployment Guide & Checklists

This skill provides deployment checklists for the ship agent.

## Deployment Targets

| Service | Purpose | Free Tier |
|---------|---------|-----------|
| Vercel | Frontend (Next.js) | Yes — generous |
| Railway | Backend (FastAPI) | Yes — $5/mo usage |
| MongoDB Atlas | Database | Yes — 512MB |
| Sentry | Error tracking | Yes — 5k events/mo |

## Pre-Deployment Checklist

### Code & Tests
- [ ] All backend tests pass: `pytest tests/ -x -q`
- [ ] Frontend builds: `npm run build`
- [ ] No hardcoded secrets (grep verified)
- [ ] `.env` is in `.gitignore`
- [ ] `.env.example` committed with placeholder values

### Environment Variables
- [ ] All vars in `.env.example` set in deployment platform
- [ ] `CORS_ORIGINS` set to production frontend URL (not `*`)
- [ ] `JWT_SECRET` is 256-bit random value
- [ ] `MONGODB_URL` uses `mongodb+srv://` (TLS)
- [ ] `SENTRY_DSN` set in both backend and frontend

### Database
- [ ] Atlas cluster reachable from deployment platform
- [ ] Database user has readWrite (not atlas admin)
- [ ] Indexes created for queried fields
- [ ] Automated backups enabled

## Deployment Steps

1. **Database:** Verify Atlas cluster, create indexes, confirm backups
2. **Backend (Railway):** Connect repo → set env vars → set start command → deploy → verify health
3. **Frontend (Vercel):** Connect repo → set `NEXT_PUBLIC_API_URL` → deploy → verify 200

## Start Command
```bash
cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
```

## Smoke Test Pattern
```bash
# Register → Login → Create → Read → Delete → Verify 401
BACKEND_URL="https://your-app.railway.app"
curl -s -X POST "$BACKEND_URL/api/v1/auth/register" -H "Content-Type: application/json" \
  -d '{"email":"smoke@test.com","password":"SmokeTest1234!","name":"Smoke"}'
```

## Rollback
- Railway: Dashboard → Deployments → select previous → Redeploy
- Vercel: Dashboard → Deployments → Promote to Production
- Expected time: < 5 minutes
