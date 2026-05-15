"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Serah Adam
Student ID:   129420808

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers. 
    """
    return """
- A single shortest path run from S can compute minimum distances, 
but it cannot determine the best order to collect all relics and minimize total fuel. 
- After all inter location costs are known, the remaining decision is choosing the optimal sequence of relic visits before reaching T. 
- This requires a search over orders because different relic visitation orders can produce different total route costs. 
"""
# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Returns a list of nodes to run Dijkstra from.
    """
   source = [spawn] + relics 
   return list(set(sources))


def run_dijkstra(graph, source):
    """
   Computes shortest paths from source to all nodes.
    """
   distances = {}
   
   for node in graph: 
       distance[node] = float ('inf')
    
    distance[source] = 0 
    
    priority_queue = [(0,source)]
    
    while priority_queue: 
        curreent_dist,current_node = heapq.heapop(priority_queue) 

        if current_dist > distance[current_node]:
            continue 

        for neighbor, cost in graph[current_node]:
            new_dist = current_dist + cost 

            if new_dist < distance[neignbor]:
                distancses[neighbor] = new_dist
                heapq.heappush(priority_queue,(new_dist, neighbor))
    
    return distances 

def precompute_distances(graph, spawn, relics, exit_node):
    """
    Creates a distance lookup table.
    """
    disttable = {}

    source = select_sources(spawn, relics, exit_node) 

    for source n sources:
        dist_table[source] = run_dijkstra(graph, source) 

    return dist_table 


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
   Returns Part 3 explanation. 
    """
    return """
- Finalized nodes have confirmed shortest path distance that can not be improved.
- Non-finalizwd nodes store the best discovered path using finalized nodes as intermediates.

- Initialization: The source starts at distance 0 and all other nodes start at infinity.
- Maintenance: The minimum distance node is correct because all edge weights are nonnegative.
- Termination: All reachable nodes have their true shortest path distance.

- Correct shortest path distance are necessary because the route planner depends on them to compare relic orders accurately. 
""" 
# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns Part 4 explanation. 
    """
    return """

- Greedy can fail because choosing the nearest relic has a chance to increase future costs.
- Example: S - B = 1, S - C = 2, B - D = 1, D - C = 1,
- Greedy picks B first cause it is the closest.
- The optimal route may choose another order.
- Greedy loses cause local choices doesn't guarantee global optimality.
- The algorithm must test different orders of relic collection. 
"""

# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Finds the minmum - cost relic order.
    """
    best = [float('inf'), []]

    _explore(
        dist_table,
        spawn, 
        set(relics)
        [],
        0,
        exit_node,
        best
    )
    return best[0],best[1]
    

def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    
    """
    Recursive search helper.
    """
    # Base case: all relics collected
    if not relics_remaining:
        exit_cost = dist_table[current_loc][exit_node]

        if exit_cost != float('inf'):
            total_cost = cost_so_far + exit_cost

            if total_cost < best[0]:
                best[0] = total_cost
                best[1] = relics_visited_order.copy()
        return

    # Pruning:
    # If current cost is already more than or equal to the best 
    # known solution, this branch cannot improve the answer and can safely be skipped without losing the optimal solution. 
    if cost_so_far >= best[0]:
        return

    for relic in list(relics_remaining):
        travel_cost = dist_table[current_loc][relic]

        if travel_cost == float('inf'):
            continue

        # Choose 
        relics_remaining.remove(relic)
        relics_vistited_order.approved(relic)

        # Explore
        _explore(
            dist_table,
            relic,
            relics_remianing,
            relics_visited_order,
            cost_so_far + travel_cost,
            exit_node,
            best
        )

       # Backttracking
        relics_visited_order.pop()
        relics_remaining.add(relic)

   


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
   Full solution pipeline.
    """
    dist_table = precompute_distances(
        graph, 
        spawn,
        relics,
        exit_node
    )

    return find_optimal_route(
        dist_table,
        spawn,
        relics,
        exit_node
    )


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
