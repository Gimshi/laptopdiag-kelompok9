import { motion } from 'framer-motion';
import { Users, GraduationCap, User } from 'lucide-react';

const TeamSection = () => {
  const teamMembers = [
    {
      name: 'Adri Lorenzo Patiaraja',
      nim: '1313624063',
      color: 'from-primary-400 to-primary-600'
    },
    {
      name: 'Gideon Miracle Sihombing',
      nim: '1313624081',
      color: 'from-accent-400 to-accent-600'
    },
    {
      name: 'Muhammad Dheki Akbar',
      nim: '1313624076',
      color: 'from-primary-500 to-accent-500'
    },
    {
      name: 'M. Zacky Nauval',
      nim: '1313624068',
      color: 'from-accent-500 to-primary-500'
    },
    {
      name: 'Rafi Ruzain Raba',
      nim: '1313624072',
      color: 'from-primary-400 to-accent-400'
    },
    {
      name: 'Rizky Raffandy Halim',
      nim: '1313624067',
      color: 'from-accent-400 to-primary-400'
    }
  ];

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1
      }
    }
  };

  const cardVariants = {
    hidden: { 
      opacity: 0, 
      y: 30,
      scale: 0.95
    },
    visible: { 
      opacity: 1, 
      y: 0,
      scale: 1,
      transition: {
        duration: 0.5,
        ease: "easeOut"
      }
    }
  };

  return (
    <section className="py-16 md:py-24 bg-gradient-to-b from-secondary-50 to-secondary-100">
      <div className="max-w-7xl mx-auto px-4 md:px-8">
        {/* Section Header */}
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.6 }}
          className="text-center mb-12 md:mb-16"
        >
          <div className="inline-flex items-center gap-2 px-4 py-2 bg-primary-100 rounded-full mb-4">
            <Users className="w-5 h-5 text-primary-600" />
            <span className="text-sm font-semibold text-primary-700">Meet Our Team</span>
          </div>
          
          <h2 className="text-3xl md:text-4xl lg:text-5xl font-bold text-highlight-900 mb-4">
            Kelompok 9
          </h2>
          
          <p className="text-base md:text-lg text-highlight-600 max-w-2xl mx-auto">
            Tim developer yang berdedikasi dalam menciptakan solusi diagnosis laptop berbasis AI
          </p>
          
          <div className="flex items-center justify-center gap-2 mt-4 text-sm text-highlight-500">
            <GraduationCap className="w-5 h-5" />
            <span>Pengantar Kecerdasan Buatan - Ilmu Komputer UNJ 2024</span>
          </div>
        </motion.div>

        {/* Team Cards Grid */}
        <motion.div
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: "-100px" }}
          className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8"
        >
          {teamMembers.map((member, index) => (
            <motion.div
              key={member.nim}
              variants={cardVariants}
              whileHover={{ 
                y: -8,
                transition: { duration: 0.3 }
              }}
              className="group"
            >
              <div className="relative bg-white rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden h-full">
                {/* Gradient Background Decoration */}
                <div className={`absolute top-0 left-0 right-0 h-2 bg-gradient-to-r ${member.color}`} />
                
                {/* Card Content */}
                <div className="p-6 md:p-8">
                  {/* Avatar Circle with User Icon */}
                  <div className="mb-6 flex justify-center">
                    <div className={`relative w-20 h-20 md:w-24 md:h-24 rounded-full bg-gradient-to-br ${member.color} flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300`}>
                      <User className="w-10 h-10 md:w-12 md:h-12 text-white" strokeWidth={2} />
                    </div>
                  </div>

                  {/* Member Info */}
                  <div className="text-center space-y-3">
                    <h3 className="text-lg md:text-xl font-bold text-highlight-900 group-hover:text-primary-600 transition-colors">
                      {member.name}
                    </h3>
                    
                    <div className={`inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-r ${member.color} bg-opacity-10 rounded-full`}>
                      <span className="text-sm md:text-base font-mono font-semibold text-highlight-700">
                        {member.nim}
                      </span>
                    </div>
                  </div>
                </div>

                {/* Bottom Accent Line */}
                <div className={`h-1 bg-gradient-to-r ${member.color} transform scale-x-0 group-hover:scale-x-100 transition-transform duration-300 origin-left`} />
              </div>
            </motion.div>
          ))}
        </motion.div>

        {/* Bottom Decoration */}
        <motion.div
          initial={{ opacity: 0, scale: 0.8 }}
          whileInView={{ opacity: 1, scale: 1 }}
          viewport={{ once: true }}
          transition={{ delay: 0.5, duration: 0.6 }}
          className="mt-12 text-center"
        >
          <div className="inline-flex items-center gap-3 px-6 py-3 bg-white rounded-full shadow-md">
            <div className="flex -space-x-2">
              {[...Array(6)].map((_, i) => (
                <div
                  key={i}
                  className={`w-8 h-8 rounded-full bg-gradient-to-br ${teamMembers[i].color} border-2 border-white`}
                />
              ))}
            </div>
            <span className="text-sm font-semibold text-highlight-700">
              6 Members
            </span>
          </div>
        </motion.div>
      </div>
    </section>
  );
};

export default TeamSection;
