scores = [85, 92, 78, 92, 88, 78, 95, 88, 70, 92]

# (a)
unique_scores = set(scores)
print("Unique scores:", unique_scores)

# (b)
score_counts = {}
for score in unique_scores:
    score_counts[score] = scores.count(score)
print("Score counts:", score_counts)

# (c)
sorted_counts = dict(sorted(score_counts.items()))
print("Sorted scores:")
for score, count in sorted_counts.items():
    print(score, ":", count)

# (d)
score_details = (min(scores), max(scores), len(scores))
print("Min, Max, Count:", score_details)

# (e)
nums = [4, 7, 4, 2, 7, 9]
unique = set(nums)
counts = {n: nums.count(n) for n in unique}
print(sorted(counts.items()))