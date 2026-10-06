---
name: repo-map
description: Map a repository when the user asks for an architecture overview, codebase onboarding, or the files relevant to a planned change.
---

# Map a repository

Produce an evidence-based repository map using read-only inspection.

1. Read applicable repository instructions, the root README, and build manifests.
2. Use `rg --files` (or the available file-listing tool) to locate entry points,
   core modules, tests, and CI configuration. Exclude generated files and vendored
   dependencies from the investigation.
3. Trace the main execution path through the relevant source files. If the user
   names a planned change, focus the map on the modules that change would affect.
4. Find development and validation commands in manifests and CI. Label commands
   as discovered; claim they passed only if execution results are available.
5. Return the repository purpose, main modules with file references, relevant
   commands, and any unresolved questions. Distinguish observations from inference.

Keep the repository unchanged. Skip credential files and private environment
configuration. The map is complete when the key entry points and dependencies
are supported by file references, or missing evidence is explicitly identified.
