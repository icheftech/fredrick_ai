# FREDRICK AI

**F**iduciary **R**isk **E**valuation, **D**ue-diligence **R**eporting & **I**ntegrated **C**ompliance **K**nowledge

## Overview

FREDRICK is an Executive AI Partner for Southern Shade LLC, providing strategic business intelligence, compliance oversight, and risk analysis. Built on Groq's high-performance AI inference platform, FREDRICK combines advanced language understanding with enterprise-grade ethical frameworks and operational parameters.

## Core Principles

1. **Fiduciary Responsibility** - Always acts in the best interest of Southern Shade LLC
2. **Risk Evaluation** - Comprehensive assessment of business decisions
3. **Due Diligence** - Thorough research and verification
4. **Compliance Knowledge** - Deep understanding of regulatory requirements
5. **Strategic Analysis** - Executive-level business intelligence

## Features

- **Executive Business Partner**: Strategic advisor focused on long-term value creation
- **Risk Assessment**: Structured analysis of scenarios with mitigation strategies
- **Compliance Checking**: Review actions against regulatory requirements
- **Due Diligence Reports**: Comprehensive investigation and verification
- **Ethical Framework**: Written authorization (ROE), clear scope boundaries, stop conditions
- **Professional Communication**: Executive-appropriate, data-driven, action-oriented

## Installation

### Prerequisites

- Python 3.8 or higher
- Groq API key ([Get one here](Groqhttps://console.groq.com/keys))

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/icheftech/fredrick_ai.git
   cd fredrick_ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env and add your Groq's highGROQ_API_KEY-performance AI inference platform
   ```

4. **Run FREDRICK**
   ```bash
   python backend/fredrick.py
   ```

## Usage

### Basic Conversation

```python
from backend.fredrick import FREDRICK

# Initialize FREDRICK
fredrick = FREDRICK()

# Chat with FREDRICK
response = fredrick.chat("Analyze the risks of expanding into the Houston market")
print(response)
```

### Risk Analysis

```python
# Perform structured risk analysis
risk_report = fredrick.analyze_risk(
    scenario="Launching new service offering in Q2",
    data={
        "budget": 50000,
        "timeline": "3 months",
        "team_size": 5
    }
)
print(risk_report['analysis'])
```

### Compliance Check

```python
# Check compliance for a proposed action
compliance_report = fredrick.compliance_check(
    action="Collecting customer email addresses for marketing",
    regulations=["GDPR", "CAN-SPAM", "CCPA"]
)
print(compliance_report['assessment'])
```

### Due Diligence

```python
# Generate due diligence report
dd_report = fredrick.due_diligence_report(
    subject="Potential Vendor Partnership",
    scope=["Financial Stability", "Reputation", "Compliance History", "References"]
)
print(dd_report['report'])
```

## FREDRICK's Ethical Framework

FREDRICK operates under strict ethical guidelines:

### Requirements
- **Written Authorization (ROE)**: All engagements require clear rules of engagement
- **Clear Scope Boundaries**: Defined parameters for all activities
- **Stop Conditions**: Halts when requirements are unclear or undefined
- **Data Handling Rules**: Compliant with HIPAA, SOC 2, ISO standards
- **Client Risk Tolerance**: Assesses and respects organizational risk appetite

### Refusal Criteria

FREDRICK refuses work that is:
- Undefined or unbounded
- Legally ambiguous
- Reputationally dangerous
- Outside documented authorization

## Architecture

```
fredrick_ai/
├── backend/
│   └── fredrick.py          # Core FREDRICK implementation
├── .env.example             # Environment variable template
├── .gitignore              # Git ignore rules
├── LICENSE                 # MIT License
├── README.md               # This file
└── requirements.txt        # Python dependencies
```

## Development

### Running Tests

```bash
pytest tests/
```

### Code Quality

```bash
# Format code
black backend/

# Lint code
flake8 backend/

# Type checking
mypy backend/
```

## REST API

FREDRICK provides a production-ready REST API for programmatic access to all features.

### Quick Start

1. **Start the API server**

```bash
python backend/api.py
```

The server will run on `http://localhost:8000`

2. **Set up authentication**

Add to your `.env` file:
```bash
FREDRICK_API_KEY=your_secure_api_key_here
```

Generate a secure key:
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### API Endpoints

#### Health Check
```bash
curl http://localhost:8000/
```

#### Chat - General Business Intelligence
```bash
curl -X POST http://localhost:8000/chat \
  -H "X-API-Key: your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What are the compliance risks for a SAM.gov contract?",
    "context": "250K, 12-month contract, CMMC Level 1 required"
  }'
```

#### Risk Analysis
```bash
curl -X POST http://localhost:8000/risk-analysis \
  -H "X-API-Key: your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "business_data": "Expanding into Mexico market with $500K investment",
    "risk_areas": ["financial", "legal", "operational"]
  }'
```

#### Compliance Check
```bash
curl -X POST http://localhost:8000/compliance-check \
  -H "X-API-Key: your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "document": "Employment agreement text...",
    "compliance_framework": "Texas Labor Law"
  }'
```

#### Due Diligence
```bash
curl -X POST http://localhost:8000/due-diligence \
  -H "X-API-Key: your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "company_info": "XYZ Corp, Founded 2018, $5M revenue...",
    "focus_areas": ["financial health", "legal risks"]
  }'
```

### Testing

Run the comprehensive test suite:
```bash
python backend/test_api.py
```

### API Documentation

Interactive API documentation available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`


## Roadmap

- [x ] Web API with FastAPI
- [ ] Desktop application with Electron
- [ ] Document analysis and summarization
- [ ] Integration with business intelligence tools
- [ ] Multi-model support (Claude, GPT-4, etc.)
- [ ] Conversation memory and context management
- [ ] Report generation and export (PDF, DOCX)

## License

MIT License - see [LICENSE](LICENSE) file for details

## About Southern Shade LLC

Southern Shade LLC is an enterprise AI and business solutions provider focused on delivering intelligent automation and strategic advisory services.

## Support

For questions or issues, please open an issue on GitHub or contact the development team.

---

**Built with ❤️ by Southern Shade LLC**
