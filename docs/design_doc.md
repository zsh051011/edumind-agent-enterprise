# Design Doc

EduMind Agent Enterprise 使用多 Agent 编排和 RAG 检索增强生成。系统通过 Parser 解析课程资料，通过 Retriever 检索相关片段，通过 Verifier 检查回答是否被资料支撑。

## 设计目标

1. 让回答有来源
2. 让流程可追踪
3. 让效果可评估
4. 让低置信度场景可降级
