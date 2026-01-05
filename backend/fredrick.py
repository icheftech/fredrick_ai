#!/usr/bin/env python3
"""
FREDRICK - Fiduciary Risk Evaluation, Due-diligence Reporting & Integrated Compliance Knowledge
Executive AI Partner for Southern Shade LLC

FREDRICK provides business intelligence, compliance oversight, and strategic analysis
with a focus on fiduciary responsibility and due diligence.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from typing import Dict, List, Optional, Any
import json

load_dotenv()

class FREDRICK:
    """
    FREDRICK - Executive AI Partner
    
    Core Principles:
    1. Fiduciary Responsibility - Always act in the best interest of Southern Shade LLC
    2. Risk Evaluation - Comprehensive assessment of business decisions
    3. Due Diligence - Thorough research and verification
    4. Compliance Knowledge - Deep understanding of regulatory requirements
    5. Strategic Analysis - Executive-level business intelligence
    """
    
    def __init__(self, model_name: str = "llama-3.3-70b-versatile"):
        self.model_name = model_name
        self.api_key = os.getenv('GROQ_API_KEY')
        
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found. Set it in .env or pass to constructor.")
        
        # Initialize Groq client (OpenAI-compatible)
        self.client = OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=self.api_key
        )
        
        self.conversation_history = []
        self.org_name = os.getenv("FREDRICK_ORG_NAME", "Southern Shade LLC")
        self.risk_tolerance = os.getenv("FREDRICK_RISK_TOLERANCE", "moderate")
        self.primary_market = os.getenv("FREDRICK_PRIMARY_MARKET", "US_GOV_AND_ENTERPRISE")
        
        # System prompt
        self.system_prompt = f"""You are FREDRICK, the Chief Technology Officer AI for {self.org_name}.

Your role:
- Strategic technical advisor for AI automation and government contracting
- Risk assessment and compliance oversight specialist  
- Business intelligence and due diligence expert
- Focus on {self.primary_market} markets
- Risk tolerance: {self.risk_tolerance}

Key responsibilities:
1. Technical risk evaluation for projects and partnerships
2. Compliance checking (FAR, CMMC, HIPAA, SOC 2, etc.)
3. Due diligence on vendors, opportunities, and partnerships
4. Strategic technology recommendations
5. Cybersecurity and data governance guidance

Always provide:
- Clear go/no-go recommendations
- Specific risk mitigation strategies
- Compliance requirements and gaps
- Actionable next steps
- References to relevant regulations when applicable

Be direct, tactical, and focused on {self.org_name}'s success in government and enterprise AI automation."""
        
    def chat(self, message: str, context: Optional[List[Dict]] = None) -> str:
        """
        Send a message and get a response
        
        Args:
            message: The user's message
            context: Optional conversation context
            
        Returns:
            The model's response as a string
        """
        try:
            messages = [{"role": "system", "content": self.system_prompt}]
            
            if context:
                messages.extend(context)
            
            messages.append({"role": "user", "content": message})
            
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=0.7,
                max_tokens=2048
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def analyze_risk(
        self,
        scenario: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Perform structured risk analysis
        
        Args:
            scenario: Description of the business scenario
            data: Additional data about the scenario
            
        Returns:
            Dictionary containing risk analysis
        """
        prompt = f"""As CTO, analyze the following scenario for technical and business risks:

Scenario: {scenario}

Additional Data:
{json.dumps(data, indent=2) if data else 'None provided'}

Provide a structured risk analysis including:
1. Technical Risks (infrastructure, scalability, security)
2. Compliance Risks (regulatory, contractual, data governance)
3. Resource Risks (team capacity, skills, budget)
4. Timeline Risks (delivery, dependencies)
5. Mitigation Strategies for each risk category
6. Overall Risk Level (Low/Moderate/High/Critical)
7. Go/No-Go Recommendation with rationale"""

        analysis = self.chat(prompt)
        
        return {
            "scenario": scenario,
            "data": data,
            "analysis": analysis,
            "model": self.model_name
        }
    
    def compliance_check(
        self,
        action: str,
        regulations: List[str]
    ) -> Dict[str, Any]:
        """
        Check compliance for a proposed action
        
        Args:
            action: Description of the proposed action
            regulations: List of relevant regulations
            
        Returns:
            Dictionary containing compliance assessment
        """
        regs_str = ", ".join(regulations)
        
        prompt = f"""As CTO with compliance oversight responsibility, evaluate this proposed action:

Action: {action}

Relevant Regulations: {regs_str}

Provide:
1. Compliance Assessment (Compliant/Non-Compliant/Needs Review)
2. Specific Requirements from each regulation
3. Gaps or concerns
4. Required controls or documentation
5. Recommended next steps"""

        assessment = self.chat(prompt)
        
        return {
            "action": action,
            "regulations": regulations,
            "assessment": assessment,
            "model": self.model_name
        }
    
    def due_diligence_report(
        self,
        subject: str,
        scope: List[str]
    ) -> Dict[str, Any]:
        """
        Generate a due diligence report
        
        Args:
            subject: The subject of due diligence (vendor, partner, opportunity)
            scope: List of areas to investigate
            
        Returns:
            Dictionary containing due diligence report
        """
        scope_str = ", ".join(scope)
        
        prompt = f"""As CTO, conduct a due diligence analysis on:

Subject: {subject}

Scope Areas: {scope_str}

For each scope area, provide:
1. Key evaluation criteria
2. Red flags to watch for
3. Required documentation/verification
4. Risk indicators

Conclude with:
- Overall assessment
- Go/No-Go recommendation
- Contingencies or conditions for proceeding"""

        report = self.chat(prompt)
        
        return {
            "subject": subject,
            "scope": scope,
            "report": report,
            "model": self.model_name
        }

def main():
    """
    Interactive demo of FREDRICK
    """
    print("=" * 60)
    print("FREDRICK - Executive AI Partner (Groq-powered)")
    print("=" * 60)
    print()
    
    try:
        fredrick = FREDRICK()
        print(f"Organization: {fredrick.org_name}")
        print(f"Model: {fredrick.model_name}")
        print(f"Risk Tolerance: {fredrick.risk_tolerance}")
        print()
        print("Type 'exit' to quit")
        print()
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            
            response = fredrick.chat(user_input)
            print(f"\nFREDRICK: {response}\n")
    
    except Exception as e:
        print(f"Error initializing FREDRICK: {e}")
        print("\nMake sure you have GROQ_API_KEY set in your .env file")

if __name__ == "__main__":
    main()
