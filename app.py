import streamlit as st
from src.core.planner import Planner
from src.core.retriever import Retriever
from src.core.verifier import Verifier
from src.evaluation.metrics import build_metrics

st.set_page_config(page_title="EduMind Agent Enterprise", layout="wide")

st.title("EduMind Agent Enterprise")
st.caption("RAG · Multi-Agent · Guardrails · Observability")

planner = Planner()
retriever = Retriever()
verifier = Verifier()

with st.sidebar:
    st.header("Agent Modules")
    st.write("Intent Router")
    st.write("Planner")
    st.write("Retriever")
    st.write("Reranker")
    st.write("Generator")
    st.write("Verifier")
    st.write("Exporter")
    

question = st.text_input("输入课程问题", "监督学习、无监督学习和强化学习有什么区别？")
uploaded = st.file_uploader("上传课程资料", type=["pdf", "pptx", "docx", "txt"], accept_multiple_files=True)

metrics = build_metrics()
cols = st.columns(5)
for col, (k, v) in zip(cols, metrics.items()):
    col.metric(k, v)

if st.button("Run Enterprise Agent"):
    plan = planner.plan(question)
    sources = retriever.search(question)
    answer = (
        "监督学习依赖带标签样本学习输入到输出的映射；"
        "无监督学习从无标签数据中发现结构；"
        "强化学习通过奖励反馈学习策略。"
        "在课程复习中，可分别理解为：有答案学习、自己找规律、通过试错优化。"
    )
    check = verifier.check(answer, sources)

    st.subheader("Agent Plan")
    st.json(plan)

    st.subheader("Retrieved Sources")
    st.table(sources)

    st.subheader("Answer")
    st.info(answer)

    st.subheader("Verifier Result")
    st.json(check)

    report = "# EduMind Agent Report\n\n" + answer
    st.download_button("下载学习报告", report, file_name="edumind_report.md")
