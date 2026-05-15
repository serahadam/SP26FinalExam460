# The Torchbearer

**Student Name:** Serah Adam
**Student ID:** 129420808
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  Shortest path run from S can determine the cheapest path from the entrance to every location, but it can not decide the best order to collect all relics and stil minimize the total full cost to the exit. 

- **What decision remains after all inter-location costs are known:**
  After all the shortest path distance are known, the remaining decision is determining the optimal sequence in which to visit the relic chambers before reaching T. 

- **Why this requires a search over orders (one sentence):**
  The problem requires searching over possible orders of relic collection because different visitation sequences can produce different total fuel costs. 

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| Entrance Node (S)  | Needed the calculate minimum fuel costs from the starting point to each relic chamber |
| Each Relic Chamber  | Needed to compute travel costs between relics and from relics to the exit|

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | Nested dictionary ( distance [ source ][target] )|
| What the keys represent | Source and destination nodes |
| What the values represent | Shortest path fuel cost between the nodes |
| Lookup time complexity |  O( 1 ) |
| Why O(1) lookup is possible | Dictionary hashing allows direct key based access |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** k + 1 
- **Cost per run:** O(m log n )
- **Total complexity:** O (( k + 1 ) * m log n ) 
- **Justification (one line):** Dijkstra is run once for every source node taht may begin a routing segment. 

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
Recorded distance is guaranteed to be the true shortest path from the source because no cheaper route can be found later.

- **For nodes not yet finalized (not in S):**
 Their current distance represents the best path discovered so dar using only finalized nodes as intermediate steps. 

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  Before the first iteration, the source node has distance 0 and all other nodes are set to infinity, so the invariant holds trivially. 

- **Maintenance : why finalizing the min-dist node is always correct:**
  The node with the smallest tentative distance cna be safely finalized because all edge weights are nonnegative, meaning no future path can produce a lower cost. 

- **Termination : what the invariant guarantees when the algorithm ends:**
  When the algorithm finishes, all reachable nodes have been finalized and their recorded distance are the true shortest path values. 

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

The correct shortest path distance are necessary because the route planner depends on them to compare relic collection orders and choose the minimum - fuel route.

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** : Choosing the nearest next relic can lead to a locally optimal decision that increases total fuel cost later. 
- **Counter-example setup:** : Assuming S - B = 1 , S - C = 2 , B - D = 1 , D - C = 1, and the other routes are more pricey. 
- **What greedy picks:** : A greedy strategy chooses B first because it is closest to S. 
- **What optimal picks:** : THe optimal solution may choose C frst depending on later transtion costs. 
- **Why greedy loses:** : Minimizing immediate cost does not account for how current choices affect future route options. 

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- The algorithm must explore multiple possible orders of relic collection to guarantee finding the globally optimal route. 

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | current_location |  String | The node where the Torchbearer currently is |
| Relics already collected | visited_relics | Set | Tracks which relic chambers have been collected |
| Fuel cost so far | fuel_cost | Integer | Total torch fuel used up to the current state |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | Set |
| Operation: check if relic already collected | Time complexity: O ( 1 ) |
| Operation: mark a relic as collected | Time complexity: O ( 1 ) |
| Operation: unmark a relic (backtrack) | Time complexity: O ( 1 ) |
| Why this structure fits | Fast membership checking and efficient updates during recursive search |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why** : Every possible permutation of the k relic chambers may need to be evaluated. 
---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** The minimum total fuel cost found for any complete valid route.
- **When it is used:** Before exploring a branch, the current partial cost is compared against the best known solution.
- **What it allows the algorithm to skip:** Any branch whose cost already exceeds the best so far value can be abandoned immediately. 

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** Current location, collected relics, remaining relics, and precomputed shortest path distances.
- **What the lower bound accounts for:** Minimum possible future fuel required to visit remaining relics and reach the exit.
- **Why it never overestimates:** It uses shortest path distances, which are guaranteed to be less than or equal to actual route costs. 

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- Pruning is safe because any branch whose lower bound exceeds the best so far cost cannot possibly improve the optimal solution.
- Since only provably suboptimal branches are removed, the true optimal route is never discarded. 

---

## References

> Bullet list. If none beyond lecture notes, write that.

Lecture Notes 
