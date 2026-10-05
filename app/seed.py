from sqlmodel import Session, SQLModel, select

from app import models  # noqa: F401
from app.database import engine
from app.models import Hero, Mission, Team


def seed():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        if session.exec(select(Team)).first():
            print("Database already seeded, nothing to do.")
            return

        avengers = Team(name="Avengers", headquarters="New York")
        xmen = Team(name="X-Men", headquarters="Westchester")
        sokovia = Mission(title="Battle of Sokovia")
        genosha = Mission(title="Save Genosha")

        heroes = [
            Hero(name="Tony", age=45, secret_name="Iron Man", team=avengers, missions=[sokovia]),
            Hero(name="Natasha", age=35, secret_name="Black Widow", team=avengers, missions=[sokovia]),
            Hero(name="Logan", age=150, secret_name="Wolverine", team=xmen, missions=[genosha]),
            Hero(name="Jean", age=30, secret_name="Phoenix", team=xmen, missions=[genosha]),
            Hero(name="Peter", age=16, secret_name="Spider-Man", missions=[sokovia, genosha]),
        ]
        session.add_all(heroes)   # team và mission được lưu theo qua relationship
        session.commit()
        print(f"Seeded {len(heroes)} heroes.")


if __name__ == "__main__":
    seed()