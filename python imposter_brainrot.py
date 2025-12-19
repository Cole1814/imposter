import random
import time

# ===== PLAYERS =====
players = ["Player 1", "Player 2", "Player 3", "Player 4"]

# ===== 100+ BRAINROT WORDS =====
brainrot_words = [
    "Skibidi", "Sigma", "Ohio Final Boss", "Fanum Tax", "NPC", "Gyatt",
    "Rizz", "Kai Cenat", "Adin Ross", "Wocky Slush", "Grimace Shake",
    "Level 10 Gyatt", "Sus", "Bussin", "Mid", "Cooked", "Let him cook",
    "Based", "Cringe", "Bro fell off", "No cap", "On god", "Fr fr",
    "Lowkey", "Highkey", "Caught lacking", "Blud", "Nah jit trippin",
    "Zesty", "Glizzy", "Sheesh", "Side eye", "Bombastic side eye",
    "Digital footprint", "Goofy ahh", "Slay", "Ate", "Not the",
    "Main character", "NPC walk", "He tweakin", "Menace",
    "Ohio vs the world", "Core memory", "It's giving",
    "Bro thinks he's him", "Himothy", "Sussy baka",
    "Skill issue", "Cope", "Seethe", "Ratio", "Touch grass",
    "Ick", "Gaslight", "Gatekeep", "Girlboss", "Brainrot",
    "Absolute cinema", "Canon event", "Delulu",
    "Bro is yapping", "Hard watch", "W take", "L take",
    "Unhinged", "Fermented", "Ain't no way", "Wild",
    "Certified hood classic", "NPC dialogue",
    "Default settings", "Factory reset",
    "He cooked", "Let bro cook", "Bro burnt it",
    "Peak", "Mid behavior", "Down bad",
    "Chat is this real", "We live we love we lie",
    "Lore drop", "Character arc", "Villain era",
    "Sigma silence", "Bro spawned in",
    "IRL side quest", "Main quest energy"
]

# ===== GAME SETUP =====
word = random.choice(brainrot_words)
imposter = random.choice(players)

print("\n🧠 IMPOSTER: BRAINROT EDITION 🧠")
print("4 Players | 1 Imposter")
print("GitHub Safe Version\n")
time.sleep(1)

# ===== ROLE REVEAL =====
for p in players:
    input(f"{p}, press ENTER to see your role (others look away) 👀")
    print("\n" * 40)

    if p == imposter:
        print("💀 YOU ARE THE IMPOSTER 💀")
        print("You do NOT know the word.")
    else:
        print("✅ YOU ARE A NORMIE")
        print(f"🧠 The brainrot word is: {word}")

    input("\nPress ENTER when done")
    print("\n" * 40)

# ===== QUESTIONS =====
questions = [
    "When do people use this word?",
    "Is it cringe or sigma? Why?",
    "Describe the word without saying it."
]

print("🎤 ANSWER OUT LOUD 🎤\n")

for q in questions:
    print("QUESTION:", q)
    input("Press ENTER after everyone answers...\n")

# ===== VOTING =====
print("🗳️ TIME TO VOTE 🗳️")
votes = {}

for p in players:
    vote = input(f"{p}, who do you vote for? ").strip()
    votes[vote] = votes.get(vote, 0) + 1

# ===== RESULTS =====
voted_out = max(votes, key=votes.get)

print("\n🔥 RESULTS 🔥")
print(f"{voted_out} was voted out!")

if voted_out == imposter:
    print("🎉 NORMIES WIN 🎉")
else:
    print("💀 IMPOSTER WINS 💀")
    print(f"The Imposter was: {imposter}")
    print(f"The word was: {word}")
