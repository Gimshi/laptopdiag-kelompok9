"""
Test Partial Matching Feature
Test untuk fitur partial matching dengan confidence score
"""

from knowledge_base import KnowledgeBase
from forward_chaining import ForwardChainingEngine

# Initialize
kb = KnowledgeBase()
engine = ForwardChainingEngine(kb)

print("="*60)
print("🧪 TEST PARTIAL MATCHING FEATURE")
print("="*60)

# Test Case 1: Partial Match (75% confidence)
print("\n📋 TEST CASE 1: Partial Match - Baterai Rusak")
print("-" * 60)
print("Symptoms: ['P02', 'P03', 'P04']")
print("Expected: R01 (Baterai) at 75% confidence (missing P05)")
print()

symptoms_1 = ['P02', 'P03', 'P04']
result_1 = engine.run(symptoms_1, threshold=60, top_n=5)

print(f"✅ Total Candidates Found: {result_1['total_candidates']}")
print(f"✅ Threshold Used: {result_1['threshold_used']}%")
print(f"\n🎯 Top Results:")

for i, diag in enumerate(result_1['diagnoses'], 1):
    print(f"\n{i}. {diag['diagnosis']['diagnosis']}")
    print(f"   Rule: {diag['rule_id']}")
    print(f"   Confidence: {diag['confidence']}%")
    print(f"   Match: {diag['matched_count']}/{diag['total_conditions']} symptoms")
    print(f"   Matched: {', '.join(diag['matched_symptoms'])}")
    print(f"   Missing: {', '.join(diag['missing_symptoms']) if diag['missing_symptoms'] else 'None'}")

# Test Case 2: Perfect Match (100% confidence)
print("\n\n📋 TEST CASE 2: Perfect Match - Baterai Rusak")
print("-" * 60)
print("Symptoms: ['P02', 'P03', 'P04', 'P05']")
print("Expected: R01 (Baterai) at 100% confidence")
print()

symptoms_2 = ['P02', 'P03', 'P04', 'P05']
result_2 = engine.run(symptoms_2, threshold=60, top_n=5)

print(f"✅ Total Candidates Found: {result_2['total_candidates']}")
print(f"\n🎯 Top Result:")

if result_2['diagnoses']:
    diag = result_2['diagnoses'][0]
    print(f"\n1. {diag['diagnosis']['diagnosis']}")
    print(f"   Rule: {diag['rule_id']}")
    print(f"   Confidence: {diag['confidence']}%")
    print(f"   Match: {diag['matched_count']}/{diag['total_conditions']} symptoms")

# Test Case 3: Multiple Partial Matches
print("\n\n📋 TEST CASE 3: Multiple Partial Matches")
print("-" * 60)
print("Symptoms: ['P20']")
print("Expected: Multiple rules containing P20")
print()

symptoms_3 = ['P20']
result_3 = engine.run(symptoms_3, threshold=20, top_n=10)  # Lower threshold for demo

print(f"✅ Total Candidates Found: {result_3['total_candidates']}")
print(f"✅ Threshold Used: {result_3['threshold_used']}%")
print(f"\n🎯 All Matches:")

for i, diag in enumerate(result_3['diagnoses'], 1):
    print(f"\n{i}. {diag['diagnosis']['diagnosis']}")
    print(f"   Rule: {diag['rule_id']}")
    print(f"   Confidence: {diag['confidence']}%")
    print(f"   Match: {diag['matched_count']}/{diag['total_conditions']} symptoms")

# Test Case 4: Strict Mode (100% only)
print("\n\n📋 TEST CASE 4: Strict Mode (100% Match Only)")
print("-" * 60)
print("Symptoms: ['P02', 'P03', 'P04']")
print("Expected: No results (because strict mode requires 100%)")
print()

symptoms_4 = ['P02', 'P03', 'P04']
result_4 = engine.run(symptoms_4, threshold=100, top_n=5, strict_mode=True)

print(f"✅ Strict Mode: {result_4['strict_mode']}")
print(f"✅ Diagnoses Found: {len(result_4['diagnoses'])}")

if result_4['diagnoses']:
    print("\n🎯 Results:")
    for i, diag in enumerate(result_4['diagnoses'], 1):
        print(f"{i}. {diag['diagnosis']['diagnosis']}")
else:
    print("\n❌ No perfect matches found (as expected)")

print("\n" + "="*60)
print("✅ ALL TESTS COMPLETED")
print("="*60)
