import axios from 'axios';

// Use environment variable for production, fallback to localhost for development
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const diagnosisAPI = {
  // Get all symptoms
  getSymptoms: async () => {
    const response = await api.get('/symptoms');
    return response.data;
  },

  // Get all rules
  getRules: async () => {
    const response = await api.get('/rules');
    return response.data;
  },

  // Diagnose based on symptoms
  diagnose: async (symptoms, detailed = true) => {
    const response = await api.post('/diagnose', {
      symptoms,
      detailed
    });
    return response.data;
  },

  // Get single symptom detail
  getSymptomDetail: async (symptomCode) => {
    const response = await api.get(`/symptom/${symptomCode}`);
    return response.data;
  },

  // Health check
  healthCheck: async () => {
    const response = await api.get('/health');
    return response.data;
  }
};

export default api;
