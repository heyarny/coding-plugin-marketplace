---
name: entry-debug
description: "Use whenever the Debug plugin is selected. Route the request to the intended bundled workflow while keeping all dependencies internal to this plugin."
---

# Debug

This is the public entry workflow for this plugin. The bundled skills below are dependencies, not competing entry points.

## Mandatory routing

Use diagnosing-bugs for hard bugs flakes or regressions and debugging-and-error-recovery for general systematic diagnosis. Fix behavior with TDD. Use browser or performance tooling only when evidence points there and resolving-merge-conflicts only during an active conflict.

If a bundled workflow calls another bundled skill, read and apply that local bundled copy. Use the host's skill loader when available; otherwise read its linked `SKILL.md` directly. Never require the user to install another plugin to complete this workflow.

## Bundled workflows

- [diagnosing-bugs](../diagnosing-bugs/SKILL.md)
- [debugging-and-error-recovery](../debugging-and-error-recovery/SKILL.md)
- [tdd](../tdd/SKILL.md)
- [test-driven-development](../test-driven-development/SKILL.md)
- [codebase-design](../codebase-design/SKILL.md)
- [browser-testing-with-devtools](../browser-testing-with-devtools/SKILL.md)
- [resolving-merge-conflicts](../resolving-merge-conflicts/SKILL.md)
- [performance-optimization](../performance-optimization/SKILL.md)
