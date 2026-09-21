Thursday 2:17 PM
What's in ai what's an AI agent I am planning to build an identic assistant basically and AI agent which can automate all of my task and have it visual dashboard on my desktop also I am thinking to connect it to Omni road and automatic all of my task also I am thinking to build it using online models not offline not locally like all and quentry and other models which are completely free and I don't want to use any pdpi or any pet subscription or services and thinking to build it on my own free also I have Gemini prom model free subscriptions on my Google account and thinking to make it the brain of the agent you know the brain which will be connected to Omni road and Omni route as a access to multiple models the brain has its own contacts memory the brain keeps evolving tips thinking and from the repetitive task and understand the pattern or on which I work and on which I used to work I like to work like that my laptop configuration is i5 83500 Ram and 5 minutes integrated USB graphics given from the Intel the laptop

Yes — what you're describing is much more than a chatbot. You're essentially describing a personal AI agent / desktop AI operating layer.

And given your i5-8350U-class laptop, 8 GB RAM, and integrated graphics, your decision to keep the heavy AI inference online is sensible. The laptop should run the orchestration, UI, memory, tools, and automation, while cloud models do the expensive reasoning.

The core idea

Think of your system like this:

                    ┌─────────────────────────┐
                    │     YOU / DESKTOP       │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      AI ASSISTANT       │
                    │       "BRAIN"           │
                    │                          │
                    │ • Understands intent     │
                    │ • Plans tasks             │
                    │ • Maintains memory       │
                    │ • Learns preferences     │
                    │ • Decides which tools    │
                    │ • Evaluates results      │
                    └────────────┬────────────┘
                                 │
                    ┌────────────┴────────────┐
                    ▼                         ▼
             ┌──────────────┐          ┌──────────────┐
             │ OmniRoute    │          │ Local Tools  │
             │              │          │              │
             │ Gemini       │          │ Files        │
             │ Claude       │          │ Browser      │
             │ Other models │          │ Terminal     │
             │ Free models  │          │ Windows      │
             └──────┬───────┘          │ VS Code      │
                    │                  │ Apps         │
                    ▼                  └──────────────┘
              Online AI models

The important distinction is:

The model isn't the agent.

An AI model is the reasoning engine.

An agent = model + memory + tools + planning + execution + feedback loop + permissions.

What I would build in your situation

I'd call the architecture something like:

MAYA Agent OS

A personal desktop AI agent with a central reasoning brain, persistent memory, multi-model routing, tool execution, and a visual control dashboard.

You already have the idea of MAYA, so this could become a significantly more capable version of it.

1. The Brain

Gemini can be your primary reasoning model.

But don't hard-code Gemini everywhere.

Instead:

                 MAYA Brain
                     │
             Task classification
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
   Coding         Research       Simple task
       │             │             │
   OmniRoute      OmniRoute      OmniRoute
       │             │             │
       ▼             ▼             ▼
  Best model      Best model     Fast model

This is where your OmniRoute setup becomes extremely useful.

The brain shouldn't necessarily say:

"Always use Gemini."

It should say:

"What am I trying to accomplish?"

Then select an appropriate model.

For example:

Task	Potential route
Simple conversation	Fast/free model
Coding	Coding-capable model
Debugging	Strong reasoning model
Documentation	Gemini
Large context	Model with large context
Planning	Strong reasoning model
Summarization	Cheap/free model
Image understanding	Vision-capable model

That makes OmniRoute the model layer, not the brain itself.

2. Memory

This is where your idea becomes genuinely interesting.

Don't make memory simply:

chat_history.txt

Instead, create several types.

Short-term memory

What is happening right now.

Current task:
Build MAYA

Current project:
D:\CODE\MAYA

Current objective:
Implement agent tool system

Recent actions:
Created planner.py
Modified memory.py
Running tests
Long-term memory

Things that remain useful.

For example:

User prefers:
- Python
- Django
- VS Code
- Windows
- Dark UI
- Practical projects
- Minimal unnecessary complexity
Project memory

Separate memories for:

MAYA
LexArena
DevTrack
Backend Lab
College projects
etc.
Episodic memory

Actual past experiences:

2026-09-17

Task:
Fix OmniRoute configuration

Result:
Model routing failed because model identifier was invalid.

Lesson:
Validate model IDs before modifying routing configuration.
Procedural memory

This is especially powerful.

The agent learns:

When user asks for X:

1. Open VS Code
2. Navigate to project
3. Inspect files
4. Run tests
5. Analyze errors
6. Modify code
7. Test again
8. Explain changes

Eventually it develops workflows.

3. The "learning" system

I'd be careful with the word learning.

You don't actually need to retrain Gemini.

Instead, MAYA can learn your behavior through memory.

Example:

You repeatedly do:

Open VS Code
↓
Open backend project
↓
Run server
↓
Check terminal
↓
Ask AI about error
↓
Modify code
↓
Run again

MAYA can eventually detect:

"This appears to be a recurring development workflow."

Then it can ask:

"Would you like me to turn this into an automated workflow?"

You approve.

Now it stores:

{
  "workflow": "django_debug",
  "trigger": "Django server error",
  "steps": [
    "inspect_terminal",
    "inspect_recent_changes",
    "analyze_error",
    "suggest_fix",
    "wait_for_approval",
    "apply_fix",
    "run_tests"
  ]
}

That's much safer and more practical than allowing an AI to blindly modify everything.

4. Tools

This is probably the most important part.

Your agent needs tools such as:

filesystem
terminal
browser
VS Code
clipboard
Windows applications
screenshots
notifications
calendar
email
documents
Git
GitHub

But each should be an explicit tool.

For example:

tools = {
    "read_file": ...,
    "write_file": ...,
    "run_terminal": ...,
    "search_files": ...,
    "open_application": ...,
    "take_screenshot": ...,
    "git_status": ...,
    "git_diff": ...,
}

The LLM doesn't directly control your computer.

It requests:

CALL TOOL:
read_file(
    path="D:/CODE/MAYA/main.py"
)

Your agent executes it and gives the result back to the model.

That's the foundation of an actual agent.

5. Your desktop dashboard

This is where I'd make MAYA visually impressive.

Something like:

┌─────────────────────────────────────────────┐
│ MAYA                              ● ONLINE  │
├─────────────────────────────────────────────┤
│                                             │
│  Good afternoon, Anshuman.                 │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │ What should I do?                   │    │
│  │                                     │    │
│  │ > ______________________________    │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ACTIVE TASK                                │
│  ───────────────────────────────────────    │
│  Building MAYA Agent                       │
│  ████████████████░░░░ 78%                  │
│                                             │
│  AGENT ACTIVITY                             │
│  ✓ Read project structure                   │
│  ✓ Analysed configuration                   │
│  → Testing model router                     │
│  ○ Update memory                            │
│                                             │
│  MEMORY                 MODELS              │
│  1,284 memories          Gemini ●           │
│  37 workflows            Claude ●           │
│  12 preferences          Other ●            │
│                                             │
└─────────────────────────────────────────────┘

And you could have panels for:

Tasks
Memory
Projects
Workflows
Model routing
Agent activity
System status
Permissions
Logs
6. The most important feature: permissions

This is something I would not compromise on.

Don't build:

"MAYA can do literally anything."

Build:

"MAYA can do anything I have explicitly permitted."

For example:

Level 0 — Read
Read files
Search files
Inspect screen
Read terminal
Level 1 — Suggest
Generate code
Generate emails
Suggest commands
Suggest changes
Level 2 — Execute safely
Create files
Run tests
Run development servers
Git status
Level 3 — Sensitive

Require confirmation:

Delete files
Send emails
Push Git
Install software
Modify system settings
Purchase something

And potentially:

Level 4 — Never autonomous
Financial transactions
Password handling
Security-sensitive actions
Destructive system operations

That gives you an agent rather than a dangerous unrestricted automation script.

Your laptop is actually enough

Your hardware:

i5-8350U + 8 GB RAM + Intel integrated graphics

isn't suitable for running serious modern LLMs locally.

But that's okay.

Your architecture should be:

Laptop
│
├── MAYA UI
├── Agent runtime
├── Memory database
├── Tool system
├── Automation
├── OmniRoute
└── Logs
        │
        ▼
     Internet
        │
        ├── Gemini
        ├── Claude
        ├── other available models
        └── free model providers

The local machine is essentially the nervous system and hands.

The online model is the reasoning engine.

But there's one major issue with your "completely free" requirement

This part needs careful architecture.

There are three different things:

Free model

A model may be available without payment.

Free API

A provider may expose that model through an API with free quotas.

Free consumer subscription

You may have access to a model through a web application, but that does not automatically mean you can programmatically use that subscription as an API.

Your Gemini subscription is therefore useful, but we should not assume that your consumer Gemini subscription can simply become an unlimited API backend for MAYA.

Similarly, some models/services have free tiers, rate limits, changing availability, or restrictions on automated use.

So I'd design MAYA so that:

MAYA
  ↓
OmniRoute
  ↓
Available providers

and the provider configuration can change without rebuilding MAYA.

That protects you from one free endpoint disappearing.

The architecture I'd recommend

I'd keep the first version surprisingly small.

MAYA/
│
├── core/
│   ├── agent.py
│   ├── planner.py
│   ├── executor.py
│   ├── router.py
│   └── permissions.py
│
├── brain/
│   ├── prompts.py
│   ├── reasoning.py
│   └── evaluator.py
│
├── memory/
│   ├── short_term.py
│   ├── long_term.py
│   ├── episodic.py
│   ├── procedural.py
│   └── vector_store.py
│
├── tools/
│   ├── filesystem.py
│   ├── terminal.py
│   ├── browser.py
│   ├── vscode.py
│   ├── windows.py
│   └── git.py
│
├── workflows/
│   ├── manager.py
│   └── learned.py
│
├── dashboard/
│   └── ...
│
├── config/
│   └── models.json
│
└── main.py

I'd probably use Python for the agent core because it fits what you're already learning and gives you a huge ecosystem for automation.

For the dashboard, you could use something lightweight rather than making an enormous frontend initially.

The agent loop

The heart of MAYA could be conceptually this:

             ┌─────────────┐
             │     USER    │
             └──────┬──────┘
                    ↓
              UNDERSTAND
                    ↓
                 PLAN
                    ↓
             CHECK MEMORY
                    ↓
             SELECT MODEL
                    ↓
             SELECT TOOLS
                    ↓
                EXECUTE
                    ↓
               OBSERVE
                    ↓
               EVALUATE
                 /     \
              success  failure
                ↓         ↓
             MEMORY ←── REPLAN
                ↓
             RESPOND

That loop is the agent.

Not the dashboard.

Not Gemini.

Not OmniRoute.

Not the model.

The entire loop.

And here's where your idea gets really powerful

Eventually you could tell MAYA:

"Prepare my development environment."

Instead of merely answering:

"Sure, open VS Code."

MAYA could reason:

User wants development environment.

Current project:
MAYA

Check:
✓ VS Code installed
✓ Project exists
✓ Git repository exists
✓ Python environment exists
✗ Dependencies possibly outdated

Actions:
→ Open VS Code
→ Open project
→ inspect git status
→ activate environment
→ start required services
→ inspect terminal

Then your dashboard shows:

MAYA is working...

✓ Identified project
✓ Opened VS Code
✓ Checked Git
✓ Activated environment
→ Starting development server...

That is an agentic desktop assistant.

I would NOT build everything at once

This is where projects like this usually collapse.

Don't start with:

"I'll build Jarvis that controls my entire PC."

Start with:

MAYA v0.1
Chat
+
Gemini/OmniRoute
+
Memory
+
Filesystem tools
+
Terminal
+
Basic dashboard

Then:

MAYA v0.2
Planning
+
Tool calling
+
Agent loop
+
Task history
MAYA v0.3
Browser automation
+
VS Code automation
+
Git
+
Workflows
MAYA v0.4
Pattern detection
+
Workflow learning
+
Preference learning
+
Task evaluation
MAYA v1.0
Persistent personal agent
+
Multi-model routing
+
Long-term memory
+
Desktop automation
+
Visual dashboard
+
Permission system
+
Self-improvement through feedback
And one important correction to your idea

Don't make the brain "evolve itself."

Make it propose improvements to itself and ask you to approve them.

For example:

MAYA detected a repeated workflow.

You've performed these steps 7 times:

Open VS Code
Open backend-lab
Start Django server
Inspect terminal

Suggested automation: start_django_workspace

[Approve] [Modify] [Reject]

You approve it.

Now MAYA stores the workflow.

That's much more robust than letting an LLM rewrite its own core system.

And honestly, your OmniRoute setup is a very good foundation for this project. You already have the multi-model routing problem partially solved; the next layer is building the actual agent runtime + memory + tools + dashboard around it.

If we build this together, I would treat MAYA as a real software project, not a toy chatbot: architecture first, then a minimal working agent, then tools, memory, automation, and finally the "learns my workflow" layer.

Absolutely. We’ll build MAYA from an empty folder → working agent → desktop application → integrations → autonomous workflows → production release, and I’ll guide you through it one implementation step at a time.

Since you’re still learning agent architecture, I don't want to dump 100 commands on you and say "go build it." We'll work like a small professional engineering team: I’ll explain the engineering decision, give you the exact task, you implement it with Antigravity/Gemini/Claude Code, test it, commit it, and then we move forward.

MAYA — Build-to-Production Roadmap
The final product

Our target is:

                         ┌──────────────────────┐
                         │        MAYA          │
                         │   Desktop Assistant  │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────▼───────────────┐
                    │         AGENT MANAGER         │
                    │                               │
                    │ Planner • Executor • Evaluator│
                    └───────────────┬───────────────┘
                                    │
          ┌─────────────────────────┼────────────────────────┐
          │                         │                        │
          ▼                         ▼                        ▼
      🧠 BRAIN                   🧠 MEMORY                 🛠 TOOLS
      Gemini                    Short-term                Files
      OmniRoute                 Long-term                 Terminal
      Other models              Episodic                  Browser
                                Procedural                VS Code
                                                          Git
                                                          Windows
                                                          Google
          │                         │                        │
          └─────────────────────────┼────────────────────────┘
                                    │
                                    ▼
                           WORKFLOW ENGINE
                                    │
                                    ▼
                         PATTERN / LEARNING LAYER
                                    │
                                    ▼
                              MAYA DASHBOARD

Eventually you should be able to say:

"MAYA, prepare my day."

and have it:

Calendar
   ↓
Tasks
   ↓
Important emails
   ↓
Pending MAYA work
   ↓
Recent projects
   ↓
Generate briefing

Or:

"MAYA, continue working on my Django project."

and it can inspect the project, understand its current state, use tools, run tests, report what it did, and ask before sensitive actions.

That's the destination.

PHASE 0 — Engineering Foundation

Goal: Create a professional software project before writing the actual AI.

Deliverables
Git repository
Project structure
Python environment
Configuration system
Logging
Documentation
Product requirements
Master backlog
Development workflow
Testing framework
PHASE 1 — MAYA Core

Goal: MAYA can communicate with an online model.

Architecture:

User
 ↓
MAYA
 ↓
Model Gateway
 ↓
OmniRoute
 ↓
Gemini / other model
 ↓
MAYA
 ↓
User

Deliverables:

model abstraction
OmniRoute integration
structured messages
configuration
error handling
model selection
PHASE 2 — Actual Agent

This is where MAYA stops being a chatbot.

USER
 ↓
UNDERSTAND
 ↓
PLAN
 ↓
SELECT TOOL
 ↓
EXECUTE
 ↓
OBSERVE
 ↓
EVALUATE
 ↓
RESPOND

Deliverables:

planner
agent loop
tool registry
tool execution
execution state
error recovery
task history
PHASE 3 — MAYA Gets Hands

First tools:

Filesystem
Terminal
Process management
Git
VS Code/project inspection

Example:

"Find why my Django server isn't starting."

MAYA:

Inspect project
       ↓
Read configuration
       ↓
Inspect terminal
       ↓
Identify error
       ↓
Explain
       ↓
Suggest fix
       ↓
Ask permission
       ↓
Apply fix
       ↓
Run test
PHASE 4 — Memory

We'll create several memory layers.

                 MEMORY
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
   Working       Long-term     Episodic
   Memory        Memory        Memory
       │            │            │
       └────────────┼────────────┘
                    ▼
              Procedural
                Memory

MAYA can remember things such as:

"This is the user's MAYA project."

"This project uses Python."

"This workflow was previously successful."

"The previous approach failed."

Importantly, memory is not the same as retraining the model.

We're giving the model useful context at runtime.

PHASE 5 — Permission & Security

This comes before serious automation.

MAYA gets permission levels.

READ
read files
inspect projects
read calendar
read approved messages
WRITE
create files
modify code
create documents
EXECUTE
run commands
run tests
start applications
EXTERNAL ACTION
send email
create calendar event
send message
push Git
DESTRUCTIVE
delete files
remove repositories
system changes

Sensitive operations require confirmation.

We'll also have:

Audit Log
Emergency Stop
Tool Permissions
Secret Management
PHASE 6 — Desktop Dashboard

Now we make MAYA visually real.

Something like:

┌──────────────────────────────────────────────────┐
│ MAYA                              ● ONLINE       │
├──────────────────────────────────────────────────┤
│                                                  │
│  Good morning.                                   │
│                                                  │
│  ┌────────────────────────────────────────────┐  │
│  │ What should I do?                         │  │
│  │ > ______________________________________   │  │
│  └────────────────────────────────────────────┘  │
│                                                  │
│  ACTIVE TASK                                     │
│  ──────────────────────────────────────────────  │
│  MAYA Development                               │
│  ███████████████░░░░                            │
│                                                  │
│  AGENTS                    MEMORY                │
│  ● Development            1,248 memories        │
│  ● Research                  23 workflows       │
│  ● Productivity                                   │
│                                                  │
│  ACTIVITY                                        │
│  ✓ Inspected project                            │
│  ✓ Read configuration                           │
│  → Running tests                                │
│                                                  │
└──────────────────────────────────────────────────┘

The UI comes after the underlying system works.

This prevents us from spending weeks building a beautiful interface around a broken agent.

PHASE 7 — Agent Manager

Now we introduce specialized agents.

                 MAYA
                  │
             AGENT MANAGER
                  │
      ┌───────────┼────────────┐
      ▼           ▼            ▼
 Development   Research   Productivity
      │           │            │
      ▼           ▼            ▼
    Coding      Search       Calendar
    Git         Analysis     Tasks
    VS Code     Research     Planning

Later:

Communication Agent
System Agent
College Agent
Personal Knowledge Agent

But we don't build those prematurely.

PHASE 8 — Google Environment

Now MAYA enters your real digital environment.

We'll build integrations individually.

First:

Google Calendar

Example:

"Find me a free 30-minute slot tomorrow afternoon."

MAYA:

Calendar
 ↓
Find availability
 ↓
Present options
 ↓
You approve
 ↓
Create event

Then:

Gmail

Read
 ↓
Categorize
 ↓
Summarize
 ↓
Draft
 ↓
Ask approval
 ↓
Send

We'll handle authentication and permissions properly rather than giving MAYA unrestricted access.

PHASE 9 — Windows Environment

MAYA becomes a genuine desktop assistant.

Potential capabilities:

Launch applications
Read approved notifications
Inspect files
Manage development processes
Open projects
Control approved workflows

Phone Link can be investigated as a Windows integration, but we'll treat it as one integration, not the foundation of the architecture.

The architecture should remain:

MAYA
 ↓
Integration Interface
 ↓
Windows / Google / Phone Link / etc.

rather than:

MAYA → Phone Link → everything

That keeps the system maintainable.

PHASE 10 — Workflow Engine

This is where your "automate my repetitive work" idea becomes real.

A workflow:

TRIGGER
   ↓
CONDITIONS
   ↓
ACTIONS
   ↓
VALIDATION
   ↓
RESULT

Example:

Morning briefing
08:00
 ↓
Calendar
 ↓
Tasks
 ↓
Important emails
 ↓
MAYA project status
 ↓
Generate briefing
 ↓
Show dashboard

Another:

Start development environment
Trigger:
"Start my MAYA workspace"

↓

Open VS Code
↓

Open MAYA project
↓

Check Git status
↓

Activate environment
↓

Start required processes
↓

Check health

↓

Report
PHASE 11 — Pattern Learning

Only now.

MAYA watches approved activity patterns, not everything blindly.

Suppose you perform:

Open VS Code
 ↓
Open project
 ↓
Open terminal
 ↓
Activate environment
 ↓
Run server

20 times.

MAYA can detect:

"This appears to be a repeated workflow."

Then:

┌─────────────────────────────────────────┐
│ MAYA detected a repeated workflow       │
│                                         │
│ "Start Django workspace"                │
│                                         │
│ Detected: 8 times                      │
│                                         │
│ Create automation?                     │
│                                         │
│ [Approve] [Modify] [Ignore]            │
└─────────────────────────────────────────┘

MAYA doesn't secretly rewrite itself.

It proposes improvements.

You approve them.

That's how we make the system progressively smarter without making it unpredictable.

PHASE 12 — Reliability

Before calling it production:

Unit Tests
Integration Tests
Agent Tests
Tool Tests
Permission Tests
Failure Recovery
Timeouts
Logging
Monitoring
Database Backups
Configuration Validation

We also test things like:

What happens if Gemini is unavailable?

What happens if OmniRoute fails?

What happens if a tool crashes?

What happens if the model gives invalid tool arguments?

What happens if MAYA gets stuck in a loop?

What happens if the user closes MAYA during execution?

These are real agent-engineering problems.

PHASE 13 — Production

Finally:

MAYA v1.0

We'll produce:

Installer
Configuration
Documentation
Release notes
Versioning
Logs
Recovery
Backup
Security review

And a GitHub release.

Our actual development methodology

We're going to run MAYA like a real Agile project.

Product Backlog

Every feature gets an ID.

MAYA-001
MAYA-002
MAYA-003
...

Example:

MAYA-001
Initialize repository

MAYA-002
Create Python environment

MAYA-003
Implement configuration manager

MAYA-004
Implement logging

MAYA-005
Create model gateway

MAYA-006
Connect OmniRoute
Every ticket gets
User Story
↓
Acceptance Criteria
↓
Technical Design
↓
Implementation
↓
Tests
↓
Documentation
↓
Commit

Example:

MAYA-006

User Story

As MAYA, I need access to the model gateway so that I can use online reasoning models.

Acceptance criteria

[ ] MAYA can send a prompt
[ ] MAYA receives a response
[ ] Model configurable through environment
[ ] Timeout handled
[ ] API/model errors handled
[ ] Logs generated
[ ] Tests written

Then:

git commit -m "feat: connect MAYA to OmniRoute"
Git workflow

We'll use:

main
  │
  └── develop
        │
        ├── feature/model-gateway
        ├── feature/agent-loop
        ├── feature/memory
        └── feature/google-calendar

And conventional commits:

feat:
fix:
refactor:
test:
docs:
chore:

Your Git history will eventually tell the story of the entire product.

Our MAYA documentation

The repository should contain:

MAYA/
│
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
│
├── docs/
│   ├── PRD.md
│   ├── architecture.md
│   ├── agent-runtime.md
│   ├── memory.md
│   ├── tools.md
│   ├── security.md
│   ├── integrations.md
│   ├── workflows.md
│   ├── testing.md
│   └── decisions/
│
├── src/
├── tests/
├── scripts/
└── config/

This is important for your portfolio.

You're not just saying:

"I built an AI assistant."

You're able to show:

"Here's the architecture, requirements, ADRs, test strategy, Git history, agent runtime, security model, integration architecture, and release process."

That's a completely different level of project.

How YOU and I will work on it

This is the part I want to keep simple.

You don't need to independently figure out the entire project.

For each ticket, I'll give you:

1. What we're building

Plain English.

2. Why we're building it

The engineering reasoning.

3. What you need to learn

Only the concepts necessary for that ticket.

4. Exact implementation plan

Files, modules, interfaces, etc.

5. Antigravity/Gemini prompt

You can give the implementation work to your coding agent.

6. Verification

Exactly what you should test.

7. Git commit

Exact commit message.

8. Documentation

What needs updating.

9. Review

You show me the result/errors, and we inspect it before moving on.

So you won't be blindly copying code.

🚀 TODAY: Sprint 0 starts here

We're going to actually start the project now, not just plan it.

Sprint 0 — MAYA Foundation
Sprint objective

Establish a professional development environment and repository for MAYA.

Sprint backlog
ID	Task	Priority
MAYA-001	Create Git repository	P0
MAYA-002	Create project directory	P0
MAYA-003	Initialize Python environment	P0
MAYA-004	Create architecture	P0
MAYA-005	Create configuration system	P0
MAYA-006	Create logging system	P0
MAYA-007	Create test infrastructure	P0
MAYA-008	Create PRD	P0
MAYA-009	Create master backlog	P0
MAYA-010	First successful MAYA startup	P0

But we're doing only MAYA-001 first.

STEP 1 — Create the MAYA workspace

Since you're on Windows and already use D:\CODE, open PowerShell.

Run:

cd D:\CODE
mkdir MAYA
cd MAYA

Verify:

pwd

You should see:

D:\CODE\MAYA
STEP 2 — Initialize Git

Run:

git init

Then:

git status

You should see something similar to:

On branch master/main
No commits yet

Don't worry about the branch name yet.

STEP 3 — Create the initial structure

Run:

mkdir src
mkdir tests
mkdir docs
mkdir scripts
mkdir config

Then:

mkdir src\maya
mkdir src\maya\core
mkdir src\maya\brain
mkdir src\maya\memory
mkdir src\maya\tools
mkdir src\maya\agents
mkdir src\maya\dashboard

We're deliberately keeping this structure clean.

STEP 4 — Create Python environment

Check Python:

python --version

Then:

python -m venv .venv

Activate it:

.\.venv\Scripts\Activate.ps1

Your terminal should now show something like:

(.venv) PS D:\CODE\MAYA>
STEP 5 — Create .gitignore

Create:

.gitignore

Put:

.venv/
__pycache__/
*.pyc
.env
.env.*
!.env.example

.pytest_cache/
.mypy_cache/
.ruff_cache/

logs/
data/

.vscode/
.idea/

*.db
*.sqlite
*.sqlite3

Important: We don't want API keys, personal credentials, databases, or environment secrets accidentally committed.

STEP 6 — Create the first README

Create:

README.md

For now, just:

# MAYA

MAYA is a personal AI agent manager designed to operate as a desktop AI assistant.

## Vision

MAYA will combine:

- Online AI models
- Multi-model routing
- Agent orchestration
- Persistent memory
- Tool execution
- Desktop automation
- Google integrations
- Workflow automation
- User-approved pattern learning
- A visual desktop dashboard

## Status

🚧 Early Development

## Development

MAYA is being developed incrementally using Agile software development practices.

We'll expand this later.

STEP 7 — First commit

Check:

git status

Then:

git add .

Commit:

git commit -m "chore: initialize MAYA project"

Now we've officially created the project.

STEP 8 — Don't connect Gemini yet

This is intentional.

We don't start coding the AI brain yet.

First we establish the foundation.

Our next ticket will be:

MAYA-004 — Architecture & core application skeleton

We'll decide exactly where:

Agent
Planner
Executor
Model Gateway
Memory
Tool Registry
Permissions

belong before we write those components.

That prevents the classic AI-project problem of ending up with:

main.py
main2.py
agent_final.py
agent_final2.py
memory_new.py
utils.py
utils2.py
please_work.py

😄

Our milestone map

Keep this as our master roadmap:

                    MAYA
                     │
        ┌────────────┴────────────┐
        │                         │
     FOUNDATION                 DESIGN
        │                         │
        ▼                         ▼
     SPRINT 0                 Architecture
        │
        ▼
      BRAIN
        │
        ▼
   AGENT RUNTIME
        │
        ▼
      TOOLS
        │
        ▼
     MEMORY
        │
        ▼
   PERMISSIONS
        │
        ▼
    DASHBOARD
        │
        ▼
  AGENT MANAGER
        │
        ▼
 GOOGLE / WINDOWS
        │
        ▼
   WORKFLOW ENGINE
        │
        ▼
  PATTERN LEARNING
        │
        ▼
   TESTING / HARDENING
        │
        ▼
     RELEASE
        │
        ▼
     MAYA v1.0

Your immediate task is only Steps 1–8.

Once you've done that, paste the output of:

git status
git log --oneline -1
tree /F

and we'll take MAYA-004: Architecture & Core Skeleton next. From that point onward, we'll build MAYA ticket-by-ticket rather than jumping around.

Today 11:54 AM
Pasted text.txt
Document
PS D:\CODE\MAYA_AI>  git status
On branch master
nothing to commit, working tree clean
PS D:\CODE\MAYA_AI> git log --oneline -1
f76791f (HEAD -> master) chore: initialize MAYA project
PS D:\CODE\MAYA_AI> tree /F


Perfect. MAYA's foundation commit is clean. ✅

You have:

Branch: master
Working tree: clean
Commit: f76791f
Message: chore: initialize MAYA project

So MAYA-001 → MAYA-003 are effectively complete.

One thing: your tree /F output didn't come through after the command, so I can't verify the directory structure yet. That's okay.

Before we move on

Run this once:

tree /F

and paste the output here.

Then we'll start MAYA-004 — Architecture & Core Skeleton.

This is an important step: we're going to design the actual internal architecture before asking Antigravity/Gemini to generate code.

We'll establish:

MAYA
│
├── Core
│   ├── Agent
│   ├── Planner
│   ├── Executor
│   └── Evaluator
│
├── Brain
│   └── Model Gateway → OmniRoute
│
├── Memory
│
├── Tools
│   └── Tool Registry
│
├── Agents
│
├── Security
│   └── Permission Manager
│
├── Dashboard
│
└── Infrastructure
    ├── Config
    ├── Logging
    └── Database

And we'll turn that into the first actual architecture document + ADRs + package structure + MAYA backlog tickets.

Don't install a bunch of packages or connect APIs yet. We're still laying the foundation.

the output is massive also includes the files from venv and othe unwanted files 

Yep — don’t paste the full tree /F. A Python venv can make it enormous.

We only need the project structure, excluding generated/unwanted directories.

From D:\CODE\MAYA_AI, run:

tree /F /A | Select-String -NotMatch "venv|__pycache__|\.git|\.pytest_cache|node_modules"

However, that can still show some unwanted files.

Better: show only the important project files

Run this:

Get-ChildItem -Recurse -File |
Where-Object {
    $_.FullName -notmatch '\\(\.git|venv|__pycache__|\.pytest_cache|node_modules)\\'
} |
ForEach-Object {
    $_.FullName.Replace((Get-Location).Path + "\", "")
}

That will give us something like:

README.md
.gitignore
src
src\maya
src\maya\main.py
tests
docs
...

Paste that output here.

Then I'll inspect the actual structure and we'll proceed with MAYA-004 — Architecture & Core Skeleton without randomly creating files or installing unnecessary packages.