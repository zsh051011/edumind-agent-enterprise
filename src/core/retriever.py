class Retriever:
    def search(self, query: str):
        return [
            {"source": "机器学习基础.pdf#p12", "text": "监督学习使用带标签样本训练模型。", "score": 0.94},
            {"source": "人工智能导论.pdf#p15", "text": "无监督学习用于发现数据内部结构。", "score": 0.91},
            {"source": "强化学习课件.pptx#p08", "text": "强化学习通过奖励信号优化策略。", "score": 0.89},
            {"source": "课堂笔记.docx#p03", "text": "学习范式可以从数据、目标和反馈方式区分。", "score": 0.86},
        ]
