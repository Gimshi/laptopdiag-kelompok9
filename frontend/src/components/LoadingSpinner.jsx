import { motion } from 'framer-motion';
import { Loader2 } from 'lucide-react';

const LoadingSpinner = ({ message = 'Loading...' }) => {
  return (
    <div className="card text-center py-16">
      <motion.div
        animate={{ rotate: 360 }}
        transition={{ duration: 1, repeat: Infinity, ease: 'linear' }}
        className="w-20 h-20 mx-auto mb-6 flex items-center justify-center"
      >
        <Loader2 className="w-20 h-20 text-primary-500" />
      </motion.div>
      <p className="text-slate-100 font-bold text-xl mb-2">{message}</p>
      <p className="text-base text-slate-400">Mohon tunggu sebentar...</p>
    </div>
  );
};

export default LoadingSpinner;
