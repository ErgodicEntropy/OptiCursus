from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import HttpRequest, Http404
from django.urls import reverse

# Create your views here.



# def quality_scale(self):
#     pass

# def tuition_fee_scale(self):
#     pass

# def living_cost_scale(self):
#     pass








# masters_programs = [
#     {"name": "Program A", "university": "Uni 1", "quality": 8, "tuition_fee": 5000, 
#      "living_cost": 12000, "domain": "AI", "type": "Research", "eligibility_score": 75},
#     {"name": "Program B", "university": "Uni 2", "quality": 7, "tuition_fee": 3000, 
#      "living_cost": 10000, "domain": "Data Science", "type": "Professional", "eligibility_score": 85},
#     # Add more programs...
# ]



# def calculate_program_score(user_profile, program, weights):
#     # weights: dict of weights for factors like quality, cost, etc.
#     eligibility = calculate_eligibility_score(user_profile, program)
#     cost = program["tuition_fee"] + program["living_cost"]
#     if cost > user_profile["budget"]:
#         return 0  # Filter out programs exceeding the budget
#     return (weights["quality"] * program["quality"] + 
#             weights["eligibility"] * eligibility +
#             weights["cost"] * (1 / cost))  # Lower cost = higher score


#  Program Selection
# Use multi-factor optimization to rank programs.
# Apply Gini Index or diversity check to reduce redundancy.
# Incorporate the Barbell Strategy by separating high-risk and low-risk programs.


# def recommend_programs(user_profile, programs, weights, max_choices=7):
#     scores = []
#     for program in programs:
#         score = calculate_program_score(user_profile, program, weights)
#         if score > 0:
#             scores.append((program, score))
    
#     # Sort programs by score (descending)
#     scores.sort(key=lambda x: x[1], reverse=True)
    
#     # Apply Barbell Strategy
#     low_risk = [p for p in scores if p[0]["eligibility_score"] > 70][:max_choices//2]
#     high_risk = [p for p in scores if p[0]["eligibility_score"] <= 70][:max_choices//2]
    
#     return low_risk + high_risk
