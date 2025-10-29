import { motion } from 'framer-motion';
import { Heart, Github, Mail } from 'lucide-react';

const Footer = () => {
  const currentYear = new Date().getFullYear();

  return (
    <motion.footer
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ delay: 0.5 }}
      className="bg-highlight-800 mt-0 pt-16"
    >
      <div className="max-w-8xl mx-auto px-8 pb-12">
        {/* Main Footer Content */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-12 mb-10">
          {/* About */}
          <div>
            <h3 className="font-bold text-secondary-100 mb-4 text-lg">LaptopDoc AI</h3>
            <p className="text-base text-secondary-200 leading-relaxed">
              Sistem pakar berbasis AI untuk mendiagnosa kerusakan laptop menggunakan algoritma Forward Chaining.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="font-bold text-secondary-100 mb-4 text-lg">Teknologi</h3>
            <ul className="space-y-3 text-base text-secondary-200">
              <li>• Forward Chaining Algorithm</li>
              <li>• React + Vite</li>
              <li>• Flask REST API</li>
              <li>• UnoCSS Framework</li>
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h3 className="font-bold text-secondary-100 mb-4 text-lg">Kontak</h3>
            <div className="space-y-3">
              <a
                href="mailto:kelompok9@unj.ac.id"
                className="flex items-center gap-3 text-base text-secondary-200 hover:text-primary-400 transition-colors"
              >
                <Mail className="w-5 h-5" />
                kelompok9@unj.ac.id
              </a>
              <a
                href="#"
                className="flex items-center gap-3 text-base text-secondary-200 hover:text-primary-400 transition-colors"
              >
                <Github className="w-5 h-5" />
                GitHub Repository
              </a>
            </div>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="pt-8 border-t border-accent-500">
          <div className="flex flex-col md:flex-row items-center justify-between gap-5">
            <div className="flex items-center gap-2 text-base text-secondary-200">
              <span>© {currentYear}</span>
              <span className="font-semibold text-primary-400">Kelompok 9</span>
              <span>-</span>
              <span>Pengantar Kecerdasan Buatan</span>
            </div>
            
            <div className="flex items-center gap-2 text-base text-secondary-200">
              <span>Made with</span>
              <Heart className="w-5 h-5 text-primary-500 fill-primary-500" />
              <span>at Universitas Negeri Jakarta</span>
            </div>
          </div>
        </div>
      </div>
    </motion.footer>
  );
};

export default Footer;
