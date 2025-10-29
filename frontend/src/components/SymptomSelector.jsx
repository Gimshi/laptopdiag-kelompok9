import { motion } from 'framer-motion';
import { Check, AlertCircle } from 'lucide-react';

const SymptomSelector = ({ symptoms, selectedSymptoms, onToggleSymptom }) => {
  const isSelected = (code) => selectedSymptoms.includes(code);

  return (
    <div className="card">
      <div className="flex items-center gap-4 mb-8">
        <div className="w-14 h-14 bg-primary-500/20 border border-primary-500/30 rounded-xl flex items-center justify-center">
          <AlertCircle className="w-7 h-7 text-primary-400" />
        </div>
        <div>
          <h2 className="text-2xl font-bold text-slate-100">
            Pilih Gejala Kerusakan
          </h2>
          <p className="text-base text-slate-400">
            Pilih semua gejala yang Anda alami
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 gap-5 max-h-[600px] overflow-y-auto pr-3 custom-scrollbar">
        {symptoms.map((symptom, index) => (
          <motion.div
            key={symptom.code}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.02 }}
          >
            <motion.button
              whileHover={{ scale: 1.01, y: -2 }}
              whileTap={{ scale: 0.99 }}
              onClick={() => onToggleSymptom(symptom.code)}
              className={`
                w-full p-6 rounded-xl border-2 text-left transition-all duration-200
                ${
                  isSelected(symptom.code)
                    ? 'border-primary-500 bg-primary-500/10 shadow-lg shadow-primary-500/20'
                    : 'border-slate-600 bg-slate-700/50 hover:border-slate-500 hover:bg-slate-700'
                }
              `}
            >
              <div className="flex items-start gap-5">
                {/* Custom Large Checkbox */}
                <div
                  className={`
                    flex-shrink-0 w-7 h-7 rounded-lg border-2 flex items-center justify-center transition-all duration-200
                    ${
                      isSelected(symptom.code)
                        ? 'border-primary-500 bg-primary-500 shadow-md shadow-primary-500/50'
                        : 'border-slate-500 bg-slate-800'
                    }
                  `}
                >
                  {isSelected(symptom.code) && (
                    <motion.div
                      initial={{ scale: 0 }}
                      animate={{ scale: 1 }}
                      transition={{ type: "spring", stiffness: 300, damping: 20 }}
                    >
                      <Check className="w-5 h-5 text-white" strokeWidth={3} />
                    </motion.div>
                  )}
                </div>

                <div className="flex-1">
                  <div className={`text-sm font-bold mb-2 ${isSelected(symptom.code) ? 'text-primary-400' : 'text-slate-400'}`}>
                    {symptom.code}
                  </div>
                  <div className="text-base text-slate-200 leading-relaxed font-medium">
                    {symptom.description}
                  </div>
                </div>
              </div>
            </motion.button>
          </motion.div>
        ))}
      </div>

      {/* Selection Summary */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.3 }}
        className="mt-8 p-6 bg-slate-700/50 border border-slate-600 rounded-xl"
      >
        <div className="flex items-center justify-between">
          <div>
            <p className="text-base font-bold text-slate-200">
              {selectedSymptoms.length} gejala dipilih
            </p>
            {selectedSymptoms.length > 0 && (
              <p className="text-sm text-slate-400 mt-1">
                {selectedSymptoms.join(', ')}
              </p>
            )}
          </div>
          {selectedSymptoms.length > 0 && (
            <div className="w-10 h-10 bg-primary-500 rounded-xl flex items-center justify-center shadow-lg shadow-primary-500/50">
              <Check className="w-6 h-6 text-white" strokeWidth={3} />
            </div>
          )}
        </div>
      </motion.div>
    </div>
  );
};

export default SymptomSelector;
