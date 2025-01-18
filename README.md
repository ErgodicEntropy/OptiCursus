# OptiCursus

**OptiCursus** is your ultimate companion for finding the perfect academic program. Designed to simplify the overwhelming process of choosing a cursus, OptiCursus helps students make confident, informed decisions that align with their unique profile, goals, and preferences. By combining cutting-edge technology with a user-friendly approach, OptiCursus ensures that every student finds their ideal path to success.

Whether you're a student navigating the complexities of program selection or an educational institution aiming to guide students effectively, OptiCursus delivers tailored recommendations that minimize stress and maximize outcomes.

---

## Problem Statement
Choosing the right academic program can be overwhelming. With countless options, vague descriptions, and imperfect information, students often struggle to make decisions that truly align with their goals. This leads to misalignment, dissatisfaction, and even burnout. OptiCursus solves this problem by providing clarity, confidence, and personalized guidance.

---

## Stakeholders/End Users

### Primary Users:
- **Students** seeking a cursus program that is **optimal** and **best aligned** with their:
  - **Profile** (academic background, skills, strengths),
  - **Eligibility** (entry requirements, prerequisites),
  - **Preferences/Interests** (career goals, passions, learning style).

### Secondary Users:
- **Educational Institutions**: To guide students effectively and improve program alignment.
- **Career Counselors**: To provide data-driven recommendations to students.
- **Parents/Guardians**: To support students in making informed decisions.

---

## How It Helps
OptiCursus addresses the challenges students face in selecting the right program by:

1. **Reducing Ambiguity**: Cutting through vague program descriptions and imperfect information.
2. **Enhancing Decision-Making**: Offering data-driven, personalized recommendations.
3. **Saving Time**: Streamlining the search process by filtering out mismatched options.
4. **Improving Alignment**: Ensuring students choose programs that align with their profile, goals, and preferences.
5. **Preventing Burnout**: Minimizing misalignment and dissatisfaction by guiding students toward programs that suit them best.

---

## How It Works
OptiCursus leverages advanced technology to deliver a seamless, intelligent decision-making experience:

### 1. Data Collection
- **Student Input**: Students provide details about their profile, eligibility, preferences, and career goals.
- **Program Database**: A comprehensive database of cursus programs, including entry requirements, curriculum details, and outcomes.

### 2. Analysis & Matching
- **Smart Algorithms**: Uses factors like academic background, interests, and career goals to rank programs.
- **Personalized Insights**: Provides tailored recommendations based on the student’s unique profile.

### 3. AI-Powered Guidance
- **Context-Aware Explanations**: Helps students understand why a program is a good fit.
- **Predictive Insights**: Forecasts potential outcomes (e.g., career prospects, satisfaction) based on historical data.

### 4. Interactive Recommendations
- **Tailored Suggestions**: Delivers a shortlist of programs that best match the student’s profile and goals.
- **Easy Comparison**: Allows students to explore and compare programs in detail.

---

## Product Strategy
OptiCursus is designed to evolve and scale, ensuring long-term value for users and stakeholders.

### Phase 1: Launch Plan
- **Key Deliverables**:
  1. **Core Platform**: A user-friendly interface for students to input data and receive recommendations.
  2. **Program Database**: A robust database of cursus programs with detailed metadata.
  3. **Basic AI Integration**: Initial implementation of smart algorithms for personalized recommendations.

### Phase 2: Expansion
- **Key Deliverables**:
  1. **Advanced AI Features**: Integration of context-aware explanations and predictive insights.
  2. **Institutional Partnerships**: Collaborate with universities and colleges to expand the program database.
  3. **Mobile App**: Launch a mobile version for on-the-go access.

### Phase 3: Future Enhancements
- **Key Deliverables**:
  1. **Global Expansion**: Expand the database to include international programs.
  2. **Career Pathway Integration**: Link program recommendations to long-term career pathways.
  3. **Gamification**: Introduce interactive features (e.g., quizzes, progress tracking) to engage students.
  4. **AI-Powered Counseling**: Offer virtual counseling sessions powered by AI for personalized guidance.

---

## Value Proposition
- **For Students**: Simplifies the program selection process, reduces stress, and ensures alignment with their goals.
- **For Educational Institutions**: Improves student satisfaction and retention by guiding students to the right programs.
- **For Career Counselors**: Provides a data-driven tool to enhance their advisory services.
- **For Parents/Guardians**: Offers peace of mind by helping students make informed decisions.

---

## Key Differentiators
1. **Smart Recommendations**: Combines advanced algorithms with AI for personalized, context-aware suggestions.
2. **User-Centric Design**: Focuses on simplicity, accessibility, and engagement for students.
3. **Scalability**: Designed to grow with user needs, from local to global program coverage.
4. **Comprehensive Database**: Offers a wide range of programs with detailed metadata for accurate matching.

## **Key Benefits**
- **Personalization**: Tailored recommendations based on the student’s unique profile and preferences.
- **Efficiency**: Saves time by filtering out mismatched programs.
- **Confidence**: Helps students make informed decisions with data-driven insights.
- **Diversity**: Ensures a balanced mix of safe and aspirational choices.


## System Engineering

### Logical Architecture
![Logical Architecture](diagrams/Logical%20Architecture.jpeg)
#### Component Analysis

**1. Student Input**
The system relies on two main types of input from the student: **Preferences** and **Profile**.

- **Preferences**
  - **Favorite Domains**: Subjects the student enjoys or excels in (e.g., mathematics, literature, biology).
  - **Career Goals**: Desired career paths or industries (e.g., software engineering, medicine, finance).
  - **Cursus Level**: the program level searched for (e.g. Bachelor, Master, PhD)
- **Profile**
  - **CV or Resume**: Academic/Industry Background (CV or Resume): Certifications, Skills (Hard and Soft), Experience Achievements, Projects Extracurricular Activities, Awards, Linguistic Skills   
  - **Portfolio**: A collection of work samples showcasing skills (e.g., GitHub projects, design portfolios, or writing samples). 
  - **Motivation Letter**:  A document explaining your interest and fit for a role or program (e.g., job application or university admission letter)
  -  **LinkedIn Profile**:  A professional online presence summarizing career history and skills (e.g., profile with endorsements and activiy posts).  
  -  **Educational Level**:  Highest formal education achieved or pursued (e.g. Bachelor, Master, PhD, Courses taken with Domains)
  -  **GPA**: Numerical representation of academic performance and grades (e.g., 3.8/4.0 or 9.5/10)
  -  **Constraints**: Limitations such as budget, time, or accessibility. 



**2. Matching Algorithm (OptiCursus Engine)**
The system processes the student's input using advanced algorithms and strategies to generate optimal program recommendations.

  - **Operations Research Agent**
    - **Purpose**: Ensures recommendations are diverse, non-redundant, and optimized for the student’s unique profile.
    - **How It Works**:
      - Applies **operations research techniques** to analyze and optimize program recommendations.
      - Uses the **GINI Index** to measure the diversity of recommendations and minimize redundancy.
      - Ensures a balanced mix of programs that cover a wide range of options, avoiding over-concentration in a single field.
      - Example: Recommends interdisciplinary programs (e.g., computational finance) instead of only pure computer science or business programs.

  - **Optimization Algorithm**
    - **Purpose**: Evaluates how well the student meets the entry requirements for each program and optimizes recommendations based on eligibility.
    - **How It Works**:
      - Calculates an **eligibility score** based on the student’s academic background, skills, and achievements.
      - Ranks programs by how closely the student’s profile matches their eligibility criteria.
      - Uses **constraint optimization** to ensure recommendations align with the student’s constraints (e.g., budget, location, time).
      - Example: Prioritizes programs requiring a high GPA if the student meets this criterion.

  - **Investment Agent**
    - **Purpose**: Balances multiple factors (e.g., preferences, profile, eligibility) to find the best-fit programs, treating the decision like an investment in the student’s future.
    - **How It Works**:
      - Uses **weighted optimization** to prioritize factors based on their importance to the student.
      - Considers trade-offs between preferences (e.g., career goals, location) and constraints (e.g., budget, time).
      - Example: Recommends programs with strong career outcomes if the student prioritizes career goals over location.

  - **Investment Strategy**
    - **Purpose**: Balances **safe choices** and **aspirational choices** in the recommendations, similar to an investment portfolio strategy.
    - **How It Works**:
      - Recommends a mix of:
        1. **Safe Choices**: Programs where the student is highly likely to be accepted and succeed, ensuring a solid foundation.
        2. **Aspirational Choices**: Programs that are more competitive or challenging but align with the student’s long-term goals, encouraging ambition.
      - Example: Recommends both local universities (safe) and competitive international programs (aspirational).

**3. Output: Aligned Cursus Programs**
The final output is a list of **Aligned Cursus Programs** that match the student’s profile, preferences, and goals.

**4. Post Processing**
  - **Recommendation**
    - **Program Details**: Name, institution, curriculum, duration, and location.
    - **Alignment Score**: A score indicating how well the program aligns with the student’s input.
    - **Eligibility Status**: Whether the student meets the program’s entry requirements.
    - **Career Outcomes**: Potential career paths and job prospects after completing the program.
    - **Comparison Metrics**: Key metrics (e.g., cost, acceptance rate, student satisfaction) to help the student compare programs.
  - **Context-Aware Explanation**
    - **Purpose**: Provides clear, context-aware explanations for why a program is recommended, helping students understand the reasoning behind each suggestion.
    - **How It Works**:
      - Uses **natural language processing (NLP)** to generate explanations tailored to the student’s profile and preferences.
      - Highlights key factors (e.g., alignment with career goals, eligibility status) that influenced the recommendation.
      - Example: “This program is recommended because it aligns with your interest in data science and offers strong career outcomes in your preferred location.”

  - **Programs Comparison**
    - **Purpose**: Allows students to compare recommended programs side-by-side, making it easier to evaluate trade-offs and make informed decisions.
    - **How It Works**:
      - Displays key metrics (e.g., cost, duration, acceptance rate) in a tabular or visual format.
      - Enables students to rank programs based on their priorities (e.g., cost vs. career outcomes).
      - Example: Compare two programs based on cost, location, and career outcomes.

  - **Career Pathways Exploration**
    - **Purpose**: Helps students explore long-term career pathways associated with recommended programs, connecting education to future opportunities.
    - **How It Works**:
      - Links programs to potential career paths and job market trends.
      - Provides insights into salary ranges, job growth, and required skills for each career.
      - Example: Show how a Master’s in Data Science can lead to careers as a Data Scientist, Machine Learning Engineer, or Business Analyst.

  - **Virtual Counseling**
    - **Purpose**: Offers personalized guidance through AI-powered virtual counseling, simulating a one-on-one counseling session.
    - **How It Works**:
      - Uses **AI chatbots** or **virtual assistants** to answer student questions and provide recommendations.
      - Offers tailored advice based on the student’s profile and preferences.
      - Example: A virtual counselor explains why a specific program is a good fit and answers questions about application requirements.


### Physical Architecture
![Physical Architecture](diagrams/Physical%20Architecture.jpeg)
#### Component Analysis

**1. Student**

- **User Registration**: The process where a new user signs up for an account by providing basic information (e.g., email, password).  
- **Profile Creation**: The step where a registered user adds personal details and preferences to customize their account (e.g., name, bio, profile picture).  
- **Input Data**: The system relies on two main types of input from the student: **Preferences** and **Profile**.

**2. System Processing**
The system processes the student's input using advanced algorithms and strategies.

- **a. Multi-Redundancy Elimination (GINI Index Minimization)**
  - **Purpose**: Ensures recommendations are diverse and non-redundant.
  - **How It Works**:
    - Uses the **GINI Index** to evaluate diversity.
    - Minimizes redundancy by recommending programs that cover a wide range of options.
    - Example: Recommends blended programs (e.g., computational finance) instead of only pure computer science or business programs.

- **Preference Score**  
  - **Purpose**: Evaluates how well a program aligns with the student’s preferences and goals.  
  - **How It Works**:  
    - Calculates a score based on the alignment between the student’s preferences (e.g., location, program type, career goals) and the program’s offerings.  
    - Ranks programs by how closely they match the student’s desired criteria.  
    - Example: Prioritizes programs in a specific location or with a focus on research if the student prefers these features.  

- **c. Multi-Variate Optimization**
  - **Purpose**: Balances multiple factors (e.g., preferences, profile, eligibility) to find the best-fit programs.
  - **How It Works**:
    - Uses **weighted optimization** to prioritize factors based on their importance to the student.
    - Example: Recommends programs with strong career outcomes if the student prioritizes career goals over location.

- **Eligibility Score**
  - **Purpose**: Evaluates how well the student meets the entry requirements for each program.
  - **How It Works**:
    - Calculates a score based on the student’s academic background, skills, and achievements.
    - Ranks programs by how closely the student’s profile matches their eligibility criteria.
    - Example: Prioritizes programs requiring a high GPA if the student meets this criterion.

- **Barbell Strategy**
  - **Purpose**: Balances **safe choices** and **aspirational choices** in the recommendations.
  - **How It Works**:
    - Recommends a mix of:
      1. **Safe Choices**: Programs where the student is highly likely to be accepted and succeed.
      2. **Aspirational Choices**: Programs that are more competitive or challenging but align with the student’s long-term goals.
    - Example: Recommends both local universities (safe) and competitive international programs (aspirational).


**3. Output: Aligned Cursus Programs**
The final output is a list of **Aligned Cursus Programs** that match the student’s profile, preferences, and goals.

**4. Post Processing**
  - **Recommendation**
    - **Program Details**: Name, institution, curriculum, duration, and location.
    - **Alignment Score**: A score indicating how well the program aligns with the student’s input.
    - **Eligibility Status**: Whether the student meets the program’s entry requirements.
    - **Career Outcomes**: Potential career paths and job prospects after completing the program.
    - **Comparison Metrics**: Key metrics (e.g., cost, acceptance rate, student satisfaction) to help the student compare programs.
  - **Context-Aware Explanation**
    - **Purpose**: Provides clear, context-aware explanations for why a program is recommended, helping students understand the reasoning behind each suggestion.
    - **How It Works**:
      - Uses **natural language processing (NLP)** to generate explanations tailored to the student’s profile and preferences.
      - Highlights key factors (e.g., alignment with career goals, eligibility status) that influenced the recommendation.
      - Example: “This program is recommended because it aligns with your interest in data science and offers strong career outcomes in your preferred location.”

  - **Programs Comparison**
    - **Purpose**: Allows students to compare recommended programs side-by-side, making it easier to evaluate trade-offs and make informed decisions.
    - **How It Works**:
      - Displays key metrics (e.g., cost, duration, acceptance rate) in a tabular or visual format.
      - Enables students to rank programs based on their priorities (e.g., cost vs. career outcomes).
      - Example: Compare two programs based on cost, location, and career outcomes.

  - **Career Pathways Exploration**
    - **Purpose**: Helps students explore long-term career pathways associated with recommended programs, connecting education to future opportunities.
    - **How It Works**:
      - Links programs to potential career paths and job market trends.
      - Provides insights into salary ranges, job growth, and required skills for each career.
      - Example: Show how a Master’s in Data Science can lead to careers as a Data Scientist, Machine Learning Engineer, or Business Analyst.

  - **Virtual Counseling**
    - **Purpose**: Offers personalized guidance through AI-powered virtual counseling, simulating a one-on-one counseling session.
    - **How It Works**:
      - Uses **AI chatbots** or **virtual assistants** to answer student questions and provide recommendations.
      - Offers tailored advice based on the student’s profile and preferences.
      - Example: A virtual counselor explains why a specific program is a good fit and answers questions about application requirements.
