"""Membuat halaman peta subkompetensi (skills.md) dari 02-kompetensi-dan-subkompetensi.md.

Pemakaian (dari akar repositori):
    python3 tools/buat_peta.py path/ke/02-kompetensi-dan-subkompetensi.md .

Skrip menulis skills.md. Sebelum menulis, skrip memeriksa isi 02: jumlah subkompetensi
per kompetensi, kode prasyarat, siklus, nama kembar, awalan capaian, serta panjang nama
dan capaian. Hasil pemeriksaan dicetak sebagai peringatan.

Skrip ini belum membuat index.md dan halaman kompetensi. Keduanya masih memakai
tools/generate_pages.py versi Inggris sampai diterjemahkan.
"""
import re, sys, html

ref, site = sys.argv[1], sys.argv[2]
s = open(ref, encoding='utf-8').read()

# Tautan ke halaman kompetensi. Selama halaman kompetensi masih memakai nama berkas
# berbahasa Inggris, PAKAI_SLUG_LAMA bernilai True. Ubah menjadi False setelah halaman
# kompetensi dibuat ulang dengan slug dari kolom "Slug halaman" di 02.
PAKAI_SLUG_LAMA = True
SLUG_LAMA = {
    'C1': 'epidemiological-and-economic-thinking', 'C2': 'population-unit-and-case',
    'C3': 'data-sources-and-sampling', 'C4': 'diagnostic-test-quality',
    'C5': 'occurrence-and-burden', 'C6': 'patterns-by-animal-place-and-time',
    'C7': 'surveillance-systems', 'C8': 'comparing-groups-and-association',
    'C9': 'analysing-several-factors-together', 'C10': 'appraising-analytical-reports',
    'C11': 'designing-observational-studies', 'C12': 'outbreak-investigation',
    'C13': 'disease-spread-and-models', 'C14': 'risk-of-introduction-and-spread',
    'C15': 'intervention-options', 'C16': 'economic-impact-of-disease',
    'C17': 'economic-comparison-and-decision', 'C18': 'evaluating-interventions',
    'C19': 'integrated-strategy',
}

# ---------------- baca 02 ----------------
comps = re.findall(r'^\| (C\d+) \| (T\d|Integrasi) \| (.+?) \| (.+?) \| (.+?) \| (\d+) \| ([a-z0-9-]+) \|$', s, re.M)
skills = re.findall(r'^\| (S(\d+)\.\d+) \| (.+?) \| (.+?) \| (.+?) \| (.+?) \| (Inti|Terapan|Pengenalan) \|$', s, re.M)
xs = re.findall(r'^\| (X\d) \| (.+?) \|$', s, re.M)
C = {c[0]: dict(code=c[0], tahap=c[1], nama=c[2], capaian=c[3], depth=c[4], n=int(c[5]), slug=c[6]) for c in comps}
S = {}
for code, cn, nama, capaian, cakupan, pre, dep in skills:
    S[code] = dict(code=code, comp='C' + cn, nama=nama, capaian=capaian, cakupan=cakupan,
                   pre=[] if pre == 'Tidak ada' else [p.strip() for p in pre.split(',')], depth=dep)
X = dict(xs)

# ---------------- periksa 02 ----------------
warn = []
for c in C.values():
    n = sum(1 for v in S.values() if v['comp'] == c['code'])
    if n != c['n']:
        warn.append(f"{c['code']}: tabel kompetensi menyebut {c['n']} subkompetensi, rinciannya {n}")
for k, v in S.items():
    for p in v['pre']:
        if p not in S and p not in X:
            warn.append(f"{k}: prasyarat {p} tidak ada")
state = {}
def dfs(k, path):
    if state.get(k) == 2: return
    if state.get(k) == 1:
        warn.append('siklus prasyarat: ' + ' > '.join(path + [k])); return
    state[k] = 1
    for p in S[k]['pre']:
        if p in S: dfs(p, path + [k])
    state[k] = 2
for k in S: dfs(k, [])
semua = [(k, v['nama']) for k, v in S.items()] + [(k, v['nama']) for k, v in C.items()]
vistos = {}
for k, nm in semua:
    if nm.lower() in vistos: warn.append(f"nama kembar: {k} dan {vistos[nm.lower()]} ({nm})")
    vistos[nm.lower()] = k
for k, v in S.items():
    if not re.match(r'Me', v['capaian']) or re.match(r'Mampu', v['capaian']):
        warn.append(f"{k}: capaian tidak berawalan me-: {v['capaian']}")
    if len(v['capaian'].split()) > 10: warn.append(f"{k}: capaian lebih dari 10 kata ({len(v['capaian'].split())})")
    if len(v['nama'].split()) > 6 and ',' not in v['nama']: warn.append(f"{k}: nama lebih dari 6 kata ({len(v['nama'].split())})")
for k, v in C.items():
    if len(v['nama'].split()) > 6: warn.append(f"{k}: nama lebih dari 6 kata")
    if not re.match(r'Me', v['capaian']): warn.append(f"{k}: capaian tidak berawalan me-")
for k, t in [(k, v['nama'] + ' ' + v['capaian']) for k, v in {**S, **C}.items()]:
    if '—' in t or '–' in t: warn.append(f"{k}: ada tanda pisah panjang")

# ---------------- bantuan ----------------
TAHAP = [
 ("T0", "d0", "Tahap 0", "Mengapa epidemiologi?", "Apa itu epidemiologi dan ekonomi veteriner, serta bagaimana cara mengubah kasus individual menjadi pertanyaan berskala populasi."),
 ("T1", "d1", "Tahap 1", "Apa yang terjadi?", "Tentukan populasi dan kasus, kumpulkan data, nilai uji diagnostik, dan deskripsikan pola penyakit."),
 ("T2", "d2", "Tahap 2", "Mengapa ia terjadi?", "Bandingkan kelompok, analisis beberapa faktor secara bersamaan, telaah laporan, rancang kajian, dan selidiki wabah."),
 ("T3", "d3", "Tahap 3", "Apa yang dapat terjadi?", "Proyeksikan penyebaran penyakit dalam populasi dan nilai risiko masuknya penyakit."),
 ("T4", "d4", "Tahap 4", "Apa yang perlu dilakukan?", "Pilih intervensi dan bandingkan dari sisi kesehatan dan ekonomi."),
 ("T5", "d5", "Tahap 5", "Apakah intervensinya berhasil?", "Nilai apakah intervensi mengubah penyakit atau mengubah cara deteksinya."),
 ("Integrasi", "integration", "Integrasi", "Semua pertanyaan bersama", "Gabungkan bukti menjadi satu strategi dan pertahankan strategi itu."),
]
VAR = {"T0": "--d0", "T1": "--d1", "T2": "--d2", "T3": "--d3", "T4": "--d4", "T5": "--d5", "Integrasi": "--dint"}
KELAS = {"Inti": "core", "Terapan": "applied", "Pengenalan": "introduced"}
def e(t): return html.escape(t, quote=True)
def anc(code): return code.lower().replace('.', '-')
def comp_slug(c): return SLUG_LAMA[c] if PAKAI_SLUG_LAMA else C[c]['slug']
def comp_url(c): return f"competencies/{comp_slug(c)}.html"
def skill_url(k): return f"{comp_url(S[k]['comp'])}#{anc(k)}"

nC, nS = len(C), len(S)

# ---------------- halaman peta ----------------
out = ['---', 'title: Peta subkompetensi', 'toc: true', 'toc-depth: 2', 'toc-title: Tahap', '---', '',
'```{=html}',
'<div class="readme">',
'<h2 class="readme-title" id="cara-membaca">Cara membaca halaman ini</h2>',
f'<p>Halaman ini memuat semua {nS} subkompetensi dalam mata kuliah. Subkompetensi dikelompokkan menurut kompetensi, dan kompetensi dikelompokkan menurut tahap.</p>',
'<p>Setiap kompetensi dan subkompetensi punya nama dan capaian. Nama berupa frasa nomina yang menyebut topiknya. Capaian berupa kalimat berkata kerja yang menyatakan apa yang dilakukan mahasiswa. Daftar di bawah menampilkan nama. Capaian subkompetensi muncul saat penunjuk diarahkan ke nama, atau dapat ditampilkan sekaligus dengan tombol di bawah.</p>',
'<p>Pilih sebuah kompetensi atau subkompetensi untuk membuka halamannya. Halaman itu memuat cakupan, prasyarat, dan bahan ajar.</p>',
'<dl class="depth-legend"><div><dt>Inti</dt><dd>Setiap mahasiswa melakukannya sendiri.</dd></div><div><dt>Terapan</dt><dd>Mahasiswa melakukannya dengan templat, alat, atau bimbingan.</dd></div><div><dt>Pengenalan</dt><dd>Mahasiswa mengenali dan menafsirkannya.</dd></div></dl>',
'<button type="button" class="btn-toggle" id="toggle-capaian" aria-pressed="false">Tampilkan capaian subkompetensi</button>',
'<script>',
"document.addEventListener('DOMContentLoaded', function () {",
"  var b = document.getElementById('toggle-capaian');",
"  if (!b) return;",
"  b.addEventListener('click', function () {",
"    var on = document.body.classList.toggle('show-capaian');",
"    b.setAttribute('aria-pressed', on ? 'true' : 'false');",
"    b.textContent = on ? 'Sembunyikan capaian subkompetensi' : 'Tampilkan capaian subkompetensi';",
"  });",
"});",
'</script>',
'</div>', '```', '']
for t, did, tn, q, desc in TAHAP:
    head = f'{tn}. {q}' if t != 'Integrasi' else f'{tn}. {q}'
    out += [f'## {head} {{#{did} .domain-title style="--dc:var({VAR[t]})"}}', '', desc, '', '```{=html}', '<div class="card-grid">']
    for c in C.values():
        if c['tahap'] != t: continue
        n = sum(1 for v in S.values() if v['comp'] == c['code'])
        lis = ''.join(
            f'<li><a href="{skill_url(k)}" title="Capaian: {e(v["capaian"])}"><span class="code">{k}</span>'
            f'<span class="s-text"><span class="s-name">{e(v["nama"])}</span><span class="s-outcome">{e(v["capaian"])}</span></span>'
            f'<span class="depth depth-{KELAS[v["depth"]]}">{v["depth"]}</span></a></li>'
            for k, v in S.items() if v['comp'] == c['code'])
        out.append(
            f'<article class="comp-card" style="--dc:var({VAR[t]})"><header><p class="card-meta"><span class="dot"></span><span class="code">{c["code"]}</span><span>{n} subkompetensi</span></p>'
            f'<h3><a href="{comp_url(c["code"])}">{e(c["nama"])}</a></h3>'
            f'<p class="card-stmt"><span class="stmt-label">Capaian</span> {e(c["capaian"])}</p></header>'
            f'<ol class="skill-list">{lis}</ol></article>')
    out += ['</div>', '```', '']
out += ['## Kemampuan dari mata kuliah sebelumnya {#x-skills}', '',
        'Kemampuan ini berasal dari Biostatistika dan mata kuliah sebelumnya. Mata kuliah ini memakainya tanpa mengajarkannya lagi.',
        '', '| Kode | Kemampuan |', '|-|-|']
out += [f'| {k} | {v} |' for k, v in X.items()]
open(f'{site}/skills.md', 'w', newline='', encoding='utf-8').write('\r\n'.join(out) + '\r\n')

print(f'{nC} kompetensi, {nS} subkompetensi, {len(X)} kemampuan prasyarat')
for w in warn: print('PERINGATAN:', w)
if not warn: print('Pemeriksaan 02: tidak ada peringatan')
