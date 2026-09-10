#!/usr/bin/env python3
"""Build AI 101 for technology as a 16:9 PowerPoint deck."""

from pathlib import Path

from PIL import Image as PILImage
from PIL import ImageDraw, ImageFilter
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
OUT = ROOT / "AI-101-for-technology.pptx"

W, H = 13.333, 7.5
BG = RGBColor(0x09, 0x09, 0x0B)
INK = RGBColor(0xF5, 0xF3, 0xEE)
MUTED = RGBColor(0xA1, 0xA1, 0xA7)
ORANGE = RGBColor(0xFF, 0x77, 0x4D)
CARD = RGBColor(0x14, 0x14, 0x18)
CARD2 = RGBColor(0x1A, 0x1A, 0x1F)
LINE = RGBColor(0x3A, 0x3A, 0x40)
GREEN = RGBColor(0x9B, 0xD5, 0xAD)
FONT = "Calibri"
MONO = "Consolas"

NOTES = [
    "Bugün “AI çok iyi, hayatımız değişecek” demeyeceğim; bunu zaten biliyoruz. Bugün yapay zekayı sadece bir sohbet kutusu yani bir chatbot'dan farklı olarak ele alacağız. Bir fikrin doğru model ve doğru araçlarla nasıl çalışan bir sisteme dönüştüğünü konuşacağız. Bu tür örneklerimiz şirket içerisinde fazlasıyla mevcut ve onların bir kaçı ilerleyen saatlerde Cem'in güzel sunumu ile anlatılacak. Yeterince spoiler verdiğime göre devam edebilirim. Uzun zamandır zaten ai 1. dereceden odak noktamız. Gençimizden, yaşlımıza herkesin aktif olarak kullandığı bir durumdayız. Geçen haftalarda köy konusunu anlat. Bugün de elimden geldikçe sizlere doğru işi doğru modele vereceğimiz, lokal modelin ne zaman mantıklı olduğunu göreceğiz ve agent kurarken nerede frene basacağımızı konuşacağız. Ve tabi ai kör körüne güvenmeli miyiz konusuna değineceğim.",
    "Yapay zeka (ai) nedir dediğimizde hepimizin kafasında bir şeyler oluşuyor. En basit haliyle şöyle düşünün: Yapay zeka, bilgisayarların veya makinelerin insan gibi düşünmesi, öğrenmesi ve karar vermesi için yapılan akıllı program diyebiliriz. Bugün yapay zekayı kaç kişi kullandı desem salonun yaklaşık %80 ellerini havada görebileceğimi düşünüyorum. Ama %20 lik kısımda aslında direk olmasada kullanmış olduğu herhangi bir ott cihazından kullanmıştır. Telefonun yüz tanıması bile aslında bir yapay zeka örneği çünkü. Bunları söyleme nedenim aslında yapay zeka artık hayatımızın merkezinde. Eskiden teknoloji bizim verdiğimiz komutları harfiyen yerine getiren pasif bir araçtı; biz basardık, o çalışırdı. Bugün ise teknoloji artık bizimle birlikte düşünen, bizi tahmin eden ve hayatı bizim yerimize kolaylaştıran aktif bir ortağa dönüştü. Peki biz yapay zekayı nasıl daha verimli ve işimize adepte edebiliriz.",
    "Model, büyük miktarda veriyle eğitilmiş ve aldığı bilgileri kullanarak çıktı üretebilen yapay zekâ sistemidir. Farklı görevler için farklı modeller kullanılabilir. Örneğin, bir görüntü modeli bir fotoğrafa bakıp “Bu bir kedi” diyebilir. Bu bir modeldir, ancak LLM değildir.\nLLM (Large Language Model), yani Büyük Dil Modeli ise özellikle metin ve dil üzerine eğitilmiş bir model türüdür. Soruları cevaplayabilir, metin yazabilir, özet çıkarabilir, kod yazabilir ve problem çözebilir.\nKısaca: Her LLM bir modeldir, ancak her model bir LLM değildir.\nModel örnekleri: Görüntü modeli (YOLOv8), Ses modeli (Whisper).\nLLM örnekleri: GPT-5.6, GPT-4.1, Claude, Gemini, Llama.",
    "En güçlü modeli her çağrıda kullanmak, mahalleye ekmek almaya yarış arabasıyla gitmek gibi. Örneğin OpenAI’nin güncel kataloğunda Luna’nın input fiyatı 20 cent, Astra’nın 10 dolar: elli kat fark. Peki hangi modeli hangi iş için kullanmalıyız? Ben bunun için farklı API’lerden veri çekip işlediğim bir site hazırladım: Mercury AI Bench. Haftalık takip ediyorum; hangi işe hangi model ve fiyatını oradan bakıyorum. Benchmark sitelerinin yanında YouTube kanallarını da izliyorum. Çünkü firmalar kendi modelleri için benchmark’larını bildiği için skoru şişirecek şekilde optimize edebiliyor. Daha gerçekçi sonuç için Venelin Valkov’u takip ediyorum; modelleri aynı prompt ile yan yana test ediyor.",
    "Peki AI sistemini daha verimli kullanmak için neler yapmalıyız? Önce çok duyduğumuz terimleri insan analojisiyle açalım. LLM beynimiz: dili anlıyor, metin üretiyor, örüntülerden akıl yürütüyor; ama şirketimizin güncel bilgisini kendiliğinden bilmiyor. RAG, beynin önüne doğru kitabı açıyor. MCP (sinir sistemi) standart bağlantı: AI’ı API’lere, dosyalara, veritabanlarına bağlar — yani eller / araçlar. Memory hafıza: bağlamı ve geçmişi tutar. Yapay zeka (LLM) sadece düşünen bir beyindir; Agent ise bu beyne hafıza, planlama ve eller (araçlar) verilmiş halidir. Formül: Model + Tools + Memory = Agent. Ekrandaki n8n örneğinde de Redis memory agent’a bağlı. Jira Task Açılır → Task Detayları Alınır → AI Analiz Eder → Developer Agent Çalışır → Kod Değişikliği → PR → Jira Güncelleme → Bildirim. Kritik işlemde son onay yine insanda. Zaten bunun örneğini hermes üzerinden birazdan yapılacak. O yüzden bu kısmı sadece ön bilgilendirme olarak geçiyorum.",
    "Bu görsele bakın: “AI düşünmek için milyar watt harcıyor.” Sayı abartılı olabilir; mesele sayı değil. AI’yı açmak bir düğmeye basmak kadar kolay — o yüzden her işi ona yıkmak da kolay geliyor. Ama her küçük soruyu, her basit kontrolü, her iki dakikalık işi modele vermek hem pahalıya hem karmaşaya gider. Akıllıca kullanım şu: gerçekten zaman kazandıran, zor veya tekrarlayan işe ver. Kendinin daha hızlı biteceği işi vermezsin. En güçlü modeli de her sefere koşturma. Kısaca: AI varsayılan cevap olmasın; bilinçli bir tercih olsun.",
    "AI’a güven sorusunun cevabı evet ya da hayır değil; risk kadar kontrol. Bir başlık taslağı hata verirse düzeltiriz. Üretim kodu için test ve review gerekir. Sağlık, para, güvenlik veya canlı sistem kararı insan onayı ister. Modelin “eminim” demesi ölçüm değildir. Kaynak, çalıştırılmış test ve bağımsız kontrol isteriz. Mantarı yerken geri alma tuşu yok; burada AI’a danışmak karar vermek değildir.",
    "Lokal LLM, model ağırlıklarının kendi cihazımızda veya kontrol ettiğimiz sunucuda çalışmasıdır. Hassas kod, kapalı ağ, düşük gecikme ya da çevrimdışı kullanım için anlamlı olabilir. Ama “lokal” otomatik olarak güvenli demek değil: uygulama telemetri gönderebilir, model lisansı kısıtlı olabilir, dosya izinleri fazla geniş olabilir. API faturası azalır; donanım, elektrik ve bakım maliyeti bize geçer.",
    "Önce cihazın kaldırıp kaldırmadığını kontrol edin. CanIRun.ai, Qwen 3 8B için minimum 4,5, önerilen 7,5 GB bellek; Q4_K_M quantization için yaklaşık 4,6 GB VRAM gösteriyor. Quantization modeli sıkıştırır: daha az bellek, biraz kalite kaybı. Sonra Hugging Face’e gidiyoruz. Model ağırlıkları, model card, lisans ve çalıştırma örnekleri burada. Hugging Face modellerin GitHub’ı gibi. Başlangıçta lisansı, dosya biçimini ve kaynağın güvenilirliğini kontrol edin; Ollama veya LM Studio en kolay masaüstü yollarından.",
    "Kodu satır satır kendimiz yazmak yerine, yapmak istediğimiz şeyi yapay zekâya doğal bir dille anlatarak yazılım geliştirme yaklaşımıdır. Yani artık “Bu fonksiyonu nasıl kodlarım?” yerine, “Bana kullanıcıların giriş yapabileceği bir sistem oluştur” diyoruz. Yapay zekâ kodu yazıyor, dosyaları oluşturuyor, hataları buluyor ve gerektiğinde düzeltiyor. Biz ise daha çok ne istediğimize ve ortaya çıkan sonucun doğru olup olmadığına odaklanıyoruz.\nPeki bunu nerede yapıyoruz?\nİki temel seçenek var: IDE ve CLI.\nCursor gibi IDE’ler görsel bir arayüz sunuyor; kodu ve yapılan değişiklikleri takip etmek daha kolay. Bu yüzden başlangıç için oldukça uygun. Claude Code veya Codex gibi CLI araçları ise terminal üzerinden çalışıyor. Daha teknik görünüyorlar ama özellikle büyük projelerde ve agent tabanlı çalışmalarda oldukça güçlüler. Kısacası, Spec-Driven Development (vibe coding)’de mesele daha az kod yazmak değil; doğru şeyi tarif edip yapay zekâyı doğru yönlendirmek.",
    "Prompt engineering sihirli kelime bulmak değil; işi ölçülebilir bir mini briefe çevirmek. Ne istiyorum, hangi bağlam var, sınır ne, çıktı biçimi ne, nasıl kontrol edeceğim? “Bunu düzelt” yerine diff’i ve kabul kriterini verip risk, kanıt ve test tablosu isteyin. Bir örnek çıktı vermek formatı güçlü biçimde öğretir. PromptingGuide.ai başlangıç için düzenli bir kaynak. Modelden alkış değil itiraz isteyin: en zayıf varsayımım ne, hangi kanıt fikrimi değiştirir?",
    "Markdown, biçimlendirmesi sade bir metin dosyasıdır; nokta md uzantısı bunu söyler. README projenin ne olduğunu, AGENTS.md ise sistemin kimliğini, davranışını ve genel kurallarını belirleyen ana kılavuzken skill.md bu sistemin yapabileceği belirli ve uzmanlaşmış tek bir işin yönergelerini içerir. Kısacası AGENTS.md, sistemimizin karakteri ve beynidir. SKILL.md ise sistemimizin uzmanlık alanları ve araçlarıdır. Yapay zeka projelerimiz büyüdükçe yönetilemez bir karmaşaya dönüşür. Ama güzel yönetilen bir şirket gibi kurgulanırsa AGENTS.md vizyoner bir lider, SKILL.md ise işinin ehli bir çalışan olarak düşünülür.",
    "gstack, Y Combinator CEO'su Garry Tan’ın geliştirmiş olduğu planlama, tasarım, review, QA ve shipping rollerini komutlara dönüştüren açık kaynak bir skill paketi. Genel amacı yapay zekâ asistandan, farklı görevlerde uzmanlaşmış bir yazılım geliştirme ekibine dönüştüren açık kaynaklı bir araç seti. Mesela bir web uygulamasına login özelliği ekledim. Gstack kullanarak önce geliştirme planımı kontrol ettirebilirim. Kod bittikten sonra /review ile kod incelemesi yaptırabilirim, /qa ile uygulamanın gerçekten çalışıp çalışmadığını test ettirebilirim ve son olarak /ship ile değişikliği gönderime hazırlayabilirim.",
    "Graphify’ı kısaca kodun haritasını çıkaran bir araç olarak düşünebiliriz. Büyük bir projede sadece dosyalara tek tek bakmak yerine, hangi parçanın hangi parçayla bağlantılı olduğunu görsel olarak gösteriyor. Örneğin bir fonksiyonda değişiklik yapacağım zaman, bu değişiklik başka nereleri etkiler, hangi fonksiyonlar birbirini çağırıyor veya sistemde aşırı bağımlı hale gelmiş kritik bir nokta var mı, bunu Graphify üzerinden görebiliyor yapay zeka. Böylece özellikle büyük projelerde sistemi anlamak ve değişikliklerin etkisini görmek kolaylaşıyor.",
    "Geleceğin sorusu “Yapay zekâ işimizi alacak mı?” değil, “Onunla birlikte ne kadar ileri gidebiliriz?” Teşekkürler. Erdinç Yılmaz.",
]


def _no_line(shape):
    shape.line.fill.background()


def _fill(shape, color):
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    _no_line(shape)


def _tf(shape, margin=0.06):
    tf = shape.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    tf.margin_left = Inches(margin)
    tf.margin_right = Inches(margin)
    tf.margin_top = Inches(margin * 0.7)
    tf.margin_bottom = Inches(margin * 0.5)
    return tf


def _run(p, text, size, color, bold=False, font=FONT, italic=False):
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    run.font.name = font
    rpr = run._r.get_or_add_rPr()
    ea = rpr.find(qn("a:ea"))
    if ea is None:
        ea = rpr.makeelement(qn("a:ea"), {})
        rpr.append(ea)
    ea.set("typeface", font)
    return run


def _clear_p(tf):
    p = tf.paragraphs[0]
    p.clear()
    return p


def add_rect(slide, l, t, w, h, color, radius=None):
    kind = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    shape = slide.shapes.add_shape(kind, Inches(l), Inches(t), Inches(w), Inches(h))
    _fill(shape, color)
    if radius:
        try:
            shape.adjustments[0] = radius
        except Exception:
            pass
    return shape


def add_oval(slide, l, t, w, h, color):
    shape = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(l), Inches(t), Inches(w), Inches(h))
    _fill(shape, color)
    return shape


def add_box(slide, l, t, w, h, text_parts, size=14, color=INK, bold=False, align=PP_ALIGN.LEFT, font=FONT, margin=0.08, anchor=MSO_ANCHOR.TOP):
    shape = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = _tf(shape, margin)
    tf.paragraphs[0].alignment = align
    shape.text_frame.paragraphs[0].space_after = Pt(0)
    if isinstance(text_parts, str):
        text_parts = [(text_parts, color, bold)]
    p = _clear_p(tf)
    p.alignment = align
    for part in text_parts:
        if len(part) == 2:
            txt, col = part
            _run(p, txt, size, col, bold, font)
        else:
            txt, col, b = part[:3]
            fnt = part[3] if len(part) > 3 else font
            _run(p, txt, size, col, b, fnt)
    try:
        tf.auto_size = None
        shape.text_frame._txBody.bodyPr.set("anchor", {MSO_ANCHOR.TOP: "t", MSO_ANCHOR.MIDDLE: "ctr", MSO_ANCHOR.BOTTOM: "b"}.get(anchor, "t"))
    except Exception:
        pass
    return shape


def add_para_box(slide, l, t, w, h, paragraphs, margin=0.08, anchor="t"):
    """paragraphs: list of dicts with text/parts, size, color, bold, space_after, font, align."""
    shape = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = _tf(shape, margin)
    try:
        tf._txBody.bodyPr.set("anchor", anchor)
    except Exception:
        pass
    first = True
    for spec in paragraphs:
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = spec.get("align", PP_ALIGN.LEFT)
        p.space_after = Pt(spec.get("space_after", 6))
        p.space_before = Pt(spec.get("space_before", 0))
        parts = spec.get("parts")
        if parts is None:
            parts = [(spec.get("text", ""), spec.get("color", INK), spec.get("bold", False), spec.get("font", FONT))]
        for part in parts:
            txt = part[0]
            col = part[1] if len(part) > 1 else spec.get("color", INK)
            b = part[2] if len(part) > 2 else spec.get("bold", False)
            fnt = part[3] if len(part) > 3 else spec.get("font", FONT)
            sz = spec.get("size", 14)
            if len(part) > 4:
                sz = part[4]
            _run(p, txt, sz, col, b, fnt)
    return shape


def add_picture_fit(slide, path, l, t, w, h):
    path = Path(path)
    if not path.exists():
        return None
    with PILImage.open(path) as im:
        iw, ih = im.size
    box_a = w / h
    img_a = iw / ih
    if img_a > box_a:
        nw, nh = w, w / img_a
        nl, nt = l, t + (h - nh) / 2
    else:
        nh, nw = h, h * img_a
        nl, nt = l + (w - nw) / 2, t
    return slide.shapes.add_picture(str(path), Inches(nl), Inches(nt), Inches(nw), Inches(nh))


def set_bg(slide):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = BG


def chrome(slide, label, idx, total=15, show_brand=True):
    if show_brand:
        add_para_box(
            slide, 0.62, 0.18, 6.2, 0.38,
            [{"parts": [("ai", INK, True), ("101", INK, False), ("  /  ", ORANGE, False), ("technology", MUTED, False)], "size": 14, "space_after": 0}],
            margin=0,
        )
        add_box(slide, 7.4, 0.22, 5.3, 0.32, label, size=10, color=MUTED, align=PP_ALIGN.RIGHT, margin=0)
        add_rect(slide, 0.62, 0.58, 12.1, 0.012, LINE)
    add_box(slide, 0.62, 7.12, 8.5, 0.24, "DIGITURK  ·  TECHNOLOGY TALKS", size=9, color=MUTED, margin=0)
    add_box(slide, 10.6, 7.12, 2.1, 0.24, f"{idx:02d}  /  {total:02d}", size=9, color=MUTED, align=PP_ALIGN.RIGHT, margin=0)
    add_rect(slide, 0, 7.46, W * (idx / total), 0.04, ORANGE)


def notes(slide, text):
    ns = slide.notes_slide
    tf = ns.notes_text_frame
    tf.text = text


def make_orb(path: Path):
    s = 900
    img = PILImage.new("RGBA", (s, s), (0, 0, 0, 0))
    px = img.load()
    cx = cy = s / 2
    stops = [
        (0.00, (255, 229, 178)),
        (0.15, (255, 172, 99)),
        (0.36, (247, 91, 53)),
        (0.59, (147, 43, 34)),
        (0.78, (21, 12, 19)),
        (1.00, (9, 9, 11)),
    ]
    rmax = 300

    def lerp_c(t):
        for i in range(len(stops) - 1):
            t0, c0 = stops[i]
            t1, c1 = stops[i + 1]
            if t0 <= t <= t1:
                u = 0 if t1 == t0 else (t - t0) / (t1 - t0)
                return tuple(int(c0[k] + (c1[k] - c0[k]) * u) for k in range(3))
        return stops[-1][1]

    for y in range(s):
        for x in range(s):
            dx, dy = x - cx, y - cy
            d = (dx * dx + dy * dy) ** 0.5
            if d <= rmax:
                c = lerp_c(d / rmax)
                a = 255
                if d > rmax - 8:
                    a = int(255 * (rmax - d) / 8)
                px[x, y] = (*c, a)
    overlay = PILImage.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    d.ellipse([118, 118, s - 118, s - 118], outline=(239, 173, 134, 110), width=3)
    d.ellipse([168, 168, s - 168, s - 168], outline=(231, 140, 97, 70), width=2)
    img = PILImage.alpha_composite(img, overlay)
    img = img.filter(ImageFilter.GaussianBlur(radius=0.6))
    img.save(path)
    return path


def new_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_bg(slide)
    return slide


def card(slide, l, t, w, h, fill=CARD, radius=0.08):
    return add_rect(slide, l, t, w, h, fill, radius=radius)


def eyebrow(slide, l, t, w, text):
    add_box(slide, l, t, w, 0.28, text.upper(), size=10, color=ORANGE, bold=True, font=MONO, margin=0)


def title(slide, l, t, w, h, parts, size=34):
    add_para_box(
        slide, l, t, w, h,
        [{"parts": [(p[0], p[1] if len(p) > 1 else INK, p[2] if len(p) > 2 else False) for p in parts], "size": size, "space_after": 0}],
        margin=0,
    )


def point_card(slide, l, t, w, h, head, body):
    card(slide, l, t, w, h)
    add_box(slide, l + 0.16, t + 0.12, w - 0.3, 0.26, head.upper(), size=10, color=ORANGE, bold=True, font=MONO, margin=0)
    add_box(slide, l + 0.16, t + 0.38, w - 0.32, h - 0.5, body, size=13, color=MUTED, margin=0)


def hyper(slide, l, t, w, h, text, url, size=13, color=GREEN):
    shape = add_box(slide, l, t, w, h, text, size=size, color=color, margin=0)
    for p in shape.text_frame.paragraphs:
        for run in p.runs:
            run.hyperlink.address = url
    return shape


def build():
    prs = Presentation()
    prs.slide_width = Inches(W)
    prs.slide_height = Inches(H)
    prs.core_properties.title = "AI 101 for technology"
    prs.core_properties.author = "Erdinç Yılmaz"
    prs.core_properties.subject = "Digiturk Technology Talks"

    tmp = ROOT / ".pptx-tmp"
    tmp.mkdir(exist_ok=True)
    orb_path = make_orb(tmp / "orb.png")

    # 1 · Hero
    s = new_slide(prs)
    chrome(s, "DIGITURK  ·  TECHNOLOGY TALKS", 1)
    eyebrow(s, 0.7, 1.05, 7.5, "DIGITURK  ·  TECHNOLOGY TALKS")
    add_para_box(
        s, 0.68, 1.4, 7.6, 2.4,
        [{
            "parts": [("AI  ", INK, True), ("101", RGBColor(0xC8, 0xC4, 0xBE), False)],
            "size": 78, "space_after": 0,
        }, {
            "parts": [("for technology", INK, False), (".", ORANGE, True)],
            "size": 36, "space_after": 0, "space_before": 4,
        }],
        margin=0,
    )
    add_para_box(
        s, 0.7, 4.05, 7.2, 1.1,
        [
            {"text": "AI her şeyi biliyor gibi konuşur.", "size": 20, "color": MUTED, "space_after": 4},
            {"parts": [("Biz ne zaman dinleyeceğimizi bilmeliyiz.", INK, True)], "size": 20, "space_after": 0},
        ],
        margin=0,
    )
    add_picture_fit(s, orb_path, 8.15, 1.15, 4.7, 4.7)
    add_box(s, 9.15, 5.55, 3.0, 0.28, "HUMAN  ×  AI", size=10, color=RGBColor(0xD9, 0x9A, 0x81), align=PP_ALIGN.CENTER, font=MONO, margin=0)
    add_box(
        s, 0.7, 6.55, 12.0, 0.32,
        "LLM  ·  RAG  ·  MCP  ·  AGENT  ·  LOCAL AI  ·  Spec-Driven Development (VIBE CODING)",
        size=11, color=MUTED, margin=0,
    )
    notes(s, NOTES[0])

    # 2 · AI nedir
    s = new_slide(prs)
    chrome(s, "01  /  AI NEDİR?", 2)
    eyebrow(s, 0.7, 0.78, 6.4, "Hayatımızın ortasında  ·  aktif ortak")
    title(s, 0.68, 1.08, 6.5, 1.35, [("Yapay zeka nedir?\n", INK), ("En basit haliyle.", ORANGE)], size=32)
    add_para_box(
        s, 0.7, 2.5, 6.4, 0.85,
        [{"parts": [
            ("Bilgisayarların ve makinelerin ", MUTED, False),
            ("insan gibi düşünmesi, öğrenmesi ve karar vermesi", INK, True),
            (" için yazılmış akıllı program.", MUTED, False),
        ], "size": 16, "space_after": 0}],
        margin=0,
    )
    rows = [
        ("Zaten kullanıyorsun", "Salonun çoğu doğrudan kullanıyor. Kalanı da dolaylı: yüz tanıma, harita, öneri…"),
        ("Eskiden pasif araçtı", "Biz basardık, o çalışırdı. Komut neyse onu yapardı."),
        ("Bugün aktif ortak", "Bizimle düşünüyor, bizi tahmin ediyor, hayatı kolaylaştırıyor."),
    ]
    y = 3.42
    for head, body in rows:
        point_card(s, 0.7, y, 6.35, 0.78, head, body)
        y += 0.86
    add_para_box(
        s, 0.7, 6.1, 6.4, 0.55,
        [{"parts": [("Peki AI’yı işimize nasıl daha verimli adapte ederiz?", INK, True)], "size": 15, "space_after": 0}],
        margin=0,
    )
    add_rect(s, 0.7, 6.1, 0.06, 0.5, ORANGE)
    add_picture_fit(s, ASSETS / "ai-nedir.jpg", 7.3, 0.85, 5.5, 5.9)
    notes(s, NOTES[1])

    # 3 · Model
    s = new_slide(prs)
    chrome(s, "02  /  MODEL NEDİR?", 3)
    eyebrow(s, 0.7, 0.78, 6.2, "Modelin içinde LLM de var")
    title(s, 0.68, 1.08, 6.3, 1.2, [("Model ve LLM nedir?\n", INK), ("En sade haliyle.", ORANGE)], size=30)
    add_para_box(
        s, 0.7, 2.35, 6.2, 0.8,
        [{"parts": [
            ("Model, büyük miktarda veriyle eğitilmiş ve aldığı bilgiyi ", MUTED, False),
            ("çıktıya dönüştüren", INK, True),
            (" yapay zekâ sistemidir.", MUTED, False),
        ], "size": 15, "space_after": 0}],
        margin=0,
    )
    card(s, 0.7, 3.25, 3.0, 1.15)
    add_box(s, 0.86, 3.38, 2.7, 0.24, "MODEL", size=11, color=ORANGE, bold=True, font=MONO, margin=0)
    add_box(s, 0.86, 3.64, 2.7, 0.62, "Görüntü, ses veya metin gibi farklı görevler için eğitilebilir.", size=13, color=MUTED, margin=0)
    card(s, 3.85, 3.25, 3.05, 1.15, RGBColor(0x2A, 0x18, 0x14))
    add_box(s, 4.01, 3.38, 2.75, 0.24, "LLM", size=11, color=ORANGE, bold=True, font=MONO, margin=0)
    add_box(s, 4.01, 3.64, 2.75, 0.62, "Metin ve dil üzerine eğitilmiş model türüdür.", size=13, color=MUTED, margin=0)
    add_rect(s, 0.7, 4.58, 0.06, 0.7, ORANGE)
    add_para_box(
        s, 0.9, 4.55, 6.0, 0.7,
        [{"parts": [("Her LLM bir modeldir.", INK, True)], "size": 16, "space_after": 2},
         {"text": "Her model bir LLM değildir.", "size": 15, "color": MUTED, "space_after": 0}],
        margin=0,
    )
    chips = ["Görüntü · YOLOv8", "Ses · Whisper", "LLM · GPT-5.6", "LLM · Claude", "LLM · Gemini"]
    x = 0.7
    for ch in chips:
        wch = 0.12 * len(ch) + 0.35
        card(s, x, 5.45, wch, 0.42, CARD2, radius=0.5)
        add_box(s, x, 5.5, wch, 0.34, ch, size=10, color=INK, font=MONO, align=PP_ALIGN.CENTER, margin=0)
        x += wch + 0.12
    add_picture_fit(s, ASSETS / "model-nedir.png", 7.2, 0.85, 5.55, 5.85)
    notes(s, NOTES[2])

    # 4 · Model seçimi
    s = new_slide(prs)
    chrome(s, "03  /  MODEL SEÇİMİ VE MALİYET", 4)
    eyebrow(s, 0.7, 0.78, 6.0, "Göreve göre model  ·  fiyat × kalite")
    title(s, 0.68, 1.08, 6.1, 1.25, [("En güçlü model,\n", INK), ("her işte en iyi değil.", ORANGE)], size=30)
    add_para_box(
        s, 0.7, 2.4, 6.1, 0.55,
        [{"parts": [("Mahalleye ekmek almaya ", MUTED, False), ("yarış arabasıyla", INK, True), (" gitmek gibi.", MUTED, False)], "size": 16, "space_after": 0}],
        margin=0,
    )
    card(s, 0.7, 3.05, 6.1, 1.35)
    add_box(s, 0.95, 3.22, 2.0, 0.22, "LUNA", size=11, color=ORANGE, bold=True, font=MONO, margin=0)
    add_box(s, 0.95, 3.44, 2.0, 0.5, "$0.20", size=32, color=INK, bold=True, margin=0)
    add_box(s, 0.95, 3.95, 2.2, 0.28, "input / 1M token", size=11, color=MUTED, margin=0)
    add_box(s, 3.15, 3.5, 1.1, 0.45, "~ 50×", size=18, color=ORANGE, bold=True, font=MONO, align=PP_ALIGN.CENTER, margin=0)
    add_box(s, 4.4, 3.22, 2.1, 0.22, "ASTRA", size=11, color=ORANGE, bold=True, font=MONO, margin=0)
    add_box(s, 4.4, 3.44, 2.1, 0.5, "$10", size=32, color=INK, bold=True, margin=0)
    add_box(s, 4.4, 3.95, 2.2, 0.28, "input / 1M token", size=11, color=MUTED, margin=0)
    card(s, 0.7, 4.55, 2.95, 1.55)
    add_box(s, 0.86, 4.68, 2.65, 0.2, "KENDİ BENCHMARK’IM", size=9, color=ORANGE, bold=True, font=MONO, margin=0)
    add_box(s, 0.86, 4.9, 2.65, 0.28, "Mercury AI Bench", size=15, color=INK, bold=True, margin=0)
    add_box(s, 0.86, 5.2, 2.65, 0.5, "Hangi işe hangi model ve fiyat — haftalık takip.", size=12, color=MUTED, margin=0)
    hyper(s, 0.86, 5.72, 2.65, 0.25, "mercury-ai-bench.netlify.app ↗", "https://mercury-ai-bench.netlify.app/")
    card(s, 3.8, 4.55, 3.0, 1.55)
    add_box(s, 3.96, 4.68, 2.7, 0.2, "GERÇEK TEST", size=9, color=ORANGE, bold=True, font=MONO, margin=0)
    add_box(s, 3.96, 4.9, 2.7, 0.28, "Venelin Valkov", size=15, color=INK, bold=True, margin=0)
    add_box(s, 3.96, 5.2, 2.7, 0.5, "Aynı prompt ile modelleri yan yana deniyor.", size=12, color=MUTED, margin=0)
    hyper(s, 3.96, 5.72, 2.7, 0.25, "youtube.com/@venelin_valkov ↗", "https://www.youtube.com/@venelin_valkov/videos")
    add_picture_fit(s, ASSETS / "mercury-bench.png", 7.15, 0.82, 5.55, 3.7)
    add_picture_fit(s, ASSETS / "venelin-youtube.png", 7.15, 4.65, 5.55, 2.05)
    notes(s, NOTES[3])

    # 5 · Terimler
    s = new_slide(prs)
    chrome(s, "04  /  AI 101 TERİMLERİ", 5)
    eyebrow(s, 0.55, 0.76, 5.4, "LLM  ·  RAG  ·  MCP  ·  MEMORY  ·  AGENT")
    title(s, 0.52, 1.04, 5.5, 1.1, [("Tek sistem.\n", INK), ("Memory ile Agent.", ORANGE)], size=28)
    add_para_box(
        s, 0.55, 2.2, 5.4, 0.5,
        [{"parts": [("Parçalar ayrı ayrı güçlü. Birleşince ", MUTED, False), ("Agent", INK, True), (" olur.", MUTED, False)], "size": 15, "space_after": 0}],
        margin=0,
    )
    formula = [("MODEL", CARD), ("+", None), ("TOOLS", CARD), ("+", None), ("MEMORY", RGBColor(0xFF, 0xB0, 0x89)), ("=", None), ("AGENT", ORANGE)]
    x = 0.55
    for item, fill in formula:
        if fill is None:
            add_box(s, x, 2.82, 0.32, 0.42, item, size=16, color=ORANGE, bold=True, align=PP_ALIGN.CENTER, margin=0)
            x += 0.34
        else:
            wch = 1.05 if item != "MEMORY" else 1.18
            fg = BG if item in ("MEMORY", "AGENT") else INK
            card(s, x, 2.78, wch, 0.46, fill, radius=0.1)
            add_box(s, x, 2.84, wch, 0.36, item, size=11, color=fg, bold=True, font=MONO, align=PP_ALIGN.CENTER, margin=0)
            x += wch + 0.06
    minis = [
        ("LLM", "Beyin · dili anlar, üretir"),
        ("RAG", "Kitaplar · ilgili belgeyi getirir"),
        ("MCP", "Bağlantı · araç ve verilere açar"),
        ("MEMORY", "Hafıza · bağlamı ve geçmişi tutar"),
    ]
    positions = [(0.55, 3.4), (3.25, 3.4), (0.55, 4.28), (3.25, 4.28)]
    for (head, body), (lx, ty) in zip(minis, positions):
        point_card(s, lx, ty, 2.58, 0.78, head, body)
    add_para_box(
        s, 0.55, 5.2, 5.3, 0.7,
        [{"text": "Agent: hangi adımı atacağına karar verir, araç kullanır, hatırlar, devam eder.", "size": 13, "color": MUTED, "space_after": 0}],
        margin=0,
    )
    terms = [
        ("LLM", "= BEYİN", "Dili anlar ve üretir.", "Örüntülerden akıl yürütür.", RGBColor(0xFF, 0x8B, 0x67)),
        ("RAG", "= BEYİN + KİTAPLAR", "İlgili bilgiyi bulur.", "Belgeyi yanıtın bağlamına ekler.", RGBColor(0x7E, 0xCF, 0xB0)),
        ("MCP", "= STANDART BAĞLANTI", "AI’ı araç ve verilere bağlar.", "API · dosya · veritabanı · servis", RGBColor(0xA9, 0xA0, 0xFF)),
        ("AI AGENT", "= BEYİN + ELLER", "Hangi adımı atacağına karar verir.", "Araç kullanır ve eyleme geçebilir.", RGBColor(0xFF, 0xD1, 0x7B)),
    ]
    x = 6.2
    for head, sub, body, small, accent in terms:
        card(s, x, 0.78, 1.68, 2.55)
        add_oval(s, x + 0.62, 0.92, 0.42, 0.42, accent)
        add_box(s, x + 0.08, 1.42, 1.52, 0.28, head, size=12, color=ORANGE, bold=True, font=MONO, align=PP_ALIGN.CENTER, margin=0)
        add_box(s, x + 0.08, 1.7, 1.52, 0.4, sub, size=9, color=INK, bold=True, font=MONO, align=PP_ALIGN.CENTER, margin=0)
        add_box(s, x + 0.1, 2.15, 1.48, 0.5, body, size=11, color=INK, align=PP_ALIGN.CENTER, margin=0)
        add_box(s, x + 0.1, 2.65, 1.48, 0.5, small, size=10, color=MUTED, align=PP_ALIGN.CENTER, margin=0)
        x += 1.76
    add_picture_fit(s, ASSETS / "agent-n8n.png", 6.2, 3.5, 6.55, 3.2)
    notes(s, NOTES[4])

    # 6 · Akıllı kullanım
    s = new_slide(prs)
    chrome(s, "05  /  AKILLI KULLANIM", 6)
    eyebrow(s, 0.7, 0.82, 12.0, "Akıllı kullanım  ·  her işe AI değil")
    title(s, 0.68, 1.15, 12.0, 1.3, [("AI güçlü.\n", INK), ("Ama bedava değil.", ORANGE)], size=40)
    add_para_box(
        s, 0.7, 2.55, 12.0, 0.55,
        [{"text": "Her soruyu, her taslağı, her küçük işi AI’ya yıkmak hem pahalıya hem yavaşlığa gider.", "size": 18, "color": MUTED, "space_after": 0}],
        margin=0,
    )
    points = [
        ("Akıllıca kullan", "Gerçekten değer üreten işe ver: zor problem, tekrarlayan yük, zaman kazandıran adım."),
        ("Her işe verme", "İki dakikalık iş, basit kontrol, net kural — insan daha hızlı ve ucuz biter."),
        ("Ölçüyü kaçırma", "En büyük model + sonsuz deneme = faturayı ve enerjiyi şişirir."),
    ]
    x = 0.7
    for head, body in points:
        point_card(s, x, 3.3, 3.9, 1.85, head, body)
        x += 4.1
    card(s, 0.7, 5.4, 12.0, 1.15, RGBColor(0x2A, 0x18, 0x14))
    add_para_box(
        s, 0.95, 5.6, 11.5, 0.8,
        [{"parts": [("Kural:  ", MUTED, False), ("AI’yı varsayılan değil, bilinçli seçim yap.", ORANGE, True)], "size": 22, "space_after": 0}],
        margin=0, anchor="ctr",
    )
    notes(s, NOTES[5])

    # 7 · Güven
    s = new_slide(prs)
    chrome(s, "06  /  GÜVEN KALİBRASYONU", 7)
    eyebrow(s, 0.7, 0.78, 6.4, "Akıcı cevap  ≠  doğru cevap")
    title(s, 0.68, 1.1, 6.6, 1.5, [('“Evet,\n', INK), ("yenilebilir.”", ORANGE)], size=40)
    ladder = [
        ("Düşük risk", "taslak, fikir, özet  →  hızlı kontrol"),
        ("Orta risk", "kod, analiz  →  kaynak + test"),
        ("Yüksek risk", "sağlık, para, prod  →  uzman / onay"),
    ]
    y = 2.75
    for head, body in ladder:
        add_rect(s, 0.7, y, 0.07, 1.05, ORANGE)
        card(s, 0.92, y, 6.15, 0.98)
        add_box(s, 1.12, y + 0.12, 5.75, 0.26, head.upper(), size=12, color=ORANGE, bold=True, font=MONO, margin=0)
        add_box(s, 1.12, y + 0.42, 5.75, 0.42, body, size=16, color=INK, margin=0)
        y += 1.12
    add_picture_fit(s, ASSETS / "mushroom-meme.png", 7.35, 0.78, 5.4, 6.05)
    notes(s, NOTES[6])

    # 8 · Lokal
    s = new_slide(prs)
    chrome(s, "07  /  MODEL CİHAZINDA ÇALIŞIR", 8)
    eyebrow(s, 0.7, 0.82, 12.0, "Bulut yerine kendi Mac’inde / GPU’nda")
    title(s, 0.68, 1.15, 12.0, 1.4, [("Veri dışarı çıkmadan\n", INK), ("model içeride çalışır.", ORANGE)], size=36)
    items = [
        ("Gizlilik", "Kaynak cihazda kalır", "Doğru kurulum ve lokal araçlarla."),
        ("Çevrimdışı", "İnternetsiz kullanılabilir", "Saha, demo ve kapalı ağ senaryoları."),
        ("Kontrol", "Sürüm ve maliyet sende", "API ücreti yok; donanım ve bakım var."),
    ]
    x = 0.7
    for head, h3, body in items:
        card(s, x, 2.85, 3.9, 2.55)
        add_box(s, x + 0.28, 3.1, 3.35, 0.28, head.upper(), size=11, color=ORANGE, bold=True, font=MONO, margin=0)
        add_box(s, x + 0.28, 3.5, 3.35, 0.9, h3, size=24, color=INK, bold=True, margin=0)
        add_box(s, x + 0.28, 4.5, 3.35, 0.6, body, size=15, color=MUTED, margin=0)
        x += 4.1
    add_box(
        s, 0.7, 5.7, 12.0, 0.7,
        "Bedava değildir: RAM/VRAM, elektrik, güncelleme, güvenlik ve operasyon maliyeti cihazına geçer.",
        size=15, color=MUTED, margin=0,
    )
    notes(s, NOTES[7])

    # 9 · CanIRun + HF
    s = new_slide(prs)
    chrome(s, "08  /  CANIRUN.AI + HUGGING FACE", 9)
    eyebrow(s, 0.7, 0.78, 6.0, "Adım 1  ·  donanımı kontrol et")
    title(s, 0.68, 1.08, 6.2, 1.2, [("8B model ≠\n", INK), ("8 GB dosya.", ORANGE)], size=32)
    card(s, 0.7, 2.5, 6.15, 3.55)
    add_rect(s, 0.7, 2.5, 6.15, 0.42, RGBColor(0x1C, 0x1D, 0x20), radius=0.02)
    add_oval(s, 0.9, 2.62, 0.16, 0.16, RGBColor(0xFF, 0x6F, 0x61))
    add_oval(s, 1.12, 2.62, 0.16, 0.16, RGBColor(0xFF, 0xC1, 0x45))
    add_oval(s, 1.34, 2.62, 0.16, 0.16, RGBColor(0x69, 0xC7, 0x79))
    add_box(s, 1.7, 2.56, 4.8, 0.3, "canirun.ai/model/qwen3-8b", size=11, color=MUTED, font=MONO, margin=0)
    add_box(s, 0.95, 3.15, 5.6, 0.45, "Qwen 3 8B", size=26, color=INK, bold=True, font=MONO, margin=0)
    add_box(s, 0.95, 3.65, 5.6, 0.35, "4.5 GB minimum  ·  7.5 GB önerilen", size=15, color=MUTED, margin=0)
    card(s, 0.95, 4.15, 5.65, 0.85, RGBColor(0x18, 0x1A, 0x1C))
    add_box(s, 1.1, 4.28, 1.8, 0.28, "Q4_K_M", size=14, color=INK, bold=True, font=MONO, margin=0)
    add_box(s, 3.0, 4.28, 2.2, 0.28, "4.6 GB VRAM", size=14, color=MUTED, margin=0)
    add_box(s, 5.2, 4.28, 1.2, 0.28, "Good", size=14, color=GREEN, bold=True, align=PP_ALIGN.RIGHT, margin=0)
    hyper(s, 0.95, 5.2, 5.6, 0.35, "Cihazını kontrol et ↗", "https://www.canirun.ai/model/qwen3-8b", size=15)
    eyebrow(s, 7.2, 0.78, 5.5, "Adım 2  ·  modeli bul")
    add_box(s, 7.2, 1.15, 5.5, 0.7, "Hugging Face", size=36, color=INK, bold=True, margin=0)
    add_para_box(
        s, 7.2, 2.0, 5.5, 1.2,
        [{"text": "Modellerin GitHub’ı: model ağırlıkları, model card, lisans, kullanım örneği.", "size": 18, "color": MUTED, "space_after": 0}],
        margin=0,
    )
    hyper(s, 7.2, 3.35, 5.5, 0.4, "Trending models ↗", "https://huggingface.co/models?inference_provider=all&sort=trending", size=16)
    add_box(
        s, 7.2, 4.0, 5.5, 0.7,
        "GGUF + Q4: lokal kullanım için sık görülen pratik başlangıç.",
        size=14, color=MUTED, margin=0,
    )
    notes(s, NOTES[8])

    # 10 · Vibe coding
    s = new_slide(prs)
    chrome(s, "09  /  SPEC-DRIVEN DEVELOPMENT (VIBE CODING)", 10)
    eyebrow(s, 0.55, 0.76, 6.2, "Doğal dil  →  ürün")
    title(s, 0.52, 1.04, 6.3, 1.35, [("Spec-Driven Development.\n", INK), ("Satır satır değil, tarif.", ORANGE)], size=26)
    add_para_box(
        s, 0.55, 2.45, 6.2, 0.85,
        [{"parts": [
            ("“Bu fonksiyonu nasıl kodlarım?” yerine\n", MUTED, False),
            ("“Bana kullanıcıların giriş yapabileceği bir sistem oluştur”", INK, True),
            (" diyoruz.", MUTED, False),
        ], "size": 14, "space_after": 0}],
        margin=0,
    )
    point_card(s, 0.55, 3.4, 6.2, 0.85, "AI ne yapar", "Kodu yazar, dosyaları oluşturur, hataları bulur ve düzeltir")
    point_card(s, 0.55, 4.32, 6.2, 0.85, "Biz neye bakarız", "Ne istediğimize ve sonucun doğru olup olmadığına")
    card(s, 0.55, 5.25, 3.0, 1.15)
    add_box(s, 0.7, 5.38, 2.7, 0.22, "IDE", size=11, color=ORANGE, bold=True, font=MONO, margin=0)
    add_box(s, 0.7, 5.62, 2.7, 0.65, "Cursor · görsel arayüz · diff takibi · başlangıç için uygun", size=12, color=MUTED, margin=0)
    card(s, 3.7, 5.25, 3.05, 1.15)
    add_box(s, 3.85, 5.38, 2.75, 0.22, "CLI", size=11, color=ORANGE, bold=True, font=MONO, margin=0)
    add_box(s, 3.85, 5.62, 2.75, 0.65, "Claude Code / Codex · terminal · büyük proje ve agent işleri", size=12, color=MUTED, margin=0)
    add_picture_fit(s, ASSETS / "vibe-coding.jpg", 6.95, 0.78, 5.8, 5.95)
    notes(s, NOTES[9])

    # 11 · Prompt
    s = new_slide(prs)
    chrome(s, "10  /  PROMPT = MİNİ BRIEF", 11)
    eyebrow(s, 0.7, 0.78, 6.5, "Kötü prompt")
    card(s, 0.7, 1.12, 6.3, 0.85)
    add_box(s, 0.95, 1.32, 5.9, 0.5, "“Bunu düzelt.”", size=26, color=MUTED, margin=0)
    eyebrow(s, 0.7, 2.15, 6.5, "Daha iyi prompt")
    recipe = [
        ("İş:", "Bu API değişikliğinin risklerini çıkar."),
        ("Bağlam:", "Diff + kabul kriterleri."),
        ("Sınır:", "Dosya değiştirme; sadece öner."),
        ("Çıktı:", "Risk / kanıt / test tablosu."),
        ("Kontrol:", "Bilmediğini açıkça yaz."),
    ]
    card(s, 0.7, 2.48, 6.3, 3.15)
    y = 2.62
    for head, body in recipe:
        add_para_box(
            s, 0.95, y, 5.85, 0.48,
            [{"parts": [(head + "  ", ORANGE, True, MONO), (body, INK, False)], "size": 16, "space_after": 0}],
            margin=0,
        )
        y += 0.52
    hyper(s, 0.7, 5.8, 6.3, 0.4, "promptingguide.ai ↗", "https://www.promptingguide.ai/", size=16)
    card(s, 7.3, 0.85, 5.4, 5.7)
    add_box(s, 7.55, 1.15, 5.0, 0.3, "KARŞI KANIT İSTE", size=11, color=ORANGE, bold=True, font=MONO, margin=0)
    add_box(s, 7.55, 1.55, 5.0, 1.3, "“Harika fikir!” yerine\nkarşı kanıt iste.", size=26, color=INK, bold=True, margin=0)
    add_para_box(
        s, 7.55, 3.1, 5.0, 2.6,
        [
            {"text": "Modelden alkış değil itiraz isteyin.", "size": 16, "color": MUTED, "space_after": 12},
            {"text": "En zayıf varsayımım ne?", "size": 18, "color": INK, "space_after": 8},
            {"text": "Hangi kanıt fikrimi değiştirir?", "size": 18, "color": INK, "space_after": 16},
            {"text": "HTML sunumdaki mizah videosu PowerPoint’e gömülmedi; canlı slaytta oynatın.", "size": 13, "color": MUTED, "space_after": 0},
        ],
        margin=0,
    )
    notes(s, NOTES[10])

    # 12 · SKILL.md
    s = new_slide(prs)
    chrome(s, "11  /  AI İÇİN ÇALIŞMA KILAVUZU", 12)
    eyebrow(s, 0.55, 0.76, 6.4, ".MD = markdown  ·  insanın da AI’ın da okuyabildiği metin")
    title(s, 0.52, 1.08, 6.2, 1.25, [("Model aynı.\n", INK), ("Çalışma biçimi değişir.", ORANGE)], size=28)
    stack = [
        ("README.md", "Bu proje nedir?", False),
        ("AGENTS.md", "Bu repoda nasıl çalışılır?", False),
        ("SKILL.md", "Bu iş adım adım nasıl yapılır?", True),
    ]
    y = 2.5
    for name, body, active in stack:
        fill = RGBColor(0x2A, 0x18, 0x14) if active else CARD
        card(s, 0.55 + (0.12 if active else 0), y, 6.15, 0.78, fill)
        add_box(s, 0.75 + (0.12 if active else 0), y + 0.12, 2.2, 0.28, name, size=14, color=ORANGE if active else INK, bold=True, font=MONO, margin=0)
        add_box(s, 3.05 + (0.12 if active else 0), y + 0.22, 3.4, 0.38, body, size=14, color=INK if active else MUTED, margin=0)
        y += 0.9
    add_box(
        s, 0.55, 5.35, 6.2, 0.85,
        "Her .md dosyası skill değildir. SKILL.md; ad, tetikleyici açıklama ve uygulanacak yöntemi taşır.",
        size=13, color=MUTED, margin=0,
    )
    card(s, 7.05, 0.85, 5.65, 2.55)
    add_box(s, 7.3, 1.05, 5.2, 0.3, "SKILL.md", size=18, color=ORANGE, bold=True, font=MONO, margin=0)
    add_box(s, 7.3, 1.45, 5.2, 0.35, "talimat  ·  örnek  ·  kontrol", size=13, color=MUTED, font=MONO, margin=0)
    add_box(s, 7.3, 2.0, 5.2, 0.9, "AI okur  →  araçları kullanır  →  tekrarlanabilir sonuç\naynı standart · daha az sürpriz", size=15, color=INK, margin=0)
    links = [
        ("agentskills.io", "açık standart", "https://agentskills.io/"),
        ("openai/plugins", "güncel OpenAI örnekleri", "https://github.com/openai/plugins"),
        ("anthropics/skills", "resmî örnekler", "https://github.com/anthropics/skills"),
        ("skills.sh", "topluluk dizini", "https://skills.sh/"),
    ]
    y = 3.55
    for name, sub, url in links:
        card(s, 7.05, y, 5.65, 0.55)
        add_box(s, 7.22, y + 0.12, 2.6, 0.32, name, size=13, color=ORANGE, bold=True, font=MONO, margin=0)
        hyper(s, 9.7, y + 0.12, 2.8, 0.32, sub + " ↗", url, size=12, color=MUTED)
        y += 0.62
    add_rect(s, 7.05, 6.1, 0.07, 0.55, ORANGE)
    add_box(s, 7.25, 6.12, 5.4, 0.55, "Yüklemeden önce: yayıncı · SKILL.md · scriptler · izinler · sürüm", size=12, color=MUTED, margin=0)
    notes(s, NOTES[11])

    # 13 · gstack
    s = new_slide(prs)
    chrome(s, "12  /  PROMPT’TAN SÜRECE", 13)
    eyebrow(s, 0.7, 0.85, 12.0, "Garry Tan’ın AI engineering workflow’u")
    title(s, 0.68, 1.2, 12.0, 1.35, [("Tek prompt değil.\n", INK), ("Tekrarlanabilir roller.", ORANGE)], size=40)
    flow = [
        ("/office-hours", "fikri zorla"),
        ("/plan-eng-review", "planı incele"),
        ("/review", "kodu eleştir"),
        ("/qa", "ürünü dene"),
    ]
    x = 0.7
    for i, (cmd, sub) in enumerate(flow):
        card(s, x, 2.85, 2.55, 1.7)
        add_box(s, x + 0.16, 3.05, 2.25, 0.55, cmd, size=16, color=ORANGE, bold=True, font=MONO, margin=0)
        add_box(s, x + 0.16, 3.65, 2.25, 0.55, sub, size=16, color=MUTED, margin=0)
        if i < 3:
            add_box(s, x + 2.5, 3.4, 0.4, 0.45, "→", size=22, color=ORANGE, align=PP_ALIGN.CENTER, margin=0)
        x += 3.15
    add_box(
        s, 0.7, 4.85, 12.0, 0.5,
        "23 opinionated tool  ·  Claude Code / Codex desteği  ·  açık kaynak",
        size=18, color=MUTED, margin=0,
    )
    hyper(s, 0.7, 5.5, 12.0, 0.4, "github.com/garrytan/gstack ↗", "https://github.com/garrytan/gstack", size=18)
    notes(s, NOTES[12])

    # 14 · Graphify
    s = new_slide(prs)
    chrome(s, "13  /  CODE KNOWLEDGE GRAPH", 14)
    eyebrow(s, 0.7, 0.78, 6.2, "graphify.com")
    title(s, 0.68, 1.08, 6.2, 1.25, [("AI dosya değil,\n", INK), ("ilişki görür.", ORANGE)], size=32)
    add_para_box(
        s, 0.7, 2.45, 6.2, 0.9,
        [{"text": "“Graphify kodu okumak yerine, kodun ilişki haritasını görmemizi sağlıyor.”", "size": 16, "color": MUTED, "space_after": 0}],
        margin=0,
    )
    add_rect(s, 0.7, 3.5, 0.07, 1.7, ORANGE)
    add_para_box(
        s, 0.95, 3.5, 5.9, 1.75,
        [{"parts": [("Güvenlik:  ", ORANGE, True), ("Site yerel parsing ve telemetri olmadığını söylüyor. Yine de sürümü sabitle, kaynağı incele, üretilen graph dosyalarını ve model sağlayıcısına giden sorguları veri politikanla kontrol et.", MUTED, False)], "size": 14, "space_after": 0}],
        margin=0,
    )
    hyper(s, 0.7, 5.45, 6.2, 0.4, "graphify.com ↗", "https://graphify.com/", size=16)
    card(s, 7.15, 0.85, 5.55, 5.7, RGBColor(0x08, 0x0A, 0x0B))
    add_rect(s, 7.15, 0.85, 5.55, 0.4, RGBColor(0x1C, 0x1D, 0x20))
    add_oval(s, 7.35, 0.96, 0.16, 0.16, RGBColor(0xFF, 0x6F, 0x61))
    add_oval(s, 7.57, 0.96, 0.16, 0.16, RGBColor(0xFF, 0xC1, 0x45))
    add_oval(s, 7.79, 0.96, 0.16, 0.16, RGBColor(0x69, 0xC7, 0x79))
    add_box(s, 8.1, 0.9, 3.3, 0.28, "graphify.com", size=11, color=MUTED, font=MONO, margin=0)
    nodes = [
        (7.55, 2.0, 1.05, "billing", ORANGE),
        (9.15, 2.85, 1.25, "API", ORANGE),
        (11.05, 1.95, 1.05, "auth", RGBColor(0x74, 0xCC, 0xB3)),
        (7.7, 4.55, 1.05, "player", RGBColor(0xA9, 0xA0, 0xFF)),
        (10.7, 4.45, 1.05, "tests", RGBColor(0xFF, 0xD3, 0x7C)),
    ]
    for lx, ty, nw, name, col in nodes:
        add_oval(s, lx, ty, nw, nw, col)
        add_box(s, lx, ty + nw * 0.32, nw, 0.4, name, size=11, color=BG, bold=True, align=PP_ALIGN.CENTER, margin=0)
    add_box(s, 7.4, 5.95, 5.1, 0.35, "Bir cevap yerine denetlenebilir bir yol.", size=13, color=GREEN, align=PP_ALIGN.CENTER, margin=0)
    notes(s, NOTES[13])

    # 15 · Teşekkür
    s = new_slide(prs)
    chrome(s, "TEŞEKKÜRLER", 15, show_brand=True)
    glow = add_oval(s, 8.4, 3.6, 6.2, 5.2, RGBColor(0x5A, 0x22, 0x14))
    add_para_box(
        s, 1.1, 1.7, 11.1, 1.6,
        [{"parts": [
            ("Geleceğin sorusu “Yapay zekâ işimizi alacak mı?” değil,\n", MUTED, False),
            ("“Onunla birlikte ne kadar ileri gidebiliriz?”", ORANGE, True),
        ], "size": 22, "align": PP_ALIGN.CENTER, "space_after": 0}],
        margin=0,
    )
    add_para_box(
        s, 1.1, 3.5, 11.1, 1.4,
        [{"parts": [("Teşekkürler", INK, True), (".", ORANGE, True)], "size": 64, "align": PP_ALIGN.CENTER, "space_after": 0}],
        margin=0,
    )
    add_box(s, 1.1, 5.1, 11.1, 0.45, "Erdinç Yılmaz", size=20, color=MUTED, align=PP_ALIGN.CENTER, margin=0)
    notes(s, NOTES[14])
    _ = glow

    prs.save(OUT)
    return OUT


if __name__ == "__main__":
    path = build()
    print(path)
