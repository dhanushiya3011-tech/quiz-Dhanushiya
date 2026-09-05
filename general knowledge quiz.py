"""
Python Programming Project 4 — The General Knowledge Quiz
DecodeLabs Industrial Training Kit | Batch 2026

Goal: Ask 3 general knowledge questions, keep a running score,
and print the final score at the end.

Key skills demonstrated (per the project brief):
  - Input          -> input() captures raw user data
  - Sanitization   -> .strip().lower() defends against whitespace & case bugs
  - Control Flow   -> if / elif / else routes execution based on the answer
  - State Mgmt     -> score = 0, then score += 1 (accumulator pattern)
  - Output         -> f-strings deliver clean, formatted feedback
"""

# ---------------------------------------------------------
# STORAGE: initialize state. Integer 0 guarantees reliable
# cumulative math for the score (Type Integrity requirement).
# ---------------------------------------------------------
score = 0
total_questions = 3

print("=" * 40)
print("   WELCOME TO THE GENERAL KNOWLEDGE QUIZ")
print("=" * 40)
print()

# ---------------------------------------------------------
# QUESTION BLOCK 1
# Step 1: Ask & Capture -> Step 2: Sanitize ->
# Step 3: Evaluate -> Step 4: Execute
# ---------------------------------------------------------
answer1 = input("Q1. What is the capital of France? ")
answer1 = answer1.strip().lower()          # remove stray spaces/newlines, normalize case

if answer1 == "paris":
    print("Correct! ✅")
    score += 1                             # only the success path touches the score
else:
    print(f"Wrong! The correct answer was 'Paris'.")

print()

# ---------------------------------------------------------
# QUESTION BLOCK 2
# ---------------------------------------------------------
answer2 = input("Q2. Which planet is known as the Red Planet? ")
answer2 = answer2.strip().lower()

if answer2 == "mars":
    print("Correct! ✅")
    score += 1
else:
    print(f"Wrong! The correct answer was 'Mars'.")

print()

# ---------------------------------------------------------
# QUESTION BLOCK 3
# ---------------------------------------------------------
answer3 = input("Q3. Who wrote the play 'Romeo and Juliet'? ")
answer3 = answer3.strip().lower()

if answer3 == "william shakespeare" or answer3 == "shakespeare":
    print("Correct! ✅")
    score += 1
else:
    print(f"Wrong! The correct answer was 'William Shakespeare'.")

print()

# ---------------------------------------------------------
# OUTPUT: deliver the final result using an f-string.
# ---------------------------------------------------------
print("=" * 40)
print(f"Quiz complete! Your final score is: {score}/{total_questions}")
print("=" * 40)
