# BRIEFING — 2026-11-13T14:50:00Z

## Mission
Điều phối nhóm biên soạn và nâng cấp toàn diện các chương còn lại (Chương 01 đến Chương 28, Phụ lục) theo tiêu chuẩn Siêu Giáo Trình, phục vụ xuất bản tài liệu học tập chuẩn mực (Production).

## 🔒 My Identity
- Archetype: orchestrator
- Roles: orchestrator, user_liaison, human_reporter, successor
- Working directory: /home/nam/Documents/learncpp
- State folder: /home/nam/Documents/learncpp/.agents/teamwork/orchestrator/
- Original parent: parent
- Original parent conversation ID: a69260af-05ba-4ff5-8688-6d0b29abf745

## 🔒 My Workflow
- **Pattern**: Project Pattern
- **Scope document**: /home/nam/Documents/learncpp/PROJECT.md
1. **Decompose**: Decompose full translation and upgrade of LearnCpp (Chapters 01-28 + Appendices) into milestones by chapter groups and dual-track E2E testing
2. **Dispatch & Execute** (pick ONE):
   - **Delegate (sub-orchestrator)**: Spawn sub-orchestrators for milestones and E2E testing orchestrator
3. **On failure** (in this order):
   - Retry: nudge stuck agent or re-send task
   - Replace: spawn fresh agent with partial progress
   - Skip: proceed without (only if non-critical)
   - Redistribute: split stuck agent's remaining work
   - Redesign: re-partition decomposition
   - Escalate: report to parent (sub-orchestrators only, last resort)
4. **Succession**: At 16 spawns, write handoff.md, spawn successor
- **Work items**:
  1. Survey phase (3 Explorers / Spec Miners) [in-progress]
  2. Initial decomposition & PROJECT.md creation [pending]
  3. Milestone dispatches to Sub-orchestrators + E2E Testing Orchestrator [pending]
  4. Final Milestone verification & E2E completion [pending]
- **Current phase**: 0 (Survey)
- **Current focus**: Mapping full scope of docs/en vs docs/vi, data/toc.json, glossary, and VitePress config

## 🔒 Key Constraints
- NEVER write, modify, or create source code files directly.
- NEVER run build/test commands yourself — require workers to do so.
- NEVER investigate or explore the problem at the code level — dispatch Explorers for technical investigation.
- You MAY use file-editing tools ONLY for metadata/state files (.md) in your .agents/teamwork/ folder.
- Follow Project Pattern dual track (Implementation + E2E Testing).
- Never reuse a subagent after it has delivered its handoff — always spawn fresh

## Current Parent
- Conversation ID: a69260af-05ba-4ff5-8688-6d0b29abf745
- Updated: not yet

## Key Decisions Made
- Selected Project Pattern with 3 Survey Explorers (including spec mining) for initial full-scope mapping.
- Dispatched survey_spec_miner_1, survey_explorer_1, survey_explorer_2.

## Team Roster
| Agent | Type | Work Item | Status | Conv ID |
|-------|------|-----------|--------|---------|
| survey_spec_miner_1 | teamwork_spec_miner | TOC & Spec Mining | in-progress | ffde0596-3e99-4031-8f70-87941ad193ce |
| survey_explorer_1 | teamwork_explorer | Standard & Blueprint | in-progress | a9c9a51d-d713-4a3d-9f5c-a06b2af3d415 |
| survey_explorer_2 | teamwork_explorer | English Source & Scope | in-progress | 64abc6e0-bb9e-473a-aef5-b5134edf6a3c |

## Succession Status
- Succession required: no
- Spawn count: 3 / 16
- Pending subagents: ffde0596-3e99-4031-8f70-87941ad193ce, a9c9a51d-d713-4a3d-9f5c-a06b2af3d415, 64abc6e0-bb9e-473a-aef5-b5134edf6a3c
- Predecessor: none
- Successor spawned: not yet spawned
- Successor generation: none
- Successor state folder: none

## Active Timers
- Heartbeat cron: c5e28284-a077-40a6-97ed-a436139bf61c/task-40
- Safety timer: c5e28284-a077-40a6-97ed-a436139bf61c/task-42
- On succession: kill all timers before spawning successor
- On context truncation: handle timers as step 4 of the State Recovery section of your prompt says

## Artifact Index
- /home/nam/Documents/learncpp/.agents/teamwork/ORIGINAL_REQUEST.md — Original request
- /home/nam/Documents/learncpp/.agents/teamwork/orchestrator/DISPATCH.md — Dispatch log
- /home/nam/Documents/learncpp/.agents/teamwork/orchestrator/BRIEFING.md — Working memory
- /home/nam/Documents/learncpp/.agents/teamwork/orchestrator/progress.md — Progress heartbeat
