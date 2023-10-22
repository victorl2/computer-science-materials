# Computer Science Materials
Courses and other resources with a focus on **Computer Science**, **Artificial Inteligence** and **Math curated** by [**me**](www.github.com/victorl2)

# Courses included
+ Introduction to Probability for Computer Scientists.
+ A 2020 Vision of Linear Algebra. ( by Gilbert Strang - MIT )
+ Introduction to Reinforcement Learning and deep RL. ( Hado van Hasselt, Diana Borsa & Matteo Hessel - DeepMind )

# Papers included
+ Eureka: Human-Level Reward Design via Coding Large Language Models.


# Project structure
This repository contains the required information to start learning about the topics mentioned above. All for **courses** and **research papers** are in a pre-defined json format, that are easily parsed by the scripts in the `scripts` folder, or directly read by humans. The format for the json is as follows: 

### Course's json
```json
{
    "course_details": { 
        "source": "who produced the course ( university, company or individual )",
        "title": "title of the course",
        "course_id": "unique identifier for the course - most commonly applied for university courses",
        "professors": "who is teaching the course (may be multiple people)",
        "website_url" : "url to the course website",
        "year": 2020 
    }, 
    "lectures": [
        { 
            "number": 1,
            "description": "lecture title/description",
            "video_url": "https://www.youtube.com/watch?v=2MuDZIAzBMY"
        }
    ]
}
```

### papers's json
```json
{
    "title": "title for the paper/article",
    "paper_url": "https://arxiv.org/abs/2310.12931",
    "code_repository": "https://github.com/eureka-research/Eureka",
    "project_page": "https://eureka-research.github.io",
    "topics": ["Reinforcement Learning", "Natural Language Processing", "Reward Design", "Language Models"]
}
```