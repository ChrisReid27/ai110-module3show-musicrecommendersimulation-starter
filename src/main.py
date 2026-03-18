"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # Starter example profile
    #user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    high_energy_pop = { # conflicting preferences for testing
        "genre": "pop",
        "mood": "moody", # testing how the system handles a mismatch in mood preference while having a strong genre match and high energy preference
        "energy": 0.9,
        "likes_acoustic": False,
        }
    chill_lofi = { # boundary testing: All minimized preferences to see if the system can handle extreme cases
        #"genre": "lofi",
        #"mood": "chill",
        "energy": 0.0,
        "tempo_bpm": 0.0,
        "valence": 0.0,
        "danceability": 0.0,
        "acousticness": 1.0,
        }
    deep_intense_rock = { # unusual combination to test edge cases
        "genre": "rock",
        "mood": "intense",
        "energy": 0.2, # low energy but intense mood to see how the system balances these factors
       "likes_acoustic": True, # testing preference for acoustic music in a typically non-acoustic genre
       }
    
    profiles = {
        "High-Energy Pop": high_energy_pop,
        "Chill Lofi": chill_lofi,
        "Deep Intense Rock": deep_intense_rock,
    }

    # Show recommendations for each profile
    for profile_name, user_prefs in profiles.items():
        print(f"\n{'='*50}")
        print(f"Profile: {profile_name}")
        print(f"Preferences: {user_prefs}")
        print(f"{'='*50}\n")

        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("Top recommendations:\n")
        for song, score, reasons in recommendations:
            print(f"  {song['title']} - Score: {score:.2f}")
            print(f"  Because: {'; '.join(reasons)}")
            print()

'''
    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, reasons = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {'; '.join(reasons)}")
        print()
'''

if __name__ == "__main__":
    main()
