import { defineConfig, presetUno, presetAttributify, presetIcons } from 'unocss'

export default defineConfig({
  presets: [
    presetUno(), // Tailwind-like utilities
    presetAttributify(), // Attributify mode
    presetIcons({
      scale: 1.2,
      warn: true,
    }),
  ],
  theme: {
    colors: {
      // Warm Earthy Palette - Terracotta, Cream, Peach, Brown (prioritized by box size)
      // #B77466 (Terracotta/Rose Brown) - LARGEST box → Primary
      primary: {
        50: '#fdf5f4',
        100: '#fbe9e7',
        200: '#f7d4cf',
        300: '#f0bfb8',
        400: '#e6a59b',
        500: '#d98c7e',
        600: '#B77466', // Main Terracotta - LARGEST
        700: '#a05d51',
        800: '#87493e',
        900: '#6d382f',
      },
      // #FFE1AF (Soft Cream/Peach) - 2nd LARGEST box → Secondary/Background
      secondary: {
        50: '#fffcf7',
        100: '#fff8ed',
        200: '#fff2db',
        300: '#FFE1AF', // Main Cream - 2nd LARGEST
        400: '#ffd89a',
        500: '#ffc97f',
        600: '#f5b565',
        700: '#e09a4a',
        800: '#c07c32',
        900: '#9a5e21',
      },
      // #E2B59A (Warm Peach/Tan) - 3rd box → Accent
      accent: {
        50: '#faf7f5',
        100: '#f5eeea',
        200: '#ebddd5',
        300: '#E2B59A', // Main Peach - 3rd
        400: '#d8a385',
        500: '#cc8e6e',
        600: '#bd7858',
        700: '#a96345',
        800: '#8f5037',
        900: '#723e2a',
      },
      // #957C62 (Warm Brown) - SMALLEST box → Highlight/Dark
      highlight: {
        50: '#f7f5f3',
        100: '#eeebe7',
        200: '#ddd7cf',
        300: '#cbbfb3',
        400: '#b7a795',
        500: '#a18d79',
        600: '#957C62', // Main Brown - SMALLEST
        700: '#7a6550',
        800: '#604f3f',
        900: '#483a2f',
      },
      // Neutral grays with subtle warm brown tint
      slate: {
        50: '#faf9f7',
        100: '#f5f2ee',
        200: '#ebe6df',
        300: '#ddd4c9',
        400: '#cbbfb0',
        500: '#b5a593',
        600: '#9d8b78',
        700: '#826f5f',
        800: '#67574a',
        850: '#4d4038',
        900: '#3a2f28',
        950: '#2a211b',
      },
      // Status colors with green harmony
      success: {
        400: '#88b45e',
        500: '#4c763b',
        600: '#3d6130',
      },
      warning: {
        400: '#fffd8f',
        500: '#ffd740',
        600: '#f5c51e',
      },
      danger: {
        400: '#e87171',
        500: '#d84c4c',
        600: '#b93939',
      }
    }
  },
  shortcuts: {
    'btn': 'px-7 py-3.5 rounded-xl font-semibold transition-all duration-300 cursor-pointer shadow-md text-base',
    'btn-primary': 'btn bg-primary-500 text-slate-50 hover:bg-primary-600 hover:shadow-lg hover:shadow-primary-500/30 active:scale-98',
    'btn-secondary': 'btn bg-slate-700 text-slate-100 border-2 border-slate-600 hover:border-primary-500 hover:bg-slate-650 active:scale-98',
    'card': 'bg-slate-800 rounded-2xl shadow-lg border border-slate-700 p-10 transition-all duration-300 hover:shadow-xl hover:border-slate-650',
    'input': 'w-full px-5 py-3.5 rounded-xl border-2 border-slate-600 bg-slate-750 text-slate-100 focus:border-primary-500 focus:outline-none transition-all placeholder-slate-400 text-base',
  }
})
