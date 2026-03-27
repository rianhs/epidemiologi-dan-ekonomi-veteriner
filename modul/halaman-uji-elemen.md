---
layout: default
title: "Halaman Uji Elemen"
description: "Pengujian berbagai elemen yang didukung dalam templat ini"
prev_url: ""
prev_title: ""
next_url: ""
next_title: ""
---

## A. Diagram Batang

<div class="chart-wrapper">
  <canvas class="js-chart"
    data-type="bar"
    data-label="Jumlah Kasus"
    data-labels='["Jan", "Feb", "Mar", "Apr", "Mei", "Jun"]'
    data-values='[12, 19, 8, 15, 22, 10]'>
  </canvas>
  <p class="text-xs text-center text-slate-500 mt-2">Diagram 1. Jumlah kasus penyakit per bulan (ilustrasi).</p>
</div>

## B. Diagram Garis

<div class="chart-wrapper">
  <canvas class="js-chart"
    data-type="line"
    data-label="Prevalensi (%)"
    data-labels='["2018", "2019", "2020", "2021", "2022", "2023"]'
    data-values='[3.2, 4.1, 6.8, 5.5, 4.9, 3.7]'>
  </canvas>
  <p class="text-xs text-center text-slate-500 mt-2">Diagram 2. Tren prevalensi penyakit selama enam tahun (ilustrasi).</p>
</div>

## C. Diagram Diagram Alir

Diagram alir **tidak bisa** dibuat secara otomatis dari Markdown biasa. Ada dua opsi yang tersedia dalam sistem ini:

1. **Gambar statis** — buat diagram alir di aplikasi lain (misalnya draw.io atau Canva), ekspor sebagai gambar, lalu sisipkan ke modul.
2. **HTML manual** — diagram alir sederhana bisa dibuat dengan HTML dan CSS secara langsung di dalam file `.md`, seperti contoh berikut.

<div style="display: flex; flex-direction: column; align-items: center; gap: 0; margin: 2rem 0; font-size: 0.9rem;">
  <div style="background: #4f46e5; color: white; padding: 0.6rem 1.5rem; border-radius: 0.5rem; font-weight: 600;">Mulai</div>
  <div style="width: 2px; height: 1.5rem; background: #94a3b8;"></div>
  <div style="border: 2px solid #4f46e5; padding: 0.6rem 1.5rem; border-radius: 0.5rem; color: #0f172a; background: white;">Identifikasi kasus</div>
  <div style="width: 2px; height: 1.5rem; background: #94a3b8;"></div>
  <div style="border: 2px solid #f59e0b; padding: 0.6rem 1.5rem; border-radius: 0.5rem; background: #fef3c7; color: #92400e; font-weight: 600;">Apakah memenuhi definisi kasus?</div>
  <div style="display: flex; align-items: flex-start; gap: 3rem; margin-top: 0;">
    <div style="display: flex; flex-direction: column; align-items: center;">
      <div style="width: 2px; height: 1.5rem; background: #94a3b8;"></div>
      <div style="font-size: 0.75rem; color: #64748b; margin-bottom: 0.25rem;">Ya</div>
      <div style="border: 2px solid #4f46e5; padding: 0.6rem 1.5rem; border-radius: 0.5rem; background: white;">Laporkan ke dinas</div>
    </div>
    <div style="display: flex; flex-direction: column; align-items: center;">
      <div style="width: 2px; height: 1.5rem; background: #94a3b8;"></div>
      <div style="font-size: 0.75rem; color: #64748b; margin-bottom: 0.25rem;">Tidak</div>
      <div style="border: 2px solid #94a3b8; padding: 0.6rem 1.5rem; border-radius: 0.5rem; background: white; color: #64748b;">Pemantauan lanjut</div>
    </div>
  </div>
</div>

<p class="text-xs text-center text-slate-500">Diagram 3. Alur sederhana identifikasi kasus (ilustrasi).</p>

## D. Rumus Matematika

Rumus dapat ditulis secara *inline* maupun *display*. Berikut beberapa contoh.

### I. Rumus inline

Incidence rate dihitung dengan rumus $IR = \frac{D}{PT}$, di mana $D$ adalah jumlah kasus baru dan $PT$ adalah person-time at risk.

### II. Rumus display

**Rumus prevalensi:**

$$P = \frac{\text{Jumlah kasus aktif}}{\text{Jumlah populasi berisiko}} \times 100\%$$

**Rumus ukuran sampel:**

$$n = \frac{Z^2 \times p \times (1-p)}{d^2}$$

**Rumus odds ratio:**

$$OR = \frac{a \times d}{b \times c}$$

## E. Tabel

| Parameter | Rumus | Satuan |
|-----------|-------|--------|
| Incidence Rate | $\frac{D}{PT}$ | Kasus per hewan-tahun |
| Prevalensi | $\frac{D}{N} \times 100$ | % |
| Case Fatality Rate | $\frac{\text{Kematian}}{\text{Kasus}} \times 100$ | % |
| Attack Rate | $\frac{\text{Kasus baru}}{\text{Populasi awal}} \times 100$ | % |

## F. Callout

<div class="callout">
  <i data-lucide="info" class="w-5 h-5"></i>
  <p>Callout digunakan untuk menyoroti informasi penting yang perlu diperhatikan pembaca. Gunakan elemen ini dengan hemat agar tidak kehilangan efeknya.</p>
</div>

<div class="callout" style="background-color: rgba(245, 158, 11, 0.06); border-color: rgba(245, 158, 11, 0.2);">
  <i data-lucide="triangle-alert" class="w-5 h-5" style="color: #f59e0b;"></i>
  <p>Callout peringatan bisa dibuat dengan mengubah warna secara manual melalui atribut <code>style</code>.</p>
</div>

## G. Tombol Simulasi

<div class="btn-container">
  <a href="#" class="btn-action shadow-md">
    <span>Buka Simulasi</span>
    <i data-lucide="chevron-right" class="w-4 h-4"></i>
  </a>
</div>

## H. Kuis

<div class="p-6 md:p-8 rounded-2xl bg-[#f2f2f2] dark:bg-[#0d0d0d] border border-slate-200 dark:border-white/5 shadow-sm" data-quiz>
  <h4 class="text-lg font-semibold mb-2">Pertanyaan Uji</h4>
  <p class="text-slate-600 dark:text-slate-400">Manakah yang merupakan ukuran frekuensi penyakit yang paling tepat untuk penyakit kronis dengan durasi panjang?</p>
  <div class="space-y-3">
    <label class="flex items-start gap-3 p-4 rounded-xl border border-slate-200 dark:border-slate-800 hover:bg-slate-50 dark:hover:bg-slate-800 transition cursor-pointer">
      <input type="radio" name="q1" value="a" class="mt-1.5 accent-brand">
      <span>Incidence rate</span>
    </label>
    <label class="flex items-start gap-3 p-4 rounded-xl border border-slate-200 dark:border-slate-800 hover:bg-slate-50 dark:hover:bg-slate-800 transition cursor-pointer">
      <input type="radio" name="q1" value="b" data-correct class="mt-1.5 accent-brand">
      <span>Prevalensi</span>
    </label>
    <label class="flex items-start gap-3 p-4 rounded-xl border border-slate-200 dark:border-slate-800 hover:bg-slate-50 dark:hover:bg-slate-800 transition cursor-pointer">
      <input type="radio" name="q1" value="c" class="mt-1.5 accent-brand">
      <span>Attack rate</span>
    </label>
    <label class="flex items-start gap-3 p-4 rounded-xl border border-slate-200 dark:border-slate-800 hover:bg-slate-50 dark:hover:bg-slate-800 transition cursor-pointer">
      <input type="radio" name="q1" value="d" class="mt-1.5 accent-brand">
      <span>Case fatality rate</span>
    </label>
  </div>
  <div class="mt-8 flex items-center gap-4">
    <button data-check class="bg-brand hover:bg-indigo-700 text-white transition font-medium">Periksa Jawaban</button>
    <button data-reset class="text-slate-500 hover:text-slate-700 dark:hover:text-slate-300 text-sm font-medium">Reset</button>
  </div>
  <div data-feedback class="mt-4 font-medium hidden"></div>
</div>

## I. Gambar dengan Keterangan

<figure>
  <img src="https://images.unsplash.com/photo-1628595351029-c2bf17511435?auto=format&fit=crop&q=80&w=800" style="width: 500px;" alt="Ilustrasi analisis data epidemiologi">
  <figcaption>Gambar 1. Ilustrasi analisis data dalam kajian epidemiologi veteriner.</figcaption>
</figure>

## J. Blockquote

> Epidemiologi adalah ilmu dasar kesehatan masyarakat. Tanpanya, kita tidak bisa membedakan mana yang kebetulan dan mana yang merupakan pola yang bermakna.

## K. Daftar Bertingkat

Berikut contoh daftar bertingkat yang mendukung hingga empat level:

1. Pendekatan epidemiologi
   1. Deskriptif
      1. Studi kasus
      2. Studi ekologi
   2. Analitis
      1. Observasional
         1. Kohort
         2. Kasus-kontrol
         3. Potong lintang
      2. Eksperimental
2. Ukuran epidemiologi
   - Frekuensi
   - Asosiasi
   - Dampak
