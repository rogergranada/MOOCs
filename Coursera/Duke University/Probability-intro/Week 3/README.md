# Week 3 : Introduction to Probability

This week we discuss probability, conditional probability, the Bayes' theorem, and provide a light introduction to Bayesian inference.  

### Objectives

1) Define the probability of an outcome as the proportion of times the outcome would occur if we observed the random process that gives rise to it an infinite number of times.  
2) Explain why the long-run relative frequency of repeated independent events settles down to the true probability as the number of trials increases, i.e. why the law of large numbers holds.  
3) Define disjoint (mutually exclusive) events as events that cannot both happen at the same time:  
- If A and B are disjoint, P(A and B) = 0  
4) Distinguish between disjoint and independent events.  
- If A and B are independent, then having information on A does not tell us anything about B (and vice versa).
- If A and B are disjoint, then knowing that A occurs tells us that B cannot occur (and vice versa).
- Disjoint (mutually exclusive) events are always dependent since if one event occurs we know the other one cannot.  
5) Draw Venn diagrams representing events and their probabilities.  
6) Define a probability distribution as a list of the possible outcomes with corresponding probabilities that satisfies three rules:
- The outcomes listed must be disjoint.
- Each probability must be between 0 and 1.
- The probabilities must total 1.
7) Define complementary outcomes as mutually exclusive outcomes of the same random process whose probabilities add up to 1.  
- If A and B are complementary, P(A) + P(B) = 1
8) Distinguish between union of events (A or B) and intersection of events (A and B). 
Calculate the probability of union of events using the (general) addition rule:  
- If A and B are not mutually exclusive, P(A or B) = P(A) + P(B) − P(A and B)
- If A and B are mutually exclusive, P (A or B) = P (A) + P (B), since for mutually exclusive events P(A and B) = 0  
Calculate the probability of intersection of independent events using the multiplication rule:
- If A and B are independent, P(A and B) = P(A) × P(B)
- If A and B are dependent, P(A and B) = P(A|B) × P(B)

### How it is divided

The week is composed by three parts:

[Defining probability](1.%20Defining%20Probability.ipynb)

[Conditional probability](2.%20Conditional%20Probability.ipynb)

[Strengthen Your Understanding](Exercises.ipynb)  
