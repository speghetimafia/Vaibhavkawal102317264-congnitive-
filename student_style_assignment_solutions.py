
# Question 1: List Operations
L = [10, 20,30,40,50, 60, 70,80]
L.extend([200,300])


L.remove(10); L.remove(30)
L.sort( )
L.sort(reverse =True)
print("Final List:", L)



# Question 2: Tuple Operations
scores=(45, 89.5,76, 45.4,89,92,58,45)
highest_score = max(scores) 
highest_index = scores.index(highest_score)
lowest_score = min(scores)
lowest_count=scores.count(lowest_score)   
reversed_list = list(scores[::-1])

search_score=76
if search_score in scores: 
    first_index=scores.index(search_score)
    message = f"Score {search_score} found at index {first_index}."
else: 
    message=f"Score {search_score} not found."
print("Highest Score:",highest_score, "at Index:",highest_index)
print("Lowest Score:", lowest_score, "appears", lowest_count, "times")
print("Reversed Tuple as List:",reversed_list)
print(message)



# Question 3: Random Numbers and Counting
import random 
random_numbers=[random.randint(100,900) for _ in range(100)]
odd_numbers=[num for num in random_numbers if num%2 !=0]
even_numbers= [num for num in random_numbers if num%2 == 0]
def is_prime(num): 
    if num<2: 
        return False
    for i in range(2,int(num**0.5)+1): 
        if num%i==0: 
            return False
    return True
prime_numbers=[num for num in random_numbers if is_prime(num)]

print("Odd Numbers:",odd_numbers)
print("Even Numbers:", even_numbers)
print("Prime Numbers:",prime_numbers)


# Question 4: Set Operations
A= {34,56,78,90}
B={78,45,90,23}
unique_scores= A|B
common_scores= A&B
exclusive_scores=A^B
is_subset= A.issubset(B)
is_superset= B.issuperset(A)
score_to_remove=int(input("Enter score to remove from A: "))
if score_to_remove in A:
    A.remove(score_to_remove)
    message=f"Score {score_to_remove} removed from A."
else:
    message=f"Score {score_to_remove} is not in A."
print("Unique Scores:",unique_scores)
print("Common Scores:",common_scores)
print("Exclusive Scores:",exclusive_scores)
print("Is A a subset of B?",is_subset)
print("Is B a superset of A?", is_superset)
print(message)


# Question 5: Dictionary Operation
data = {"city": "New York", "population": 8419600, "area":468.9}
data["location"] = data.pop("city")
print("Updated Dictionary:",data)
