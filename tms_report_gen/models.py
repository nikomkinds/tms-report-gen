from dataclasses import dataclass, field


# Given in steps CSV
@dataclass
class TestStep:
    id: int
    step_type: str
    action: str
    expected_result: str
    order: int | None


# Given in case CSV
@dataclass
class TestCase:
    id: int

    name: str
    title: str

    status: int | None

    is_tracked: bool
    is_auto: bool
    is_individ: bool
    is_unique: bool

    priority: int | None
    test_type: int | None
    complexity: int | None

    steps: list[TestStep] = field(default_factory=list)