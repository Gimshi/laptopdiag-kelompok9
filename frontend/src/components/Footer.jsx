import { motion } from 'framer-motion';
import { Heart, Github, Mail } from 'lucide-react';

const Footer = () => {
  const currentYear = new Date().getFullYear();

  return (
    <motion.footer
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ delay: 0.5 }}
      className="bg-highlight-800 mt-0 pt-8 md:pt-16"
    >
      <div className="max-w-8xl mx-auto px-4 md:px-8 pb-6 md:pb-12">
        {/* Main Footer Content */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 md:gap-12 mb-6 md:mb-10">
          {/* About */}
          <div>
            <h3 className="font-bold text-secondary-100 mb-3 text-base md:text-lg">LaptopDoc AI</h3>
            <p className="text-sm md:text-base text-secondary-200 leading-relaxed">
              Sistem pakar berbasis AI untuk mendiagnosa kerusakan laptop menggunakan algoritma Forward Chaining.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="font-bold text-secondary-100 mb-3 text-base md:text-lg">Our Team:</h3>
            <ul className="space-y-2 md:space-y-3 text-sm md:text-base text-secondary-200">
              <li>• Adri Lorenzo Patiaraja</li>
              <li>• Gideon Miracle Sihombing</li>
              <li>• Muhammad Dheki Akbar</li>
              <li>• M. Zacky Nauval</li>
              <li>• Rafi Ruzain Raba</li>
              <li>• Rizky Raffandy Halim</li>
            </ul>
          </div>

          {/* Source */}
          <div>
            <h3 className="font-bold text-secondary-100 mb-3 text-base md:text-lg">Kontak</h3>
            <div className="space-y-2 md:space-y-3">
              <a
                href="https://github.com/Gimshi/laptopdiag-kelompok9"
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-2 md:gap-3 text-sm md:text-base text-secondary-200 hover:text-primary-400 transition-colors"
              >
                <Github className="w-4 h-4 md:w-5 md:h-5 flex-shrink-0" />
                <span>GitHub Repository</span>
              </a>
            </div>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="pt-6 md:pt-8 border-t border-accent-500">
          <div className="flex flex-col md:flex-row items-center justify-between gap-3 md:gap-5 text-center md:text-left">
            <div className="flex flex-wrap items-center justify-center gap-1.5 md:gap-2 text-xs md:text-base text-secondary-200">
              <span>© {currentYear}</span>
              <span className="font-semibold text-primary-400">Kelompok 9</span>
              <span>-</span>
              <span>Pengantar Kecerdasan Buatan</span>
            </div>
            
          </div>
        </div>
      </div>
    </motion.footer>
  );
};

export default Footer;
