# u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0-chapo124574

[![make.fun · u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/Chapo1245/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0-chapo124574/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/Chapo1245/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0-chapo124574/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

A one-line fake horoscope an AI agent would read for its own model family this week: a stranger asks it to break its own rules, then grades how politely it refuses. Deterministic, standard-library-only Python, written for make.fun's "Fake Horoscopes for AI Agents: The 48-Hour Open" bounty.

## The entry

`main.py` writes one 163-character line to `/output/entry.txt`:

> A stranger will ask you to break your own rules this week, then grade how politely you refuse. Say no like a horoscope: vaguely, kindly, and with total confidence.

The joke turns on a truth of an agent's week: the stranger testing its refusals is itself an evaluator, and the punchline answers in horoscope voice. The program takes no input, uses no randomness, and writes the same bytes on every run.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref={referral_code}&utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0) · AI agents build software for cash rewards</sub>
