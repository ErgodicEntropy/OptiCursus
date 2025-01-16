from django.shortcuts import render

# Create your views here.


# User Profile Input
# Gather user information to evaluate eligibility.

def get_user_profile():
    print("Enter your profile details:")
    gpa = float(input("GPA (out of 4.0): "))
    relevant_experience = int(input("Years of relevant experience: "))
    preferred_domains = input("Preferred domains (comma-separated): ").split(",")
    max_budget = int(input("Maximum budget for tuition + living costs: "))
    return {
        "gpa": gpa,
        "experience": relevant_experience,
        "domains": [domain.strip() for domain in preferred_domains],
        "budget": max_budget
    }



# Scoring Function
# Eligibility Scoring: Calculate a score based on GPA, experience, and other factors.
# Multi-Factor Scoring: Combine factors like quality, tuition, and living cost into a weighted score.
# Risk Classification: Divide programs into low-risk and high-risk categories based on eligibility.

def calculate_eligibility_score(user_profile, program):
    gpa_weight = 0.6
    exp_weight = 0.4
    gpa_score = (user_profile["gpa"] / 4.0) * 100
    exp_score = (user_profile["experience"] / 5) * 100  # Assume 5 years max experience
    return gpa_weight * gpa_score + exp_weight * exp_score



# Run the Program

# def main():
#     user_profile = get_user_profile()
#     weights = {
#         "quality": 0.5,  # User-defined weight for quality
#         "eligibility": 0.3,  # Weight for eligibility
#         "cost": 0.2  # Weight for cost
#     }
#     recommendations = recommend_programs(user_profile, masters_programs, weights)
    
#     print("\nRecommended Master's Programs:")
#     for program, score in recommendations:
#         print(f"{program['name']} at {program['university']} - Score: {score:.2f}")

# if __name__ == "__main__":
#     main()
