# Architecture
Use a modular monolith for NestJS initially, with a separately deployable Python recommendation service. Avoid premature microservices/Kubernetes.

## Core modules
Identity/sessions; users/preferences; sports; competitions/seasons; teams/players; matches/participants; events; statistics/standings; favourites; search; editorial/news; notifications; provider adapters; subscriptions; audit logs.

## Live data flow
Licensed provider -> adapter/poller/webhook -> validation -> external ID mapping -> idempotency/deduplication -> event ordering/correction handling -> canonical match state -> PostgreSQL -> cache invalidation -> Socket.IO broadcast. Provider events, not client submissions, are authoritative.

## News recommendation
NestJS owns authentication, consent and canonical articles. Python ranks a limited set of candidate articles using transparent rules and TF-IDF similarity. Add collaborative filtering only when there is sufficient quality interaction data. Support opt-out, retention and deletion.

## Multi-sport
Scoring differs by sport. Keep shared match metadata but add sport-specific periods, statistics and rulesets as sports are onboarded.
