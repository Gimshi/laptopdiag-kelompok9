# Knowledge Base untuk Deteksi Kerusakan Laptop
# Berisi rules dan facts untuk forward chaining

class KnowledgeBase:
    """
    Knowledge Base untuk sistem pakar deteksi kerusakan laptop
    Menggunakan rule-based system dengan format IF-THEN
    """
    
    def __init__(self):
        self.rules = self._initialize_rules()
        self.symptoms = self._initialize_symptoms()
        
    def _initialize_symptoms(self):
        """Daftar gejala yang bisa dipilih user"""
        return {
            'S01': 'Laptop tidak bisa menyala sama sekali',
            'S02': 'Laptop menyala tapi layar hitam/blank',
            'S03': 'Laptop sangat lambat/lemot',
            'S04': 'Laptop sering restart sendiri',
            'S05': 'Laptop sangat panas/overheat',
            'S06': 'Kipas laptop berbunyi sangat keras',
            'S07': 'Baterai cepat habis',
            'S08': 'Laptop tidak bisa charging',
            'S09': 'Layar bergaris atau tampilan aneh',
            'S10': 'Keyboard tidak berfungsi sebagian',
            'S11': 'Touchpad tidak responsif',
            'S12': 'Suara speaker pecah atau tidak keluar',
            'S13': 'WiFi tidak terdeteksi/tidak bisa connect',
            'S14': 'USB port tidak berfungsi',
            'S15': 'Blue Screen of Death (BSOD)',
            'S16': 'Laptop freeze/hang sering',
            'S17': 'Hard disk berbunyi aneh (klik-klik)',
            'S18': 'Laptop berbau terbakar',
            'S19': 'Laptop mati sendiri saat digunakan',
            'S20': 'Aplikasi sering crash/error'
        }
    
    def _initialize_rules(self):
        """
        Rules dalam format:
        {
            'rule_id': {
                'conditions': ['symptom_codes'],
                'conclusion': {
                    'diagnosis': 'nama kerusakan',
                    'category': 'hardware/software',
                    'severity': 'ringan/sedang/berat',
                    'solutions': ['solusi1', 'solusi2', ...],
                    'description': 'penjelasan kerusakan'
                }
            }
        }
        """
        return {
            'R01': {
                'conditions': ['S01', 'S08'],
                'conclusion': {
                    'diagnosis': 'Kerusakan Charger atau Port Charging',
                    'category': 'hardware',
                    'severity': 'sedang',
                    'solutions': [
                        'Cek charger dengan multimeter',
                        'Periksa port charging apakah longgar',
                        'Ganti charger jika rusak',
                        'Repair atau ganti port charging'
                    ],
                    'description': 'Laptop tidak mendapat daya dari charger, bisa karena charger rusak atau port charging bermasalah.'
                }
            },
            'R02': {
                'conditions': ['S01', 'S18'],
                'conclusion': {
                    'diagnosis': 'Kerusakan Motherboard (Short Circuit)',
                    'category': 'hardware',
                    'severity': 'berat',
                    'solutions': [
                        'Matikan laptop segera',
                        'Bawa ke teknisi profesional',
                        'Kemungkinan perlu ganti motherboard',
                        'Backup data jika memungkinkan'
                    ],
                    'description': 'Terjadi short circuit pada motherboard, sangat berbahaya dan perlu penanganan segera.'
                }
            },
            'R03': {
                'conditions': ['S02', 'S06'],
                'conclusion': {
                    'diagnosis': 'Kerusakan VGA/Graphics Card',
                    'category': 'hardware',
                    'severity': 'berat',
                    'solutions': [
                        'Update driver VGA',
                        'Cek koneksi kabel LCD ke motherboard',
                        'Test dengan monitor eksternal',
                        'Ganti VGA card jika memungkinkan',
                        'Reflow/reball VGA chip (teknisi)'
                    ],
                    'description': 'VGA card bermasalah sehingga tidak bisa menampilkan gambar ke layar.'
                }
            },
            'R04': {
                'conditions': ['S05', 'S06', 'S19'],
                'conclusion': {
                    'diagnosis': 'Overheating - Sistem Pendingin Bermasalah',
                    'category': 'hardware',
                    'severity': 'sedang',
                    'solutions': [
                        'Bersihkan kipas dan heatsink dari debu',
                        'Ganti thermal paste CPU dan GPU',
                        'Pastikan ventilasi tidak tertutup',
                        'Gunakan cooling pad',
                        'Cek apakah kipas masih berfungsi normal'
                    ],
                    'description': 'Laptop overheat karena sistem pendinginan tidak bekerja optimal, bisa menyebabkan thermal shutdown.'
                }
            },
            'R05': {
                'conditions': ['S03', 'S16', 'S20'],
                'conclusion': {
                    'diagnosis': 'RAM Bermasalah atau Tidak Cukup',
                    'category': 'hardware',
                    'severity': 'sedang',
                    'solutions': [
                        'Cek usage RAM di Task Manager',
                        'Bersihkan slot RAM dan konektor',
                        'Coba lepas-pasang RAM',
                        'Test RAM satu per satu jika ada 2 slot',
                        'Upgrade RAM jika kapasitas kurang',
                        'Ganti RAM jika rusak'
                    ],
                    'description': 'RAM tidak berfungsi dengan baik atau kapasitas tidak mencukupi untuk kebutuhan.'
                }
            },
            'R06': {
                'conditions': ['S03', 'S17'],
                'conclusion': {
                    'diagnosis': 'Hard Disk/HDD Rusak atau Bad Sector',
                    'category': 'hardware',
                    'severity': 'berat',
                    'solutions': [
                        'Backup data segera!',
                        'Scan disk dengan CHKDSK atau HD Tune',
                        'Defragment disk jika HDD',
                        'Pertimbangkan upgrade ke SSD',
                        'Ganti hard disk jika banyak bad sector'
                    ],
                    'description': 'Hard disk mengalami kerusakan fisik atau bad sector yang menyebabkan performa lambat.'
                }
            },
            'R07': {
                'conditions': ['S07', 'S19'],
                'conclusion': {
                    'diagnosis': 'Baterai Laptop Sudah Rusak/Kembung',
                    'category': 'hardware',
                    'severity': 'sedang',
                    'solutions': [
                        'Cek kondisi fisik baterai (kembung?)',
                        'Cek battery health dengan software',
                        'Kalibrasi baterai',
                        'Ganti baterai baru jika sudah rusak',
                        'Jangan gunakan baterai kembung (berbahaya!)'
                    ],
                    'description': 'Baterai sudah aus atau rusak sehingga tidak bisa menyimpan daya dengan baik.'
                }
            },
            'R08': {
                'conditions': ['S15', 'S04'],
                'conclusion': {
                    'diagnosis': 'Kerusakan Driver atau Sistem Operasi',
                    'category': 'software',
                    'severity': 'sedang',
                    'solutions': [
                        'Catat kode error BSOD',
                        'Update semua driver',
                        'Scan malware/virus',
                        'System File Checker (sfc /scannow)',
                        'System Restore ke titik sebelumnya',
                        'Reinstall Windows jika perlu'
                    ],
                    'description': 'Driver atau sistem operasi bermasalah menyebabkan BSOD dan restart tidak normal.'
                }
            },
            'R09': {
                'conditions': ['S09'],
                'conclusion': {
                    'diagnosis': 'Kerusakan Layar LCD atau Kabel Flexible',
                    'category': 'hardware',
                    'severity': 'sedang',
                    'solutions': [
                        'Cek apakah garis hilang saat layar ditekan',
                        'Tes dengan monitor eksternal',
                        'Cek kabel flexible LCD (buka engsel)',
                        'Ganti layar LCD jika rusak permanen',
                        'Re-seat kabel flexible'
                    ],
                    'description': 'Layar LCD rusak atau kabel penghubung layar bermasalah.'
                }
            },
            'R10': {
                'conditions': ['S10'],
                'conclusion': {
                    'diagnosis': 'Kerusakan Keyboard',
                    'category': 'hardware',
                    'severity': 'ringan',
                    'solutions': [
                        'Bersihkan keyboard dari debu/kotoran',
                        'Cek apakah ada tombol yang macet',
                        'Update driver keyboard',
                        'Test dengan keyboard eksternal',
                        'Ganti keyboard laptop jika perlu'
                    ],
                    'description': 'Keyboard laptop tidak berfungsi sebagian, bisa karena kotoran atau kerusakan hardware.'
                }
            },
            'R11': {
                'conditions': ['S13'],
                'conclusion': {
                    'diagnosis': 'Kerusakan WiFi Card atau Driver',
                    'category': 'hardware',
                    'severity': 'sedang',
                    'solutions': [
                        'Pastikan WiFi tidak dalam mode airplane',
                        'Restart router',
                        'Update driver WiFi',
                        'Uninstall dan install ulang driver WiFi',
                        'Cek apakah WiFi card terdeteksi di Device Manager',
                        'Ganti WiFi card jika rusak'
                    ],
                    'description': 'WiFi card atau driver bermasalah sehingga tidak bisa mendeteksi jaringan.'
                }
            },
            'R12': {
                'conditions': ['S03', 'S20'],
                'conclusion': {
                    'diagnosis': 'Sistem Operasi Corrupt atau Virus',
                    'category': 'software',
                    'severity': 'sedang',
                    'solutions': [
                        'Scan dengan antivirus terbaru',
                        'Hapus program yang tidak perlu',
                        'Bersihkan temporary files',
                        'Disable startup programs yang tidak penting',
                        'System Restore',
                        'Clean install Windows jika perlu'
                    ],
                    'description': 'Sistem operasi terinfeksi virus atau file sistem corrupt.'
                }
            },
            'R13': {
                'conditions': ['S14'],
                'conclusion': {
                    'diagnosis': 'Kerusakan USB Port atau Driver USB',
                    'category': 'hardware',
                    'severity': 'ringan',
                    'solutions': [
                        'Coba port USB yang lain',
                        'Update driver USB controller',
                        'Uninstall device di Device Manager lalu restart',
                        'Cek power management USB (jangan sleep)',
                        'Ganti USB port jika rusak fisik'
                    ],
                    'description': 'USB port tidak berfungsi karena driver atau kerusakan hardware.'
                }
            },
            'R14': {
                'conditions': ['S12'],
                'conclusion': {
                    'diagnosis': 'Kerusakan Speaker atau Driver Audio',
                    'category': 'hardware',
                    'severity': 'ringan',
                    'solutions': [
                        'Cek volume dan mute status',
                        'Update driver audio',
                        'Reinstall driver audio',
                        'Test dengan headphone',
                        'Troubleshoot audio Windows',
                        'Ganti speaker jika rusak'
                    ],
                    'description': 'Speaker tidak berfungsi atau suara pecah karena driver atau kerusakan hardware.'
                }
            },
            'R15': {
                'conditions': ['S11'],
                'conclusion': {
                    'diagnosis': 'Kerusakan Touchpad atau Driver',
                    'category': 'hardware',
                    'severity': 'ringan',
                    'solutions': [
                        'Pastikan touchpad tidak di-disable (Fn+F-key)',
                        'Update driver touchpad',
                        'Bersihkan permukaan touchpad',
                        'Cek setting touchpad di Windows',
                        'Test dengan mouse eksternal',
                        'Ganti touchpad jika rusak'
                    ],
                    'description': 'Touchpad tidak responsif karena setting, driver, atau kerusakan hardware.'
                }
            }
        }
    
    def get_all_symptoms(self):
        """Return list of all symptoms"""
        return [{'code': code, 'description': desc} 
                for code, desc in self.symptoms.items()]
    
    def get_symptom_description(self, symptom_code):
        """Get description of a symptom"""
        return self.symptoms.get(symptom_code, "Unknown symptom")
    
    def get_all_rules(self):
        """Return all rules"""
        return self.rules
