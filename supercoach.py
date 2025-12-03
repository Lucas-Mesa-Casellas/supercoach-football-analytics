"""
supercoach.py
--------------
Main pipeline: loads video, runs detection + tracking + tactical analysis.
"""

from detection import PlayerDetector
from tracking import PlayerTracker
from tactical_analysis import TacticalAnalyzer

class SuperCoach:
    def __init__(self):
        self.detector = PlayerDetector()
        self.tracker = PlayerTracker()
        self.analyzer = TacticalAnalyzer()

    def process_frame(self, frame):
        detections = self.detector.detect(frame)
        tracked = self.tracker.update(detections)
        metrics = self.analyzer.compute_heatmap(tracked)
        return metrics
