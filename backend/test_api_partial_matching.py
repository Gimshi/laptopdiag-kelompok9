"""
API Test untuk Partial Matching Feature
Test endpoint /api/diagnose dengan berbagai skenario
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def print_header(title):
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def print_result(result, test_name):
    print(f"\n📝 {test_name}")
    print("-" * 60)
    
    if result.get('success'):
        data = result['data']
        
        # Summary
        if 'summary' in data:
            summary = data['summary']
            print(f"\n✅ Summary:")
            print(f"   Total Symptoms: {summary.get('total_symptoms', 'N/A')}")
            print(f"   Total Diagnoses: {summary.get('total_diagnoses', 'N/A')}")
            print(f"   Total Candidates: {summary.get('total_candidates', 'N/A')}")
            print(f"   Threshold Used: {summary.get('threshold_used', 'N/A')}%")
            print(f"   Strict Mode: {summary.get('strict_mode', 'N/A')}")
        
        # Diagnoses
        diagnoses = data.get('diagnoses_found', [])
        if diagnoses:
            print(f"\n🎯 Diagnoses Found ({len(diagnoses)}):")
            for i, diag in enumerate(diagnoses, 1):
                print(f"\n{i}. {diag['diagnosis']}")
                
                # Check if it's detailed response
                if isinstance(diag, dict) and 'confidence' in diag:
                    print(f"   Confidence: {diag['confidence']}%")
                    
                    if 'matched_symptoms' in diag:
                        print(f"   Matched: {', '.join(diag['matched_symptoms'])}")
                    
                    if 'missing_symptoms' in diag and diag['missing_symptoms']:
                        print(f"   Missing: {', '.join(diag['missing_symptoms'])}")
                    
                    if 'match_ratio' in diag:
                        print(f"   Match Ratio: {diag['match_ratio']}")
        else:
            print("\n❌ No diagnoses found")
    else:
        print(f"\n❌ Error: {result.get('error', 'Unknown error')}")

# ============================================================
# TESTS
# ============================================================

print_header("🧪 API PARTIAL MATCHING TESTS")

# Test 1: Partial Match - 75%
print_header("TEST 1: Partial Match (75%)")
test_data = {
    "symptoms": ["P02", "P03", "P04"],
    "detailed": True,
    "threshold": 60,
    "top_n": 5
}

try:
    response = requests.post(f"{BASE_URL}/api/diagnose", json=test_data)
    result = response.json()
    print_result(result, "Partial Match - Missing 1 symptom")
    print(f"\nRequest: {json.dumps(test_data, indent=2)}")
except Exception as e:
    print(f"❌ Error: {e}")

# Test 2: Perfect Match - 100%
print_header("TEST 2: Perfect Match (100%)")
test_data = {
    "symptoms": ["P02", "P03", "P04", "P05"],
    "detailed": True,
    "threshold": 60,
    "top_n": 5
}

try:
    response = requests.post(f"{BASE_URL}/api/diagnose", json=test_data)
    result = response.json()
    print_result(result, "Perfect Match - All symptoms present")
except Exception as e:
    print(f"❌ Error: {e}")

# Test 3: Multiple Partial Matches
print_header("TEST 3: Multiple Partial Matches")
test_data = {
    "symptoms": ["P20"],
    "detailed": True,
    "threshold": 20,  # Lower threshold
    "top_n": 10
}

try:
    response = requests.post(f"{BASE_URL}/api/diagnose", json=test_data)
    result = response.json()
    print_result(result, "Single symptom matches multiple rules")
except Exception as e:
    print(f"❌ Error: {e}")

# Test 4: Strict Mode
print_header("TEST 4: Strict Mode (100% Only)")
test_data = {
    "symptoms": ["P02", "P03", "P04"],
    "detailed": True,
    "threshold": 100,
    "top_n": 5,
    "strict_mode": True
}

try:
    response = requests.post(f"{BASE_URL}/api/diagnose", json=test_data)
    result = response.json()
    print_result(result, "Strict Mode - Should find no results")
except Exception as e:
    print(f"❌ Error: {e}")

# Test 5: High Threshold (80%)
print_header("TEST 5: High Threshold (80%)")
test_data = {
    "symptoms": ["P02", "P03", "P04"],
    "detailed": True,
    "threshold": 80,
    "top_n": 5
}

try:
    response = requests.post(f"{BASE_URL}/api/diagnose", json=test_data)
    result = response.json()
    print_result(result, "High threshold - May filter out some results")
except Exception as e:
    print(f"❌ Error: {e}")

# Test 6: Simple Mode (non-detailed)
print_header("TEST 6: Simple Mode")
test_data = {
    "symptoms": ["P02", "P03", "P04", "P05"],
    "detailed": False,
    "threshold": 60,
    "top_n": 5
}

try:
    response = requests.post(f"{BASE_URL}/api/diagnose", json=test_data)
    result = response.json()
    print_result(result, "Simple mode - Less detailed response")
except Exception as e:
    print(f"❌ Error: {e}")

print("\n" + "="*60)
print("  ✅ ALL API TESTS COMPLETED")
print("="*60)
print("\n💡 Tips:")
print("   - threshold: 60 = Show results with 60%+ match")
print("   - top_n: 5 = Return max 5 results")
print("   - strict_mode: true = Only 100% matches")
print("   - detailed: true = Include matched/missing symptoms")
