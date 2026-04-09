from agents.planner import plan
from agents.research_agent import research
from agents.analysis_agent import analyze
from agents.reasoning_agent import reason
from agents.report_agent import generate_report
from memory.memory_store import store_memory
from rag.vector_store import VectorStore

def run_pipeline(query, documents):
    vector_store = VectorStore()
    vector_store.build_index(documents)

    steps = plan(query)
    data = research(query, vector_store)
    insights = analyze(data)
    conclusion = reason(insights)
    report = generate_report(query, insights, conclusion)

    store_memory(query, report)

    return report