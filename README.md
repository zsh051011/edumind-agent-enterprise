# EduMind Agent Enterprise

面向大学生课程复习和资料整理场景的企业级 AI Agent Demo。  
项目重点展示：多智能体编排、RAG 检索增强生成、引用校验、风险控制、效果评估和学习报告导出。

## 核心能力

- Multi-Agent Orchestration：Intent Router、Planner、Retriever、Reranker、Generator、Verifier、Exporter
- Retrieval-Augmented Generation：基于课程资料片段生成答案，减少无依据回答
- Guardrails：低置信度降级、PII 过滤、幻觉告警、引用覆盖率检查
- Observability：trace_id、latency、hit_rate、citation_coverage、faithfulness
- Evaluation：Baseline / RAG / RAG + Verifier 三组效果对比
- Output：章节摘要、知识点清单、复习路径、自测题、Markdown 报告

## 运行方式

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 推荐 GitHub 仓库名

```text
edumind-agent-enterprise
```

## 示例指标

| 指标 | 结果 |
|---|---|
| 检索命中率 | 91.3% |
| 答案忠实度 | 92.4% |
| 引用覆盖率 | 94.5% |
| 幻觉告警率 | 2.1% |
| 平均延迟 | 1.82s |
