# MatchTalk10
Cross-platform sports platform foundation: Next.js website, Expo Android/iOS app, NestJS API, PostgreSQL/Prisma, Redis/BullMQ-ready infrastructure, and Python FastAPI news recommendations.

## Requirements
Node.js 20+, pnpm 9, Python 3.11+, Docker Desktop.

## Start
1. Copy `.env.example` to `.env`.
2. `npm install -g pnpm@9`
3. `pnpm install`
4. `pnpm db:up`
5. `pnpm --filter @matchtalk10/api prisma:migrate`
6. `pnpm dev`
7. In another terminal: `cd services/news-ai`; create/activate a venv; `pip install -r requirements.txt`; `uvicorn app.main:app --reload --port 8000`.

Website http://localhost:3000 | API http://localhost:4000/api | API docs http://localhost:4000/docs | Python docs http://localhost:8000/docs.

**Important:** This is a substantial runnable foundation, not a finished production global sports service. Fixtures are demo data. Real scores/news, rights, provider credentials, complete auth/RBAC, push notifications, admin workflows, observability and production hardening remain implementation/integration work.
