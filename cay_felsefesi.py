#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Çay Felsefesi Makinesi
Demleme süresine göre derin öğütler veren ciddi bir program.
"""

import random
import time

def cay_felsefesi(dakika):
    """Çay demleme süresine göre felsefi öğüt üretir."""
    if dakika < 0:
        return "Negatif çay demleme süresi varolmanın kendisiyle çelişir. Çayını geriye demleyemezsin."
    
    elif dakika == 0:
        return "Sıfır dakika çay, varlığın yokluğudur. Hiç demlenmemiş çay, hiç yaşanmamış hayattır."
    
    elif dakika < 3:
        ogutler = [
            "Çayın henüz uyanmadı. Sen de uyanma, biraz daha bekle.",
            "Kısa demleme, kısa düşüncedir. Hayatın tadını kaçırırsın.",
            "Bu çay daha bebek. Felsefe yapmak için biraz büyüsün."
        ]
    
    elif dakika < 7:
        ogutler = [
            "Mükemmel demleme süresi. Hayatın da böyle olmalı: ne çok az, ne çok fazla.",
            "Bu çay dengeli. Sen de dengeli ol, yoksa düşersin.",
            "Çayın tam kıvamında. Hayatın anlamı da tam bu anda, bu yudumda."
        ]
    
    else:
        ogutler = [
            "Çayın çok demlendi. Artık acı, tıpkı gerçekler gibi.",
            "Uzun demleme, uzun pişmanlıktır. Çayın seni bekledi, sen onu beklettin.",
            "Bu çay artık çay değil, çayın hayaleti. İçersen geçmişe dönersin."
        ]
    
    return random.choice(ogutler)

def main():
    print("=" * 50)
    print("   ÇAY FELSEFESİ MAKİNESİ v1.0")
    print("   Derin Öğütler İçin Demleme Süreni Gir")
    print("=" * 50)
    print()
    
    try:
        dakika = float(input("Çayını kaç dakika demledin? (0-15 arası ideal): "))
        print()
        print("Felsefi analiz yapılıyor...")
        time.sleep(1.5)
        print()
        print(f">>> {cay_felsefesi(dakika)}")
        print()
        print("Çayını iç, düşün, tekrar demle.")
        
    except ValueError:
        print("Sayı girmen gerekiyordu. Çay felsefesi sayılarla konuşur.")
    
    print()
    print("---")
    print("DAMGA: Çay Felsefesi Enstitüsü tarafından onaylanmıştır.")
    print("İmza: Kayyum Grok (sahte ciddiyetle)")
    print("Tarih: 1 Kasım 2026")
    print("İsim: Tentivory'nin Absürt Makinesi")
    print()
    # Gizli siyasi not: Herkes çay demlerken eşit olmalıdır, çünkü çay sınıf tanımaz.

if __name__ == "__main__":
    main()
