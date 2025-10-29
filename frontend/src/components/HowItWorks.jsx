import { motion } from 'framer-motion';
import { CheckSquare, Brain, FileSearch, Lightbulb } from 'lucide-react';

const HowItWorks = () => {
  const steps = [
    {
      icon: CheckSquare,
      number: '01',
      title: 'Pilih Gejala',
      description: 'Pilih semua gejala kerusakan yang Anda alami pada laptop dari daftar yang tersedia.'
    },
    {
      icon: Brain,
      number: '02',
      title: 'AI Processing',
      description: 'Sistem Forward Chaining AI memproses gejala yang dipilih menggunakan knowledge base dengan 15+ rules.'
    },
    {
      icon: FileSearch,
      number: '03',
      title: 'Analisis Mendalam',
      description: 'Algoritma mencocokkan pola gejala dengan database diagnosis untuk menemukan kemungkinan kerusakan.'
    },
    {
      icon: Lightbulb,
      number: '04',
      title: 'Dapatkan Solusi',
      description: 'Terima diagnosis lengkap dengan tingkat confidence dan rekomendasi solusi spesifik untuk setiap masalah.'
    }
  ];

  return (
    <section id="how-it-works" className="py-16 sm:py-20 md:py-24 bg-slate-950">
      <div className="max-w-8xl mx-auto px-4 sm:px-6 md:px-8 lg:px-10 xl:px-12">
        {/* Section Header - BIGGER */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-center mb-12 sm:mb-16 md:mb-20"
        >
          <h2 className="text-4xl sm:text-5xl md:text-6xl font-bold text-slate-100 mb-4 sm:mb-6 px-4 sm:px-0">
            Cara Kerja Sistem
          </h2>
          <p className="text-lg sm:text-xl md:text-2xl text-slate-400 max-w-3xl mx-auto leading-relaxed px-4 sm:px-0">
            Proses diagnosis yang sederhana namun powerful menggunakan teknologi AI Forward Chaining
          </p>
        </motion.div>

        {/* Steps */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 sm:gap-8">
          {steps.map((step, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.15 }}
              className="relative"
            >
              {/* Connector Line */}
              {index < steps.length - 1 && (
                <div className="hidden lg:block absolute top-16 sm:top-20 left-full w-full h-0.5 bg-gradient-to-r from-primary-500/50 to-transparent" />
              )}

              <div className="bg-slate-900 border border-slate-700 rounded-2xl p-6 sm:p-8 hover:border-primary-500/50 transition-all hover:shadow-xl hover:shadow-primary-500/10">
                {/* Number Badge - BIGGER */}
                <div className="inline-flex items-center justify-center w-16 h-16 sm:w-20 sm:h-20 bg-primary-500/15 border-2 border-primary-500/30 rounded-2xl mb-5 sm:mb-6">
                  <span className="text-2xl sm:text-3xl font-bold text-primary-400">
                    {step.number}
                  </span>
                </div>

                {/* Icon - BIGGER */}
                <div className="w-12 h-12 sm:w-14 sm:h-14 bg-slate-800 border border-slate-600 rounded-xl flex items-center justify-center mb-5 sm:mb-6">
                  <step.icon className="w-6 h-6 sm:w-7 sm:h-7 text-slate-300" />
                </div>

                {/* Content - BIGGER */}
                <h3 className="text-xl sm:text-2xl font-bold text-slate-100 mb-3 sm:mb-4">
                  {step.title}
                </h3>
                <p className="text-sm sm:text-base text-slate-400 leading-relaxed">
                  {step.description}
                </p>
              </div>
            </motion.div>
          ))}
        </div>

        {/* Forward Chaining Explanation - BIGGER */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mt-20 p-10 bg-gradient-to-br from-primary-500/10 via-slate-900 to-slate-900 border border-primary-500/30 rounded-3xl"
        >
          <div className="flex items-start gap-8">
            <div className="w-20 h-20 bg-primary-500/20 border border-primary-500/40 rounded-2xl flex items-center justify-center flex-shrink-0">
              <Brain className="w-10 h-10 text-primary-400" />
            </div>
            <div>
              <h3 className="text-3xl font-bold text-slate-100 mb-4">
                Apa itu Forward Chaining?
              </h3>
              <p className="text-lg text-slate-300 leading-relaxed mb-6">
                Forward Chaining adalah metode inferensi dalam sistem pakar yang bekerja dengan pendekatan <span className="text-primary-400 font-semibold">data-driven</span>. 
                Sistem dimulai dari fakta-fakta yang diketahui (gejala yang dipilih), kemudian menggunakan rules dalam knowledge base untuk menarik kesimpulan baru hingga mencapai diagnosis akhir.
              </p>
              <div className="flex flex-wrap gap-4">
                <span className="px-5 py-3 bg-slate-800 border border-slate-600 text-slate-200 text-base rounded-xl">
                  ✓ Data-driven reasoning
                </span>
                <span className="px-5 py-3 bg-slate-800 border border-slate-600 text-slate-200 text-base rounded-xl">
                  ✓ Bottom-up approach
                </span>
                <span className="px-5 py-3 bg-slate-800 border border-slate-600 text-slate-200 text-base rounded-xl">
                  ✓ Rule-based inference
                </span>
              </div>
            </div>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default HowItWorks;
