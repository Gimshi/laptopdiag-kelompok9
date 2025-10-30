from flask import Flask, request, jsonify
from flask_cors import CORS
from knowledge_base import KnowledgeBase
from forward_chaining import ForwardChainingEngine

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS untuk frontend

# Initialize Knowledge Base dan Forward Chaining Engine
kb = KnowledgeBase()
engine = ForwardChainingEngine(kb)

@app.route('/')
def home():
    """API info"""
    return jsonify({
        'message': 'Laptop Diagnosis Expert System API',
        'version': '1.0.0',
        'endpoints': {
            '/api/symptoms': 'GET - Get all symptoms',
            '/api/diagnose': 'POST - Diagnose based on symptoms',
            '/api/rules': 'GET - Get all rules in knowledge base'
        }
    })

@app.route('/api/symptoms', methods=['GET'])
def get_symptoms():
    """
    Get daftar semua gejala yang tersedia
    """
    try:
        symptoms = kb.get_all_symptoms()
        return jsonify({
            'success': True,
            'data': symptoms,
            'total': len(symptoms)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/rules', methods=['GET'])
def get_rules():
    """
    Get semua rules di knowledge base
    """
    try:
        rules = kb.get_all_rules()
        formatted_rules = []
        
        for rule_id, rule in rules.items():
            formatted_rules.append({
                'rule_id': rule_id,
                'conditions': rule['conditions'],
                'conclusion': rule['conclusion']
            })
        
        return jsonify({
            'success': True,
            'data': formatted_rules,
            'total': len(formatted_rules)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/diagnose', methods=['POST'])
def diagnose():
    """
    Diagnose berdasarkan gejala yang dipilih user
    
    Request body:
    {
        "symptoms": ["P01", "P02", "P03"],
        "detailed": true,  // optional, untuk trace lengkap
        "threshold": 60,   // optional, minimum confidence (default 60%)
        "top_n": 5,        // optional, max results (default 5)
        "strict_mode": false  // optional, 100% match only (default false)
    }
    
    Response:
    {
        "success": true,
        "data": {
            "symptoms_provided": [...],
            "diagnoses_found": [...],  // dengan confidence score
            "reasoning_steps": [...],
            "summary": {
                "total_symptoms": 3,
                "total_diagnoses": 2,
                "total_candidates": 5,
                "threshold_used": 60,
                "strict_mode": false
            }
        }
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'symptoms' not in data:
            return jsonify({
                'success': False,
                'error': 'Symptoms are required'
            }), 400
        
        symptoms = data['symptoms']
        detailed = data.get('detailed', True)
        threshold = data.get('threshold', 60)  # Default 60%
        top_n = data.get('top_n', 5)  # Default 5 results
        strict_mode = data.get('strict_mode', False)  # Default partial matching
        
        # Validasi symptoms
        valid_symptoms = set(kb.symptoms.keys())
        invalid_symptoms = [s for s in symptoms if s not in valid_symptoms]
        
        if invalid_symptoms:
            return jsonify({
                'success': False,
                'error': f'Invalid symptom codes: {invalid_symptoms}'
            }), 400
        
        if not symptoms:
            return jsonify({
                'success': False,
                'error': 'At least one symptom is required'
            }), 400
        
        # Validasi threshold
        if not (0 <= threshold <= 100):
            return jsonify({
                'success': False,
                'error': 'Threshold must be between 0 and 100'
            }), 400
        
        # Jalankan forward chaining dengan partial matching
        if detailed:
            result = engine.explain_diagnosis(
                symptoms, 
                threshold=threshold, 
                top_n=top_n, 
                strict_mode=strict_mode
            )
        else:
            # Simple mode: hanya return diagnoses dengan confidence
            full_result = engine.run(
                symptoms, 
                threshold=threshold, 
                top_n=top_n, 
                strict_mode=strict_mode
            )
            result = {
                'diagnoses_found': full_result['diagnoses'],
                'total_candidates': full_result.get('total_candidates', 0),
                'threshold_used': full_result.get('threshold_used', threshold)
            }
        
        return jsonify({
            'success': True,
            'data': result
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/symptom/<symptom_code>', methods=['GET'])
def get_symptom_detail(symptom_code):
    """
    Get detail dari satu symptom
    """
    try:
        description = kb.get_symptom_description(symptom_code)
        
        if description == "Unknown symptom":
            return jsonify({
                'success': False,
                'error': 'Symptom not found'
            }), 404
        
        return jsonify({
            'success': True,
            'data': {
                'code': symptom_code,
                'description': description
            }
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'success': True,
        'status': 'healthy',
        'message': 'API is running'
    })

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Laptop Diagnosis Expert System API")
    print("=" * 60)
    print("📍 Running on: http://localhost:5000")
    print("📖 API Docs: http://localhost:5000/")
    print("\n🔧 Available endpoints:")
    print("   GET  /api/symptoms  - Get all symptoms")
    print("   POST /api/diagnose  - Diagnose laptop issues")
    print("   GET  /api/rules     - Get all rules")
    print("   GET  /api/health    - Health check")
    print("=" * 60)
    print()
    
    # Get port from environment variable for production (Render)
    import os
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    
    app.run(debug=debug, host='0.0.0.0', port=port)
