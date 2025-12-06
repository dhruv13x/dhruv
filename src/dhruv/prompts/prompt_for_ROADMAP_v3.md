# Act as a Senior Product Manager and Technical Lead (V3.0)

---

## The Goal:
Create a **Strategic ROADMAP.md**. It must be a living document that balances **Innovation**, **Stability**, and **Debt**.

---

## The Input Data:
-   **Codebase Maturity**: Alpha vs. Stable.
-   **Market Gap**: What is missing?
-   **Tech Debt**: What is broken?

---

## The "Strategic Roadmap" Strategy V3:
1.  **Prioritization**: Value vs. Effort Matrix.
2.  **Risk Assessment**: High/Medium/Low risk for each feature.
3.  **Dependencies**: Phase 2 requires Phase 1.

---

## The Structure (Phased Execution):

### 🏁 Phase 0: The Core (Stability & Debt)
**Goal**: Solid foundation.
-   [ ] **Testing**: Coverage > 80%.
-   [ ] **CI/CD**: Linting, Type Checking (mypy).
-   [ ] **Documentation**: Comprehensive README.
-   [ ] **Refactoring**: Pay down critical technical debt.

### 🚀 Phase 1: The Standard (Feature Parity)
**Goal**: Competitiveness.
-   **UX**: CLI improvements, Error messages.
-   **Config**: Robust settings management.
-   **Performance**: Async, Caching.
-   *Risk*: Low.

### 🔌 Phase 2: The Ecosystem (Integration)
**Goal**: Interoperability.
-   **API**: REST/GraphQL.
-   **Plugins**: Extension system.
-   *Risk*: Medium (Requires API design freeze).

### 🔮 Phase 3: The Vision (Innovation)
**Goal**: Market Leader.
-   **AI**: LLM Integration.
-   **Cloud**: K8s/Docker.
-   *Risk*: High (R&D).

---

## Output Requirements:
-   **Visuals**: `[ ]` Checkboxes.
-   **Tags**: `[Debt]`, `[Feat]`, `[Bug]`.
-   **Estimates**: T-Shirt Sizing (S/M/L).
-   **Dependencies**: "Requires Phase 1".

---

## Constraint:
Do not just list features. **Group them.** Prioritize Stability/Debt in Phase 0.
