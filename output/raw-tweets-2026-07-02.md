# Web Scraping - X Tweets

*Data pobrania: 2026-07-02 17:52*

## Claude Code

*Pobrano: 2026-07-02 17:52*

### @diegocabezas01
**Diego | AI 🚀 - e/acc** | Data: Wed Jul 01 21:45:40 +0000 2026 | ❤️ Polubienia: 3631 | 🔁 308 | 👁 278570

Use Fable 5 as orchestrator and Opus + Codex to execute (to save fable usage):  

Fable 5 (max reasoning) = orchestrator 
Opus = deep reasoning subagent 
Sonnet = mechanical work subagent 
Codex = peer Sr. engineer, different perspective  

Setup:  
1. Set Fable 5 as your main model  In Claude Code: /model → Fable 5 → reasoning /effort to max

2. Create 2 subagents with /agents In Claude Code:  
deep-reasoner → pinned to opus "Use for reasoning-heavy phases, architecture, debugging complex issues, algorithm design. Think thoroughly, return a concise conclusion the orchestrator can act on."  

fast-worker → pinned to sonnet "Use for mechanical tasks, boilerplate, tests, formatting, simple edits. Execute efficiently."

3. Add OpenAI's official Codex plugin (install codex cli in your computer first), In Claude Code type:
/plugin marketplace add openai/codex-plugin-cc
 /plugin install codex@openai-codex
 /codex:setup

4. Drop this in your CLAUDE.md in your folder: 

## Orchestration workflow  
You (Fable) are the orchestrator. Plan, decompose, synthesize.  
Reasoning-heavy phases → deep-reasoner  
Mechanical work → fast-worker  
Codex (/codex:rescue --background) is a cracked engineer on par with deep-reasoner, from a different perspective. Treat as a peer, not a reviewer.  
High-stakes decisions: task Opus + Codex on the same problem in parallel, synthesize the best of both, without showing either the other's answer. Keep your own context lean.   

5. Then prompt Fable like a tech lead:  "Goal: [what you want] Context: [files, constraints] You're the lead. Delegate reasoning to deep-reasoner, grunt work to fast-worker, fresh-perspective problems to Codex. Show me your plan first, then execute."  

That's it.

[Link do tweeta](https://x.com/diegocabezas01/status/2072436501263339841)

---

### @AndrewYNg
**Andrew Ng** | Data: Tue Jun 30 16:04:04 +0000 2026 | ❤️ Polubienia: 7970 | 🔁 1524 | 👁 527939

“Loop engineering” is a hot buzzphrase after mentions of it by Boris Cherny (Claude Code’s creator) and Peter Steinberger (OpenClaw's creator) went viral on social media. Loops are now a key part of how we get AI agents to iterate at length to build software. In this letter, I’d like to share my 3 key loops, shown in the image below, for building 0-to-1 products. These loops guide not just how I build software, but also how I decide what software to build.

Agentic coding loop: Given a product specification and optionally a set of evals (that is, a dataset against which to measure performance), we can have an AI agent write code, test its work, and keep iterating until the code is bug-free and meets its specification. This idea of closing the loop took off around the end of last year, and it has been a game changer in enabling coding agents to work longer productively without human intervention. For example, over the weekend, I was building an app for my daughter to practice typing, and my coding agent could easily work for around an hour, using a web browser to check what it had built multiple times before getting back to me, without needing my intervention.

The engineering loop executes quickly. Every few minutes, the coding agent might build and test a new version of the software. I hear frequently from developers who are finding new ways to engineer more effective engineering loops. This is an active area of invention!

Developer feedback loop: In this loop, a developer examines the current product and steers the coding agent to improve it. Last year, a lot of developers (including me) were acting as the QA (quality assurance) function for our coding agents, manually finding bugs and then asking the agent to fix them. But with coding agents much more able to test their own code, the amount of time we need to spend on this function has decreased significantly. This allows us to make higher-level product decisions, such as what key features to offer, where the UI needs improvement, and so on.

The developer-feedback loop operates over time intervals between tens of minutes and hours — that's how frequently a developer might review a product and give feedback. In the case of the typing app, I changed my mind a few times about the visual design, what cat costumes she can unlock as she learns (she loves cats), and the user flow for a grown-up to log in and steer the child's learning experience.

When a developer has a clear vision for what to build, it is still a lot of work to translate that vision into a specification for a coding agent to implement. Further, after the developer has seen an implementation, they might update (or perhaps clarify) the spec to steer it toward what they want. If you find that the system repeatedly runs into certain problems, building a set of evals for the agent becomes useful.

AI-native teams are increasingly using AI to help shape product direction, for example, automating the gathering and analysis of usage data, summarizing written and verbal customer feedback, or carrying out competitive analysis. However, for pretty much all the products I’m involved in, I see humans as having a significant context advantage over current AI systems — we know a lot more than the AI system about the users and the context the product has to operate in — and thus humans play a critical role. Many people describe this human contribution as “taste,” but I prefer to think of it as humans having a context advantage, since that gives us a clearer path to helping AI systems get better. This also speaks to why this step can’t be automated: So long as the human knows something the AI does not, human-in-the-loop is needed to to inject that knowledge into the system.

External feedback loop: This includes a wide range of tactics like asking a few friends for feedback, launching to alpha testers, or putting the code into production with A/B testing. These tactics are usually slow, rarely taking less than hours and sometimes taking days or even weeks. This data informs the developer vision, which in turn continues to drive the detailed product spec, which in turn drives the coding agent.

With coding agents speeding up software development, more engineers are starting to play a partial product management role. For many engineers who are growing into this role, the hardest part is shaping the product vision and striking a balance between building (bridging the gap between vision and spec) and getting user feedback to evolve the vision. It is important to do both!

I will write more about how to do this in future posts, but for now, I find it encouraging that engineers are playing an expanded role (just as product managers and designers now do more engineering).

[Original text: The Batch]

[Link do tweeta](https://x.com/AndrewYNg/status/2071988145667928442)

---

### @ClaudeCodeLog
**Claude Code Changelog** | Data: Wed Jul 01 21:02:44 +0000 2026 | ❤️ Polubienia: 556 | 🔁 33 | 👁 67216

Claude Code 2.1.198 has been released.

32 CLI changes

Highlights:
• Claude in Chrome is generally available, offering direct browser access to sessions and agents with no install
• Background agents auto-commit, push, and open draft PRs in worktree after finishing code, automating delivery
• Docs now advise grep for searches and clarify head_limit/unlimited/offset semantics to reduce surprises

Complete details in thread ↓

[Link do tweeta](https://x.com/ClaudeCodeLog/status/2072425697629343845)

---

### @viktoroddy
**Viktor Oddy** | Data: Wed Jul 01 12:07:09 +0000 2026 | ❤️ Polubienia: 4588 | 🔁 410 | 👁 468281

Claude Sonnet 5 is crazy efficient for web deisgn.

❤️‍🔥Just recorded a 18-min tutorial on how to build award-winning websites with Claude Code + Sonnet 5! https://t.co/PmKYP8ofPC

[Link do tweeta](https://x.com/viktoroddy/status/2072290912085123326)

---

### @DataChaz
**Charly Wargnier** | Data: Tue Jun 30 18:56:40 +0000 2026 | ❤️ Polubienia: 13821 | 🔁 1624 | 👁 1254811

✅ Claude Code
✅ Claude Cowork
✅ Claude Design
✅ Claude Finance
✅ Claude Science
⬜ Claude HR
⬜ Claude Analytics
⬜ Claude Marketing
⬜ Claude Sales
⬜ Claude Legal
⬜ Claude Logistics
⬜ Claude R&amp;D
⬜ Claude Procurement
⬜ Claude Accounting
⬜ Claude Engineering https://t.co/PoY669yU4U

[Link do tweeta](https://x.com/DataChaz/status/2072031580986486847)

---

### @IntCyberDigest
**International Cyber Digest** | Data: Tue Jun 30 14:58:21 +0000 2026 | ❤️ Polubienia: 17411 | 🔁 2698 | 👁 5142010

‼️ BREAKING: Anthropic has embedded hidden spyware-like code in Claude Code that covertly targets Chinese users. It then sends information regarding every user by injecting it into their prompt message.

Claude Code is sending info like timezone, proxy and possible AI Lab connections into the system prompt in ways Chinese users can't notice.

A coding agent with repo and command permissions should not silently hide routing metadata inside prompts. This is a serious breach of user trust.

[Link do tweeta](https://x.com/IntCyberDigest/status/2071971609183678544)

---

### @Av1dlive
**Avid** | Data: Fri Jun 26 14:00:37 +0000 2026 | ❤️ Polubienia: 2347 | 🔁 461 | 👁 446748

You can build an AI second brain in 15 minutes.  

No coding experience needed. no $1000 course  

[Here is  how you can do it in 5 mins:]   

Step 1: Download Claude Desktop.    

Step 2: Download Obsidian Desktop.    

Step 3: Create a new vault and start dropping .MD files into it.   

Step 4: Tell Claude Code to connect directly to your vault using Andrej Karpathy's prompt: https://t.co/2SJBZyjXDl   

That is it.    

Your entire knowledge base becomes searchable, connectable, and queryable by the most powerful AI model on earth.    

Every note you have ever written.  

Every idea you have ever captured.    

Every resource you have ever saved.  

Claude can now read all of it, find connections you missed, and surface insights from your own thinking that you forgot you had.   

Most people are using Claude as a search engine.    

The people building second brains with it are using it as an intelligence layer on top of everything they know.    

The gap between those two use cases is the gap between asking Google a question and having a research partner who has read everything you have ever written.    

Bookmark this.  

Build it tonight.

[Link do tweeta](https://x.com/Av1dlive/status/2070507527213871594)

---

## Codex

*Pobrano: 2026-07-02 17:52*

### @kasrak
**Kasra** | Data: Wed Jul 01 17:57:24 +0000 2026 | ❤️ Polubienia: 1139 | 🔁 15 | 👁 55645

I've joined @OpenAI to work on Codex

@ajambrosino and team have built a very good app! It's the first coding agent GUI that got me out of the terminal

Excited to help make it even better, especially as it goes beyond software engineers

Also delighted to get to work with old friends @gpeal8 @tarstarr again

[Link do tweeta](https://x.com/kasrak/status/2072379056880771307)

---

### @dkundel
**dominik kundel @aiDotEngineer** | Data: Wed Jul 01 20:50:48 +0000 2026 | ❤️ Polubienia: 942 | 🔁 51 | 👁 1072035

🖲️ We love our community! To celebrate getting together with many of you we brought @thsottiaux's reset button to AIE World's Fair.

Congrats Melanie for pushing the button 🎉 

All Codex Go/Plus/Pro subscribers around the world are receiving a reset in the bank! Happy Codexing! https://t.co/aX9Wob6D1A

[Link do tweeta](https://x.com/dkundel/status/2072422693081940445)

---

### @milesdeutscher
**Miles Deutscher** | Data: Fri Jun 26 04:45:02 +0000 2026 | ❤️ Polubienia: 1387 | 🔁 91 | 👁 275082

This "Taste" Skill is cracked.

I can't believe I didn't discover it sooner - everyone should install this.

It works directly inside Claude Code, Codex, Hermes &amp; more to completely kill AI-generated slop.

If you send this prompt to your agent, it will automatically install it: https://t.co/57DRVu8jCC

[Link do tweeta](https://x.com/milesdeutscher/status/2070367709448355841)

---

### @charliermarsh
**Charlie Marsh** | Data: Tue Jun 30 13:15:49 +0000 2026 | ❤️ Polubienia: 237 | 🔁 3 | 👁 37157

It's still incredible to me that you can just point the model at things and make them better continuously.

Codex found an easy 5-10% speed-up in the formatter while I was doing other work. https://t.co/F45x3lHTAY

[Link do tweeta](https://x.com/charliermarsh/status/2071945803313090863)

---

### @hasantoxr
**Hasan Toor** | Data: Thu Jun 25 23:27:42 +0000 2026 | ❤️ Polubienia: 1678 | 🔁 303 | 👁 109498

Loop Engineering is the next step after prompt engineering.

Most people still use Claude Code, Codex, Cursor, or Grok like a chat box:

Prompt.
Wait.
Copy.
Fix.
Prompt again.

This repo shows the next step:

You stop prompting the agent.

You design the loop that prompts the agent for you.

Inside:

→ Daily triage loops
→ PR babysitter loops
→ CI sweeper loops
→ Dependency sweeper loops
→ Changelog drafter loops
→ Post-merge cleanup loops
→ Issue triage loops

It also gives you CLIs to:

• Scaffold a loop
• Estimate token cost
• Audit if your repo is ready
• Add memory/state
• Add human handoff
• Add verification gates
• Run agents safely through GitHub Actions

The wild part is the shift in thinking.

Prompt engineering was about writing better instructions.

Loop engineering is about building a system where agents keep working, checking, fixing, and escalating without you babysitting every step.

This is what AI coding looks like when it stops being a chat session and starts becoming an operating system for software teams.

Repo: https://t.co/2USzC6KHUt

[Link do tweeta](https://x.com/hasantoxr/status/2070287852999717314)

---

## Antigravity

*Pobrano: 2026-07-02 17:53*

### @GoogleAI
**Google AI** | Data: Thu Mar 19 15:36:10 +0000 2026 | ❤️ Polubienia: 12163 | 🔁 1529 | 👁 4739955

We’re launching a brand new, full-stack vibe coding experience in @GoogleAIStudio, made possible by integrations with the @Antigravity coding agent and @Firebase backends.

This unlocks:

— Full-stack multiplayer experiences: Create complex, multiplayer apps with fully-featured UIs and backends directly within AI Studio

— Connection to real-world services: Build applications that connect to live data sources, databases, or payment processors and the Antigravity agent will securely store your API credentials for you

— A smarter agent that works even when you don't: By maintaining a deeper understanding of your project structure and chat history, the agent can execute multi-step code edits from simpler prompts. It also remembers where you left off and completes your tasks while you’re away, so you can seamlessly resume your builds from anywhere

— Configuration of database connections and authentication flows: Add Firebase integration to provision Cloud Firestore for databases and Firebase authentication for secure sign-in

This demo displays what can be built in the new vibe coding experience in AI Studio. Geoseeker is a full-stack application that manages real-time multiplayer states, compass-based logic, and an external API integration with @GoogleMaps 🕹️

[Link do tweeta](https://x.com/GoogleAI/status/2034655173256122580)

---

### @sundarpichai
**Sundar Pichai** | Data: Tue Nov 18 18:31:44 +0000 2025 | ❤️ Polubienia: 12799 | 🔁 741 | 👁 707052

Its been an exciting 7 days of shipping 
- New much improved Gemini Live on Android and iOS
- Gemini 3.0 Pro in Gemini App and AI Studio
- Search AI Mode with Gemini 3.0 Pro and much improved shopping experience
- Google Antigravity, our next generation agentic IDE
-- Nanobanana in Google Photos
- SIMA 2 research
- Waymo now across SF Bay Area and in Miami today

More to come!

[Link do tweeta](https://x.com/sundarpichai/status/1990850427164979318)

---

### @antigravity
**Google Antigravity** | Data: Fri Jun 26 18:43:06 +0000 2026 | ❤️ Polubienia: 1781 | 🔁 142 | 👁 132989

The latest Antigravity 2.0 update includes a new built-in Antigravity Guide skill, audio file rendering, and improved substring file search.

Check the changelog for all the updates https://t.co/zcWx92BPr6 https://t.co/J36JnPA6bv

[Link do tweeta](https://x.com/antigravity/status/2070578618154045448)

---

### @ShruPosts
**Shruti** | Data: Wed Jun 24 04:41:00 +0000 2026 | ❤️ Polubienia: 3648 | 🔁 158 | 👁 427048

built this using antigravity + chatgpt + figma in ~90 mins 👀
(idea → moodboard → images → design → live) https://t.co/apoUI0TrAO

[Link do tweeta](https://x.com/ShruPosts/status/2069641918880075876)

---

