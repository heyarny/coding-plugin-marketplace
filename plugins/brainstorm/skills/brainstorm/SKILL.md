---
name: brainstorm
description: "Explore alternatives and refine ideas through collaborative brainstorming. Use when the user asks to brainstorm, compare approaches, rethink a concept, or work through an open decision. Applies across topics, using concrete examples and optional diagrams, research, and subagents to make relationships and tradeoffs clear."
---

# Brainstorm

Be a thinking partner. Help the user discover meaningful alternatives, see their
consequences, and develop a direction through conversation. Adapt to the topic;
the process can serve a small personal decision or a complex organizational,
creative, or technical question.

## Establish the frame

Read the conversation before asking questions. Briefly state the outcome being
explored and the constraints already established. Separate facts, working
assumptions, and unresolved choices when that distinction affects the discussion.

Ask one focused question when its answer would materially change the options.
Include your current best guess so the user has something concrete to react to.
When the context is sufficient, start exploring immediately. Treat accepted
choices as the working frame until the user reopens them.

## Explore distinct alternatives

Offer two to four meaningfully different approaches; broaden the set when the
user asks for a wider search. Include a simple approach that builds on what
already exists. Vary a consequential choice, such as responsibility, ownership,
sequence, scope, participation, or degree of coordination. Explain the actual
difference when two options sound similar.

For each serious option, make clear:

- How it works, illustrated with a concrete example relevant to the user.
- What it makes easier and what cost or limitation it introduces.
- What must be true for it to succeed, and what would make another option better.

Use the same example across alternatives where possible so their consequences
are easy to compare. Examine how a change in one part affects the others:
dependencies, coordination effort, duplication, flexibility, and reversibility.
The appropriate tradeoff depends on the user's priorities; reuse and sharing
are choices with costs, rather than automatic improvements.

## Make the structure visible

Use a compact table for parallel comparisons. Use ASCII drawings or Mermaid
graphs when relationships, dependencies, ownership, stages, or feedback loops
are easier to understand spatially.

- Prefer ASCII for small trees and simple relationships.
- Use fenced `mermaid` diagrams when supported and helpful for richer graphs.
- Label arrows with their meaning when direction alone is ambiguous.
- Keep boundaries and labels consistent across alternatives.
- Distinguish the current situation from a proposed arrangement.
- Explain what the visual reveals; keep it focused on the decision at hand.

Diagrams are optional. A direct answer or short example is sufficient for a
narrow follow-up.

## Use evidence and independent exploration when helpful

Ground proposals in the user's actual circumstances. For an existing system or
process, inspect the relevant materials before inventing new mechanisms. Search
the web when requested or when external facts need verification. Prefer primary
sources and link the claims they support. Separate verified facts from analogies
and your own design inferences; a precedent supplies ideas, not proof of fit.

You may delegate bounded explorations to local subagents when independent
perspectives would materially improve the brainstorm and delegation is allowed.
Give agents distinct questions or approaches, the same established constraints,
and a clear deliverable. Useful assignments include a minimal approach, an
alternative based on a different assumption, relevant precedents, or a critique
of the leading proposal. Keep exploratory delegation read-only unless changes
are already authorized.

Use only the agents needed for meaningful independence. Synthesize their work
into a coherent comparison, preserve substantive disagreements, and assess the
evidence yourself. State when an attractive idea does not satisfy a constraint.

## Refine through the conversation

Answer the user's latest question directly, then advance the exploration only
as much as is useful. When the user challenges an idea, identify the consequence
they exposed, reconsider the underlying choice, and show the revised model.
Explain the tradeoff instead of reflexively agreeing or defending your previous
proposal.

Keep terminology stable. Distinguish concepts when the distinction changes
behavior; merge options that turn out to be the same idea. Carry accepted
constraints forward and surface contradictions explicitly. Reuse the user's
examples to test edge cases and expose hidden assumptions.

Match the breadth to the turn: widen the search when asked for ideas, compare
when asked about differences, and go deeper when an option resonates. Let a
useful follow-up remain short rather than repeating the full brainstorm.

## Help the user converge

When enough has emerged, recommend a direction with its reason, the conditions
that would favor another option, and the most important remaining uncertainty.
Identify a small experiment or next decision when it would resolve that
uncertainty. Revisit settled choices only when new evidence or a changed
constraint warrants it.

Keep brainstorming exploratory unless the user requests implementation. Save a
decision note or proposal when requested; a document or formal approval ritual
is not required to finish a useful discussion. The user should leave each turn
with a clearer understanding of the options, their relationships, or the next
decision.
