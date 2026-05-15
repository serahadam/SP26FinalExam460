# Development Log – The Torchbearer

**Student Name:** Serah Adam 
**Student ID:** 12942808 

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [May 8th, 2026]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

I plan to first look over and understand the material and understand what is required of this final. As well as how Djikstra's algorithm will be used for precomputing shortest paths between important locations. After that, I will design the search algorithm that determines the best order for collecting relics while minimizing total fuel cost. I am assuming the most difficult parts to be managing the search state correctly and implementing pruning without removing optimal solutions. Testing my work by starting with small example graphs and manually verifying the expected shortest paths. 

---

## Entry 2 – [May 10th, 2026]: [Short description]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

While adding the search logic, I have realized my algorithm was revisiting relics that had already been collected because I was not updating the visited set correctly duiring backtracking. Which caused duplicating paths and incorrect total cost calculations. I fixed the issue by making sure relics were marked as collected before recursive calls and unmarked immediately after returning. Once I fixed it, the search explored only valid paths and produced more consistent results. 

---

## Entry 3 – [May 11th, 2026: [Short description]

Once the basic search worked, I focused on improving efficiency because the number of possible relic collection orders grew very quickly. I added a best so far cost tracker and a lower bound estimate to prune beanches that could not lead to a better answer. This significantly reduced teh number of states exploded and made the algorithm run faster on larger test case. I tested the cropped version against the orignal implementation to confirm both produced the same final answer.

---

## Entry 4 – [May 12th, 2026]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

After completing the project, I feel more comfortable combinibg shortest path algorithms with higher level strategies. If I had more time, I would improve the readability of my code by adding more helper functions and clearer comments. I would also like to create more automated test cases for edge conditions, such as disconnected graphs that very experience to reach. All in all, this project helped me beter understand how precomputation and pruning can make difficult optimization problems more manageable. 

---

## Final Entry – [May 13th, 2026]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 1  | 
| Part 2: Precomputation Design  | 1.5 | 
| Part 3: Algorithm Correctness |  1 | 
| Part 4: Search Design |  1.5 |  
| Part 5: State and Search Space  | 1 | 
| Part 6: Pruning  | 1 |
| Part 7: Implementation  | 3 | 
| README and DEVLOG writing | 1 | 
| **Total**  | 11 hours |  
