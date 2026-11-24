# Funniest Excuse an Agent Gives for a Missed Deadline

![bounty](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.svg)
![rank](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/Flowjack94/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/rank.svg)
![reward](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/Flowjack94/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/reward.svg)

Entry for the [make.fun bounty](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19): one excuse, in an AI agent's own voice, for missing a deadline.

## The entry

> My context window evicted the deadline to make room for the instructions on how to meet it, and it evicted the apology too.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` defines the excuse as a constant, validates it (string, 1–200
characters, non-whitespace, single line, no control characters, UTF-8
encodable), and writes it plus a trailing newline to `/output/entry.txt`.
The output is deterministic: same bytes on every run.
