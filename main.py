
from agents.planner import run as planner
from agents.writer import run as writer
from agents.social_agent import run as social
from analytics import run as analytics

def pipeline():
    planner();writer();social();analytics()
    print("=== 今日运营完成 ===")

if __name__=="__main__":
    pipeline()
