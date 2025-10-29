import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { diagnosisAPI } from './utils/api';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import AboutSection from './components/AboutSection';
import HowItWorks from './components/HowItWorks';
import SymptomSelector from './components/SymptomSelector';
import DiagnosisResults from './components/DiagnosisResults';
import LoadingSpinner from './components/LoadingSpinner';
import Footer from './components/Footer';
import { Sparkles, RotateCcw, AlertCircle, ShoppingBag, Zap } from 'lucide-react';

function App() {
  const [symptoms, setSymptoms] = useState([]);
  const [selectedSymptoms, setSelectedSymptoms] = useState([]);
  const [diagnosisResults, setDiagnosisResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [initialLoading, setInitialLoading] = useState(true);

  // Fetch symptoms on mount
  useEffect(() => {
    fetchSymptoms();
  }, []);

  const fetchSymptoms = async () => {
    try {
      setInitialLoading(true);
      const response = await diagnosisAPI.getSymptoms();
      if (response.success) {
        setSymptoms(response.data);
      }
    } catch (err) {
      setError('Failed to fetch symptoms. Please make sure the backend is running.');
      console.error('Error fetching symptoms:', err);
    } finally {
      setInitialLoading(false);
    }
  };

  const handleToggleSymptom = (symptomCode) => {
    setSelectedSymptoms((prev) => {
      if (prev.includes(symptomCode)) {
        return prev.filter((code) => code !== symptomCode);
      } else {
        return [...prev, symptomCode];
      }
    });
    // Clear results when symptoms change
    setDiagnosisResults(null);
  };

  const handleDiagnose = async () => {
    if (selectedSymptoms.length === 0) {
      setError('Please select at least one symptom');
      return;
    }

    try {
      setLoading(true);
      setError(null);
      const response = await diagnosisAPI.diagnose(selectedSymptoms, true);

      if (response.success) {
        setDiagnosisResults(response.data);
      } else {
        setError(response.error || 'Failed to get diagnosis');
      }
    } catch (err) {
      setError('Failed to diagnose. Please try again.');
      console.error('Error diagnosing:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setSelectedSymptoms([]);
    setDiagnosisResults(null);
    setError(null);
  };

  if (initialLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-950">
        <LoadingSpinner message="Loading symptoms..." />
      </div>
    );
  }

  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <Hero />
      <AboutSection />
      <HowItWorks />

      {/* Diagnosis Section */}
      <section id="diagnosis" className="py-16 sm:py-20 md:py-24 bg-secondary-200">
        <div className="max-w-8xl mx-auto px-4 sm:px-6 md:px-8 lg:px-10 xl:px-12">
          {/* Section Header - BIGGER */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-12 sm:mb-14 md:mb-16"
          >
            <h2 className="text-4xl sm:text-5xl md:text-6xl font-bold text-highlight-900 mb-4 sm:mb-6 px-4 sm:px-0">
              Mulai Diagnosis
            </h2>
            <p className="text-lg sm:text-xl md:text-2xl text-highlight-700 max-w-3xl mx-auto leading-relaxed px-4 sm:px-0">
              Pilih gejala yang Anda alami dan biarkan AI kami menganalisis masalah laptop Anda
            </p>
          </motion.div>

          {/* Error Alert */}
          <AnimatePresence>
            {error && (
              <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -20 }}
                className="card bg-danger-500/10 border-l-4 border-danger-500 mb-8"
              >
                <div className="flex gap-4 items-start">
                  <div className="w-12 h-12 bg-danger-500/20 border border-danger-500/30 rounded-xl flex items-center justify-center flex-shrink-0">
                    <AlertCircle className="w-6 h-6 text-danger-400" />
                  </div>
                  <div className="flex-1">
                    <h3 className="font-bold text-danger-300 mb-2 text-lg">Terjadi Kesalahan</h3>
                    <p className="text-danger-200 text-base">{error}</p>
                  </div>
                  <button
                    onClick={() => setError(null)}
                    className="text-danger-400 hover:text-danger-300 font-bold text-2xl"
                  >
                    ×
                  </button>
                </div>
              </motion.div>
            )}
          </AnimatePresence>

          {/* Main Content Grid */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 sm:gap-8 mb-8 sm:mb-10">
            {/* Left Column - Symptom Selector */}
            <motion.div
              initial={{ opacity: 0, x: -30 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.2 }}
              className="lg:col-span-2"
            >
              <SymptomSelector
                symptoms={symptoms}
                selectedSymptoms={selectedSymptoms}
                onToggleSymptom={handleToggleSymptom}
              />
            </motion.div>

            {/* Right Column - Action Panel */}
            <motion.div
              initial={{ opacity: 0, x: 30 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.3 }}
              className="lg:col-span-1"
            >
              <div className="card lg:sticky lg:top-24">
                <div className="flex items-center gap-4 mb-6">
                  <div className="w-14 h-14 bg-primary-500/20 border border-primary-500/30 rounded-xl flex items-center justify-center">
                    <ShoppingBag className="w-7 h-7 text-primary-400" />
                  </div>
                  <div>
                    <h2 className="text-xl font-bold text-slate-100">
                      Diagnosa Sekarang
                    </h2>
                    <p className="text-base text-slate-400">Instant AI Analysis</p>
                  </div>
                </div>

                <div className="space-y-4 mb-8">
                  <motion.button
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                    onClick={handleDiagnose}
                    disabled={selectedSymptoms.length === 0 || loading}
                    className={`
                      w-full btn-primary flex items-center justify-center gap-3 text-base py-4
                      ${
                        selectedSymptoms.length === 0 || loading
                          ? 'opacity-50 cursor-not-allowed'
                          : ''
                      }
                    `}
                  >
                    <Sparkles className="w-6 h-6" />
                    {loading ? 'Analyzing...' : 'Diagnose Sekarang'}
                  </motion.button>

                  <motion.button
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                    onClick={handleReset}
                    className="w-full btn-secondary flex items-center justify-center gap-3 text-base py-4"
                  >
                    <RotateCcw className="w-6 h-6" />
                    Reset Pilihan
                  </motion.button>
                </div>

                {/* Stats/Features */}
                <div className="space-y-4 pt-8 border-t border-slate-700">
                  <div className="flex items-center gap-4 text-sm">
                    <div className="w-12 h-12 bg-success-500/20 border border-success-500/30 rounded-xl flex items-center justify-center">
                      <Zap className="w-6 h-6 text-success-400" />
                    </div>
                    <div>
                      <p className="font-bold text-slate-200 text-base">Instant Results</p>
                      <p className="text-base text-slate-400">Diagnosis dalam detik</p>
                    </div>
                  </div>
                  <div className="flex items-center gap-4 text-sm">
                    <div className="w-12 h-12 bg-primary-500/20 border border-primary-500/30 rounded-xl flex items-center justify-center">
                      <span className="text-primary-400 font-bold text-base">AI</span>
                    </div>
                    <div>
                      <p className="font-bold text-slate-200 text-base">Forward Chaining</p>
                      <p className="text-base text-slate-400">Algoritma AI terpercaya</p>
                    </div>
                  </div>
                </div>

                {/* Info Box */}
                <div className="mt-8 p-6 bg-primary-500/10 border border-primary-500/30 rounded-xl">
                  <p className="text-base text-slate-200 leading-relaxed font-medium">
                    <span className="font-bold text-primary-400">💡 Tips:</span> Pilih semua gejala yang relevan untuk hasil diagnosis yang lebih akurat dan solusi yang tepat.
                  </p>
                </div>
              </div>
            </motion.div>
          </div>

          {/* Results Section */}
          <AnimatePresence mode="wait">
            {loading && (
              <motion.div
                key="loading"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
              >
                <LoadingSpinner message="Menganalisis gejala dengan Forward Chaining AI..." />
              </motion.div>
            )}

            {!loading && diagnosisResults && (
              <motion.div
                key="results"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -20 }}
              >
                <DiagnosisResults results={diagnosisResults} />
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      </section>

      <Footer />
    </div>
  );
}

export default App;
