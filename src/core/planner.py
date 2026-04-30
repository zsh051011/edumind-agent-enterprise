class Planner:
    def plan(self, question: str):
        return {
            "intent": "course_qa_and_review",
            "steps": [
                "parse user question",
                "retrieve course chunks",
                "rerank evidence",
                "generate grounded answer",
                "verify citations",
                "export study report"
            ],
            "fallback": "ask user to upload more course material if retrieval confidence is low"
        }
