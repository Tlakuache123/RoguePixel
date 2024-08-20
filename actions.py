from attrs import define


@define
class Action:
    pass


@define
class EscapeAction(Action):
    pass


@define
class MovementAction(Action):
    dx: int
    dy: int
