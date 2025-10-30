"""
Quick Browser Test - Partial Matching
Simulasi request dari browser
"""

import requests
import json

print("="*60)
print("🧪 TESTING PARTIAL MATCHING - Browser Simulation")
print("="*60)

# Test 1: Partial Match (seperti user pilih 3 dari 4 gejala)
print("\n📝 Test 1: Partial Match (75% confidence)")
print("-" * 60)

response = requests.post(
    "http://localhost:5000/api/diagnose",
    json={
        "symptoms": ["P02", "P03", "P04"],
        "detailed": True,
        "threshold": 60,
        "top_n": 5
    }
)

print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    
    if data.get('success'):
        result = data['data']
        diagnoses = result.get('diagnoses_found', [])
        
        print(f"✅ Success! Found {len(diagnoses)} diagnosis")
        
        if diagnoses:
            diag = diagnoses[0]
            print(f"\n🎯 Top Result:")
            print(f"   Diagnosis: {diag.get('diagnosis', 'N/A')}")
            print(f"   Confidence: {diag.get('confidence', 'N/A')}%")
            print(f"   Category: {diag.get('category', 'N/A')}")
            print(f"   Severity: {diag.get('severity', 'N/A')}")
            
            if 'matched_symptoms' in diag:
                print(f"   ✓ Matched: {', '.join(diag['matched_symptoms'])}")
            
            if 'missing_symptoms' in diag and diag['missing_symptoms']:
                print(f"   ✗ Missing: {', '.join(diag['missing_symptoms'])}")
            
            print(f"\n📋 Full Response Structure:")
            print(json.dumps(data, indent=2, ensure_ascii=False)[:500] + "...")
        else:
            print("❌ No diagnoses found")
    else:
        print(f"❌ API Error: {data.get('error', 'Unknown error')}")
else:
    print(f"❌ HTTP Error: {response.status_code}")
    print(response.text[:200])

print("\n" + "="*60)
print("✅ Test Complete!")
print("="*60)
