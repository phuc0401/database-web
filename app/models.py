from sqlmodel import Field, Relationship, SQLModel

class TeamBase(SQLModel):
    
    name: str = Field(index=True, unique=True)
    headquarters: str

class Team(TeamBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    heroes: list["Hero"] = Relationship(back_populates="team")

class TeamCreate(TeamBase):
    pass


class TeamPublic(TeamBase):
    id: int



class HeroBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = None
    power: str | None = None
    team_id: int | None = Field(default=None, foreign_key="team.id")


class HeroMissionLink(SQLModel, table=True):
    hero_id: int | None = Field(default=None, foreign_key="hero.id", primary_key=True)
    mission_id: int | None = Field(default=None, foreign_key="mission.id", primary_key=True)

class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    secret_name: str
    team: Team | None = Relationship(back_populates="heroes")
    missions: list["Mission"] = Relationship(
        back_populates="heroes", link_model=HeroMissionLink
    )


class HeroCreate(HeroBase):
    secret_name: str


class HeroPublic(HeroBase):
    id: int


class HeroUpdate(SQLModel):
    name: str | None = None
    age: int | None = None
    team_id: int | None = None
    secret_name: str | None = None




class MissionBase(SQLModel):
    title: str


class Mission(MissionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    heroes: list[Hero] = Relationship(
        back_populates="missions", link_model=HeroMissionLink
    )


class MissionCreate(MissionBase):
    pass


class MissionPublic(MissionBase):
    id: int