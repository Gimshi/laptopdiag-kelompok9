"""
Test API P13 - Browser Simulation
"""

import requests
import json

print("="*60)
print("🧪 Testing P13 with Adaptive Threshold")
print("="*60)

# Test dengan P13 saja
print("\n📝 Request: P13 (Mouse tidak berfungsi)")
print("-" * 60)

response = requests.post(
    "http://localhost:5000/api/diagnose",
    json={
        "symptoms": ["P13"],
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
        summary = result.get('summary', {})
        diagnoses = result.get('diagnoses_found', [])
        
        print(f"\n✅ Success!")
        print(f"   Total Candidates: {summary.get('total_candidates', 0)}")
        print(f"   Diagnoses Shown: {len(diagnoses)}")
        print(f"   Adaptive Mode: {summary.get('adaptive_mode', False)}")
        print(f"   Original Threshold: {summary.get('original_threshold', 'N/A')}%")
        print(f"   Used Threshold: {summary.get('threshold_used', 'N/A')}%")
        
        if diagnoses:
            print(f"\n🎯 Results:")
            for i, diag in enumerate(diagnoses, 1):
                print(f"\n{i}. {diag.get('diagnosis', 'N/A')}")
                print(f"   Confidence: {diag.get('confidence', 'N/A')}%")
                print(f"   Category: {diag.get('category', 'N/A')}")
                print(f"   Severity: {diag.get('severity', 'N/A')}")
                
                if 'matched_symptoms' in diag:
                    print(f"   ✓ Matched: {', '.join(diag['matched_symptoms'])}")
                
                if 'missing_symptoms' in diag and diag['missing_symptoms']:
                    print(f"   ✗ Missing: {', '.join(diag['missing_symptoms'])}")
        else:
            print("\n❌ No diagnoses found")
    else:
        print(f"❌ API Error: {data.get('error', 'Unknown error')}")
else:
    print(f"❌ HTTP Error: {response.status_code}")

print("\n" + "="*60)
print("✅ Test Complete!")
print("="*60)
