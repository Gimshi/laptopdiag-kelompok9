import { motion } from 'framer-motion';
import { Brain, Target, Shield, Zap } from 'lucide-react';

const AboutSection = () => {
  const features = [
    {
      icon: Brain,
      title: 'Forward Chaining AI',
      description: 'Menggunakan algoritma forward chaining untuk reasoning data-driven yang akurat'
    },
    {
      icon: Zap,
      title: 'Diagnosis Cepat',
      description: 'Hasil diagnosis instan dalam hitungan detik tanpa perlu menunggu lama'
    },
    {
      icon: Target,
      title: 'Solusi Tepat',
      description: 'Rekomendasi solusi spesifik berdasarkan diagnosis yang ditemukan'
    },
    {
      icon: Shield,
      title: 'Knowledge Base',
      description: '20+ gejala dan 15+ rules untuk diagnosis kerusakan laptop yang komprehensif'
    }
  ];

  return (
    <section id="about" className="py-16 sm:py-20 md:py-24 bg-slate-900">
      <div className="max-w-8xl mx-auto px-4 sm:px-6 md:px-8 lg:px-10 xl:px-12">
        {/* Section Header - BIGGER */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-center mb-12 sm:mb-16 md:mb-20"
        >
          <h2 className="text-4xl sm:text-5xl md:text-6xl font-bold text-slate-100 mb-4 sm:mb-6 px-4 sm:px-0">
            Tentang Sistem Ini
          </h2>
          <p className="text-lg sm:text-xl md:text-2xl text-slate-400 max-w-3xl mx-auto leading-relaxed px-4 sm:px-0">
            Sistem pakar berbasis AI yang dirancang untuk membantu Anda mengidentifikasi dan mengatasi masalah laptop dengan cepat dan akurat.
          </p>
        </motion.div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 sm:gap-8">
          {features.map((feature, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.1 }}
              className="bg-slate-800 border border-slate-700 rounded-2xl p-8 hover:border-primary-500/50 transition-all"
            >
              <div className="w-16 h-16 bg-primary-500/15 border border-primary-500/30 rounded-2xl flex items-center justify-center mb-6">
                <feature.icon className="w-8 h-8 text-primary-400" />
              </div>
              <h3 className="text-xl font-bold text-slate-100 mb-3">
                {feature.title}
              </h3>
              <p className="text-base text-slate-400 leading-relaxed">
                {feature.description}
              </p>
            </motion.div>
          ))}
        </div>

        {/* Tech Stack */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mt-12 sm:mt-16 md:mt-20 p-6 sm:p-8 md:p-10 bg-slate-800 border border-slate-700 rounded-3xl"
        >
          <h3 className="text-2xl sm:text-3xl font-bold text-slate-100 mb-6 sm:mb-8 text-center px-4 sm:px-0">
            Teknologi yang Digunakan
          </h3>
          <div className="flex flex-wrap justify-center gap-3 sm:gap-4 md:gap-5">
            {['Python', 'Flask', 'React', 'Vite', 'UnoCSS', 'Forward Chaining', 'REST API', 'Framer Motion'].map((tech, index) => (
              <span
                key={index}
                className="px-4 py-2 sm:px-5 sm:py-2.5 md:px-6 md:py-3 bg-slate-700 border border-slate-600 text-slate-200 text-sm sm:text-base font-medium rounded-xl hover:border-primary-500/50 transition-colors"
              >
                {tech}
              </span>
            ))}
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default AboutSection;
