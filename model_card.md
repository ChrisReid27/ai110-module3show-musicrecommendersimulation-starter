# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**Music Taste Discerner (MTD) Version 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

One weakness I found when the energy weight got doubled from 1.5 to 3.0 in the experiment was that the system became significantly more likely to group users into energy-based "bubbles." Users with extreme energy preferences (like preferring 0.2 or 0.9 on a 0-1 scale) will find it nearly impossible to discover songs outside their range, since a mismatch of 0.7 energy points now costs them 2.0 scoring points which is difficult to overcome even with a perfect genre and mood match. This reveals that the system over-prioritizes energy similarity in a way that locks users into narrow recommendation bands (which happened with genre before the shift), particularly disadvantaging low-energy and acoustic music listeners (only 2 songs with energy <=0.3 vs. 11 songs with energy >=0.7).

---

## 7. Evaluation  

I checked if the recommender was behaving as expected by running three different listener profiles and checking whether the top songs felt reasonable to me. One profile was a high-energy pop listener who wanted very energetic music and didn't like acoustic songs. In that case, Night Drive Loop was their top song before and after weight shifting even though the scores were different (Before: 4.26, After: 5.54) because it has very high energy, and after my weight-shift experiment energy became one of the strongest parts of the score. MTD started mainly focusing on energy similarity more than before, so songs with matching energy were pushed up even when other traits were not perfect matches. This helped me confirm the model was working as coded, but also that the ranking can become repetitive for users with extreme energy preferences.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
