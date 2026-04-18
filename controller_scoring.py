import math
from config import SCORING_RINGS

class ScoringEngine:
    def __init__(self):
        pass

    def calculate_distance_from_center(self, x, y):
        """Calculate the distance from the center (0, 0) to the point (x, y)."""
        return math.sqrt(x**2 + y**2)

    def calculate_score(self, x, y):
        """Calculate the score based on the coordinates (x, y) and the configuration of rings."""
        distance = self.calculate_distance_from_center(x, y)
        for ring in SCORING_RINGS:
            if distance <= ring['radius']:
                return ring['score']  # Return score of the ring hit
        return 0  # No score if outside all rings

    def calculate_total_score(self, shots):
        """Calculate the total score from a list of (x, y) shots."""
        total_score = 0
        for shot in shots:
            total_score += self.calculate_score(shot[0], shot[1])
        return total_score
