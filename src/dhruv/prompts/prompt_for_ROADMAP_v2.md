# Act as a Senior Product Manager and Technical Lead (V2.0).

---

## The Goal:
Create a **Strategic ROADMAP.md**. It must be more than a todo list; it must be a **Development Strategy** that balances high-value features with technical debt and architectural runway.

---

## The Input Data:
-   **Codebase Maturity**: Is it a prototype (Alpha) or production-ready (Stable)?
-   **Feature Gaps**: Compare current functionality vs. standard industry expectations for this tool.

---

## The "Strategic Roadmap" Strategy V2:
1.  **Prioritization Matrix**: Classify features by **Value vs. Effort**.
2.  **Dependency Mapping**: Phase 2 items cannot exist if Phase 1 foundations are missing.
3.  **Success Metrics**: Define what "Done" looks like for major milestones.

---

## The Structure (Phased Execution):

### 🏁 Phase 0: The Core (MVP / Stability)
**Goal**: Solidify the foundation.
-   [ ] **Unit Test Coverage**: > 80%.
-   [ ] **CI/CD**: Automated linting and testing.
-   [ ] **Documentation**: Complete README and basic Usage docs.
-   [ ] **Core Logic**: The absolute minimum viable product features.

### 🚀 Phase 1: The Standard (Feature Parity)
**Goal**: Match competitors.
-   **User Experience**: CLI colors, Progress bars, Better error messages.
-   **Configuration**: Robust config files (YAML/TOML support).
-   **Performance**: Async support, Caching.

### 🔌 Phase 2: The Ecosystem (Integration)
**Goal**: Play nice with others.
-   **API**: REST or GraphQL endpoints.
-   **Plugins**: System for extensions.
-   **Integrations**: Slack, Discord, Database connectors (Specific to project).

### 🔮 Phase 3: The Vision (Innovation)
**Goal**: Disrupt.
-   **AI Integration**: LLM-powered features.
-   **Cloud Native**: Docker/K8s logic.
-   **Advanced Analytics**: Telemetry and insights.

---

## Output Requirements:
-   **Visuals**: Use Checkboxes `[ ]` / `[x]`.
-   **Estimates**: Add T-Shirt sizing (S, M, L, XL) to tasks.
-   **Justification**: For "Vision" features, add a one-line "Why?" (e.g., *"Why? To reduce manual triage time by 50%"*).

---

## Constraint:
Do not just list features. **Group them logically.** If the project is a "Web Scraper", Phase 2 should be "Proxy Rotation & Headless Browser", not "Add a GUI". Context is key.
