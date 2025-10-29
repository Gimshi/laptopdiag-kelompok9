import { motion } from 'framer-motion';
import { Cpu, Github } from 'lucide-react';

const Navbar = () => {
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

      // Add flash animation to target section
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
    <motion.nav
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      className="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b-2 border-primary-400 shadow-xl"
    >
      <div className="max-w-8xl mx-auto px-4 sm:px-6 md:px-8 lg:px-10 xl:px-12">
        <div className="flex items-center justify-between h-16 sm:h-18 md:h-20">
          {/* Logo - Bigger & More Prominent */}
          <div className="flex items-center gap-2 sm:gap-3 md:gap-4">
            <div className="w-10 h-10 sm:w-12 sm:h-12 md:w-14 md:h-14 bg-gradient-to-br from-primary-400 to-primary-600 rounded-xl sm:rounded-2xl flex items-center justify-center shadow-xl shadow-primary-400/30">
              <Cpu className="w-5 h-5 sm:w-6 sm:h-6 md:w-8 md:h-8 text-white" />
            </div>
            <div>
              <h1 className="text-base sm:text-lg md:text-xl font-bold text-highlight-900">LaptopDiag AI</h1>
              <p className="text-xs sm:text-sm text-accent-600 hidden sm:block">Expert System</p>
            </div>
          </div>

          {/* Navigation Links - BIGGER & MORE SPACE */}
          <div className="hidden md:flex items-center gap-6 lg:gap-8 xl:gap-12">
            <a
              href="#about"
              onClick={(e) => handleSmoothScroll(e, '#about')}
              className="text-base lg:text-lg font-medium text-highlight-800 hover:text-primary-500 transition-all hover:scale-105"
            >
              About
            </a>
            <a
              href="#how-it-works"
              onClick={(e) => handleSmoothScroll(e, '#how-it-works')}
              className="text-base lg:text-lg font-medium text-highlight-800 hover:text-primary-500 transition-all hover:scale-105"
            >
              How It Works
            </a>
            <a
              href="#diagnosis"
              onClick={(e) => handleSmoothScroll(e, '#diagnosis')}
              className="text-base lg:text-lg font-medium text-highlight-800 hover:text-primary-500 transition-all hover:scale-105"
            >
              Diagnosis
            </a>
            <a
              href="https://github.com/yourusername/laptop-diagnosis"
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center gap-2 text-base lg:text-lg font-medium text-highlight-800 hover:text-primary-500 transition-all hover:scale-105"
            >
              <Github className="w-4 h-4 lg:w-5 lg:h-5" />
              <span className="hidden lg:inline">GitHub</span>
            </a>
          </div>

          {/* CTA Button - Bigger & Mobile Menu */}
          <div className="flex items-center gap-3">
            <a
              href="#diagnosis"
              onClick={(e) => handleSmoothScroll(e, '#diagnosis')}
              className="px-4 py-2 sm:px-5 sm:py-2.5 md:px-6 md:py-3 bg-primary-400 hover:bg-primary-500 text-white text-sm sm:text-base font-bold rounded-xl transition-all shadow-lg shadow-primary-400/30 hover:shadow-xl hover:shadow-primary-500/40 hover:scale-105"
            >
              <span className="hidden sm:inline">Start Diagnosis</span>
              <span className="sm:hidden">Mulai</span>
            </a>
          </div>
        </div>
      </div>
    </motion.nav>
  );
};

export default Navbar;
