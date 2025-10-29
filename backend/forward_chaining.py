# Forward Chaining Engine untuk Sistem Pakar
# AI Agent untuk deteksi kerusakan laptop

class ForwardChainingEngine:
    """
    Forward Chaining Inference Engine
    Metode: Data-driven reasoning (dari fakta menuju kesimpulan)
    
    Algoritma:
    1. Mulai dengan working memory (facts/gejala yang dipilih user)
    2. Cari rules yang kondisinya match dengan working memory
    3. Fire rule yang match (tambahkan conclusion ke working memory)
    4. Repeat sampai tidak ada rule yang bisa di-fire
    """
    
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        self.working_memory = set()  # Fakta yang diketahui
        self.fired_rules = []  # Rules yang sudah di-fire
        self.inferred_facts = []  # Kesimpulan yang didapat
        self.trace = []  # Trace untuk debugging/demonstrasi
        
    def reset(self):
        """Reset engine untuk diagnosis baru"""
        self.working_memory = set()
        self.fired_rules = []
        self.inferred_facts = []
        self.trace = []
        
    def add_facts(self, facts):
        """
        Tambahkan fakta awal ke working memory
        facts: list of symptom codes (e.g., ['S01', 'S02'])
        """
        self.working_memory.update(facts)
        self.trace.append({
            'step': 'initialization',
            'action': 'add_facts',
            'facts': list(facts),
            'working_memory': list(self.working_memory)
        })
        
    def match_rule(self, rule_id, rule):
        """
        Cek apakah semua kondisi rule terpenuhi di working memory
        Return: True jika match, False jika tidak
        """
        conditions = set(rule['conditions'])
        return conditions.issubset(self.working_memory)
    
    def fire_rule(self, rule_id, rule):
        """
        Fire rule: tambahkan conclusion ke inferred facts
        """
        conclusion = rule['conclusion']
        self.fired_rules.append(rule_id)
        self.inferred_facts.append({
            'rule_id': rule_id,
            'diagnosis': conclusion
        })
        
        self.trace.append({
            'step': len(self.fired_rules),
            'action': 'fire_rule',
            'rule_id': rule_id,
            'conditions_met': rule['conditions'],
            'conclusion': conclusion['diagnosis']
        })
        
    def run(self, symptoms):
        """
        Jalankan forward chaining engine
        
        Args:
            symptoms: list of symptom codes
            
        Returns:
            dict: {
                'diagnoses': list of diagnoses,
                'trace': execution trace,
                'fired_rules': rules yang di-fire,
                'working_memory': final working memory
            }
        """
        self.reset()
        self.add_facts(symptoms)
        
        # Forward chaining loop
        iteration = 0
        max_iterations = 100  # Prevent infinite loop
        
        while iteration < max_iterations:
            iteration += 1
            rules_fired_this_iteration = False
            
            # Cek semua rules
            for rule_id, rule in self.kb.get_all_rules().items():
                # Skip jika rule sudah pernah di-fire
                if rule_id in self.fired_rules:
                    continue
                    
                # Cek apakah rule match
                if self.match_rule(rule_id, rule):
                    self.fire_rule(rule_id, rule)
                    rules_fired_this_iteration = True
            
            # Jika tidak ada rule yang fire, berhenti
            if not rules_fired_this_iteration:
                self.trace.append({
                    'step': 'termination',
                    'action': 'no_more_rules',
                    'message': 'No more rules to fire. Forward chaining complete.'
                })
                break
        
        return {
            'diagnoses': self.inferred_facts,
            'trace': self.trace,
            'fired_rules': self.fired_rules,
            'working_memory': list(self.working_memory),
            'total_iterations': iteration
        }
    
    def explain_diagnosis(self, symptoms):
        """
        Jalankan diagnosis dan berikan penjelasan lengkap
        """
        result = self.run(symptoms)
        
        # Format output yang user-friendly
        explanation = {
            'symptoms_provided': [
                {
                    'code': s,
                    'description': self.kb.get_symptom_description(s)
                } for s in symptoms
            ],
            'diagnoses_found': [],
            'reasoning_steps': [],
            'summary': {}
        }
        
        # Format diagnoses
        for diag in result['diagnoses']:
            explanation['diagnoses_found'].append({
                'rule_id': diag['rule_id'],
                'diagnosis': diag['diagnosis']['diagnosis'],
                'category': diag['diagnosis']['category'],
                'severity': diag['diagnosis']['severity'],
                'description': diag['diagnosis']['description'],
                'solutions': diag['diagnosis']['solutions']
            })
        
        # Format reasoning steps
        for trace_item in result['trace']:
            if trace_item['action'] == 'fire_rule':
                explanation['reasoning_steps'].append({
                    'step': trace_item['step'],
                    'rule_fired': trace_item['rule_id'],
                    'conditions_met': [
                        self.kb.get_symptom_description(c) 
                        for c in trace_item['conditions_met']
                    ],
                    'conclusion': trace_item['conclusion']
                })
        
        # Summary
        explanation['summary'] = {
            'total_symptoms': len(symptoms),
            'total_diagnoses': len(result['diagnoses']),
            'rules_fired': len(result['fired_rules']),
            'iterations': result['total_iterations']
        }
        
        return explanation
    
    def get_confidence_score(self, diagnosis, symptoms):
        """
        Hitung confidence score berdasarkan jumlah gejala yang match
        Simple scoring: (matched_symptoms / total_conditions) * 100
        """
        if not diagnosis:
            return 0
        
        rule_id = diagnosis['rule_id']
        rule = self.kb.get_all_rules()[rule_id]
        conditions = set(rule['conditions'])
        matched = conditions.intersection(set(symptoms))
        
        confidence = (len(matched) / len(conditions)) * 100
        return round(confidence, 2)
    