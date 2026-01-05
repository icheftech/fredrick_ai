#!/usr/bin/env python3
"""
FREDRICK AI REST API Test Script

This script demonstrates how to interact with the FREDRICK AI REST API.

Setup:
1. Ensure the API server is running: python backend/api.py
2. Set FREDRICK_API_KEY in your .env file
3. Run this script: python backend/test_api.py
"""

import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
API_BASE_URL = "http://localhost:8000"
API_KEY = os.getenv("FREDRICK_API_KEY")

if not API_KEY:
    print("ERROR: FREDRICK_API_KEY not found in .env file")
    print("Please add: FREDRICK_API_KEY=your_secret_key_here")
    exit(1)

headers = {
    "X-API-Key": API_KEY,
    "Content-Type": "application/json"
}

def test_health_check():
    """Test the health check endpoint"""
    print("\n=== Testing Health Check ===")
    response = requests.get(f"{API_BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    return response.status_code == 200

def test_chat():
    """Test the chat endpoint"""
    print("\n=== Testing Chat Endpoint ===")
    payload = {
        "message": "What are the key risks in expanding into international markets?",
        "context": "Southern Shade LLC is considering expansion into Mexico"
    }
    response = requests.post(
        f"{API_BASE_URL}/chat",
        json=payload,
        headers=headers
    )
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Model: {data['model']}")
        print(f"Response: {data['response'][:200]}...")  # First 200 chars
        return True
    else:
        print(f"Error: {response.text}")
        return False

def test_risk_analysis():
    """Test the risk analysis endpoint"""
    print("\n=== Testing Risk Analysis Endpoint ===")
    payload = {
        "business_data": """Company: Southern Shade LLC
Revenue: $2.5M annually
Employees: 15
Industry: Construction/Outdoor Services
Operations: Texas-based, expanding to new markets
Current Contracts: 5 major government contracts""",
        "risk_areas": ["financial", "operational", "legal"]
    }
    response = requests.post(
        f"{API_BASE_URL}/risk-analysis",
        json=payload,
        headers=headers
    )
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Analysis Preview: {data['analysis'][:200]}...")  # First 200 chars
        return True
    else:
        print(f"Error: {response.text}")
        return False

def test_compliance_check():
    """Test the compliance check endpoint"""
    print("\n=== Testing Compliance Check Endpoint ===")
    payload = {
        "document": """EMPLOYMENT AGREEMENT
Employee shall work 50 hours per week with no overtime compensation.
Termination without cause is permitted with 1 day notice.
Employee agrees to non-compete for 5 years in Texas.""",
        "compliance_framework": "Texas Labor Law"
    }
    response = requests.post(
        f"{API_BASE_URL}/compliance-check",
        json=payload,
        headers=headers
    )
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Framework: {data['framework']}")
        print(f"Report Preview: {data['compliance_report'][:200]}...")  # First 200 chars
        return True
    else:
        print(f"Error: {response.text}")
        return False

def test_due_diligence():
    """Test the due diligence endpoint"""
    print("\n=== Testing Due Diligence Endpoint ===")
    payload = {
        "company_info": """Company: XYZ Construction Inc.
Founded: 2018
Revenue: $5M (2023), $3M (2022), $1.5M (2021)
Debt: $2M outstanding
Lawsuits: 2 pending labor disputes
Contracts: Mix of government and private sector
Management: CEO with 15 years experience, CFO new hire (6 months)""",
        "focus_areas": ["financial health", "legal risks", "management team"]
    }
    response = requests.post(
        f"{API_BASE_URL}/due-diligence",
        json=payload,
        headers=headers
    )
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"Report Preview: {data['due_diligence_report'][:200]}...")  # First 200 chars
        return True
    else:
        print(f"Error: {response.text}")
        return False

def main():
    """Run all API tests"""
    print("="*60)
    print("FREDRICK AI REST API Test Suite")
    print("="*60)
    
    results = {
        "Health Check": test_health_check(),
        "Chat": test_chat(),
        "Risk Analysis": test_risk_analysis(),
        "Compliance Check": test_compliance_check(),
        "Due Diligence": test_due_diligence()
    }
    
    # Summary
    print("\n" + "="*60)
    print("Test Results Summary")
    print("="*60)
    for test_name, passed in results.items():
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{test_name}: {status}")
    
    total = len(results)
    passed = sum(results.values())
    print(f"\nTotal: {passed}/{total} tests passed")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
