"""
Test P13 Mouse Issue
"""

from knowledge_base import KnowledgeBase
from forward_chaining import ForwardChainingEngine

kb = KnowledgeBase()
engine = ForwardChainingEngine(kb)

print("="*60)
print("Testing P13 (Mouse tidak berfungsi)")
print("="*60)

# Test dengan threshold 60% (default)
print("\n📝 Test 1: Threshold 60% (default)")
print("-" * 60)
result = engine.run(['P13'], threshold=60)
print(f"Total Candidates: {result['total_candidates']}")
print(f"Diagnoses Shown: {len(result['diagnoses'])}")

if result['diagnoses']:
    for i, d in enumerate(result['diagnoses'], 1):
        print(f"{i}. {d['diagnosis']['diagnosis']} - {d['confidence']}%")
else:
    print("❌ No results (semua di bawah threshold 60%)")

# Test dengan threshold lebih rendah
print("\n📝 Test 2: Threshold 30% (lower)")
print("-" * 60)
result2 = engine.run(['P13'], threshold=30)
print(f"Total Candidates: {result2['total_candidates']}")
print(f"Diagnoses Shown: {len(result2['diagnoses'])}")

if result2['diagnoses']:
    for i, d in enumerate(result2['diagnoses'], 1):
        print(f"{i}. {d['diagnosis']['diagnosis']} - {d['confidence']}%")
        print(f"   Matched: {', '.join(d['matched_symptoms'])}")
        print(f"   Missing: {', '.join(d['missing_symptoms'])}")

# Cek rule mana saja yang punya P13
print("\n📝 Rules yang mengandung P13:")
print("-" * 60)
for rule_id, rule in kb.get_all_rules().items():
    if 'P13' in rule['conditions']:
        conditions = rule['conditions']
        confidence = (1 / len(conditions)) * 100
        print(f"{rule_id}: {rule['conclusion']['diagnosis']}")
        print(f"   Conditions: {', '.join(conditions)} ({len(conditions)} total)")
        print(f"   P13 only = {confidence:.1f}% confidence")
        print()
