#!/usr/bin/env python3
"""PR Ouija Board - When developers can't be bothered to write descriptions."""

import random
import sys

# The spirits of past PRs guide us to better descriptions
SPIRITS = [
    "Fixed a bug",  # The classic - tells us nothing but feels familiar
    "Updated dependencies",  # Vague enough to hide breaking changes
    "Refactored code",  # Translation: I made it worse but prettier
    "Added feature",  # What feature? Who knows! Surprise!"
    "Improved performance",  # Probably added a cache. Or removed one.
    "Fixed typo",  # Changed 'teh' to 'the' - critical fix
    "Updated README",  # Added an emoji, removed a comma
    "Code cleanup",  # Deleted three lines, added twenty
]

# Ouija board responses - what the spirits REALLY mean
TRANSLATIONS = {
    "Fixed a bug": "Something was broken, now it's... probably still broken",
    "Updated dependencies": "Upgraded to breaking changes v2.0",
    "Refactored code": "Moved the bug to a different file",
    "Added feature": "Introduced new bugs to replace the old ones",
    "Improved performance": "Made it 0.0001% faster on Tuesdays",
    "Fixed typo": "Changed 'color' to 'colour' to assert dominance",
    "Updated README": "Added 'coming soon' to unfinished features",
    "Code cleanup": "Replaced working code with 'cleaner' broken code",
}

# The actual ouija board - asks spirits for PR wisdom
def consult_ouija():
    """Summon the spirits of lazy PR descriptions past."""
    print("\n🔮 The PR Ouija Board is consulting the spirits...\n")
    
    # The planchette moves mysteriously
    spirit = random.choice(SPIRITS)
    translation = TRANSLATIONS[spirit]
    
    print(f"The spirits say: '{spirit}'")
    print(f"Translation: {translation}")
    
    # Bonus: sometimes the spirits are extra helpful
    if random.random() < 0.3:  # 30% chance of extra snark
        extras = [
            "\n💡 Tip: Try actually describing what changed!",
            "\n👻 Ghost of PRs Past: 'I regret nothing!'",
            "\n📝 Pro tip: 'git diff' is not a description",
        ]
        print(random.choice(extras))
    
    return spirit

# Main function - because every script needs one
def main():
    """Main entry point for summoning PR wisdom."""
    print("PR Description Ouija Board")
    print("=" * 30)
    print("\nWhen your PR description is empty, let the spirits decide!")
    
    try:
        consult_ouija()
        
        # Offer to try again - because first answers are always 'Fixed a bug'
        if len(sys.argv) > 1 and sys.argv[1] == "--desperate":
            print("\n🔮 The spirits sense your desperation... consulting again!")
            consult_ouija()
            
    except KeyboardInterrupt:
        print("\n\n👻 The spirits have left the building. Good luck with your PR!")

if __name__ == "__main__":
    main()
