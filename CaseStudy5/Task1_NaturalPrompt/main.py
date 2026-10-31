import os
from data_loader import DataLoader
from analytics import AnalyticsEngine
from risk_detector import RiskDetector
from recommender import Recommender

def main():
    print("==================================================")
    print("   EduTrack - Learning Analytics Dashboard        ")
    print("==================================================")
    
    filepath = input("Enter CSV path (press Enter for default 'data/student_records.csv'): ").strip()
    if not filepath:
        filepath = "data/student_records.csv"
        
    try:
        loader = DataLoader(filepath)
        df = loader.load_and_validate()
        
        analytics = AnalyticsEngine(df)
        df = analytics.calculate_overall_scores()
        
        summary = analytics.get_class_summary()
        print("\n--- [1] Class Summary Statistics ---")
        print(f"Total Students:   {summary['total_students']}")
        print(f"Class Average:    {summary['class_average']:.2f}%")
        print(f"Pass Rate:        {summary['pass_rate']:.1f}%")
        print(f"Avg Attendance:   {summary['avg_attendance']:.1f}%")
        
        risk_detector = RiskDetector(df)
        at_risk = risk_detector.identify_at_risk_students()
        print(f"\n--- [2] At-Risk Students Identified ({len(at_risk)}) ---")
        for _, row in at_risk.iterrows():
            rec = Recommender.generate_recommendation(row)
            print(f"• ID: {row['student_id']} | Name: {row['name']} | Score: {row['overall_score']:.1f} | Reason: {row['risk_reason']}")
            print(f"  Recommendation: {rec}\n")
            
    except Exception as e:
        print(f"\n❌ Error processing file: {e}")

if __name__ == "__main__":
    main()