import { motion } from 'framer-motion';
import { Sparkles, ArrowRight, Zap } from 'lucide-react';

const Hero = () => {
  const handleSmoothScroll = (e, targetId) => {
    e.preventDefault();
    const element = document.querySelector(targetId);
    if (element) {
      const navbarHeight = 80;
      const elementPosition = element.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - navbarHeight;

      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });

      // Add flash animation
      element.style.transition = 'transform 0.3s ease, box-shadow 0.3s ease';
      element.style.transform = 'scale(1.01)';
      element.style.boxShadow = '0 0 40px rgba(176, 206, 136, 0.4)';
      
      setTimeout(() => {
        element.style.transform = 'scale(1)';
        element.style.boxShadow = 'none';
      }, 600);
    }
  };

  return (
    <section className="relative py-16 sm:py-20 md:py-24 overflow-hidden">
      {/* Background Gradient - Warm Cream Theme */}
      <div className="absolute inset-0 bg-gradient-to-br from-secondary-300 via-secondary-200 to-secondary-100" />
      <div className="absolute inset-0 bg-[url('data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNjAiIGhlaWdodD0iNjAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGRlZnM+PHBhdHRlcm4gaWQ9ImdyaWQiIHdpZHRoPSI2MCIgaGVpZ2h0PSI2MCIgcGF0dGVyblVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+PHBhdGggZD0iTSAxMCAwIEwgMCAwIDAgMTAiIGZpbGw9Im5vbmUiIHN0cm9rZT0icmdiYSgxODMsMTE2LDEwMiwwLjA4KSIgc3Ryb2tlLXdpZHRoPSIxIi8+PC9wYXR0ZXJuPjwvZGVmcz48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSJ1cmwoI2dyaWQpIi8+PC9zdmc+')] opacity-40" />
      
      <div className="relative max-w-8xl mx-auto px-4 sm:px-6 md:px-8 lg:px-10 xl:px-12">
        <div className="text-center">
          {/* Badge */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
            className="inline-flex items-center gap-2 px-4 py-2 sm:px-5 sm:py-2.5 bg-primary-300/30 border-2 border-primary-400 rounded-full mb-8 sm:mb-10"
          >
            <Sparkles className="w-4 h-4 sm:w-5 sm:h-5 text-primary-600" />
            <span className="text-sm sm:text-base font-semibold text-primary-700">
              AI-Powered Expert System
            </span>
          </motion.div>

          {/* Main Heading - BIGGER */}
          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
            className="text-4xl sm:text-5xl md:text-6xl lg:text-7xl xl:text-8xl font-bold text-highlight-900 mb-6 sm:mb-8 leading-tight px-4 sm:px-0"
          >
            Diagnosa Kerusakan Laptop{' '}
            <span className="bg-gradient-to-r from-primary-400 via-primary-500 to-primary-600 bg-clip-text text-transparent">
              dengan AI
            </span>
          </motion.h1>

          {/* Description - BIGGER */}
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3 }}
            className="text-lg sm:text-xl md:text-2xl text-highlight-800 mb-10 sm:mb-12 max-w-3xl mx-auto leading-relaxed px-4 sm:px-0"
          >
            Sistem pakar berbasis Forward Chaining AI untuk mendeteksi masalah laptop Anda secara akurat dan memberikan solusi tepat dalam hitungan detik.
          </motion.p>

          {/* CTA Buttons - BIGGER */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.4 }}
            className="flex flex-col sm:flex-row gap-4 sm:gap-5 justify-center px-4 sm:px-0"
          >
            <a
              href="#diagnosis"
              onClick={(e) => handleSmoothScroll(e, '#diagnosis')}
              className="inline-flex items-center justify-center gap-2 sm:gap-3 px-8 sm:px-10 py-4 sm:py-5 bg-primary-600 hover:bg-primary-700 text-white text-base sm:text-lg font-bold rounded-2xl transition-all shadow-2xl shadow-primary-600/30 hover:shadow-3xl hover:shadow-primary-700/40 hover:scale-105 cursor-pointer"
            >
              Mulai Diagnosis
              <ArrowRight className="w-5 h-5 sm:w-6 sm:h-6" />
            </a>
            <a
              href="#how-it-works"
              onClick={(e) => handleSmoothScroll(e, '#how-it-works')}
              className="inline-flex items-center justify-center gap-2 sm:gap-3 px-8 sm:px-10 py-4 sm:py-5 bg-white hover:bg-secondary-50 border-2 border-primary-500 text-highlight-900 text-base sm:text-lg font-semibold rounded-2xl transition-all cursor-pointer hover:scale-105"
            >
              Pelajari Cara Kerja
            </a>
          </motion.div>

          {/* Stats - BIGGER */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.5 }}
            className="mt-16 sm:mt-20 grid grid-cols-3 gap-6 sm:gap-10 max-w-3xl mx-auto px-4 sm:px-0"
          >
            <div className="text-center">
              <div className="text-3xl sm:text-4xl md:text-5xl font-bold text-highlight-900 mb-2">20+</div>
              <div className="text-sm sm:text-base text-highlight-700">Gejala</div>
            </div>
            <div className="text-center">
              <div className="text-3xl sm:text-4xl md:text-5xl font-bold text-highlight-900 mb-2">15+</div>
              <div className="text-sm sm:text-base text-highlight-700">Diagnosis</div>
            </div>
            <div className="text-center">
              <div className="flex items-center justify-center gap-1 sm:gap-2 text-3xl sm:text-4xl md:text-5xl font-bold text-highlight-900 mb-2">
                <Zap className="w-7 h-7 sm:w-10 sm:h-10 text-primary-500" />
                <span className="hidden sm:inline">Fast</span>
                <span className="sm:hidden">⚡</span>
              </div>
              <div className="text-sm sm:text-base text-highlight-700">AI Analysis</div>
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
