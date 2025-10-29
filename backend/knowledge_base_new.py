# Knowledge Base Baru untuk Deteksi Kerusakan Laptop
# Berisi rules dan facts untuk forward chaining
# Data berdasarkan tabel premis-konklusi kelompok

class KnowledgeBase:
    """
    Knowledge Base untuk sistem pakar deteksi kerusakan laptop
    Menggunakan rule-based system dengan format IF-THEN
    Total: 53 Symptoms (Premis) & 24 Rules (Konklusi)
    """
    
    def __init__(self):
        self.rules = self._initialize_rules()
        self.symptoms = self._initialize_symptoms()
        
    def _initialize_symptoms(self):
        """Daftar 53 gejala (premis) yang bisa dipilih user"""
        return {
            'P01': 'Indikator Mesin Tidak Menyala',
            'P02': 'Indikator Baterai Tidak Menyala',
            'P03': 'Indikator Mesin Menyala',
            'P04': 'Indikator Baterai Berkedip',
            'P05': 'Indikator Charge Menyala',
            'P06': 'Indikator Charge Mati',
            'P07': 'Indikator Capslock dapat berfungsi',
            'P08': 'Keyboard tidak dapat digunakan',
            'P09': 'Touchpad tidak dapat digunakan',
            'P10': 'Touchpad dapat digunakan',
            'P11': 'Tombol Sisi Touchpad Berfungsi',
            'P12': 'Mouse Berfungsi',
            'P13': 'Mouse tidak berfungsi',
            'P14': 'Flashdrive atau Harddisk External dapat digunakan',
            'P15': 'Flashdrive atau Harddisk External tidak dapat digunakan',
            'P16': 'Camera tidak dapat digunakan',
            'P17': 'Mic tidak dapat digunakan',
            'P18': 'Suara dari Speaker Kurang Jelas',
            'P19': 'Speaker tidak mengeluarkan suara',
            'P20': 'Speaker mengeluarkan distorsi suara, atau suara tak beraturan',
            'P21': 'Suara dari Speaker/Headphone Eksternal normal dan jelas',
            'P22': 'Layar blank',
            'P23': 'Layar Normal',
            'P24': 'Layar menyala, tetapi redup dan perlu disenter agar terlihat',
            'P25': 'Wifi tidak dapat menyala',
            'P26': 'Wifi tidak dapat terhubung',
            'P27': 'Bluetooth tidak dapat menyala',
            'P28': 'Bluetooth tidak dapat terhubung',
            'P29': 'Monitor tidak dapat terhubung melalui kabel',
            'P30': 'Monitor tidak dapat terhubung melalui media wireless',
            'P31': 'Laptop tidak dapat menyala',
            'P32': 'Laptop Menyala',
            'P33': 'Charger sudah terpasang',
            'P34': 'Baterai dapat terisi',
            'P35': 'Pengunaan RAM Tinggi',
            'P36': 'Penggunaan CPU Tinggi',
            'P37': 'Penyimpanan Penuh',
            'P38': 'Data Sering Hilang atau tidak tersimpan',
            'P39': 'Laptop Sering Mati Tiba-tiba',
            'P40': 'Suhu Laptop tidak wajar (Overheat)',
            'P41': 'Kipas Laptop menyala',
            'P42': 'Kipas Laptop Tidak Menyala',
            'P43': 'Sering Freeze',
            'P44': 'Layar Glitch',
            'P45': 'Layar Tiba-Tiba Berubah Warna',
            'P46': 'Muncul Logo OS laptop',
            'P47': 'Restart Kembali setelah menyala',
            'P48': 'Muncul peringatan "repairing your drive"',
            'P49': 'Kabel sensitif terhadap gerakan',
            'P50': 'Tangan sering tersetrum saat bersentuhan dengan laptop',
            'P51': 'Camera dapat digunakan',
            'P52': 'Mic dapat digunakan',
            'P53': 'Jam dan Tanggal tidak sesuai yang sebenarnya'
        }
    
    def _initialize_rules(self):
        """
        24 Rules dalam format IF-THEN
        Berdasarkan tabel konklusi yang diberikan
        """
        return {
            'R01': {
                'conditions': ['P02', 'P03', 'P04', 'P05'],
                'conclusion': {
                    'diagnosis': 'Baterai Kembung, Bocor, Atau Rusak',
                    'category': 'hardware',
                    'severity': 'sedang',
                    'solutions': [
                        'Matikan laptop dan lepas baterai segera',
                        'Cek kondisi fisik baterai (kembung/bocor)',
                        'Jangan gunakan baterai yang kembung (berbahaya)',
                        'Ganti dengan baterai baru yang original',
                        'Bawa ke service center jika ragu'
                    ],
                    'description': 'Baterai laptop mengalami kerusakan fisik seperti kembung, bocor, atau sudah tidak dapat menyimpan daya dengan baik.'
                }
            },
            'R02': {
                'conditions': ['P08', 'P07'],
                'conclusion': {
                    'diagnosis': 'Keyboard Rusak',
                    'category': 'hardware',
                    'severity': 'sedang',
                    'solutions': [
                        'Coba restart laptop terlebih dahulu',
                        'Update atau reinstall driver keyboard',
                        'Cek koneksi kabel flexible keyboard (buka casing)',
                        'Bersihkan keyboard dari debu dan kotoran',
                        'Ganti keyboard laptop jika rusak permanen',
                        'Gunakan keyboard eksternal sebagai alternatif sementara'
                    ],
                    'description': 'Keyboard laptop tidak berfungsi meskipun indikator capslock masih berfungsi, kemungkinan kerusakan hardware keyboard.'
                }
            },
            'R03': {
                'conditions': ['P09', 'P11'],
                'conclusion': {
                    'diagnosis': 'Touchpad Rusak',
                    'category': 'hardware',
                    'severity': 'ringan',
                    'solutions': [
                        'Pastikan touchpad tidak di-disable (Fn + F-key)',
                        'Update driver touchpad dari Device Manager',
                        'Bersihkan permukaan touchpad dari kotoran',
                        'Cek setting touchpad di Windows Settings',
                        'Ganti touchpad jika rusak permanen',
                        'Gunakan mouse eksternal sebagai alternatif'
                    ],
                    'description': 'Touchpad tidak dapat digunakan untuk menggerakkan kursor, namun tombol sisi touchpad masih berfungsi.'
                }
            },
            'R04': {
                'conditions': ['P13', 'P15'],
                'conclusion': {
                    'diagnosis': 'Port USB Rusak',
                    'category': 'hardware',
                    'severity': 'sedang',
                    'solutions': [
                        'Coba port USB yang berbeda',
                        'Test dengan device USB lain (mouse, flashdrive)',
                        'Update driver USB controller di Device Manager',
                        'Uninstall dan install ulang USB driver',
                        'Cek apakah port USB kotor atau patah',
                        'Ganti atau repair port USB jika rusak fisik'
                    ],
                    'description': 'Port USB tidak dapat mendeteksi perangkat eksternal seperti mouse atau flashdrive/harddisk external.'
                }
            },
            'R05': {
                'conditions': ['P10', 'P13', 'P14'],
                'conclusion': {
                    'diagnosis': 'Mouse Rusak',
                    'category': 'hardware',
                    'severity': 'ringan',
                    'solutions': [
                        'Cek koneksi mouse (USB atau wireless)',
                        'Ganti baterai mouse jika wireless',
                        'Coba port USB lain',
                        'Update driver mouse',
                        'Test mouse di laptop/PC lain',
                        'Ganti mouse jika rusak'
                    ],
                    'description': 'Mouse eksternal tidak berfungsi meskipun touchpad dan USB port masih normal, kemungkinan mouse yang rusak.'
                }
            },
            'R06': {
                'conditions': ['P16', 'P17', 'P26'],
                'conclusion': {
                    'diagnosis': 'Konektor Fleksibel Kamera dan mic rusak',
                    'category': 'hardware',
                    'severity': 'sedang',
                    'solutions': [
                        'Cek privacy settings untuk camera dan mic',
                        'Update driver camera dan audio',
                        'Scan dengan Windows troubleshooter',
                        'Cek apakah app memiliki permission untuk camera/mic',
                        'Buka casing dan cek koneksi kabel flexible',
                        'Ganti atau repair konektor flexible'
                    ],
                    'description': 'Camera dan microphone tidak berfungsi karena konektor fleksibel yang rusak atau terlepas.'
                }
            },
            'R07': {
                'conditions': ['P03', 'P05', 'P07', 'P22'],
                'conclusion': {
                    'diagnosis': 'RAM Kotor, Kendor, Rusak',
                    'category': 'hardware',
                    'severity': 'sedang',
                    'solutions': [
                        'Matikan laptop dan lepas baterai',
                        'Buka casing dan lepas RAM',
                        'Bersihkan konektor RAM dengan penghapus/kuas',
                        'Pasang kembali RAM dengan benar hingga klik',
                        'Test RAM satu per satu jika ada 2 slot',
                        'Ganti RAM jika masih bermasalah'
                    ],
                    'description': 'Laptop menyala namun layar blank, kemungkinan RAM kotor, kendor, atau rusak sehingga tidak terbaca sistem.'
                }
            },
            'R08': {
                'conditions': ['P03', 'P22', 'P24'],
                'conclusion': {
                    'diagnosis': 'LED Backlight Layar Rusak',
                    'category': 'hardware',
                    'severity': 'sedang',
                    'solutions': [
                        'Test dengan monitor eksternal',
                        'Atur brightness ke maksimal',
                        'Cek inverter backlight',
                        'Cek kabel flexible LCD',
                        'Ganti LED backlight atau inverter',
                        'Pertimbangkan ganti layar LCD jika biaya repair mahal'
                    ],
                    'description': 'Layar menyala namun sangat redup dan perlu disenter untuk melihat tampilan, menandakan LED backlight rusak.'
                }
            },
            'R09': {
                'conditions': ['P25', 'P26', 'P27', 'P28', 'P30'],
                'conclusion': {
                    'diagnosis': 'Network Card Bermasalah',
                    'category': 'hardware',
                    'severity': 'sedang',
                    'solutions': [
                        'Pastikan airplane mode OFF',
                        'Restart router/modem WiFi',
                        'Update driver network adapter',
                        'Reset network settings Windows',
                        'Cek apakah network card terdeteksi di Device Manager',
                        'Ganti network card WiFi/Bluetooth jika rusak'
                    ],
                    'description': 'WiFi dan Bluetooth tidak dapat menyala atau terhubung, monitor wireless juga bermasalah, kemungkinan network card rusak.'
                }
            },
            'R10': {
                'conditions': ['P26', 'P28', 'P30'],
                'conclusion': {
                    'diagnosis': 'Koneksi wireless Bermasalah',
                    'category': 'software',
                    'severity': 'ringan',
                    'solutions': [
                        'Restart laptop dan router',
                        'Forget network dan connect ulang',
                        'Update driver WiFi dan Bluetooth',
                        'Reset network adapter',
                        'Cek password WiFi sudah benar',
                        'Disable dan enable network adapter'
                    ],
                    'description': 'Device wireless dapat menyala namun tidak dapat terhubung, kemungkinan masalah driver atau konfigurasi.'
                }
            },
            'R11': {
                'conditions': ['P35', 'P36', 'P37', 'P40', 'P43', 'P44'],
                'conclusion': {
                    'diagnosis': 'Terinfeksi Virus, Trojan, dan Malware',
                    'category': 'software',
                    'severity': 'sedang',
                    'solutions': [
                        'Scan full system dengan antivirus (Windows Defender atau third-party)',
                        'Boot ke Safe Mode dan scan ulang',
                        'Hapus program mencurigakan dari Control Panel',
                        'Reset browser settings',
                        'Gunakan anti-malware tools (Malwarebytes, AdwCleaner)',
                        'Backup data dan clean install Windows jika parah'
                    ],
                    'description': 'Penggunaan resource tinggi, laptop sering freeze, layar glitch, menandakan infeksi virus/malware yang berat.'
                }
            },
            'R12': {
                'conditions': ['P31', 'P34', 'P39'],
                'conclusion': {
                    'diagnosis': 'Konektor Baterai Bermasalah',
                    'category': 'hardware',
                    'severity': 'sedang',
                    'solutions': [
                        'Cek apakah baterai terpasang dengan benar',
                        'Lepas dan pasang kembali baterai',
                        'Bersihkan konektor baterai dari oksidasi',
                        'Cek apakah pin konektor bengkok/patah',
                        'Test dengan baterai lain jika ada',
                        'Ganti konektor baterai jika rusak'
                    ],
                    'description': 'Laptop tidak dapat menyala dan sering mati tiba-tiba meskipun baterai dapat terisi, menandakan konektor baterai bermasalah.'
                }
            },
            'R13': {
                'conditions': ['P44', 'P45', 'P29'],
                'conclusion': {
                    'diagnosis': 'Graphic Card Bermasalah',
                    'category': 'hardware',
                    'severity': 'berat',
                    'solutions': [
                        'Update driver VGA/GPU terbaru',
                        'Test dengan monitor eksternal melalui kabel',
                        'Rollback driver VGA jika masalah baru muncul',
                        'Cek temperatur GPU (mungkin overheat)',
                        'Bawa ke teknisi untuk reflow/reball GPU chip',
                        'Ganti VGA card jika memungkinkan'
                    ],
                    'description': 'Layar glitch, berubah warna tiba-tiba, dan monitor eksternal tidak berfungsi, menandakan GPU/VGA bermasalah.'
                }
            },
            'R14': {
                'conditions': ['P18', 'P19', 'P21'],
                'conclusion': {
                    'diagnosis': 'Speaker Bermasalah',
                    'category': 'hardware',
                    'severity': 'ringan',
                    'solutions': [
                        'Cek volume tidak dalam mode mute',
                        'Update atau reinstall driver audio',
                        'Test dengan headphone eksternal',
                        'Run Windows audio troubleshooter',
                        'Cek koneksi kabel speaker internal',
                        'Ganti speaker laptop jika rusak'
                    ],
                    'description': 'Speaker internal tidak jelas atau tidak mengeluarkan suara, namun audio eksternal normal, menandakan speaker rusak.'
                }
            },
            'R15': {
                'conditions': ['P01', 'P02', 'P05', 'P20', 'P31'],
                'conclusion': {
                    'diagnosis': 'IC Charge Bermasalah',
                    'category': 'hardware',
                    'severity': 'berat',
                    'solutions': [
                        'Cek charger dengan multimeter (19V/19.5V)',
                        'Coba charger lain yang compatible',
                        'Cek port charging apakah longgar/rusak',
                        'Periksa IC charging pada motherboard (perlu teknisi)',
                        'Ganti IC charging atau motherboard',
                        'Jangan paksa charge jika IC sudah rusak (bahaya)'
                    ],
                    'description': 'Indikator mesin dan baterai mati, laptop tidak bisa menyala, speaker distorsi, menandakan IC charge rusak.'
                }
            },
            'R16': {
                'conditions': ['P17', 'P18', 'P20'],
                'conclusion': {
                    'diagnosis': 'Arus Bocor pada jalur Audio',
                    'category': 'hardware',
                    'severity': 'sedang',
                    'solutions': [
                        'Jangan gunakan laptop sambil di-charge saat issue ini terjadi',
                        'Cek grounding laptop (gunakan adaptor 3 pin)',
                        'Periksa jalur audio pada motherboard',
                        'Bawa ke teknisi untuk trace jalur bocor',
                        'Ganti komponen audio yang bocor',
                        'Gunakan audio eksternal via USB sebagai workaround'
                    ],
                    'description': 'Mic tidak berfungsi, speaker kurang jelas dan distorsi, menandakan arus bocor di jalur audio motherboard.'
                }
            },
            'R17': {
                'conditions': ['P32', 'P46', 'P47'],
                'conclusion': {
                    'diagnosis': 'Bootloader Bermasalah',
                    'category': 'software',
                    'severity': 'sedang',
                    'solutions': [
                        'Masuk ke BIOS dan cek boot order',
                        'Repair bootloader dengan Windows installation media',
                        'Gunakan command: bootrec /fixmbr, /fixboot, /rebuildbcd',
                        'Cek harddisk tidak corrupt dengan CHKDSK',
                        'Restore dari system restore point',
                        'Reinstall Windows jika bootloader corrupt parah'
                    ],
                    'description': 'Laptop menyala, muncul logo OS, tapi restart kembali terus menerus, menandakan bootloader atau OS bermasalah.'
                }
            },
            'R18': {
                'conditions': ['P32', 'P46', 'P47', 'P48'],
                'conclusion': {
                    'diagnosis': 'Kesalahan atau kegagalan partisi',
                    'category': 'software',
                    'severity': 'sedang',
                    'solutions': [
                        'Biarkan proses "repairing your drive" selesai (bisa lama)',
                        'Jangan matikan paksa laptop saat repair',
                        'Gunakan CHKDSK /f /r untuk repair bad sectors',
                        'Backup data penting segera setelah bisa masuk Windows',
                        'Gunakan partition manager untuk repair partition table',
                        'Reinstall Windows jika partition corrupt parah'
                    ],
                    'description': 'Muncul peringatan "repairing your drive" dan restart terus, menandakan partisi harddisk bermasalah atau corrupt.'
                }
            },
            'R19': {
                'conditions': ['P06', 'P39', 'P49'],
                'conclusion': {
                    'diagnosis': 'Charger Bermasalah',
                    'category': 'hardware',
                    'severity': 'sedang',
                    'solutions': [
                        'Cek kabel charger apakah ada bagian yang putus',
                        'Test dengan multimeter (harus 19V/19.5V stabil)',
                        'Coba gerakan kabel, jika nyala-mati berarti kabel putus',
                        'Ganti charger baru yang original',
                        'Jangan gunakan charger KW atau tidak sesuai spek',
                        'Cek port charging laptop juga'
                    ],
                    'description': 'Indikator charge mati, laptop mati tiba-tiba, kabel sensitif terhadap gerakan, menandakan charger rusak.'
                }
            },
            'R20': {
                'conditions': ['P20', 'P50'],
                'conclusion': {
                    'diagnosis': 'Arus Bocor Pada Body',
                    'category': 'hardware',
                    'severity': 'berat',
                    'solutions': [
                        'BAHAYA! Segera hentikan pemakaian laptop',
                        'Jangan gunakan laptop sambil di-charge',
                        'Gunakan adaptor 3 pin dengan grounding yang baik',
                        'Cek body laptop apakah ada komponen yang terkelupas',
                        'Bawa ke teknisi SEGERA untuk dicek grounding',
                        'Kemungkinan perlu ganti motherboard atau PSU'
                    ],
                    'description': 'Tangan tersetrum saat menyentuh laptop, speaker distorsi, menandakan arus bocor yang BERBAHAYA pada body laptop.'
                }
            },
            'R21': {
                'conditions': ['P16', 'P52'],
                'conclusion': {
                    'diagnosis': 'Camera Terdisable',
                    'category': 'software',
                    'severity': 'ringan',
                    'solutions': [
                        'Cek Device Manager, pastikan camera enabled',
                        'Cek Privacy Settings → Camera → Allow apps',
                        'Update driver camera',
                        'Cek apakah ada physical switch/button disable camera',
                        'Scan dengan hardware troubleshooter',
                        'Reinstall camera driver'
                    ],
                    'description': 'Camera tidak dapat digunakan namun microphone normal, kemungkinan camera di-disable di system atau privacy settings.'
                }
            },
            'R22': {
                'conditions': ['P17', 'P51', 'P21'],
                'conclusion': {
                    'diagnosis': 'Mic Terdisable',
                    'category': 'software',
                    'severity': 'ringan',
                    'solutions': [
                        'Cek Device Manager, pastikan microphone enabled',
                        'Cek Privacy Settings → Microphone → Allow apps',
                        'Set microphone sebagai default recording device',
                        'Update driver audio',
                        'Test dengan Voice Recorder app',
                        'Reinstall audio driver'
                    ],
                    'description': 'Microphone tidak dapat digunakan namun camera dan speaker normal, kemungkinan mic di-disable atau muted.'
                }
            },
            'R23': {
                'conditions': ['P09', 'P11', 'P12'],
                'conclusion': {
                    'diagnosis': 'Touchpad Terdisable',
                    'category': 'software',
                    'severity': 'ringan',
                    'solutions': [
                        'Tekan kombinasi Fn + F-key untuk enable touchpad',
                        'Cek Settings → Devices → Touchpad',
                        'Cek Device Manager, pastikan touchpad enabled',
                        'Nonaktifkan "Disable touchpad when mouse connected"',
                        'Update driver touchpad',
                        'Restart laptop'
                    ],
                    'description': 'Touchpad tidak berfungsi namun tombol sisi dan mouse eksternal normal, kemungkinan touchpad di-disable.'
                }
            },
            'R24': {
                'conditions': ['P53'],
                'conclusion': {
                    'diagnosis': 'Baterai BIOS',
                    'category': 'hardware',
                    'severity': 'ringan',
                    'solutions': [
                        'Buka casing laptop',
                        'Cari baterai CMOS (coin cell CR2032)',
                        'Lepas dan ganti dengan baterai baru',
                        'Pasang kembali dan setting ulang BIOS',
                        'Set tanggal dan waktu yang benar',
                        'Save BIOS settings'
                    ],
                    'description': 'Jam dan tanggal selalu reset, menandakan baterai CMOS/BIOS sudah habis dan perlu diganti.'
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
    
    def display_knowledge_base_summary(self):
        """Display ringkasan Knowledge Base"""
        print("="*70)
        print("📚 KNOWLEDGE BASE SUMMARY")
        print("="*70)
        print(f"Total Symptoms (Premis): {len(self.symptoms)}")
        print(f"Total Rules (Konklusi): {len(self.rules)}")
        print("\n📝 Sample Symptoms:")
        for code in list(self.symptoms.keys())[:5]:
            print(f"  {code}: {self.symptoms[code]}")
        print(f"  ... dan {len(self.symptoms)-5} symptoms lainnya")
        print("\n🔧 Sample Rules:")
        for rule_id in list(self.rules.keys())[:3]:
            rule = self.rules[rule_id]
            print(f"  {rule_id}: IF {' AND '.join(rule['conditions'])}")
            print(f"       THEN {rule['conclusion']['diagnosis']}")
        print(f"  ... dan {len(self.rules)-3} rules lainnya")
        print("="*70)


# Test initialization
if __name__ == "__main__":
    kb = KnowledgeBase()
    kb.display_knowledge_base_summary()
    print("\n✅ Knowledge Base berhasil diinisialisasi!")
    print(f"✅ Ready dengan {len(kb.symptoms)} symptoms dan {len(kb.rules)} rules")
