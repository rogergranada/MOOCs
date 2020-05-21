# Week 2: Markov Decision Processes

When you're presented with a problem in industry, the first and most important step is to translate that problem into a Markov Decision Process (MDP). The quality of your solution depends heavily on how well you do this translation. This week, you will learn the definition of MDPs, you will understand goal-directed behavior and how this can be obtained from maximizing scalar rewards, and you will also understand the difference between episodic and continuing tasks. For this week's graded assessment, you will create three example tasks of your own that fit into the MDP framework.

## Key Concepts

- Understand Markov Decision Processes (MDP)
- Describe how the dynamics of an MDP are defined
- Gain experience formalizing decision-making problem as MDPs
- Appreciate the flexibility of the MDP formalism
- Describe how rewards relate to the goal of an agent
- Identify episodic tasks
- Differentiate between episodic and continuing tasks
- Formulate returns for continuing tasks using discounting
- Describe how returns at successive time steps are related to each other
- Understand when to formalize a task as episodic or continuing
- Recognize that a policy is a distribution over actions for each possible state
- Describe the similarities and differences between stochastic and deterministic policies
- Identify the characteristics of a well-defined policy
- Generate examples of valid policies for a given MDP
- Describe the roles of state-value and action-value functions in reinforcement learning
- Describe the relationship between value functions and policies
- Create examples of valid value functions for a given MDP
- Derive the Bellman equation for state-value functions
- Derive the Bellman equation for action-value functions
- Understand how Bellman equations relate current and future values
- Use the Bellman equations to compute value functions
- Define an optimal policy
- Understand how a policy can be at least as good as every other policy in every state
- Identify an optimal policy for given MDPs
- Derive the Bellman optimality equation for state-value functions
- Derive the Bellman optimality equation for state-value functions
- Understand how the Bellman optimality equations relate to the previously introduced Bellman equations
- Understand the connection between the optimal value function and optimal policies
- Verify the optimal value function for given MDPs
