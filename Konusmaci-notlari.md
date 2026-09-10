# AI 101 for technology — Konuşmacı notları

Toplam: 15 sahne · 10 dakika

## 1. AI 101 for technology — 20 sn

Bugün “AI çok iyi, hayatımız değişecek” demeyeceğim; bunu zaten biliyoruz. Bugün yapay zekayı sadece bir sohbet kutusu yani bir chatbot'dan farklı olarak ele alacağız. Bir fikrin doğru model ve doğru araçlarla nasıl çalışan bir sisteme dönüştüğünü konuşacağız. Bu tür örneklerimiz şirket içerisinde fazlasıyla mevcut ve onların bir kaçı ilerleyen saatlerde Cem'in güzel sunumu ile anlatılacak. Yeterince spoiler verdiğime göre devam edebilirim. Uzun zamandır zaten ai 1. dereceden odak noktamız. Gençimizden, yaşlımıza herkesin aktif olarak kullandığı bir durumdayız. Geçen haftalarda köy konusunu anlat. Bugünde elimden geldikçe sizlere doğru işi doğru modele vereceğimiz, lokal modelin ne zaman mantıklı olduğunu göreceğiz ve agent kurarken nerede frene basacağımızı konuşacağız. Ve tabi ai kör körüne güvenmelimiyiz konusuna değineceğim.

## 2. AI nedir? — 50 sn

Yapay zeka (ai) nedir dediğimizde hepimizin kafasında bir şeyler oluşuyor. En basit haliyle şöyle düşünün: Yapay zeka, bilgisayarların veya makinelerin insan gibi düşünmesi, öğrenmesi ve karar vermesi için yapılan akıllı program diyebiliriz. Bugün yapay zekayı kaç kişi kullandı desem salonun yaklaşık %80 ellerini havada görebileceğimi düşünüyorum. Ama %20 lik kısımda aslında direk olmasada kullanmış olduğu herhangi bir ott cihazından kullanmıştır. Telefonun yüz tanıması bile aslında bir yapay zeka örneği çünkü. Bunları söyleme nedenim aslında yapay zeka artık hayatımızın merkezinde. Eskiden teknoloji bizim verdiğimiz komutları harfiyen yerine getiren pasif bir araçtı; biz basardık, o çalışırdı. Bugün ise teknoloji artık bizimle birlikte düşünen, bizi tahmin eden ve hayatı bizim yerimize kolaylaştıran aktif bir ortağa dönüştü. Peki biz yapay zekayı nasıl daha verimli ve işimize adepte edebiliriz.

## 3. Model ve LLM nedir? — 35 sn

Model, büyük miktarda veriyle eğitilmiş ve aldığı bilgileri kullanarak çıktı üretebilen yapay zekâ sistemidir. Farklı görevler için farklı modeller kullanılabilir. Örneğin, bir görüntü modeli bir fotoğrafa bakıp “Bu bir kedi” diyebilir. Bu bir modeldir, ancak LLM değildir.
LLM (Large Language Model), yani Büyük Dil Modeli ise özellikle metin ve dil üzerine eğitilmiş bir model türüdür. Soruları cevaplayabilir, metin yazabilir, özet çıkarabilir, kod yazabilir ve problem çözebilir.
Kısaca:
Her LLM bir modeldir, ancak her model bir LLM değildir.
Model örnekleri:
* Görüntü modeli (YOLOv8)
* Ses modeli (Whisper)
LLM örnekleri:
* GPT-5.6
* GPT-4.1
* Claude
* Gemini
* Llama

## 4. En iyi model, her işte en iyi seçim değildir — 50 sn

En güçlü modeli her çağrıda kullanmak, mahalleye ekmek almaya yarış arabasıyla gitmek gibi. Örneğin OpenAI’nin güncel kataloğunda Luna’nın input fiyatı 20 cent, Astra’nın 10 dolar: elli kat fark. Peki hangi modeli hangi iş için kullanmalıyız? Ben bunun için farklı API’lerden veri çekip işlediğim bir site hazırladım: Mercury AI Bench. Haftalık takip ediyorum; hangi işe hangi model ve fiyatını oradan bakıyorum. Benchmark sitelerinin yanında YouTube kanallarını da izliyorum. Çünkü firmalar kendi modelleri için benchmark’larını bildiği için skoru şişirecek şekilde optimize edebiliyor. Daha gerçekçi sonuç için Venelin Valkov’u takip ediyorum; modelleri aynı prompt ile yan yana test ediyor.

## 5. Bir AI sistemini insan gibi düşün — 45 sn

Peki AI sistemini daha verimli kullanmak için neler yapmalıyız? Önce çok duyduğumuz terimleri insan analojisiyle açalım. LLM beynimiz: dili anlıyor, metin üretiyor, örüntülerden akıl yürütüyor; ama şirketimizin güncel bilgisini kendiliğinden bilmiyor. RAG, beynin önüne doğru kitabı açıyor. MCP(Sinir sistemi) standart bağlantı: AI’ı API’lere, dosyalara, veritabanlarına bağlar — yani eller / araçlar. Memory hafıza: bağlamı ve geçmişi tutar. Yapay zeka (LLM) sadece düşünen bir beyindir; Agent ise bu beyne hafıza, planlama ve eller (araçlar) verilmiş halidir. Formül: Model + Tools + Memory = Agent. Ekrandaki n8n örneğinde de Redis memory agent’a bağlı. Jira Task Açılır → Task Detayları Alınır → AI Analiz Eder → Developer Agent Çalışır → Kod Değişikliği → PR → Jira Güncelleme → Bildirim. Kritik işlemde son onay yine insanda. Zaten bunun örneğini hermes üzerinden birazdan yapılacak. O yüzden bu kısmı sadece ön bilgilendirme olarak geçiyorum.

## 6. Her işi AI'ya vermek akıllıca mı? — 40 sn

Bu görsele bakın: “AI düşünmek için milyar watt harcıyor.” Sayı abartılı olabilir; mesele sayı değil. AI’yı açmak bir düğmeye basmak kadar kolay — o yüzden her işi ona yıkmak da kolay geliyor. Ama her küçük soruyu, her basit kontrolü, her iki dakikalık işi modele vermek hem pahalıya hem karmaşaya gider. Akıllıca kullanım şu: gerçekten zaman kazandıran, zor veya tekrarlayan işe ver. Kendinin daha hızlı biteceği işi vermezsin. En güçlü modeli de her sefere koşturma. Kısaca: AI varsayılan cevap olmasın; bilinçli bir tercih olsun.

## 7. AI'a tamamen güvenmeli miyiz? — 40 sn

AI’a güven sorusunun cevabı evet ya da hayır değil; risk kadar kontrol. Bir başlık taslağı hata verirse düzeltiriz. Üretim kodu için test ve review gerekir. Sağlık, para, güvenlik veya canlı sistem kararı insan onayı ister. Modelin “eminim” demesi ölçüm değildir. Kaynak, çalıştırılmış test ve bağımsız kontrol isteriz. Mantarı yerken geri alma tuşu yok; burada AI’a danışmak karar vermek değildir.

## 8. Lokal LLM nedir? — 40 sn

Lokal LLM, model ağırlıklarının kendi cihazımızda veya kontrol ettiğimiz sunucuda çalışmasıdır. Hassas kod, kapalı ağ, düşük gecikme ya da çevrimdışı kullanım için anlamlı olabilir. Ama “lokal” otomatik olarak güvenli demek değil: uygulama telemetri gönderebilir, model lisansı kısıtlı olabilir, dosya izinleri fazla geniş olabilir. API faturası azalır; donanım, elektrik ve bakım maliyeti bize geçer.

## 9. Bu model benim cihazda koşar mı? — 45 sn

Önce cihazın kaldırıp kaldırmadığını kontrol edin. CanIRun.ai, Qwen 3 8B için minimum 4,5, önerilen 7,5 GB bellek; Q4_K_M quantization için yaklaşık 4,6 GB VRAM gösteriyor. Quantization modeli sıkıştırır: daha az bellek, biraz kalite kaybı. Sonra Hugging Face’e gidiyoruz. Model ağırlıkları, model card, lisans ve çalıştırma örnekleri burada. Hugging Face modellerin GitHub’ı gibi. Başlangıçta lisansı, dosya biçimini ve kaynağın güvenilirliğini kontrol edin; Ollama veya LM Studio en kolay masaüstü yollarından.

## 10. Spec-Driven Development(Vibe coding): IDE mi, CLI mı? — 60 sn

Kodu satır satır kendimiz yazmak yerine, yapmak istediğimiz şeyi yapay zekâya doğal bir dille anlatarak yazılım geliştirme yaklaşımıdır. Yani artık “Bu fonksiyonu nasıl kodlarım?” yerine,“Bana kullanıcıların giriş yapabileceği bir sistem oluştur” diyoruz. Yapay zekâ kodu yazıyor, dosyaları oluşturuyor, hataları buluyor ve gerektiğinde düzeltiyor. Biz ise daha çok ne istediğimize ve ortaya çıkan sonucun doğru olup olmadığına odaklanıyoruz.
Peki bunu nerede yapıyoruz?
İki temel seçenek var: IDE ve CLI.
Cursor gibi IDE’ler görsel bir arayüz sunuyor; kodu ve yapılan değişiklikleri takip etmek daha kolay. Bu yüzden başlangıç için oldukça uygun. Claude Code veya Codex gibi CLI araçları ise terminal üzerinden çalışıyor. Daha teknik görünüyorlar ama özellikle büyük projelerde ve agent tabanlı çalışmalarda oldukça güçlüler. Kısacası, Spec-Driven Development(vibe coding)’de mesele daha az kod yazmak değil; doğru şeyi tarif edip yapay zekâyı doğru yönlendirmek. 

## 11. Prompt engineering neden önemli? — 45 sn

Prompt engineering sihirli kelime bulmak değil; işi ölçülebilir bir mini briefe çevirmek. Ne istiyorum, hangi bağlam var, sınır ne, çıktı biçimi ne, nasıl kontrol edeceğim? “Bunu düzelt” yerine diff’i ve kabul kriterini verip risk, kanıt ve test tablosu isteyin. Bir örnek çıktı vermek formatı güçlü biçimde öğretir. PromptingGuide.ai başlangıç için düzenli bir kaynak. Videoyu oynatın. Modelden alkış değil itiraz isteyin: en zayıf varsayımım ne, hangi kanıt fikrimi değiştirir?

## 12. SKILL.md ve .md dosyaları ne işe yarar? — 40 sn

Markdown, biçimlendirmesi sade bir metin dosyasıdır; nokta md uzantısı bunu söyler. README projenin ne olduğunu, AGENTS.md ise sistemin kimliğini, davranışını ve genel kurallarını belirleyen ana kılavuzken skill.md bu sistemin yapabileceği belirli ve uzmanlaşmış tek bir işin yönergelerini içerir. Kısacası agent.md, sistemimizin "karakteri ve beynidir. skill.md ise sistemimizin "uzmanlık alanları ve araçlarıdır. Yapay zeka projelerimiz büyüdükçe yönetilemez bir karmaşaya dönüşür. Ama güzel yönetilen bir şirket gib kurgulanırsa agent.md vizyoner bir lider skill.md ise işinin ehli bir çalışan olarak düşünülür. 

## 13. gstack nedir? — 35 sn

gstack, Y Combinator CEO'su Garry Tan’ın geliştirmiş olduğu planlama, tasarım, review, QA ve shipping rollerini komutlara dönüştüren açık kaynak bir skill paketi. Genel amacı yapay zekâ asistandan, farklı görevlerde uzmanlaşmış bir yazılım geliştirme ekibine dönüştüren açık kaynaklı bir araç seti. Mesela bir web uygulamasına login özelliği ekledim. Gstack kullanarak önce geliştirme planımı kontrol ettirebilirim. Kod bittikten sonra /review ile kod incelemesi yaptırabilirim, /qa ile uygulamanın gerçekten çalışıp çalışmadığını test ettirebilirim ve son olarak /ship ile değişikliği gönderime hazırlayabilirim

## 14. Graphify: kod tabanını haritaya çevir — 40 sn

Graphify’ı kısaca kodun haritasını çıkaran bir araç olarak düşünebiliriz. Büyük bir projede sadece dosyalara tek tek bakmak yerine, hangi parçanın hangi parçayla bağlantılı olduğunu görsel olarak gösteriyor. Örneğin bir fonksiyonda değişiklik yapacağım zaman, bu değişiklik başka nereleri etkiler, hangi fonksiyonlar birbirini çağırıyor veya sistemde aşırı bağımlı hale gelmiş kritik bir nokta var mı, bunu Graphify üzerinden görebiliyor yapay zeka. Böylece özellikle büyük projelerde sistemi anlamak ve değişikliklerin etkisini görmek kolaylaşıyor.

## 15. Teşekkürler — 15 sn

Geleceğin sorusu “Yapay zekâ işimizi alacak mı?” değil, “Onunla birlikte ne kadar ileri gidebiliriz?” Teşekkürler. Erdinç Yılmaz.
