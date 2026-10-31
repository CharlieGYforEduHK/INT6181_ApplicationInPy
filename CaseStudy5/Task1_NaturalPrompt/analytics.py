class AnalyticsEngine:
    def __init__(self, df):
        self.df = df.copy()

    def calculate_overall_scores(self):
        # 按照文档公式: Quiz 30% + Assignment 30% + Exam 40%
        self.df['overall_score'] = (
            self.df['quiz_score'] * 0.30 +
            self.df['assignment_score'] * 0.30 +
            self.df['exam_score'] * 0.40
        )
        return self.df

    def get_class_summary(self):
        return {
            "total_students": len(self.df),
            "class_average": self.df['overall_score'].mean(),
            "pass_rate": (self.df['overall_score'] >= 50).mean() * 100,
            "avg_attendance": self.df['attendance'].mean(),
            "avg_study_hours": self.df['study_hours'].mean()
        }