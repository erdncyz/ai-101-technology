# AI 101 for technology — Konuşmacı notları

Toplam: 16 sahne · 10 dakika

## 1. AI 101 for technology — 20 sn

Bugün “AI çok iyi, hayatımız değişecek” demeyeceğim; bunu zaten biliyoruz. On dakika sonunda dört terimi ayıracağız, doğru işi doğru modele vereceğiz, lokal modelin ne zaman mantıklı olduğunu göreceğiz ve agent kurarken nerede frene basacağımızı konuşacağız. Bir de mantara güvenip güvenmeyeceğimizi çözeceğiz. T ile sayacı başlat.

## 2. AI nedir? — 30 sn

AI’ı en basit haliyle şöyle düşünün: geçmiş örneklerde hangi girdinin hangi sonuçla eşleştiğini inceler ve kalıbı öğrenir. Yeni bir mesaj geldiğinde, “bu daha önce gördüklerimden hangisine benziyor?” diye tahmin üretir. Örneğin “ekran siyah, maç yok” mesajını yayın sorunu olarak sınıflandırabilir. Klasik AI bir sınıf veya sayı tahmin eder. Üretken AI ise aynı olasılık mantığıyla sıradaki kelimeleri, pikselleri ya da kodu üretir. Buradaki kritik kelime tahmin: yüzde doksan iki, yüzde yüz gerçek demek değildir.

## 3. Bir AI sistemini insan gibi düşün — 40 sn

Bu dört kavramı bir insan analojisiyle düşünelim. LLM beynimiz: dili anlıyor, metin üretiyor ve örüntüler üzerinden akıl yürütüyor. Fakat şirketimizin güncel bilgisini kendiliğinden bilmiyor. RAG, beynin önüne doğru kitabı açıyor; soruyla ilgili belgeyi bulup modele veriyor. MCP standart bağlantı noktası: AI uygulamasını API’lere, dosyalara, veritabanlarına ve servislere ortak bir yöntemle bağlıyor. Agent ise beyin ve eller birlikte: hedefe ulaşmak için hangi adımı atacağını seçiyor, araç kullanıyor, sonucu görüp devam ediyor. Digiturk örneği: LLM yanıtı yazar, RAG güncel paket belgesini getirir, MCP izinli sistemlere bağlanır, agent bilgileri toplayıp yapılacak işi takip eder. Kritik işlem varsa son onay yine insanda kalır. Bunlar birbirinin alternatifi değil; aynı sistemin katmanları.

## 4. Model ve product arasındaki fark nedir? — 35 sn

Model ve product kelimelerini ayıralım. Model arabanın engine’i: dil, reasoning, vision ve code yeteneğini sağlar. Product ise kullandığımız arabanın tamamı; UI, model, tools, verilen context, memory, permissions ve guardrails birlikte çalışır. Bu yüzden aynı model bir chat product içinde yalnızca yanıt yazarken, bir coding agent içinde dosya okuyabilir, terminal kullanabilir ve test çalıştırabilir. “Hangi AI’ı kullanalım?” sorusunda yalnızca model adına bakmayın. Önce hangi product deneyimini ve hangi tools ile guardrails’i istediğinizi belirleyin.

## 5. En iyi model, her işte en iyi seçim değildir — 45 sn

En güçlü modeli her çağrıda kullanmak, mahalleye ekmek almaya yarış arabasıyla gitmek gibi. OpenAI’nin güncel kataloğunda Luna’nın input fiyatı 20 cent, Astra’nın 10 dolar: elli kat fark. Basit sınıflandırma ve çıkarımda küçük model; çoğu RAG ve günlük kod işinde dengeli model; zor agent döngülerinde güçlü model. Arama için ayrıca web arama aracı gerekir. Bunlar API liste fiyatları; gerçek maliyet çıktı uzunluğu, cache, araç çağrısı ve tekrar sayısına bağlı. Doğru seçim için kendi işimizden 20-50 örnekle kalite, gecikme ve maliyeti birlikte ölçeriz.

## 6. Her işi AI'ya vermek akıllıca mı? — 40 sn

Bu görsele bakın: “AI düşünmek için milyar watt harcıyor.” Sayı abartılı olabilir; mesele sayı değil. AI’yı açmak bir düğmeye basmak kadar kolay — o yüzden her işi ona yıkmak da kolay geliyor. Ama her küçük soruyu, her basit kontrolü, her iki dakikalık işi modele vermek hem pahalıya hem karmaşaya gider. Akıllıca kullanım şu: gerçekten zaman kazandıran, zor veya tekrarlayan işe ver. Kendinin daha hızlı biteceği işi vermezsin. En güçlü modeli de her sefere koşturma. Kısaca: AI varsayılan cevap olmasın; bilinçli bir tercih olsun.

## 7. AI'a tamamen güvenmeli miyiz? — 40 sn

AI’a güven sorusunun cevabı evet ya da hayır değil; risk kadar kontrol. Bir başlık taslağı hata verirse düzeltiriz. Üretim kodu için test ve review gerekir. Sağlık, para, güvenlik veya canlı sistem kararı insan onayı ister. Modelin “eminim” demesi ölçüm değildir. Kaynak, çalıştırılmış test ve bağımsız kontrol isteriz. Mantarı yerken geri alma tuşu yok; burada AI’a danışmak karar vermek değildir.

## 8. Lokal LLM nedir? — 40 sn

Lokal LLM, model ağırlıklarının kendi cihazımızda veya kontrol ettiğimiz sunucuda çalışmasıdır. Hassas kod, kapalı ağ, düşük gecikme ya da çevrimdışı kullanım için anlamlı olabilir. Ama “lokal” otomatik olarak güvenli demek değil: uygulama telemetri gönderebilir, model lisansı kısıtlı olabilir, dosya izinleri fazla geniş olabilir. API faturası azalır; donanım, elektrik ve bakım maliyeti bize geçer.

## 9. Bu model benim cihazda koşar mı? — 45 sn

Önce cihazın kaldırıp kaldırmadığını kontrol edin. CanIRun.ai, Qwen 3 8B için minimum 4,5, önerilen 7,5 GB bellek; Q4_K_M quantization için yaklaşık 4,6 GB VRAM gösteriyor. Quantization modeli sıkıştırır: daha az bellek, biraz kalite kaybı. Sonra Hugging Face’e gidiyoruz. Model ağırlıkları, model card, lisans ve çalıştırma örnekleri burada. Hugging Face modellerin GitHub’ı gibi. Başlangıçta lisansı, dosya biçimini ve kaynağın güvenilirliğini kontrol edin; Ollama veya LM Studio en kolay masaüstü yollarından.

## 10. Vibe coding: IDE mi, CLI mı? — 40 sn

Vibe coding doğal dille hızlı yazılım üretmek. IDE; satır içi öneri, görsel diff ve küçük değişikliklerde daha kontrollü. CLI agent; repo çapında arama, test ve uzun görevlerde güçlü. En iyi seçim ya o ya bu değil: fikir ve küçük edit IDE’de, tekrarlı veya repo çapındaki işi CLI’da yürütüp sonucu yine IDE’de inceleyebilirsiniz. Dört fren: küçük commit, test, diff review ve gizli bilgiyi bağlama vermemek.

## 11. Agent nedir, neden kurulur? — 45 sn

Agent, hedef için araç kullanan ve aldığı sonuca göre sonraki adımı seçen sistem. Neden kurarız? İş çok adımlıysa, kurallar kırılgansa ve doküman gibi yapılandırılmamış veriyi yorumlamak gerekiyorsa. En kolay başlangıç, hazır bir coding agent veya agent builder içinde tek agent kurmak: bir model, iki üç iyi tanımlı araç, açık talimat, maksimum adım ve insan onayı. İlk günden agentlar ordusu kurmayın. Örneğin Digiturk’te bir incident özet agentı logları ve runbook’u okur, taslak çıkarır; prod aksiyonunu insan onaylar.

## 12. Prompt engineering neden önemli? — 45 sn

Prompt engineering sihirli kelime bulmak değil; işi ölçülebilir bir mini briefe çevirmek. Ne istiyorum, hangi bağlam var, sınır ne, çıktı biçimi ne, nasıl kontrol edeceğim? “Bunu düzelt” yerine diff’i ve kabul kriterini verip risk, kanıt ve test tablosu isteyin. Bir örnek çıktı vermek formatı güçlü biçimde öğretir. PromptingGuide.ai başlangıç için düzenli bir kaynak. Videoyu oynatın. Modelden alkış değil itiraz isteyin: en zayıf varsayımım ne, hangi kanıt fikrimi değiştirir?

## 13. SKILL.md ve .md dosyaları ne işe yarar? — 40 sn

Markdown, biçimlendirmesi sade bir metin dosyasıdır; nokta md uzantısı bunu söyler. README projenin ne olduğunu, AGENTS.md agentın bu repoda hangi kurallarla çalışacağını anlatabilir. SKILL.md ise tekrar eden bir işi yapma kılavuzudur: skillin adı ve ne zaman devreye gireceği üst bölümde, izlenecek adımlar aşağıdadır; yanında script, referans ve şablon da bulunabilir. Yani skill modeli daha zeki yapmaz; deneyimli bir ekip arkadaşının playbook’unu önüne koyar. En güvenilir başlangıç Agent Skills açık standardı ile OpenAI ve Anthropic’in güncel resmî depolarıdır. skills.sh keşif için yararlı bir topluluk dizinidir; indirme sayısı güvenlik garantisi değildir. Skill çalıştırılabilir scriptlere ve araçlara yön verebildiği için kod gibi inceleyin: yayıncıyı, SKILL.md içeriğini, scriptleri, istediği izinleri ve sabitlediğiniz sürümü kontrol edin.

## 14. gstack nedir? — 35 sn

gstack, Garry Tan’ın kullandığı planlama, tasarım, review, QA ve shipping rollerini komutlara dönüştüren açık kaynak bir skill paketi. Değeri modelden çok süreçte: fikri CEO gözüyle sorgula, planı mühendislik açısından incele, kodu review et, staging’i QA et. Yani tek bir uzun prompt yerine tekrarlanabilir kalite kapıları. Kurmadan önce açık kaynak olsa bile setup scriptini okuyun, sürümü sabitleyin ve ekip politikanıza göre uyarlayın.

## 15. Graphify: kod tabanını haritaya çevir — 40 sn

Graphify, kodu fonksiyon, sınıf, import ve çağrı ilişkilerinden bir bilgi grafiğine dönüştürüyor. AI “billing’i kim kullanıyor?” sorusunda her dosyayı yeniden tahmin etmek yerine gerçek yolları izleyebiliyor. Site, parsing’in cihazda çalıştığını, telemetri olmadığını ve çekirdek aracın Apache 2.0 olduğunu söylüyor. Güvenlik sorunu çıkarmaz diyemeyiz: kurduğumuz paket bir supply-chain bileşeni, graph.json mimari bilgi içerir ve seçtiğimiz model sağlayıcısına sorgu gidebilir. Sürümü sabitleyin, kaynağı inceleyin, graph dosyalarını repoya yanlışlıkla commit etmeyin ve MCP yetkisini sınırlandırın.

## 16. Pazartesi hangi AI işini kuruyoruz? — 20 sn

Pazartesi bir pilot seçin: arşivde sahne bulma, incident özeti ya da PR risk analizi. Önce mevcut süreyi ve hata oranını ölçün. Sonra küçük bir modelle başlayıp kalite yetmezse yukarı çıkın. İzinli bağlam verin, çıktı için kaynak veya test isteyin, kritik aksiyonu insan onayına bağlayın. Başarı yalnızca etkileyici demo değil: kalite, gecikme, maliyet ve güvenlik birlikte. Teşekkürler.

