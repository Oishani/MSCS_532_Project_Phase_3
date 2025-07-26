from .label import Label

class LabelSet:
    """Maintain non-dominated labels per node."""
    def __init__(self):
        self.labels: List[Label] = []

    def add(self, label: Label) -> bool:
        """Add label if non-dominated; remove dominated labels."""
        if not isinstance(label, Label):
            raise TypeError("Can only add Label instances")
        new = []
        for existing in self.labels:
            if existing.dominates(label):
                return False
            if not label.dominates(existing):
                new.append(existing)
        new.append(label)
        self.labels = new
        return True

    def __repr__(self) -> str:
        return f"LabelSet({self.labels})"