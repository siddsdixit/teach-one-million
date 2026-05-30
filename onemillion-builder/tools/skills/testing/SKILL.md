# Testing Templates & Reference

Reference for the test agent. Contains test plan template, test patterns, and CI configuration.

## Test Plan Template

```markdown
# Test Plan: [App Name]

## Scope
- Backend API: [N] endpoints across [N] sprints
- E2E Browser: [N] user flows
- Accessibility: [N] pages

## Test Environment
- Backend: http://localhost:8000
- Frontend: http://localhost:3000
- Database: MongoDB (test database, isolated per test)

## Acceptance Criteria Coverage

| FR | Criterion | Test ID | Status |
|----|-----------|---------|--------|
| FR-01 | Given... | T-001 | ✅ |

## Test Execution Order
1. Backend unit tests (fast, no server)
2. Backend API tests (requires running server)
3. E2E tests (requires full stack)
4. Accessibility tests (requires full stack)
```

## Backend Test Patterns

### conftest.py

```python
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest_asyncio.fixture
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as ac:
        yield ac

@pytest_asyncio.fixture
async def auth_headers(client):
    email = f"test_{int(time.time())}@example.com"
    await client.post("/api/v1/auth/register", json={"email": email, "password": "Test1234!", "name": "Test"})
    res = await client.post("/api/v1/auth/login", json={"email": email, "password": "Test1234!"})
    token = res.json()["data"]["access_token"]
    return {"Authorization": f"Bearer {token}"}
```

### API Test Pattern

```python
async def test_create_entity_success(client, auth_headers):
    res = await client.post("/api/v1/entities", json={"name": "Test"}, headers=auth_headers)
    assert res.status_code == 201
    data = res.json()["data"]
    assert data["name"] == "Test"
    assert "id" in data

async def test_create_entity_401(client):
    res = await client.post("/api/v1/entities", json={"name": "Test"})
    assert res.status_code == 401

async def test_idor_protection(client, auth_headers):
    # Create resource as user A, try to access as user B
    ...
```

## E2E Playwright Patterns

### auth.spec.ts

```typescript
import { test, expect } from '@playwright/test';

test('register and login', async ({ page }) => {
  const email = `test_${Date.now()}@example.com`;
  
  await page.goto('/auth/register');
  await page.fill('[name="email"]', email);
  await page.fill('[name="password"]', 'Test1234!');
  await page.click('button[type="submit"]');
  
  await expect(page).toHaveURL('/dashboard');
});

test('protected route redirects to login', async ({ page }) => {
  await page.goto('/dashboard');
  await expect(page).toHaveURL(/.*auth.*/);
});
```

## CI Configuration

```yaml
name: CI
on: [push, pull_request]

jobs:
  backend:
    runs-on: ubuntu-latest
    services:
      mongodb:
        image: mongo:7
        ports: ['27017:27017']
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with: { python-version: '3.11' }
      - run: cd backend && pip install -r requirements.txt -r requirements-dev.txt
      - run: cd backend && PYTHONPATH=. pytest tests/ --cov=app -q

  frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: cd frontend && npm ci && npm run build && npm run lint
```
