import unittest
import pandas as pd
from analytics import AnalyticsEngine
from risk_detector import RiskDetector

class TestEduTrackAnalytics(unittest.TestCase):
    def setUp(self):
        self.sample_data = pd.DataFrame([{
            'student_id': 'S001', 'name': 'Alice', 'subject': 'Python',
            'quiz_score': 80, 'assignment_score': 80, 'exam_score': 80,
            'attendance': 90, 'study_hours': 5
        }, {
            'student_id': 'S002', 'name': 'Ben', 'subject': 'Python',
            'quiz_score': 40, 'assignment_score': 40, 'exam_score': 40,
            'attendance': 60, 'study_hours': 2
        }])

    def test_weighted_score_calculation(self):
        engine = AnalyticsEngine(self.sample_data)
        df_res = engine.calculate_overall_scores()
        # 80*0.3 + 80*0.3 + 80*0.4 = 80.0
        self.assertEqual(df_res.loc[0, 'overall_score'], 80.0)
        # 40*0.3 + 40*0.3 + 40*0.4 = 40.0
        self.assertEqual(df_res.loc[1, 'overall_score'], 40.0)

    def test_at_risk_detection(self):
        engine = AnalyticsEngine(self.sample_data)
        df_res = engine.calculate_overall_scores()
        detector = RiskDetector(df_res)
        at_risk = detector.identify_at_risk_students()
        
        self.assertEqual(len(at_risk), 1)
        self.assertEqual(at_risk.iloc[0]['student_id'], 'S002')

if __name__ == '__main__':
    unittest.main()