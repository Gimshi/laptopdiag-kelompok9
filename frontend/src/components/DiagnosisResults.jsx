import { motion } from 'framer-motion';
import { AlertCircle, Wrench, TrendingUp, CheckCircle2, Cpu } from 'lucide-react';

const getSeverityColor = (severity) => {
  switch (severity?.toLowerCase()) {
    case 'ringan':
      return 'success';
    case 'sedang':
      return 'warning';
    case 'berat':
      return 'danger';
    default:
      return 'gray';
  }
};

const getCategoryIcon = (category) => {
  return category?.toLowerCase() === 'hardware' ? '⚙️' : '💻';
};

const ResultCard = ({ diagnosis, index }) => {
  const severityColor = getSeverityColor(diagnosis.severity);

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: index * 0.1, duration: 0.4 }}
      className="card border-l-4 border-primary-500"
    >
      {/* Header */}
      <div className="flex flex-col sm:flex-row items-start justify-between mb-6 sm:mb-8 gap-6">
        <div className="flex items-start gap-4 sm:gap-5 w-full sm:w-auto">
          <div className="w-14 h-14 sm:w-16 sm:h-16 bg-primary-500/20 border border-primary-500/30 rounded-xl flex items-center justify-center flex-shrink-0">
            <span className="text-2xl sm:text-3xl">{getCategoryIcon(diagnosis.category)}</span>
          </div>
          <div className="flex-1">
            <h3 className="text-xl sm:text-2xl font-bold text-slate-100 mb-3 leading-tight">
              {diagnosis.diagnosis}
            </h3>
            <div className="flex flex-wrap gap-2 sm:gap-3">
              <span
                className={`text-xs sm:text-sm px-3 sm:px-5 py-1.5 sm:py-2 rounded-full font-bold bg-${severityColor}-500/20 text-${severityColor}-400 border border-${severityColor}-500/30`}
              >
                {diagnosis.severity?.toUpperCase()}
              </span>
              <span className="text-xs sm:text-sm px-3 sm:px-5 py-1.5 sm:py-2 rounded-full font-bold bg-slate-600 text-slate-200 border border-slate-500">
                {diagnosis.category?.toUpperCase()}
              </span>
            </div>
          </div>
        </div>

        {/* Confidence Badge */}
        <div className="text-center bg-primary-500/20 border border-primary-500/30 rounded-xl px-5 sm:px-6 py-3 sm:py-4 w-full sm:w-auto">
          <div className="text-2xl sm:text-3xl font-bold text-primary-400">
            {diagnosis.confidence}%
          </div>
          <div className="text-xs sm:text-sm text-slate-400 font-semibold">Akurasi</div>
        </div>
      </div>

      {/* Description */}
      <div className="mb-6 sm:mb-8 p-5 sm:p-6 bg-slate-700/50 border border-slate-600 rounded-xl">
        <div className="flex gap-3 sm:gap-4 items-start">
          <AlertCircle className="w-5 h-5 sm:w-6 sm:h-6 text-slate-400 flex-shrink-0 mt-0.5" />
          <p className="text-sm sm:text-base text-slate-200 leading-relaxed font-medium">{diagnosis.description}</p>
        </div>
      </div>

      {/* Solutions */}
      <div>
        <div className="flex items-center gap-3 sm:gap-4 mb-5 sm:mb-6">
          <div className="w-10 h-10 sm:w-12 sm:h-12 bg-primary-500/20 border border-primary-500/30 rounded-xl flex items-center justify-center">
            <Wrench className="w-5 h-5 sm:w-6 sm:h-6 text-primary-400" />
          </div>
          <h4 className="text-base sm:text-lg font-bold text-slate-100">Solusi yang Disarankan</h4>
        </div>

        <ul className="space-y-3 sm:space-y-4">
          {diagnosis.solutions?.map((solution, idx) => (
            <motion.li
              key={idx}
              initial={{ opacity: 0, x: -10 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.1 + idx * 0.05 }}
              className="flex gap-4 sm:gap-5 items-start p-5 sm:p-6 bg-slate-700/50 border border-slate-600 rounded-xl hover:border-slate-500 transition-colors"
            >
              <span className="flex-shrink-0 w-7 h-7 sm:w-8 sm:h-8 rounded-lg bg-primary-500 text-white text-xs sm:text-sm font-bold flex items-center justify-center shadow-md shadow-primary-500/50">
                {idx + 1}
              </span>
              <span className="text-sm sm:text-base text-slate-200 flex-1 leading-relaxed font-medium">{solution}</span>
            </motion.li>
          ))}
        </ul>
      </div>
    </motion.div>
  );
};

const DiagnosisResults = ({ results }) => {
  if (!results || results.diagnoses_found?.length === 0) {
    return (
      <motion.div
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        className="card text-center py-16 sm:py-20"
      >
        <div className="w-20 h-20 sm:w-24 sm:h-24 md:w-28 md:h-28 bg-slate-700/50 border border-slate-600 rounded-full flex items-center justify-center mx-auto mb-5 sm:mb-6">
          <Cpu className="w-10 h-10 sm:w-12 sm:h-12 md:w-14 md:h-14 text-slate-400" />
        </div>
        <h3 className="text-xl sm:text-2xl font-bold text-slate-100 mb-3 sm:mb-4 px-4 sm:px-0">
          Tidak Ada Diagnosis Ditemukan
        </h3>
        <p className="text-sm sm:text-base text-slate-400 px-4 sm:px-0">
          Coba pilih lebih banyak gejala untuk mendapatkan diagnosis yang akurat
        </p>
      </motion.div>
    );
  }

  return (
    <div className="space-y-6 sm:space-y-8">
      {/* Summary Card */}
      <motion.div
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        className="card bg-gradient-to-br from-primary-500 via-primary-600 to-primary-700 text-white border border-primary-400/30 shadow-2xl shadow-primary-500/30"
      >
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between mb-6 sm:mb-8 gap-4">
          <div>
            <div className="flex items-center gap-3 sm:gap-4 mb-2">
              <CheckCircle2 className="w-6 h-6 sm:w-7 sm:h-7 md:w-8 md:h-8" />
              <h2 className="text-2xl sm:text-3xl font-bold">Hasil Diagnosis</h2>
            </div>
            <p className="text-base sm:text-lg text-primary-100">
              Ditemukan {results.diagnoses_found?.length} kemungkinan kerusakan
            </p>
          </div>
          <div className="w-14 h-14 sm:w-16 sm:h-16 bg-white/20 rounded-xl flex items-center justify-center backdrop-blur-sm border border-white/30">
            <TrendingUp className="w-7 h-7 sm:w-8 sm:h-8 md:w-9 md:h-9" />
          </div>
        </div>

        <div className="grid grid-cols-3 gap-3 sm:gap-4 md:gap-5">
          <div className="bg-white/10 rounded-xl p-4 sm:p-5 md:p-6 backdrop-blur-sm border border-white/20">
            <div className="text-3xl sm:text-4xl font-bold mb-2">{results.summary?.total_symptoms}</div>
            <div className="text-xs sm:text-sm md:text-base text-primary-100 font-medium">Gejala</div>
          </div>
          <div className="bg-white/10 rounded-xl p-4 sm:p-5 md:p-6 backdrop-blur-sm border border-white/20">
            <div className="text-3xl sm:text-4xl font-bold mb-2">{results.summary?.rules_fired}</div>
            <div className="text-xs sm:text-sm md:text-base text-primary-100 font-medium">Rules</div>
          </div>
          <div className="bg-white/10 rounded-xl p-4 sm:p-5 md:p-6 backdrop-blur-sm border border-white/20">
            <div className="text-3xl sm:text-4xl font-bold mb-2">{results.summary?.total_diagnoses}</div>
            <div className="text-xs sm:text-sm md:text-base text-primary-100 font-medium">Diagnosa</div>
          </div>
        </div>
      </motion.div>

      {/* Diagnoses */}
      {results.diagnoses_found?.map((diagnosis, index) => (
        <ResultCard key={index} diagnosis={diagnosis} index={index} />
      ))}
    </div>
  );
};

export default DiagnosisResults;
