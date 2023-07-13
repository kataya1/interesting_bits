

class Action {

}
class State {

}
class SearchNode {
    state: State;
    parent: SearchNode
    action: Action // the action applied to get from parent 
    pathCost: number = 0;
    constructor(state: State, pn: SearchNode, action: Action, cost: number = 0) {
        this.state = state
        this.parent = pn
        this.action = action
        this.pathCost = this.pathCost + cost
    }
}

// Solving Search Problems
// Solution

// A sequence of actions that leads from the initial state to the goal state.

// Optimal Solution

// A solution that has the lowest path cost among all solutions.

// In a search process, data is often stored in a node, a data structure that contains the following data:

// A state
// Its parent node, through which the current node was generated
// The action that was applied to the state of the parent to get to the current node
// The path cost from the initial state to this node