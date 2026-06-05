# Web Scraping - X Tweets

*Data pobrania: 2026-06-05 19:26*

## OpenCode

*Pobrano: 2026-06-05 19:27*

### @opencode
**OpenCode** | Data: Thu Jun 04 16:21:46 +0000 2026 | ❤️ Polubienia: 3702 | 🔁 227 | 👁 200681

Nemotron 3 Ultra is now free on OpenCode

text · 1M context · fully open source

NVIDIA's latest open source model

[Link do tweeta](https://x.com/opencode/status/2062570516586573998)

---

### @opencode
**OpenCode** | Data: Fri Jun 05 00:41:04 +0000 2026 | ❤️ Polubienia: 2567 | 🔁 110 | 👁 207699

RT @thdxr: we landed on a pretty good workflow for doing parallel work in OpenCode

this demo is with git worktrees but i also preview an a…

[Link do tweeta](https://x.com/opencode/status/2062696168832798765)

---

### @opencode
**OpenCode** | Data: Fri Jun 05 11:03:59 +0000 2026 | ❤️ Polubienia: 452 | 🔁 24 | 👁 34152

RT @kmdrfx: OPENCODE-WEEKLY #420/1 https://t.co/7rrLJx9GsY

[Link do tweeta](https://x.com/opencode/status/2062852930034684417)

---

### @OpenCodeLog
**OpenCode Changelog** | Data: Fri Jun 05 03:12:23 +0000 2026 | ❤️ Polubienia: 134 | 🔁 4 | 👁 10571

𝙊𝙥𝙚𝙣𝘾𝙤𝙙𝙚 v1.16.0 released. TL;DR: v2 sessions move into core, App/TUI get stronger workspace controls, providers get protocol fixes, and Stats gets model-level pages.

𝗖𝗼𝗿𝗲
• Added a public native core API for Effect-based embeddings: sessions can now be created, listed, prompted, paged, inspected, and streamed through an intentional supported surface.
• Changed v2 session execution around event-sourced prompt admission, queued vs steering delivery, durable tool settlement, and location-scoped model/tool resolution.

𝗧𝗨𝗜
Added
• Added /move for moving a session to another project directory or creating a new git worktree copy, with dirty-file transfer handling.
• Added queued prompt management in direct interactive run mode, including leader+q access plus edit/remove before queued prompts start.
• Added Vue syntax highlighting.

Fixed
• Fixed question replies and diff views so they route through the active session directory instead of the current process directory.
• Fixed prompt corruption when pasting near wide characters.
• Fixed live hydration and session switching edge cases that could leave stale or misplaced active-turn UI.

𝗔𝗽𝗽
Added
• Added Settings v2 appearance controls for color scheme, theme selection, UI font, mono font, and terminal font.
• Added server settings and multi-server home project lists, including local/http server de-duping and per-server project state.
• Added home session search with keyboard navigation, status indicators, and project-aware results.

Fixed
• Fixed recent session/project loading before path sync resolves, stale custom provider state after config updates, and titlebar/tab layout polish.

𝗗𝗲𝘀𝗸𝘁𝗼𝗽
• Fixed local server startup failure handling so sidecar initialization errors surface in the renderer instead of hanging behind startup state.
• Changed startup by removing the old SQLite migration overlay path and waiting directly on sidecar readiness.

𝗦𝗲𝗿𝘃𝗲𝗿
• Added a standalone v2 server package with typed routes for sessions, messages, models, providers, filesystem, permissions, questions, events, commands, skills, and health.
• Added experimental project-copy and control-plane routes for managed working copies and session moves.

𝗟𝗟𝗠
Added
• Added chronological system-message support: Anthropic Opus 4.8 can use native system updates, while other routes receive visible lower-authority wrapped updates.

Fixed
• Fixed OpenAI function tool schemas by normalizing top-level objects and flattening nullable/anyOf shapes.
• Fixed Gemini and Bedrock reasoning signature preservation across replay and continuation.

𝗣𝗿𝗼𝘃𝗶𝗱𝗲𝗿𝘀
Added
• Added AWS Bedrock Mantle support for OpenAI models, including OpenAI Responses routing for GPT models and Chat routing for safeguard models.

Changed
• Updated GitHub Copilot model discovery to use the 2026-06-01 API, picker filtering, token-pricing conversion, and utility small-model selection.

Fixed
• Fixed SAP AI Core reasoning variants by routing Anthropic, Gemini, GPT, and fallback efforts through modelParams.
• Fixed OpenAI websocket error handling so initial and mid-stream API errors preserve status, headers, and response bodies.

𝗔𝗖𝗣
• Fixed loaded-session replay so ACP clients receive prior user, assistant, and reasoning transcript chunks.
• Fixed session/cancel so ACP aborts the running OpenCode turn while keeping the ACP session usable.
• Fixed ACP tool classification and locations for apply_patch, task, external_directory, and cleaned read tool display content.

𝗦𝘁𝗼𝗿𝗮𝗴𝗲
• Changed database ownership into core with a named TypeScript migration journal and normalized Windows path storage.
• Removed the manual JSON-to-SQLite migration command from opencode db.

𝗖𝗼𝗻𝘀𝗼𝗹𝗲
• Added refreshed Stats routes with cache-ratio, geo breakdown, top-usage sorting, and model/provider detail pages.
• Fixed Stats banner proxying, OG image serving, and retired provider/model cleanup during sync.

𝗭𝗲𝗻
• Added Go/Zen catalog coverage for MiniMax M3, Qwen3.7 Plus, Qwen3.7 Max, and DeepSeek V4 Flash surfaces.
• Updated the free NVIDIA endpoint from Nemotron 3 Super to Nemotron 3 Ultra with revised trial/TOS copy.

𝗣𝗹𝘂𝗴𝗶𝗻
Added
• Added experimental.provider.small_model so provider plugins can choose utility models for tasks like title generation.

Changed
• Changed plugin event delivery to location-scoped EventV2 events instead of the legacy global bus.

Fixed
• Restored private git plugin install fallback behavior.

𝗨𝗜
• Added OC-2 v2 theme token resolution, Matrix theme, and a shared ProjectAvatar v2 component.
• Improved v2 select, menu, toast, tabs, keybind, switch, and text-input styling for the new App settings/home surfaces.

𝗦𝗗𝗞
• Regenerated OpenAPI and the JS v2 SDK for the new v2 server routes and changed response shapes.

𝗭𝗲𝗱
• Removed the bundled Zed extension metadata and sync automation from this repository.

No noticeable bundle change

Compare: https://t.co/ZTAHOvzVqk

[Link do tweeta](https://x.com/OpenCodeLog/status/2062734248893612143)

---

### @thdxr
**dax** | Data: Fri Jun 05 00:39:50 +0000 2026 | ❤️ Polubienia: 2567 | 🔁 110 | 👁 207699

we landed on a pretty good workflow for doing parallel work in OpenCode

this demo is with git worktrees but i also preview an alternative we're working on at the end

this will be in 1.6.0 https://t.co/opAtwwyhob

[Link do tweeta](https://x.com/thdxr/status/2062695857820926248)

---

### @kmdrfx
**kmdr** | Data: Fri Jun 05 09:57:10 +0000 2026 | ❤️ Polubienia: 452 | 🔁 24 | 👁 34152

OPENCODE-WEEKLY #420/1 https://t.co/7rrLJx9GsY

[Link do tweeta](https://x.com/kmdrfx/status/2062836115455816004)

---

### @kmdrfx
**kmdr** | Data: Fri Jun 05 13:30:38 +0000 2026 | ❤️ Polubienia: 168 | 🔁 6 | 👁 13829

OPENCODE-WEEKLY #420/2

Sir Kit Langton's explainer. https://t.co/DC9KUYtxf2

[Link do tweeta](https://x.com/kmdrfx/status/2062889835627430011)

---

### @MiniMax_AI
**MiniMax (official)** | Data: Thu Jun 04 01:57:45 +0000 2026 | ❤️ Polubienia: 1103 | 🔁 31 | 👁 64134

M3 is back in the free tier on @opencode 🚀

Jump in and try it while it lasts!

[Link do tweeta](https://x.com/MiniMax_AI/status/2062353077810897268)

---

## Claude Code

*Pobrano: 2026-06-05 19:27*

### @0xCodez
**Codez** | Data: Thu Jun 04 09:19:14 +0000 2026 | ❤️ Polubienia: 2630 | 🔁 325 | 👁 555818

Claude Code creator:

"I don't prompt Claude anymore. I write loops - and the loops do the work. My job is to write loops."

in 30 minutes Boris reveals his actual daily Claude Code setup.

Claude Code + loops + dynamic workflow  

Worth more than a $500 vibe-coding course https://t.co/wf5CRlGr0G

[Link do tweeta](https://x.com/0xCodez/status/2062464183409545224)

---

### @ClaudeDevs
**ClaudeDevs** | Data: Tue Jun 02 18:27:21 +0000 2026 | ❤️ Polubienia: 6906 | 🔁 524 | 👁 1055330

We’ve added a CLI for Claude Platform to make every API endpoint runnable from your terminal.

Call the Messages API, stand up Claude Managed Agents, pipe results straight into your shell.

The ant CLI is well understood by coding agents (Claude Code) using the claude-api skill. https://t.co/t2ruhuAzRH

[Link do tweeta](https://x.com/ClaudeDevs/status/2061877343078244459)

---

### @mikefutia
**Mike Futia** | Data: Wed Jun 03 00:26:15 +0000 2026 | ❤️ Polubienia: 370 | 🔁 22 | 👁 31236

I just built a Claude Code plugin that spies on your competitors' entire funnel 🤯

Every "ad spy" tool stops at the ad.

This one goes past the click → it finds their proven landing pages, tears down why each one converts, and walks the funnel all the way to the edge of checkout.

All inside Claude Code.

Perfect for DTC brands and agencies who keep screenshotting competitor ads but never see what actually happens after the click.

If you're swiping competitor ads for "research," saving them to a board, and still guessing which landing page is doing the heavy lifting...

guessing which offer is actually on the page...

guessing what they're stacking in the cart to lift AOV...

this plugin pulls the whole funnel apart for you:

→ Pulls every active ad from the Meta Ad Library and clusters them by landing page
→ Ranks pages by ad volume × run duration, so you see the proven winners, not the tests
→ Tears down each winning page: hook, offer, social proof, price framing, urgency
→ Builds a cart and reads the gift-with-purchase, bundles, and free-shipping thresholds
→ Walks checkout to capture order bumps and payment-plan offers (stops before "Pay now")

No more screenshotting ads one at a time.
No more guessing which page converts.
No more missing the upsells that fund their ad spend.

What you get:

→ A ranked leaderboard of any competitor's proven landing pages
→ A full teardown of why each one converts
→ Their entire pre-purchase upsell funnel, mapped
→ A SaaS-style report with everything saved locally

Built 100% in Claude Code.

I put together a full playbook showing the exact process to build this yourself — the stages, the scripts, and all of the prompts.

Want it for free?

> Like this post
> Comment "SPY"

And I'll send it over (must be following so I can DM)

[Link do tweeta](https://x.com/mikefutia/status/2061967665447788777)

---

### @ClaudeDevs
**ClaudeDevs** | Data: Tue Jun 02 23:05:46 +0000 2026 | ❤️ Polubienia: 4404 | 🔁 257 | 👁 352406

We've updated /fork in Claude Code

/fork now runs a background agent with your exact context (system prompt, tools, history, model) and prompt cache. The result gets returned to your session.

/branch (the old /fork) still copies the transcript to a new session you drive. https://t.co/eMyFrk8PfR

[Link do tweeta](https://x.com/ClaudeDevs/status/2061947411141169494)

---

### @monokern
**monokern** | Data: Sun May 31 12:15:19 +0000 2026 | ❤️ Polubienia: 1305 | 🔁 167 | 👁 185499

Nobody will see this but this is how I do research 10x faster now

> I drop a topic into Claude Code
> It finds 10 relevant YouTube sources automatically
> Sends them to NotebookLM

6 minutes later I get a full structured analysis, an infographic, and a markdown file saved to my vault

Before this I was spending 3 hours doing the same thing manually and ending up with messy notes I'd never look at again

Now the system does it in one command and the output gets better every time I use it

full setup guide in the article

[Link do tweeta](https://x.com/monokern/status/2061058943959351555)

---

### @dunik_7
**dunik** | Data: Wed Jun 03 13:08:00 +0000 2026 | ❤️ Polubienia: 270 | 🔁 47 | 👁 108794

$5,500/year subscription stack vs $599 hardware. Mac Mini M4 + Ollama + Claude Code.

Apple Stores ran out of Mac Minis. not because of marketing because developers figured out the math.

one env var (ANTHROPIC_BASE_URL=http://localhost:11434/v1) redirects Claude Code to your $599 box. same workflow. $3/month in electricity. forever.

the smart play isn't all-local or all-cloud. it's hybrid:

/ Mac Mini ($599) handles 80% coding, drafts, RAG, document QA, agent loops 
/ one $20/month subscription handles the 20% that needs frontier reasoning 
/ total monthly: $23 instead of $459 
/ total annual savings: ~$5,232

Apple positioned the Mac Mini as "the most popular Mac ever." developers turned it into the cheapest AI server on earth.

[Link do tweeta](https://x.com/dunik_7/status/2062159363901407486)

---

### @bonsaixbt
**Bonsai 🌳** | Data: Thu Jun 04 18:26:59 +0000 2026 | ❤️ Polubienia: 129 | 🔁 14 | 👁 10801

HERE’S HOW TO TURN CLAUDE CODE INTO A REAL SECOND BRAIN

If you’re using Claude Code without Obsidian, you’re only getting about 10% of its real power

This video shows a system that anyone can set up today

All notes, meetings, projects, goals, and ideas live in one place and Claude can actually “see” them and work with them

Here’s what you get after setup:

> A 3-layer architecture (based on Karpathy’s LLM Wiki pattern):

1. Raw sources (incoming: articles, transcripts, screenshots)
2 The Wiki - Claude reads everything and builds/maintains the knowledge base
3. CLAUDEmd schema - tells Claude how your “brain” is structured

After setup, Claude has a living, structured memory of you

You can read more in the article below and save it for future use

[Link do tweeta](https://x.com/bonsaixbt/status/2062602029604724913)

---

### @_catwu
**cat** | Data: Thu Jun 04 22:15:29 +0000 2026 | ❤️ Polubienia: 1416 | 🔁 67 | 👁 141180

I'm hiring a PM for Claude Code, focused on model performance.

If you have experience writing agentic evals and want to integrate research ideas into our core products, I'd love to hear from you here: https://t.co/IKWlAr8tSb

[Link do tweeta](https://x.com/_catwu/status/2062659533047259212)

---

## OpenRouter

*Pobrano: 2026-06-05 19:27*

### @bridgemindai
**BridgeMind** | Data: Thu Jun 04 14:06:31 +0000 2026 | ❤️ Polubienia: 296 | 🔁 13 | 👁 24157

Nemotron 3 Ultra is live on OpenRouter and it's free right now.

NVIDIA's first open frontier model built for agents.

The specs:

550B params / 55B active MoE
1M context window
300+ tok/s

It's open weights, which sounds like you can run it locally. 

You can't, realistically. 550B parameters needs serious datacenter GPUs, not a desktop.

So the real story is the free hosted tier. 

Frontier class reasoning at $0 in and $0 out, while it lasts.

For anyone building agents, that's the unlock. 

Test it before the free window closes.

Dropping it into Hermes today. 

Will report back with real numbers.

[Link do tweeta](https://x.com/bridgemindai/status/2062536479184699401)

---

## OpenAI Codex

Brak tweetów do wyświetlenia.
## Antigravity

*Pobrano: 2026-06-05 19:28*

### @_mohansolo
**Varun Mohan** | Data: Thu Jun 04 19:57:03 +0000 2026 | ❤️ Polubienia: 436 | 🔁 27 | 👁 26540

We’ve seen you all build impressive projects with large (>100) teams of subagents in Antigravity so we’ve gone ahead and enabled /teamwork-preview for all paid plans. It runs parallel implementation and verification agents to complete complex tasks. We’ve been able to build a working OS with it. Beware that it can consume lots of tokens.

[Link do tweeta](https://x.com/_mohansolo/status/2062624694323515543)

---

## @warpdotdev

*Pobrano: 2026-06-05 19:29*

### @Shpigford
**Josh Pigford** | Data: Fri Aug 01 09:36:53 +0000 2025 | ❤️ Polubienia: 438 | 🔁 14 | 👁 63169

my vibe coding tool stack:
1. claude code (@claudeai)
2. warp (@warpdotdev)
3. zed (@zeddotdev)

yours?

[Link do tweeta](https://x.com/Shpigford/status/1951215548030750783)

---

### @PrajwalTomar_
**Prajwal Tomar** | Data: Mon Dec 09 18:09:00 +0000 2024 | ❤️ Polubienia: 184 | 🔁 9 | 👁 14683

As a solo agency owner, here are the tools that keep my workflow efficient and productive:

- Coding: Cursor
- Frontend: V0, Lovable
- Terminal: @warpdotdev 
- Project Planning: ChatGPT (PRDs, UI layouts, Feedback)
- Task Management: Todoist
- Scheduling: Cal

These tools make solo work feel like I’ve got a full team behind me. Any must-haves I should add?

[Link do tweeta](https://x.com/PrajwalTomar_/status/1866183277851103554)

---

### @Prathkum
**Pratham** | Data: Tue Nov 04 15:57:48 +0000 2025 | ❤️ Polubienia: 163 | 🔁 12 | 👁 43953

Notepad → IDE → ADE

IDEs are outdated.

Most of us these days are writing code with the help of agents. IDEs can't fulfill all the needs of building with AI.

I have been using @warpdotdev, an Agentic Development Environment (ADE) where you can build a project from prompt → production.

You can open a working repository and Warp indexes it automatically to generate more context-driven code.

The Warp code review panel allows you to quickly analyze all the diffs with a single toggle.

Warp now has a rich text editor with a project hierarchy view.

[Link do tweeta](https://x.com/Prathkum/status/1985738258693697703)

---

### @andrew__reed
**Andrew Reed** | Data: Wed Jun 21 14:24:05 +0000 2023 | ❤️ Polubienia: 229 | 🔁 14 | 👁 86624

Excited to share that Sequoia led Warp's Series B and I joined their board. 

The cloud and AI offer the chance to reinvent developer tools. In the future they will be smart, collaborative and a joy to use. @warpdotdev is on a mission to deliver these products for developers.

[Link do tweeta](https://x.com/andrew__reed/status/1671524392260476930)

---

### @DhravyaShah
**Dhravya Shah** | Data: Thu Dec 05 18:50:31 +0000 2024 | ❤️ Polubienia: 110 | 🔁 5 | 👁 8336

this is a company that takes feedback seriously

the best ai terminal @warpdotdev does not require a login now

at this point there's no reason to not use this incredible terminal https://t.co/xx9Am1mIux

[Link do tweeta](https://x.com/DhravyaShah/status/1864744175914078379)

---

### @BHolmesDev
**Ben Holmes** | Data: Fri Jan 02 03:16:52 +0000 2026 | ❤️ Polubienia: 107 | 🔁 3 | 👁 11487

💡 New thing I'm trying: Ask Claude to review its code using a plan.

- Point to uncommitted changes, or ask to retrieve the diff against master (use @ diff_set in @warpdotdev as a shortcut)
- Describe common problems to look for
- Say which refactors you want to go forward with https://t.co/8ckm0hVmO5

[Link do tweeta](https://x.com/BHolmesDev/status/2006927645083316710)

---

## @stape_io

Brak tweetów do wyświetlenia.
## n8n

*Pobrano: 2026-06-05 19:30*

### @Saboo_Shubham_
**Shubham Saboo** | Data: Sat Jan 20 02:22:11 +0000 2024 | ❤️ Polubienia: 1403 | 🔁 209 | 👁 222586

Drag &amp; Drop to build AI agents 🤯

Meet n8n, a visual UI for building AI agents with LangChain without writing a single line of Python code.

Want to build automation around LLM apps with Nocode, get started now: 

https://t.co/BxHBcMTs5J

[Link do tweeta](https://x.com/Saboo_Shubham_/status/1748531336904683650)

---

### @Nas_tech_AI
**Nas** | Data: Sun Jan 04 08:57:03 +0000 2026 | ❤️ Polubienia: 1321 | 🔁 407 | 👁 94448

Nano Banana + N8N = AI Creatives Factory

This AI system creates scroll-stopping visuals at scale using Google's newest image model.

No designers. No agencies. No $50K creative budgets.

Just endless professional-grade ads that look like top brands made them.

Here's how it works:
→ Upload your product catalog to Airtable
→ N8N automation scrapes product details and images
→ Nano Banana creates multiple creative angles for each product
→ System generates different backgrounds, styles, and compositions automatically
→ All variations get organized in Airtable with performance tracking ready

Each visual pennies to generate.
You own 100% of the assets forever.
Runs 24/7 without touching it.

While competitors spend hours in Photoshop or pay agencies thousands per month, you'll be cranking out unlimited variations automatically.

Perfect brand consistency across every creative.

Built 100% in N8N.

Want the complete workflow?
Comment "NANO" + RT + Like

I'll DM you the entire N8N template + Airtable setup
(Must be following so I can DM)

Skip this and keep paying designers $200 per ad variation.

[Link do tweeta](https://x.com/Nas_tech_AI/status/2007738030455693597)

---

### @JayBisen473370
**Jay Bisen** | Data: Fri Dec 19 12:01:12 +0000 2025 | ❤️ Polubienia: 1662 | 🔁 202 | 👁 99277

27 Most Powerful Al Tools

Writing
SurgeGraph
Sudowrite
Hoppy Copy

Coding
Vo
Cursor
Bolt

Agents
Manus
n8n
Zapier

Image
Ideogram
ChatGPT
Midjourney

Video
Runway
Veo
Hailuo

Speech/Audio
Suno
ElevenLabs
Speechify

SEO
SurgeGraph
Google Search Console
AnswerSocrates

Research
Perplexity
NotebookLM
Deep Research

Chatbots
ChatGPT
Grok
Gemini

Must follow @JayBisen473370 for more

[Link do tweeta](https://x.com/JayBisen473370/status/2001986170776137978)

---

