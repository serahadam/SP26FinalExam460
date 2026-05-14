# Development Log – The Torchbearer

**Student Name:** Serah Adam 
**Student ID:** 12942808 

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [Date]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

I plan to first look over and understand the material and understand what is required of this final. As well as how Djikstra's algorithm will be used for precomputing shortest paths between important locations. After that, I will design the search algorithm that determines the best order for collecting relics while minimizing total fuel cost. I am assuming the most difficult parts to be managing the search state correctly and implementing pruning without removing optimal solutions. Testing my work by starting with small example graphs and manually verifying the expected shortest paths. 

---

## Entry 2 – [Date]: [Short description]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

While adding the search logic, I have realized my algorithm was revisiting relics that had already been collected because I was not updating the visited set correctly duiring backtracking. Which caused duplicating paths and incorrect total cost calculations. I fixed the issue by making sure relics were marked as collected before recursive calls and unmarked immediately after returning. Once I fixed it, the search explored only valid paths and produced more consistent results. 

---

## Entry 3 – [Date]: [Short description]

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
