class Recommender:
    @staticmethod
    def generate_recommendation(student_row):
        recs = []
        if student_row['quiz_score'] < 60:
            recs.append("Review quiz topics and complete practice exercises.")
        if student_row['exam_score'] < 50:
            recs.append("Attend additional academic support sessions for exam prep.")
        if student_row['attendance'] < 75:
            recs.append("Monitor and improve daily lecture attendance.")
        if not recs:
            recs.append("Student is performing well; maintain current study habits.")
        return " ".join(recs)