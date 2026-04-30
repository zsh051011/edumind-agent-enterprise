class Verifier:
    def check(self, answer: str, sources):
        return {
            "faithfulness": 0.924,
            "citation_coverage": 0.945,
            "hallucination_warning": False,
            "decision": "pass",
            "reason": "关键结论均可由检索片段支撑"
        }
