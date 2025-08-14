#!/usr/bin/env python3
"""
Test script to verify the Ghana Investment Insights RAG pipeline is working correctly.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.main import retrieve_and_answer, collection, embeddings, llm

def test_rag_pipeline():
    """Test the RAG pipeline with sample questions."""
    
    test_questions = [
        "What is the inflation rate in Ghana?",
        "What are the current interest rates?",
        "How is the banking sector performing?",
        "What is the exchange rate situation?"
    ]
    
    print("🇬🇭 Ghana Investment Insights - RAG Pipeline Test")
    print("=" * 60)
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n{i}. Question: {question}")
        print("-" * 40)
        
        try:
            answer = retrieve_and_answer(question, collection, embeddings, llm)
            print(f"Answer: {answer}")
        except Exception as e:
            print(f"Error: {e}")
        
        print()
    
    print("✅ RAG pipeline test completed!")
    print("\nTo start the Streamlit app, run:")
    print("streamlit run app.py")

if __name__ == "__main__":
    test_rag_pipeline()
