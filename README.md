# 🏰 EpicTales: The AI-Powered RPG Campaign Manager

Welcome to **Squire**, your loyal digital companion for running immersive and organized tabletop RPG campaigns. Whether you're a seasoned Dungeon Master or a fledgling adventurer, Squire helps you craft, manage, and enhance your fantasy worlds with the help of artificial intelligence.

## ✨ Features

- 📝 **Campaign & Story Management**  
  Create and organize your campaigns, quests, and lore with ease. Squire keeps your storylines coherent and accessible.

- 🧠 **AI Agent "Squire"**  
  An intelligent assistant trained to help you build your world. Ask Squire about monsters, items, or lore, and it responds using context-aware retrieval via a vector database.

- 📚 **RAG System (Retrieval-Augmented Generation)**  
  Squire uses a powerful RAG system that pulls from a curated dataset of **Dungeons & Dragons** monsters, items, and spells, helping you stay focused on storytelling.

- 🧭 **Intuitive Data Storage**  
  All your campaign data—NPCs, locations, encounters, plot twists—are safely stored and searchable.

- 🔍 **Vector Database Integration**  
  Fast and relevant search of your custom and canonical RPG data, ensuring quick access to what matters mid-session.

## 🧙 Why Use Squire?

Forget flipping through manuals or scattered notes. Squire is the AI scribe every GM wishes they had—helping you:

- Generate NPCs or side quests on the fly  
- Keep your campaign consistent across sessions  
- Look up DnD content with natural language  
- Collaborate with players using shared campaign logs

## 🏗️ Tech Stack

- **Python** & **Django**
- **LangChain** for AI orchestration
- **Chroma ** (pick one) as vector database

## 🚀 Getting Started

```bash
git clone https://github.com/IagoArauj/EpicTalesDjangoBackend.git
cd EpicTalesDjangoBackend
pip install -r requirements.txt

# Apply Django Migrations
python manage.py migrate

# Create a new User
python manage.py createsuperuser

# Run django's development server
python manage.py runserver
```

## 🧭 Your Adventure Has Just Begun...
To fully experience the magic of Squire, you’ll need its trusted front-end companion:
🌐 EpicTalesNext – The Front-End Interface

This React/Next.js-powered interface brings your campaigns to life with an intuitive UI, rich storytelling tools, and seamless interaction with the Squire backend. Together, they form the full Epic Tales system.

> ⚠️ Make sure to clone and run both the backend (this repo) and the frontend to unlock the full campaign experience.

# 🎓 Academic Context
This project was developed as part of an academic assignment 
during my undergraduate studies in Computer Science at the Federal University of São João del-Rei (UFSJ). 
It served as a practical exploration of concepts such as artificial intelligence, information retrieval, 
software design, and web application development—applied in the context of tabletop RPG systems, a passion
I've discovered during my studies.


