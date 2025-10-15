# Week 43 - Exercise
System = set(range(0, 11))   # integers 0 through 10
Samples = {4.5, 5.5, 6.0, 7.0, 7.5, 8.5, 9.5}

# Event A
A = {x for x in Samples if x < 6.0}
A_cnt = len(A)

# Event B
B = {x for x in S if x > 8.5}
B_cnt = len(B)

# Event C
C = {x for x in S if 6.0 <= x <= 8.0}
C_cnt = len(C)

# Set 1: Union of events (A ∪ B, B ∪ C, A ∪ C) 
A_union_B = A.union(B)
B_union_C = B.union(C)
A_union_C = A.union(C)

# Set 2: Intersection of events (A ∩ B, A ∩ C, B ∩ C)
A_inter_B = A.intersection(B)
A_inter_C = A.intersection(C)
B_inter_C = B.intersection(C)

# Set 3: Complementary events (Aᶜ, Bᶜ, Cᶜ) 
A_comp = Samples - A
B_comp = Samples - B
C_comp = Samples - C
