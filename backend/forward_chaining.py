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
        
    def run(self, symptoms, threshold=60, top_n=5, strict_mode=False):
        """
        Jalankan forward chaining engine dengan partial matching
        
        Args:
            symptoms: list of symptom codes
            threshold: minimum confidence percentage untuk menampilkan hasil (default 60%)
            top_n: jumlah maksimal hasil yang ditampilkan (default 5)
            strict_mode: jika True, hanya tampilkan match 100% (default False)
            
        Returns:
            dict: {
                'diagnoses': list of diagnoses dengan confidence score,
                'trace': execution trace,
                'fired_rules': rules yang di-fire,
                'working_memory': final working memory,
                'total_candidates': jumlah total kandidat yang ditemukan
            }
        """
        self.reset()
        self.add_facts(symptoms)
        
        # Jika strict mode, gunakan algoritma lama (100% match only)
        if strict_mode:
            return self._run_strict_mode(symptoms)
        
        # Adaptive threshold: jika hanya 1-2 gejala, turunkan threshold
        adaptive_threshold = threshold
        if len(symptoms) <= 1:
            adaptive_threshold = min(threshold, 30)  # Max 30% untuk 1 gejala (show more results)
            self.trace.append({
                'step': 'adaptive_threshold',
                'action': 'threshold_adjusted',
                'original_threshold': threshold,
                'new_threshold': adaptive_threshold,
                'reason': 'Single symptom selected - showing more possibilities'
            })
        elif len(symptoms) == 2:
            adaptive_threshold = min(threshold, 45)  # Max 45% untuk 2 gejala
            self.trace.append({
                'step': 'adaptive_threshold',
                'action': 'threshold_adjusted',
                'original_threshold': threshold,
                'new_threshold': adaptive_threshold,
                'reason': 'Two symptoms selected - relaxed threshold'
            })
        
        # Partial matching: kumpulkan semua kandidat dengan confidence >= threshold
        candidates = []
        
        for rule_id, rule in self.kb.get_all_rules().items():
            conditions = set(rule['conditions'])
            user_symptoms = set(symptoms)
            
            # Hitung matched dan missing symptoms
            matched_symptoms = conditions.intersection(user_symptoms)
            missing_symptoms = conditions.difference(user_symptoms)
            
            # Hitung confidence score
            if len(conditions) > 0:
                confidence = (len(matched_symptoms) / len(conditions)) * 100
            else:
                confidence = 0
            
            # Tambahkan ke kandidat jika memenuhi threshold
            if confidence >= adaptive_threshold:
                candidates.append({
                    'rule_id': rule_id,
                    'confidence': round(confidence, 2),
                    'diagnosis': rule['conclusion'],
                    'matched_symptoms': list(matched_symptoms),
                    'missing_symptoms': list(missing_symptoms),
                    'total_conditions': len(conditions),
                    'matched_count': len(matched_symptoms)
                })
                
                # Tambahkan ke trace
                self.trace.append({
                    'step': len(candidates),
                    'action': 'partial_match',
                    'rule_id': rule_id,
                    'confidence': round(confidence, 2),
                    'matched': list(matched_symptoms),
                    'missing': list(missing_symptoms)
                })
        
        # Sort by confidence descending
        candidates.sort(key=lambda x: x['confidence'], reverse=True)
        
        # Ambil top N hasil
        top_candidates = candidates[:top_n]
        
        # Mark rules as fired untuk konsistensi
        for candidate in top_candidates:
            self.fired_rules.append(candidate['rule_id'])
            self.inferred_facts.append({
                'rule_id': candidate['rule_id'],
                'diagnosis': candidate['diagnosis'],
                'confidence': candidate['confidence']
            })
        
        self.trace.append({
            'step': 'termination',
            'action': 'partial_matching_complete',
            'message': f'Found {len(candidates)} candidates, returning top {len(top_candidates)}',
            'threshold_used': adaptive_threshold,
            'original_threshold': threshold,
            'adaptive_mode': adaptive_threshold != threshold
        })
        
        return {
            'diagnoses': top_candidates,
            'trace': self.trace,
            'fired_rules': self.fired_rules,
            'working_memory': list(self.working_memory),
            'total_candidates': len(candidates),
            'threshold_used': adaptive_threshold,
            'original_threshold': threshold,
            'adaptive_mode': adaptive_threshold != threshold,
            'strict_mode': False
        }
    
    def _run_strict_mode(self, symptoms):
        """
        Algoritma strict mode (100% match only) - backward compatibility
        """
        # Forward chaining loop
        iteration = 0
        max_iterations = 100
        
        while iteration < max_iterations:
            iteration += 1
            rules_fired_this_iteration = False
            
            for rule_id, rule in self.kb.get_all_rules().items():
                if rule_id in self.fired_rules:
                    continue
                    
                if self.match_rule(rule_id, rule):
                    self.fire_rule(rule_id, rule)
                    rules_fired_this_iteration = True
            
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
            'total_iterations': iteration,
            'strict_mode': True
        }
    
    def explain_diagnosis(self, symptoms, threshold=60, top_n=5, strict_mode=False):
        """
        Jalankan diagnosis dan berikan penjelasan lengkap dengan confidence score
        """
        result = self.run(symptoms, threshold=threshold, top_n=top_n, strict_mode=strict_mode)
        
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
        
        # Format diagnoses dengan confidence score
        for diag in result['diagnoses']:
            diagnosis_info = {
                'rule_id': diag['rule_id'],
                'diagnosis': diag['diagnosis']['diagnosis'],
                'category': diag['diagnosis']['category'],
                'severity': diag['diagnosis']['severity'],
                'description': diag['diagnosis']['description'],
                'solutions': diag['diagnosis']['solutions']
            }
            
            # Tambahkan confidence info jika bukan strict mode
            if not strict_mode:
                diagnosis_info['confidence'] = diag.get('confidence', 100)
                diagnosis_info['matched_symptoms'] = diag.get('matched_symptoms', [])
                diagnosis_info['missing_symptoms'] = diag.get('missing_symptoms', [])
                diagnosis_info['match_ratio'] = f"{diag.get('matched_count', 0)}/{diag.get('total_conditions', 0)}"
            
            explanation['diagnoses_found'].append(diagnosis_info)
        
        # Format reasoning steps
        for trace_item in result['trace']:
            if trace_item['action'] in ['fire_rule', 'partial_match']:
                step_info = {
                    'step': trace_item['step'],
                    'rule_fired': trace_item['rule_id'],
                }
                
                if trace_item['action'] == 'partial_match':
                    step_info['confidence'] = trace_item['confidence']
                    step_info['matched_symptoms'] = [
                        self.kb.get_symptom_description(c) 
                        for c in trace_item['matched']
                    ]
                    step_info['missing_symptoms'] = [
                        self.kb.get_symptom_description(c) 
                        for c in trace_item['missing']
                    ]
                else:
                    step_info['conditions_met'] = [
                        self.kb.get_symptom_description(c) 
                        for c in trace_item['conditions_met']
                    ]
                    step_info['conclusion'] = trace_item['conclusion']
                
                explanation['reasoning_steps'].append(step_info)
        
        # Summary
        explanation['summary'] = {
            'total_symptoms': len(symptoms),
            'total_diagnoses': len(result['diagnoses']),
            'rules_fired': len(result['fired_rules']),
            'total_candidates': result.get('total_candidates', len(result['diagnoses'])),
            'threshold_used': result.get('threshold_used', 100),
            'original_threshold': result.get('original_threshold', 100),
            'adaptive_mode': result.get('adaptive_mode', False),
            'strict_mode': result.get('strict_mode', False)
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
    