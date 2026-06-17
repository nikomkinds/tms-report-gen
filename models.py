from dataclasses import dataclass, field


# Given in steps CSV
@dataclass
class TestStep:
    id: int
    step_type: str
    action: str
    expected_result: str
    order: int


# Given in case CSV
@dataclass
class TestCase:
    id: int

    name: str
    title: str

    status: int

    is_tracked: bool
    is_auto: bool
    is_individ: bool
    is_unique: bool

    priority: int
    test_type: int
    complexity: int

    steps: list[TestStep] = field(default_factory=list)