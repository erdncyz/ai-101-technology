# AI 101 for technology — Kullanım

15 sahne, ~10 dakikalık plan. Statik site; Netlify’de build yok.

## Netlify

1. Bu klasörü GitHub’a push et (veya Netlify Drop ile sürükle).
2. Netlify’de **Publish directory** = `.` (veya `netlify.toml` otomatik okunur).
3. Deploy sonrası URL: `https://<site>.netlify.app`

CLI ile:

```bash
npx netlify deploy --prod --dir=.
```

## Yerel

`index.html` dosyasını tarayıcıda çift tıklayarak açabilirsin. Konuşmacı notları `notes.js` içinde de durur; sunucu şart değil.

Canlı düzenleme için (markdown’ı kaydedip yenilemek):

```bash
npx serve .
```

Konuşmacı metinleri `Konusmaci-notlari.md` dosyasındandır (`## N. Başlık — X sn`). HTTP ile açınca bu dosya okunur; `file://` veya önizlemede gömülü kopya kullanılır.
## Projeksiyon + laptop (önerilen)

macOS’ta ekranları **Aynalama değil, Genişlet** yap.

**Diğer ekran siyah olmasın diye (önemli):**  
Sistem Ayarları → Masaüstü ve Dock → **Ekranların ayrı Spaces’leri var** → **Açık**  
(Değişince çıkış yapıp tekrar girmen gerekebilir.)

1. Sunumu aç → `N` ile not penceresini laptop’a al.
2. Ana sunum penceresini projeksiyona sürükle.
3. `F` → tarayıcı barı kaybolur, tam ekran.
4. Oklarla ilerle. Çıkış: `F` veya `Esc`.

Pop-up engellenirse tarayıcıda izin ver. Yedek not paneli: `P`.

## Kontroller

- Oklar / boşluk: ilerle
- F: tam ekran
- G: sahne seçici
- P: konuşmacı not paneli
- N: notları ayrı pencereye aç (2. ekran)
- T: sayaç

12. sahnedeki kısa videoyu elle oynatın. Zoom/Teams paylaşımında yalnızca ana sunum penceresini seç.

Model fiyatları ve çevrimiçi kaynaklar 8 Eylül 2026 tarihinde kontrol edilmiştir. Fiyatlar değişebilir. CanIRun.ai kartı erişilen sayfa verilerinden sadeleştirilmiştir. Graphify sahnesi sitenin kendi FastAPI graph ekran görüntüsünü kullanır; internet yoksa temsili lokal grafik görünür.
