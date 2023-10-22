# Computer Science Materials
Courses, articles and research papers with a focus on **Computer Science**, **Artificial Inteligence** and **Math curated** by [**me**](www.github.com/victorl2)

## Courses
+ [Introduction to Probability for Computer Scientists.](/resources/courses/probability-for-computer-scientists.json)
+ [A 2020 Vision of Linear Algebra.](/resources/courses/a-2020-vision-of-linear-algebra.json) ( by Gilbert Strang - MIT )
+ [Introduction to Reinforcement Learning and deep RL.](/resources/courses/introduction-to-reinforcement-learning-and-deep-rl.json) ( Hado van Hasselt, Diana Borsa & Matteo Hessel - DeepMind )

## Papers
+ [Eureka: Human-Level Reward Design via Coding Large Language Models.](/resources/papers/human-level-reward-design-via-coding-llm.json)

## Articles
+ [How AI voice cloning works ?](/resources/articles/how-voice-cloning-works.MD)

## Download the materials
You can download the courses, articles and papers referenced here by using the [**download.py**](/scripts/download.py) script. The script will download all the files; some videos are very long, so it may take a while for everything to finish. 

## Project structure
This repository contains the required information to start learning about the topics mentioned above. All files for [**courses**](/resources/courses/) and [**research papers**](/resources/papers/) are in a pre-defined json format, those are easily parsed by the scripts in the `scripts` folder, or directly read by humans. The [**articles**](/resources/articles/) are in the [markdown format](https://en.wikipedia.org/wiki/Markdown). The format for the json files is as follows: 

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

### Papers's json
```json
{
    "title": "title for the paper/article",
    "paper_url": "https://arxiv.org/abs/2310.12931",
    "code_repository": "https://github.com/eureka-research/Eureka",
    "project_page": "https://eureka-research.github.io",
    "topics": ["Reinforcement Learning", "Natural Language Processing", "Reward Design", "Language Models"]
}
```