# SuperCoach Football Analytics

*AI-powered football analytics project to build a “super coach camera” that helps players and coaches understand matches better.*

---

## 🎯 Vision

The long-term goal of this project is to create an AI assistant that acts like a **super coach**:

- Watches football games (video + event data)
- Understands team shape, pressing, transitions and player decision-making
- Gives **personalised feedback** to each player
- Provides **extra tactical insights** to coaches about team play and weaknesses

This repository is **Phase 1: data & analytics**.  
Later phases will add **computer vision** and **reinforcement learning**.

---

## 🧱 Phase 1 – Data & Tactical Analytics (current repo)

Planned features:

- Load open football data (e.g. StatsBomb Open Data / public datasets)
- Build core metrics:
  - Pass maps & heatmaps
  - Shot maps and basic xG model
  - Pressing intensity (PPDA-style metric)
  - Player involvement & influence metrics
  - Team possession and transition analysis
- Create visualisations:
  - Pass networks
  - Touch maps
  - xG timeline
  - Player radar charts

The goal is to create **clean, modular code** that can later connect to the video & RL modules.

---

## 🧠 Future Phases

### Phase 2 – SuperCoach Vision (Computer Vision)

Planned second repository:

- Detect and track players from broadcast video (YOLO + tracker)
- Group players into teams (jersey colour clustering)
- Reconstruct approximate positions on a 2D pitch
- Extract trajectories, sprint intensity, and off-ball movement
- Generate “coach view” tactical summaries from video clips

### Phase 3 – SuperCoach RL (Decision Support)

Planned third repository:

- Create a simplified football simulation environment
- Use **Reinforcement Learning (PPO/DQN)** to learn passing/pressing decisions
- Compare AI agent decisions with real player decisions
- Suggest alternative passing options or positioning tips

---

## 🛠️ Tech Stack

- Python
- pandas, numpy
- matplotlib / seaborn / plotly
- (Later) PyTorch / Stable-Baselines3
- (Later) YOLO, OpenCV

---

## 📌 Status

This project is currently in **early development**.  
The first milestones are:

1. ✅ Create project structure and documentation  
2. ⏳ Add first notebook with event data analysis  
3. ⏳ Implement simple xG model  
4. ⏳ Add first visualisations (pass maps, heatmaps)  

---

## 📬 Contact

**Lucas Mesa Casellas**  
AI & Data Science student (ESILV + Cranfield)  
Interested in ML, RL trading bots & football analytics.  
🔗 LinkedIn: https://www.linkedin.com/in/lucas-mesa-casellas
