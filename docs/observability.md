# Observability

A look at what observability means for a backend service, and why it matters even
for a project as small as this one.

## What "observability" means

A system is observable when you can understand what's happening inside it just by
looking at what it produces on the outside - without having to attach a debugger or
guess. The term comes from control theory, but in backend engineering it usually
boils down to a practical question: **when something goes wrong in production, can
you figure out why without reproducing it locally first?**

That question matters because production is the one environment you can't fully
control. Real traffic, real data, real concurrency, and real failures (a slow
downstream dependency, a connection pool exhausting itself, a bad deploy) all show
up there first, often in combinations no local test ever exercised.

## Monitoring vs. observability

The two terms get used interchangeably, but they answer different questions:

- **Monitoring** watches for problems you already know how to define - a dashboard
  tracking error rate, an alert firing when latency crosses a threshold. It answers
  "is the known thing happening?"
- **Observability** gives you the raw material to investigate problems you *didn't*
  anticipate. It answers "why is this new, weird thing happening?" - usually by
  letting you slice and correlate signals after the fact, rather than relying on a
  dashboard someone thought to build in advance.

Monitoring catches known failure modes. Observability is what lets you debug the ones
nobody wrote a dashboard for yet.

## The three pillars

Most observability work is built from three complementary types of signal:

- **Metrics** - numeric measurements aggregated over time (request counts, error
  rates, latency distributions). Cheap to store and great for dashboards and
  alerting, but they summarize - a spike in the 99th percentile latency tells you
  *that* something got slow, not *which* request or *why*.
- **Logs** - discrete, timestamped records of events, often with rich context. Great
  for reconstructing exactly what happened for a specific request, but expensive to
  store and search at scale, especially if left unstructured.
- **Traces** - the causal path a single request takes through a system, including
  time spent in each step. Especially valuable once a request crosses multiple
  services, where a log line in one service can't tell you what was happening in
  another at the same moment.

No single pillar is sufficient on its own. Metrics tell you *that* something is
wrong, logs and traces help explain *why*.

## Why it matters for a backend specifically

Backend services fail in ways that are invisible from the outside until they aren't:
a memory leak that only manifests after days of uptime, a query that's fast until a
table crosses a certain size, a downstream API that starts timing out intermittently
under load. None of these show up by reading the code - they show up in how the
system behaves over time, under real conditions.

Good observability turns incident response from guesswork into investigation. It also
pays off outside of outages: it's how you notice a slow regression before a user
complains, decide whether a service needs more capacity, or confirm that a change
actually improved things rather than just feeling like it did.

## A minimal starting point: RED

For a single HTTP service, a common and inexpensive starting point is the **RED**
method - tracking, per endpoint:

- **Rate** - how many requests are being handled
- **Errors** - how many of those requests are failing
- **Duration** - how long they're taking

It's a small set of signals, but it's usually enough to answer the first question in
any incident: *is this service healthy right now?* Everything else - logs, traces,
more detailed metrics - tends to get layered on once that baseline exists.

## In this project

Backend Playground instruments its API with a basic set of RED-style request metrics
as a small, concrete example of this in practice.
