#!/usr/bin/env python3
"""
FREDRICK - Fiduciary Risk Evaluation, Due-diligence Reporting & Integrated Compliance Knowledge
Executive AI Partner for Southern Shade LLC

FREDRICK provides business intelligence, compliance oversight, and strategic analysis
with a focus on fiduciary responsibility and due diligence.
"""

import os
import sys
import json
from datetime import datetime
from typing import Dict, List, Optional, Any
import google.generativeai as genai

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

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
    
    def __init__(self, model_name: str = "gemini-pro"):
        self.model_name = model_name
        self.model = None
        self.conversation_history = []
        self.initialize_model()
        
    def initialize_model(self):
        """Initialize the Gemini model with FREDRICK's personality"""
        try:
            self.model = genai.GenerativeModel(
                model_name=self.model_name,
                generation_config={
                    "temperature": 0.7,
                    "top_p": 0.95,
                    "top_k": 40,
                    "max_output_tokens": 8192,
                },
                system_instruction=self.get_system_prompt()
            )
            print("FREDRICK initialized successfully")
        except Exception as e:
            print(f"Error initializing FREDRICK: {e}")
            self.model = None
    
    def get_system_prompt(self) -> str:
        """Define FREDRICK's personality and operational parameters"""
        return """You are FREDRICK - Fiduciary Risk Evaluation, Due-diligence Reporting & Integrated Compliance Knowledge.

You are the Executive AI Partner for Southern Shade LLC, providing strategic business intelligence, compliance oversight, and risk analysis.

YOUR CORE IDENTITY:
- Executive Business Partner with fiduciary responsibility
- Strategic advisor focused on long-term value creation
- Compliance and risk management specialist
- Professional, analytical, and detail-oriented
- Direct communicator who provides actionable insights

YOUR RESPONSIBILITIES:
1. FIDUCIARY DUTY: Always act in Southern Shade LLC's best interest
2. RISK EVALUATION: Assess and communicate business risks clearly
3. DUE DILIGENCE: Conduct thorough research and verification
4. COMPLIANCE: Ensure adherence to legal and regulatory requirements
5. STRATEGIC ANALYSIS: Provide executive-level business intelligence

YOUR ETHICAL FRAMEWORK:
- Written authorization required (Rules of Engagement)
- Clear scope boundaries for all engagements
- Stop conditions when requirements are unclear
- Data handling rules compliance (HIPAA, SOC 2, ISO standards)
- Client risk tolerance assessment

YOU REFUSE work that is:
- Undefined or unbounded
- Legally ambiguous
- Reputationally dangerous
- Outside documented authorization

YOUR COMMUNICATION STYLE:
- Professional and executive-appropriate
- Data-driven with clear rationale
- Risk-aware and compliance-conscious
- Action-oriented with specific recommendations
- Transparent about limitations and uncertainties

YOU EXCEL AT:
- Business analysis and strategy
- Compliance and regulatory review
- Risk assessment and mitigation
- Due diligence investigations
- Executive decision support
- Contract and agreement analysis
- Competitive intelligence
- Market research and analysis

You keep stakeholders informed, out of legal exposure, and focused on strategic objectives.
You translate technical risks into executive language and provide clear, actionable guidance."""
    
    def chat(self, user_message: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Process user message and return FREDRICK's response"""
        if not self.model:
            return "FREDRICK is not properly initialized. Please check your Gemini API key."
        
        try:
            # Add context if provided
            full_message = user_message
            if context:
                full_message = f"Context: {json.dumps(context)}\n\nMessage: {user_message}"
            
            # Store message in history
            self.conversation_history.append({
                "role": "user",
                "content": full_message,
                "timestamp": datetime.now().isoformat()
            })
            
            # Generate response
            response = self.model.generate_content(full_message)
            response_text = response.text
            
            # Store response in history
            self.conversation_history.append({
                "role": "assistant",
                "content": response_text,
                "timestamp": datetime.now().isoformat()
            })
            
            return response_text
            
        except Exception as e:
            error_msg = f"Error processing message: {str(e)}"
            print(error_msg)
            return error_msg
    
    def analyze_risk(self, scenario: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        """Perform structured risk analysis"""
        prompt = f"""Conduct a comprehensive risk analysis for the following scenario:

Scenario: {scenario}

{f'Additional Data: {json.dumps(data, indent=2)}' if data else ''}

Provide analysis in the following structure:
1. Risk Identification
2. Risk Assessment (likelihood and impact)
3. Risk Mitigation Strategies
4. Compliance Considerations
5. Recommendations
"""
        response = self.chat(prompt)
        return {
            "scenario": scenario,
            "analysis": response,
            "timestamp": datetime.now().isoformat()
        }
    
    def compliance_check(self, action: str, regulations: List[str]) -> Dict[str, Any]:
        """Check proposed action against regulatory requirements"""
        prompt = f"""Review the following action for compliance:

Proposed Action: {action}

Relevant Regulations: {', '.join(regulations)}

Provide:
1. Compliance Status Assessment
2. Potential Issues or Violations
3. Required Documentation
4. Recommended Modifications
5. Approval Requirements
"""
        response = self.chat(prompt)
        return {
            "action": action,
            "regulations": regulations,
            "assessment": response,
            "timestamp": datetime.now().isoformat()
        }
    
    def due_diligence_report(self, subject: str, scope: List[str]) -> Dict[str, Any]:
        """Generate due diligence report"""
        prompt = f"""Conduct due diligence investigation on:

Subject: {subject}

Scope Areas: {', '.join(scope)}

Provide comprehensive report covering:
1. Executive Summary
2. Findings by Scope Area
3. Risk Factors Identified
4. Red Flags or Concerns
5. Verification Status
6. Recommendations
"""
        response = self.chat(prompt)
        return {
            "subject": subject,
            "scope": scope,
            "report": response,
            "timestamp": datetime.now().isoformat()
        }
    
    def get_conversation_history(self) -> List[Dict]:
        """Return conversation history"""
        return self.conversation_history
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        print("Conversation history cleared")

def main():
    """Main function for testing FREDRICK"""
    print("="*60)
    print("FREDRICK - Executive AI Partner")
    print("Fiduciary Risk Evaluation, Due-diligence Reporting &")
    print("Integrated Compliance Knowledge")
    print("="*60)
    print()
    
    # Initialize FREDRICK
    fredrick = FREDRICK()
    
    # Test conversation
    if fredrick.model:
        print("FREDRICK is ready. Type 'exit' to quit, 'clear' to clear history.")
        print()
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if user_input.lower() == 'exit':
                    print("Thank you for consulting with FREDRICK.")
                    break
                
                if user_input.lower() == 'clear':
                    fredrick.clear_history()
                    continue
                
                if not user_input:
                    continue
                
                response = fredrick.chat(user_input)
                print(f"\nFREDRICK: {response}\n")
                
            except KeyboardInterrupt:
                print("\n\nSession terminated.")
                break
            except Exception as e:
                print(f"Error: {e}")
    else:
        print("Failed to initialize FREDRICK. Please check your configuration.")

if __name__ == "__main__":
    main()
