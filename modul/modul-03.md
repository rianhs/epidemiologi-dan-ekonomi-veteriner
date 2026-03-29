---
layout: default
title: "Modul 3: Frekuensi dan Distribusi Kejadian Penyakit"
prev_url: modul/modul-02
prev_title: "Modul 2: Dinamika Penyakit dalam Populasi"
next_url: modul/modul-04
next_title: "Modul 4: Uji Diagnostik"
---

## A. Posisi modul dalam struktur capaian pembelajaran

Salah satu capaian pembelajaran dalam mata kuliah ini, yaitu CPMK-1 adalah “*Mahasiswa mampu mengevaluasi status kesehatan populasi hewan melalui integrasi konsep epidemiologi deskriptif dan analitis sebagai dasar pengambilan keputusan.*”

CPMK-1 memiliki beberapa Sub-CPMK sebagai turunannya, salah satunya adalah Sub-CPMK-3, yaitu “*Mahasiswa mampu menganalisis kejadian penyakit pada populasi hewan berdasarkan parameter morbiditas, mortalitas, serta pola distribusi demografis, spasial, dan temporal*.” Modul ini dirancang sebagai bahan ajar untuk Sub-CPMK-3.

Penguasaan Sub-CPMK-3 akan membekali mahasiswa dengan cara mengukur kejadian penyakit dan bagaimana cara mendeskripsikannya dalam populasi. Setelah menyelesaikan modul ini, mahasiswa akan siap untuk mempelajari bagaimana cara memastikan bahwa angka yang kita dapatkan benar-benar akurat melalui pembahasan mengenai uji diagnostik pada Modul 4.


## B. Indikator keberhasilan

Keberhasilan pembelajaran pada modul (Sub-CPMK) ini diukur melalui empat indikator.

| Kode | Uraian indikator |
| ----- | ----- |
| Indikator 3.1 | Ketepatan perhitungan ukuran frekuensi kejadian penyakit (parameter morbiditas dan mortalitas) berdasarkan data populasi. |
| Indikator 3.2 | Ketepatan interpretasi makna epidemiologis dari hasil ukuran frekuensi kejadian penyakit untuk menilai status kesehatan populasi. |
| Indikator 3.3 | Ketepatan deskripsi pola kejadian penyakit berdasarkan data demografis (who), spasial (where), dan temporal (when). |
| Indikator 3.4 | Ketepatan interpretasi hasil penyajian epidemiologi deskriptif untuk mengidentifikasi kelompok hewan (who), lokasi (where), dan waktu (when) yang paling terdampak. |


## C. Bentuk penilaian

Penguasaan Sub-CPMK-3 dinilai dengan dua bentuk.

| No | Bentuk | Metode | Proporsi terhadap nilai akhir |
| :---: | ----- | ----- | :---: |
| 1 | Non-tes | Tugas berbasis masalah | 5% |
| 2 | Tes | Ujian tengah semester | 5% |


## D. Alokasi waktu dan kegiatan belajar

Sub-CPMK-3 dirancang untuk diselesaikan dalam satu kegiatan belajar (satu pekan), yang terdiri atas 120 menit kegiatan belajar mandiri, 100 menit kegiatan belajar terbimbing (perkuliahan tatap muka), dan 120 menit menyelesaikan kegiatan penugasan terstruktur.

| Pekan | Kode | Topik |
| :---: | ----- | ----- |
| 3 | Kegiatan belajar 3.1 | Epidemiologi deskriptif |


### Kegiatan Belajar 3.1: Frekuensi dan distribusi kejadian penyakit

#### I. Peta konsep

```text
Frekuensi dan distribusi kejadian penyakit
├── Standar dan alat hitung dasar 
│   ├── Definisi kasus 
│   └── Alat ukur dasar: rasio, proporsi, dan laju
├── Ukuran kesakitan (morbiditas)
│   ├── Prevalensi
│   │   ├── Prevalensi titik 
│   │   └── Prevalensi periode
│   │       └── Prevalensi seumur hidup
│   ├── Insidensi
│   │   ├── Insidensi kumulatif 
│   │   │   └── Tingkat serangan 
│   │   └── Laju insidensi 
│   └── Hubungan prevalensi dan insidensi
├── Ukuran kematian (mortalitas)
│   ├── Angka kematian kasar 
│   ├── Angka kematian spesifik 
│   └── Tingkat kematian kasus
└── Epidemiologi deskriptif
    ├── Distribusi demografis (who)
    ├── Distribusi spasial (where)
    └── Distribusi temporal (when)
```

<p class="chart-caption">Gambar 3.1. Peta konsep dalam modul ini.</p>

#### II. Uraian materi

##### A. Konsep dasar

###### 1. Mengapa kejadian penyakit perlu diukur

Pada modul sebelumnya, kita telah mempelajari bagaimana penyakit menyebar dalam populasi. Pertanyaan selanjutnya adalah, “Seberapa parah situasi penyakit tersebut?” Dalam epidemiologi, kita tidak bisa hanya mengandalkan persepsi atau perasaan seperti "banyak hewan yang sakit" atau "kematian ternak sedang meningkat". Kita membutuhkan angka yang pasti.

Mengukur kejadian penyakit secara kuantitatif (menggunakan angka) sangat diperlukan agar kita bisa mengambil keputusan yang tepat. Tanpa angka, kita tidak akan tahu apakah sebuah program vaksinasi berhasil atau apakah suatu wabah sudah mulai mereda.

Ada dua alasan utama mengapa kita harus mengukur kejadian penyakit dengan cermat:

a. Memberikan konteks melalui populasi berisiko. 

Dalam epidemiologi, angka kasus (pembilang) tidak akan berarti apa-apa jika kita tidak mengetahui jumlah total populasi yang berisiko tertular (penyebut). Mari kita lihat perbandingannya pada tabel berikut. 

<p class="chart-caption">Tabel 3.1. Perbandingan makna angka kasus berdasarkan populasi berisiko.</p>

| Skenario | Jumlah kasus (sapi sakit) | Total populasi | Makna epidemiologis |
| :---: | :---: | :---: | ----- |
| 1 | 5 ekor | 10 ekor | Sangat parah. Separuh populasi (50%) sakit. |
| 2 | 5 ekor | 1.000 ekor | Ringan. Hanya sedikit sekali (0,5%) yang sakit. |

Dari tabel di atas, kita bisa melihat bahwa angka "5 ekor" bisa berarti bencana di satu tempat, tetapi mungkin dianggap biasa di tempat lain. Inilah alasan mengapa kita selalu membutuhkan data populasi sebagai angka pembagi (denominator).

b. Memasukkan komponen waktu

Penyakit adalah peristiwa yang dinamis. Angka kejadian penyakit harus selalu disertai dengan keterangan waktu agar kita bisa melihat kecepatannya.
* Jika ada 10 ekor sapi mati dalam satu hari, kita sedang menghadapi situasi darurat atau wabah yang sangat ganas.
* Jika 10 ekor sapi mati dalam satu tahun, kita mungkin melihatnya sebagai kejadian yang biasa terjadi di suatu wilayah.

Tanpa unsur waktu, kita tidak mampu mengukur kecepatan penyebaran penyakit.

Apa langkah selanjutnya?

Setelah kita tahu mengapa angka itu penting, kita harus memastikan bahwa apa yang kita hitung adalah benar-benar "kasus" yang kita cari. Kita tidak boleh sembarangan memasukkan hewan ke dalam hitungan. Oleh karena itu, pada bagian selanjutnya kita akan membahas bagaimana cara mendefinisikan sebuah kasus secara standar.

###### 2. Mendefinisikan kasus

Sebelum kita mulai menghitung, kita harus sepakat terlebih dahulu mengenai apa yang disebut sebagai "sakit". Jika setiap orang memiliki kriteria yang berbeda-beda dalam menentukan hewan yang sakit, maka angka frekuensi yang kita hasilkan akan menjadi kacau dan tidak bisa dibandingkan.

Definisi kasus adalah sekumpulan kriteria standar untuk menentukan apakah seekor individu dapat digolongkan sebagai "kasus" untuk penyakit tertentu. Definisi ini harus jelas, spesifik, dan mudah diterapkan oleh petugas di lapangan.

Sebagai contoh, jika kita ingin mendata kejadian penyakit mulut dan kuku (PMK) di sebuah kabupaten:
* Definisi yang kurang baik: "*Setiap sapi yang tampak lemas dan tidak mau makan*." Definisi ini terlalu luas karena sapi yang mengalami cacingan atau demam biasa juga bisa menunjukkan tanda klinis yang sama.
* Definisi yang lebih baik: "*Setiap sapi yang ditemukan memiliki luka lepuh (vesikel) atau erosi pada gusi, lidah, atau celah kuku.*" Definisi ini jauh lebih spesifik dan mengarah langsung pada ciri khas PMK.

Ada tiga tingkatan definisi kasus. Pembagian ini sangat bergantung pada seberapa kuat bukti yang kita miliki.

<p class="chart-caption">Tabel 3.2. Tingkatan definisi kasus dalam epidemiologi.</p>

| Tingkatan | Istilah | Kriteria utama | Contoh definisi kasus untuk PMK |
| ----- | ----- | ----- | ----- |
| Tingkat 1 | Kasus suspek (suspect case) | Berdasarkan tanda klinis yang terlihat secara kasat mata | Sapi yang memiliki luka lepuh di mulut dan kaki serta mengeluarkan liur berlebih |
| Tingkat 2 | Kasus probabel (probable case) | Kasus suspek yang memiliki kaitan epidemiologis dengan kasus positif lainnya | Sapi dengan luka lepuh yang berada di satu kandang dengan sapi yang sudah dinyatakan positif PMK |
| Tingkat 3 | Kasus terkonfirmasi (confirmed case) | Kasus yang sudah dibuktikan melalui uji laboratorium yang valid | Sapi yang hasil uji PCR-nya menunjukkan positif virus PMK, meskipun sapi tersebut mungkin belum terlihat sakit |

Mengapa kita perlu membedakan tingkatan ini?

Di lapangan, kita sering kali tidak memiliki cukup waktu atau biaya untuk menguji semua hewan di laboratorium. Dengan adanya tingkatan ini, kita tetap bisa melakukan tindakan pengendalian segera pada tingkat "suspek" tanpa harus menunggu hasil laboratorium. Namun, untuk laporan resmi, terutama bagi dunia internasional atau ekspor-impor, biasanya hanya "kasus terkonfirmasi" yang diakui.

Kita juga perlu memahami bahwa definisi kasus bisa berubah seiring waktu. Pada awal sebuah wabah, kita mungkin menggunakan definisi yang sangat luas agar tidak ada kasus yang terlewat. Namun, setelah wabah mulai terkendali, kita biasanya memperketat definisi kasus agar sumber daya kita lebih fokus pada hewan yang benar-benar sakit.

Setelah kita berhasil menentukan siapa saja yang termasuk dalam "kasus", langkah selanjutnya adalah menyajikan data tersebut dalam bentuk angka. Untuk itu, kita perlu memahami tiga alat ukur dasar: rasio, proporsi, dan laju.

###### 3. Rasio, proporsi, dan laju

Kita sudah menentukan siapa yang menjadi "kasus" dan siapa yang menjadi "populasi". Langkah berikutnya adalah menyajikan data tersebut dalam bentuk angka yang bermakna.

Ada tiga alat ukur dasar yang sering kita gunakan untuk membandingkan angka-angka tersebut, yaitu rasio, proporsi, dan laju (sering juga disebut rate). Meskipun ketiganya terlihat mirip, mereka memiliki kegunaan yang berbeda.

1. Rasio (ratio). 
	Rasio adalah perbandingan antara dua nilai yang tidak saling berkaitan. Artinya, pembilang (angka di atas) bukan merupakan bagian dari penyebut (angka di bawah). Kita menggunakan rasio untuk membandingkan dua kelompok yang berbeda. 
	
	Contoh: Di sebuah peternakan, terdapat 80 ekor sapi betina dan 20 ekor sapi jantan. Rasio jenis kelamin di peternakan tersebut adalah 80:20 atau 4:1. Artinya, untuk setiap satu ekor jantan, terdapat empat ekor betina. Di sini, sapi jantan bukan bagian dari kelompok sapi betina.
	
2. Proporsi (proportion). 
	Berbeda dengan rasio, proporsi adalah perbandingan ketika pembilang merupakan bagian dari penyebut. Hasilnya kita nyatakan dalam bentuk pecahan, persentase, atau desimal. Proporsi membantu kita melihat seberapa besar bagian dari keseluruhan populasi yang terdampak. 
	
	Contoh: Dari 100 ekor ayam di sebuah kandang, 15 ekor di antaranya terkena penyakit snot. Proporsi ayam yang sakit adalah 15/100 atau 15% atau 0,15. Di sini, 15 ekor ayam yang sakit adalah bagian dari total 100 ekor ayam di kandang tersebut. 
	
3. Laju (rate). 
	Laju adalah ukuran yang lebih kompleks karena kita memasukkan unsur waktu ke dalam penyebutnya. Laju memberi tahu kita seberapa cepat suatu peristiwa (seperti penularan penyakit atau kematian) terjadi dalam populasi selama periode tertentu. 
	
	Contoh: Bayangkan speedometer pada motor. Angka "60 km/jam" adalah sebuah laju. Ia memberi tahu kita seberapa cepat kita berpindah tempat. Dalam epidemiologi, laju bisa berupa "5 kasus baru per bulan". Tanpa keterangan waktu, kita tidak bisa menyebut sebuah angka sebagai laju.

Perhatikan tabel perbandingan berikut ini untuk membedakan ketiga istilah tersebut.

<p class="chart-caption">Tabel 3.3. Perbandingan antara rasio, proporsi, dan laju.</p>

| Aspek | Rasio | Proporsi | Laju |
| ----- | ----- | ----- | ----- |
| Definisi | Perbandingan antara dua kelompok yang berbeda | Perbandingan ketika pembilang adalah bagian dari penyebut | Perbandingan yang menyertakan unsur waktu dalam penyebut |
| Dinyatakan sebagai | A dibanding B atau A:B | Pecahan, persentase, atau desimal (A / [A+B]) | Per satuan waktu (A / B per satuan waktu) |
| Kegunaan | Membandingkan dua besaran yang berbeda | Melihat beban masalah dalam satu kelompok | Mengukur kecepatan munculnya peristiwa |
| Contoh | Rasio dokter hewan terhadap jumlah ternak di suatu desa | Proporsi sapi yang positif brucellosis dari total populasi | Jumlah kasus baru rabies per tahun di suatu provinsi |

Dalam laporan kesehatan, istilah "angka" atau "tingkat" sering kali digunakan untuk mengekspresikan proporsi atau laju. Namun, kita harus jeli melihat apakah angka tersebut memiliki unsur waktu atau tidak. Pemahaman tentang rasio, proporsi, dan laju merupakan fondasi utama sebelum kita masuk ke pembahasan yang lebih dalam mengenai ukuran kesakitan (morbiditas) dan ukuran kematian (mortalitas) pada bagian selanjutnya.

##### B. Frekuensi kejadian penyakit

###### 1. Ukuran kesakitan (morbiditas)

Morbiditas digunakan untuk menggambarkan seberapa banyak hewan yang sakit atau seberapa besar risiko hewan untuk menjadi sakit dalam suatu populasi. Kita perlu mengukur morbiditas karena tidak semua penyakit menyebabkan kematian. Banyak penyakit hewan yang "hanya" menurunkan produksi susu, menghambat pertumbuhan, atau menyebabkan kemajiran (mandul). Meskipun hewannya tidak mati, kerugian ekonominya bisa sangat besar.

Dalam morbiditas, ada dua istilah utama yang akan selalu kita gunakan: prevalensi dan insidensi. Banyak orang sering tertukar dalam menggunakan kedua istilah ini, padahal maknanya sangat berbeda.

Untuk memudahkan, mari kita gunakan analogi bak mandi:
* Insidensi adalah aliran air yang baru masuk ke bak mandi. Ia menggambarkan munculnya kasus-kasus baru.
* Prevalensi adalah seluruh air yang ada di dalam bak mandi pada saat itu. Ia menggambarkan beban penyakit secara keseluruhan.

###### 1a. Prevalensi

Prevalensi adalah proporsi kasus dalam suatu populasi pada titik waktu tertentu (pada prevalensi titik) atau selama periode waktu tertentu (pada prevalensi periode). Prevalensi membantu kita menjawab pertanyaan: "Seberapa besar beban penyakit ini di populasi kita sekarang?"

Karena prevalensi adalah sebuah proporsi, maka nilainya berkisar antara 0 sampai 1. Namun, ia sering dinyatakan dalam bentuk persentase (%).

Rumus umumnya adalah:

*Prevalensi = Jumlah kasus / Jumlah populasi*

Berdasarkan jangka waktunya, kita membagi prevalensi menjadi tiga tipe:

1. Prevalensi titik (point prevalence)

Ini adalah potret sesaat mengenai situasi penyakit. Bayangkan kita datang ke sebuah peternakan, lalu memeriksa semua kambing untuk melihat siapa yang terkena scabies.

Contoh: Dari 1.000 ekor kambing yang kita periksa pada tanggal 17 Agustus, ada 50 kambing yang sedang menderita scabies. Oleh karena itu, prevalensi titiknya adalah 50/1.000 = 5%.

2. Prevalensi periode (period prevalence)

Parameter ini menunjukkan seberapa banyak hewan yang sakit selama rentang waktu tertentu (misalnya selama satu tahun). Angka ini mencakup kasus lama yang sudah ada sejak awal periode ditambah kasus baru yang muncul selama periode tersebut.

Contoh: Masih di peternakan kambing dengan 1.000 populasi. Dalam 12 bulan terakhir, ada 150 ekor kambing yang pernah menderita scabies. Oleh karena itu, prevalensi periodenya adalah 150/1.000 = 15%.

2a. Prevalensi seumur hidup (lifetime prevalence)

Ukuran ini merupakan subtipe dari prevalensi periode. Namun, rentang waktunya adalah seluruh masa hidup hewan tersebut. Ia menunjukkan apakah hewan tersebut pernah menderita penyakit itu setidaknya sekali seumur hidupnya.

Contoh: Kita ingin tahu apakah seekor kambing pernah menderita scabies selama ia hidup. Jika dari 1.000 kambing, ada 250 ekor yang pernah terkena scabies, baik pada masa lalu maupun masa kini, maka prevalensi seumur hidupnya adalah 25%.

Untuk membandingkan ketiganya, mari kita perhatikan tabel berikut.

<p class="chart-caption">Tabel 3.4. Perbandingan tipe-tipe prevalensi.</p>

| Unsur | Prevalensi titik | Prevalensi periode | Prevalensi seumur hidup |
| ----- | ----- | ----- | ----- |
| Deskripsi | Proporsi populasi yang mengalami suatu penyakit pada titik waktu tertentu | Proporsi populasi yang mengalami suatu penyakit selama periode tertentu | Proporsi populasi yang mengalami suatu penyakit kapan pun dalam hidupnya |
| Jangka waktu | Satu titik waktu tertentu (contoh: hari ini) | Periode tertentu (contoh: 1 tahun) | Seluruh rentang hidup hewan |
| Kegunaan | Menggambarkan beban penyakit saat tertentu | Memperkirakan beban penyakit dalam jangka menengah | Mengukur dampak kumulatif penyakit pada populasi |
| Pertanyaan | "Berapa banyak hewan yang sakit saat ini?" | "Berapa banyak hewan yang sakit selama periode ini?" | "Berapa banyak hewan yang pernah sakit seumur hidupnya?" |

Perlu kita pahami bahwa prevalensi sangat dipengaruhi oleh durasi penyakit. Penyakit yang bersifat kronis (berlangsung lama) seperti paratuberkulosis sapi cenderung memiliki prevalensi yang tinggi karena kasus-kasus lama terus menumpuk di dalam populasi. Sebaliknya, penyakit yang sembuhnya cepat atau menimbulkan kematian dengan cepat biasanya memiliki prevalensi yang rendah.

Setelah kita memahami beban penyakit melalui prevalensi, sekarang kita akan mempelajari seberapa cepat kasus baru muncul melalui ukuran insidensi.

###### 1b. Insidensi

Jika prevalensi berbicara tentang "beban" penyakit yang sudah ada, maka insidensi berbicara tentang "perubahan". Insidensi mengukur munculnya kasus-kasus baru pada suatu populasi, yang dapat dihitung sebagai proporsi atau risiko (pada insidensi kumulatif) atau kecepatan (pada laju insidensi). Ukuran ini sangat penting karena membantu kita memahami seberapa cepat penyakit menyebar dan seberapa besar risiko seekor hewan untuk tertular.

Dalam insidensi, kita hanya menghitung hewan yang awalnya tidak sakit (nonkasus) tetapi kemudian menjadi sakit (menjadi kasus) selama periode pengamatan. Ada dua cara utama untuk mengukur insidensi, yaitu insidensi kumulatif dan laju insidensi.
 
1. Insidensi kumulatif (cumulative incidence)

Insidensi kumulatif mengukur probabilitas atau risiko seekor hewan untuk jatuh sakit dalam jangka waktu tertentu. Ukuran ini sering kita sebut sebagai proporsi insidensi.
 
Rumusnya:

Insidensi kumulatif = Jumlah kasus baru selama periode tertentu / 
Jumlah populasi berisiko (nonkasus) pada awal periode

Contoh: Kita mengamati 100 ekor sapi yang awalnya tidak mastitis selama satu tahun. Dalam periode setahun ini, ternyata 10 ekor sapi terkena mastitis. Oleh karena itu, insidensi kumulatifnya adalah 10/100 = 10% selama satu tahun. Artinya, setiap sapi memiliki risiko 10% untuk terkena mastitis dalam satu tahun.

Perhatikan bahwa insidensi kumulatif merupakan proporsi. Dimensi waktu tidak dimasukkan secara langsung dalam perhitungannya. Oleh karena itu, jangka waktu pengamatan harus selalu disebutkan agar maknanya tidak disalahartikan. Mari kita lihat dua skenario berikut.

* Skenario 1: Jika 100 sapi dipantau selama satu tahun dan 5 di antaranya mengalami mastitis dalam periode satu tahun tersebut, insidensi kumulatifnya adalah 5%.
* Skenario 2: Jika 100 sapi dipantau selama dua tahun dan 5 di antaranya mengalami mastitis dalam periode dua tahun tersebut, insidensi kumulatifnya juga tetap 5%.

Kedua skenario di atas memiliki insidensi kumulatif yang sama, yaitu 5%. Agar pembaca tidak salah memahami, jangka waktu harus selalu dilaporkan dengan angka insidensi kumulatif. Contoh:

* Insidensi kumulatif mastitis pada skenario 1 adalah 5% selama 1 tahun. Artinya, 5% sapi pada awal penelitian kemudian mengalami mastitis dalam periode satu tahun.
* Insidensi kumulatif mastitis pada skenario 2 adalah 5% selama 2 tahun. Artinya, 5% sapi pada awal penelitian kemudian mengalami mastitis dalam periode dua tahun.

Catatan: kita tidak dapat membagi insidensi kumulatif dengan tahun karena kasus baru mungkin tidak terdistribusi secara merata selama periode pengamatan. Pada skenario 2, insidensi kumulatifnya adalah 5% dalam dua tahun. Kita tidak boleh menyimpulkan bahwa insidensi kumulatifnya adalah 2,5% dalam satu tahun. Kesimpulan ini keliru karena tahun tertentu mungkin memiliki lebih banyak kasus baru daripada tahun lainnya.

Selain dengan persentase, insidensi kumulatif juga diekspresikan dengan satuan hewan, terutama jika pertambahan kasus barunya sangat rendah. Sebagai contoh, insidensi kumulatif mastitis pada skenario 1 adalah 5% selama 1 tahun atau 5 kasus baru di antara 100 hewan berisiko. Pada penyakit lain, misalnya tetanus pada kuda, insidensi kumulatifnya adalah 0,003% selama satu tahun. Angka ini bisa diekspresikan dengan 3 kasus baru di antara 100.000 hewan berisiko selama satu tahun.

1a. Tingkat serangan (attack rate)

Ini adalah bentuk khusus dari insidensi kumulatif yang sering kita gunakan pada situasi wabah yang berlangsung singkat, misalnya keracunan pakan atau wabah influenza. Istilah "serangan" digunakan untuk menggambarkan betapa cepat dan masifnya penyakit menyerang kelompok nonkasus yang terpapar. Sementara itu, istilah “rate” sebenarnya keliru karena ukuran ini bukanlah laju, tetapi proporsi.

Contoh 1: 
Ada 50 ekor ayam yang sehat. Pada suatu hari, mereka diberi pakan dari sak baru yang ternyata terkontaminasi Salmonella. Dalam tiga hari, 15 ekor ayam mengalami diare berat. Tingkat serangannya adalah 15 kasus baru / 50 hewan berisiko = 30%. Artinya, risiko ayam untuk sakit setelah mengonsumsi pakan adalah 30%.

Tingkat serangan dapat dikategorikan menjadi tingkat serangan primer dan sekunder. Untuk lebih memahami perbedaan antara keduanya, lihat contoh berikut ini.

Contoh 2: 
Di kandang A, terdapat 200 ekor sapi yang sehat. Pada suatu hari, 20 ekor sapi baru didatangkan dari luar dan langsung digabungkan. Dalam waktu seminggu, 30 ekor dari 200 sapi lama menunjukkan tanda penyakit pernapasan akut. Tingkat serangan primer = 30 kasus baru / 200 sapi berisiko = 15%.

Satu ekor sapi yang sakit dari kandang A (kasus primer) dipindahkan ke kandang B yang berisi 20 ekor sapi sehat lainnya. Dalam seminggu berikutnya, 4 ekor sapi di kandang B ikut sakit. Tingkat serangan sekunder = 4 kasus baru (sekunder) / 20 sapi berisiko = 20%.

Kesimpulan:
* Tingkat serangan primer adalah 15% (dampak dari sumber paparan awal). 
* Tingkat serangan sekunder adalah 20% (penularan dari hewan ke hewan).

2. Laju insidensi (incidence rate)

Dalam pengamatan jangka panjang, jumlah populasi biasanya tidak stabil. Ada hewan yang dijual, ada hewan yang mati karena sebab lain, atau ada hewan yang baru masuk di tengah masa pengamatan. Jika kita menggunakan rumus insidensi kumulatif, hasilnya menjadi kurang akurat karena tidak semua hewan diamati dalam durasi yang sama.

Di sinilah kita membutuhkan laju insidensi (kadang juga disebut kepadatan insidensi). Ukuran ini tidak lagi menggunakan jumlah hewan sebagai penyebut, melainkan menggunakan komponen waktu internal (internal time component; disingkat ITC), yang dinyatakan dengan satuan hewan-waktu (animal-time).

ITC adalah jumlah total waktu yang dijalani oleh setiap individu dalam populasi selama mereka masih berisiko (masih sehat dan masih dalam masa pengamatan). Satuan yang kita gunakan bisa berupa hewan-tahun, hewan-bulan, atau hewan-hari.

Rumusnya:

Laju insidensi = Jumlah kasus baru selama periode tertentu / 
Jumlah waktu dari semua individu dalam populasi saat masih berisiko

Contoh 1:
Empat anjing sehat diamati selama satu tahun sejak 1 Januari hingga 31 Desember.
* Anjing A tetap sehat hingga akhir periode studi
* Anjing B terinfeksi parvovirus pada 1 April.
* Anjing C terinfeksi parvovirus pada 1 Juli.
* Anjing D hilang dan tidak dapat ditelusuri lagi pada 1 Oktober.

Jika menggunakan insidensi kumulatif, maka hasilnya 
= 2 kasus baru / 4 populasi non-kasus pada awal periode studi 
= 50% anjing sehat menjadi terinfeksi parvovirus dalam kurun waktu 1 tahun

Namun, jika kita menggunakan laju insidensi, waktu gabungan dari semua individu saat masih berisiko harus diperhitungkan. Gabungan angka ini dijadikan penyebut. Tabel dan gambar di bawah ini menjelaskan kontribusi setiap anjing terhadap angka penyebut.

<p class="chart-caption">Tabel 3.5. Rincian kontribusi waktu berisiko (hewan-tahun) pada empat individu anjing selama satu tahun pengamatan.</p>

| Kode anjing | Titik awal sebagai individu berisiko | Titik akhir sebagai individu berisiko | Durasi sebagai individu berisiko | Jumlah hewan × jumlah tahun |
| :---: | :---: | :---: | :---: | ----- |
| Anjing A | 1 Januari | 31 Desember | 1 tahun | 1 hewan-tahun |
| Anjing B | 1 Januari | 31 Maret | 0,25 tahun | 0,25 hewan-tahun |
| Anjing C | 1 Januari | 30 Juni | 0,50 tahun | 0,50 hewan-tahun |
| Anjing D | 1 Januari | 30 September | 0,75 tahun | 0,75 hewan-tahun |
| Waktu gabungan dari semua individu saat masih berisiko | | | | 2,5 hewan-tahun |

Total ITC (penyebut) kita adalah 1 + 0,25 + 0,5 + 0,75 = 2,5 hewan-tahun.

Karena ada 2 kasus baru, maka

laju insidensi = 2 kasus baru / 2,5 hewan-tahun 
 = 0,8 kasus baru per hewan-tahun 
 = 0,8 kasus baru per hewan per tahun 
 = 8 kasus baru per 10 hewan per tahun

<figure>
  <img src="img/gambar-03.02.png" 
       style="width: 500px;" 
       alt="Ilustrasi garis waktu dan perhitungan total waktu berisiko (hewan-tahun) pada empat individu anjing terkait infeksi parvovirus.">
  <figcaption>Gambar 3.2. Ilustrasi garis waktu dan perhitungan total waktu berisiko (hewan-tahun) pada empat individu anjing terkait infeksi parvovirus.</figcaption>
</figure>

Contoh 2:

Sebanyak 1.000 sapi sehat diamati selama satu tahun. Selama periode penelitian, ada 50 sapi yang menjadi sakit karena terinfeksi virus BVD. Detailnya dijelaskan dalam tabel ini.

<p class="chart-caption">Tabel 3.6. Rincian kontribusi waktu berisiko (hewan-tahun) pada populasi 1.000 ekor sapi selama satu tahun pengamatan.</p>

| Jumlah kelompok sapi | Titik awal sebagai individu berisiko | Titik akhir sebagai individu berisiko | Durasi sebagai individu berisiko | Jumlah hewan × jumlah tahun |
| :---: | :---: | :---: | :---: | ----- |
| 20 hewan | 1 Januari | 31 Maret | 0,25 tahun | 5 hewan-tahun |
| 10 hewan | 1 Januari | 30 Juni | 0,50 tahun | 5 hewan-tahun |
| 20 hewan | 1 Januari | 30 September | 0,75 tahun | 15 hewan-tahun |
| 950 hewan | 1 Januari | 31 Desember | 1 tahun | 950 hewan-tahun |
| Waktu gabungan dari semua individu saat masih berisiko | | | | 975 hewan-tahun |

<figure>
  <img src="img/gambar-03.03.png" 
       style="width: 500px;" 
       alt="Ilustrasi garis waktu dan perhitungan total waktu berisiko (hewan-tahun) pada populasi 1.000 ekor sapi terkait infeksi virus BVD.">
  <figcaption>Gambar 3.3. Ilustrasi garis waktu dan perhitungan total waktu berisiko (hewan-tahun) pada populasi 1.000 ekor sapi terkait infeksi virus BVD.</figcaption>
</figure>

Laju insidensi = Jumlah kasus baru / Jumlah hewan-waktu berisiko 
 = 50 / 975 
 = 0,0513 kasus baru per hewan-tahun 
 = 5,13 kasus baru per 100 hewan-tahun 
 = 5,13 kasus baru per 100 hewan per tahun

Dengan menggunakan ITC, kita bisa menghitung kecepatan munculnya penyakit dengan lebih akurat karena kita hanya menghitung waktu ketika hewan tersebut benar-benar berisiko untuk sakit.

Rangkuman perbedaan antara insidensi kumulatif dan laju insidensi dapat dilihat pada tabel di bawah ini:

<p class="chart-caption">Tabel 3.7. Perbandingan insidensi kumulatif dan laju insidensi.</p>

| Unsur | Insidensi kumulatif | Laju insidensi |
| ----- | ----- | ----- |
| Deskripsi | Proporsi kasus baru dalam populasi berisiko selama periode tertentu | Laju kasus baru dalam populasi berisiko selama periode tertentu |
| Fokus utama | Mengukur risiko atau peluang terjadinya kasus baru | Mengukur kecepatan munculnya kasus baru dalam populasi |
| Pembilang (numerator) | Jumlah kasus baru | Jumlah kasus baru |
| Penyebut (denominator) | Jumlah hewan berisiko (nonkasus) pada awal periode | Total hewan-waktu berisiko |
| Karakter populasi | Cocok untuk populasi yang stabil | Sangat cocok untuk populasi yang dinamis (jumlahnya bertambah dan/atau berkurang) |
| Pertanyaan | "Seberapa besar peluang hewan untuk sakit?" | "Seberapa cepat kasus baru muncul?" |
| Contoh jawaban | 10% dari sapi sehat mengalami mastitis dalam kurun waktu setahun | 5 kasus mastitis baru per 100 hewan-tahun |

Pemilihan antara insidensi kumulatif atau laju insidensi sangat bergantung pada ketersediaan data kita. Jika kita memiliki catatan harian yang lengkap mengenai kapan setiap hewan masuk, sakit, atau keluar dari kandang, maka laju insidensi adalah pilihan yang jauh lebih akurat.

Setelah kita memahami prevalensi dan insidensi, kita akan melihat bagaimana kedua angka ini sebenarnya saling berhubungan satu sama lain.

###### 1c. Hubungan antara prevalensi dan insidensi

Kita sudah membahas prevalensi sebagai gambaran beban penyakit dan insidensi sebagai kecepatan munculnya kasus baru. Sekarang, bagaimana keduanya saling memengaruhi?

Mari kita kembali ke analogi bak mandi yang kita gunakan sebelumnya. Proporsi air di dalam bak dibandingkan keseluruhan air (prevalensi) sangat bergantung pada dua hal, yaitu seberapa deras air yang mengalir masuk dari keran (insidensi) dan seberapa lama air itu tertahan di dalam bak sebelum keluar melalui lubang pembuangan (durasi penyakit).

<figure>
  <img src="img/gambar-03.04.png" 
       style="width: 500px;" 
       alt="Ilustrasi toren dan bak mandi untuk menggambarkan hubungan antara insidensi dan prevalensi.">
  <figcaption>Gambar 3.4. Ilustrasi toren dan bak mandi untuk menggambarkan hubungan antara insidensi dan prevalensi.</figcaption>
</figure>

Dengan analogi toren dan bak mandi, dinamika air di sistem ini bisa kita jabarkan ke dalam sebuah rumus.

Jika prevalensi adalah proporsi hewan yang sedang sakit (air di dalam bak mandi) dan dinyatakan dalam format desimal, maka sisa populasi yang tidak sedang sakit dapat kita nyatakan dengan (1 − Prevalensi).

Siapa saja kelompok (1 − Prevalensi) ini? Mereka adalah hewan yang masih rentan di dalam toren, ditambah hewan yang sudah sembuh dan keluar dari bak mandi. Catatan: hewan yang mati tidak masuk dalam kelompok ini karena mereka sudah hilang sepenuhnya dari total populasi.

Logikanya begini: aliran kasus baru (insidensi) sangat bergantung pada sisa hewan sehat di toren. Jika penyakit terus-menerus menular sehingga bak mandi terus terisi, sisa hewan sehat di toren pasti tinggal sedikit. Karena sumber hewannya hampir habis, kecepatan penularan (insidensi) secara alamiah pasti ikut melambat.

Oleh karena itu, kita tidak bisa memisahkan jumlah hewan sakit dengan sisa hewan sehat. Keduanya adalah rasio yang saling memengaruhi. Dalam keadaan yang seimbang, rasio antara hewan sakit dan hewan sehat sama dengan kecepatan penularan dikali lama waktu sakitnya. Hubungan ini menghasilkan rumus berikut:

Prevalensi / (1 - Prevalensi) = Insidensi × Rata-rata durasi penyakit

Sebagai alternatif, jika di lapangan kita sudah mengetahui beban penyakitnya dan ingin mencari tahu seberapa cepat penularan yang sedang terjadi (insidensi), rumusnya bisa kita ubah menjadi:

Insidensi = Prevalensi / [(1 - Prevalensi) × Rata-rata durasi penyakit]

Contoh skenario: Bayangkan kita mendatangi sebuah peternakan dan menemukan separuh populasi sapi di sana sedang menderita penyakit kronis. Artinya, prevalensi titik penyakit tersebut adalah 20% atau 0,2. Berdasarkan data medis, rata-rata sapi akan menderita penyakit ini selama 5 tahun (durasi) sebelum akhirnya sembuh atau mati.

Pertanyaannya, seberapa cepat penyakit ini sebenarnya menular (insidensi) di peternakan itu? Mari kita masukkan ke dalam rumus:

Insidensi = Prevalensi / [(1 - Prevalensi) × Durasi]

Insidensi = 0,2 / [(1 - 0,2) × 5]

Insidensi = 0,2 / [0,8 × 5]

Insidensi = 0,2 / 4

Insidensi = 0,05 kasus per hewan-tahun

Dari perhitungan ini, kita bisa menyimpulkan sesuatu yang bermakna. Untuk mempertahankan 20% hewan dalam keadaan sakit selama 5 tahun berturut-turut, penyakit tersebut menular dengan kecepatan 0,05 kasus baru per hewan-tahun (atau setara dengan 5 kasus baru per 100 ekor sapi setiap tahunnya).

Rumus di atas memang sangat akurat. Namun, dalam praktik sehari-hari di lapangan, rumus tersebut terkadang terasa terlalu rumit untuk dihitung dengan cepat. Bisakah kita menyederhanakannya? Jawabannya: bisa, tetapi dengan syarat khusus.

Coba bayangkan sebuah penyakit langka yang prevalensinya sangat rendah, misalnya hanya 1% (atau 0,01). Jika kita menghitung kelompok sisa populasi (1 - Prevalensi), hasilnya adalah 1 - 0,01 = 0,99.

Angka 0,99 ini sangat mendekati angka 1. Dalam matematika, membagi angka apa pun dengan angka 1 tidak akan mengubah hasil akhirnya. Karena pengaruhnya nyaris tidak ada, para ahli epidemiologi sepakat untuk membuang unsur pembagi (1 - Prevalensi) tersebut demi kepraktisan di lapangan.

Hasilnya, kita mendapatkan rumus yang jauh lebih sederhana:

Perkiraan prevalensi ≈ insidensi × rata-rata durasi penyakit

(Perhatikan penggunaan tanda "≈" atau "kira-kira" karena ini adalah rumus pendekatan).

Mari kita buktikan dengan contoh skenario:

Sebuah kabupaten memiliki 500.000 ekor sapi. Sebuah studi menemukan ada 150 kasus penyakit baru per 100.000 sapi setiap tahunnya. Penyakit ini bersifat kronis dan tidak dapat disembuhkan sehingga durasi rata-ratanya sangat panjang, katakanlah 20 tahun.

Insidensi penyakit ini = 150 kasus baru / 100.000 hewan-tahun 
 = 0,0015 kasus baru per hewan-tahun

Sekarang, mari kita hitung prevalensinya menggunakan rumus sederhana dari modul ini, lalu kita bandingkan dengan rumus lengkap yang lebih presisi.


Perkiraan prevalensi ≈ insidensi × rata-rata durasi penyakit 
 ≈ 0,0015 kasus per hewan per tahun × 20 tahun 
 ≈ 0,03 ≈ 3%

Perkiraan prevalensi di kabupaten = 3% × 500.000 ekor sapi 
 = 15.000 ekor sapi


Jika kita memutar rumus lengkap secara aljabar untuk mencari nilai prevalensi, bentuk rumusnya menjadi

Prevalensi = (Insidensi × Durasi) / [1 + (Insidensi × Durasi)]

Mari kita masukkan angkanya:

Prevalensi = (0,0015 × 20) / [1 + (0,0015 × 20)] 
 = 0,03 / (1 + 0,03) 
 = 0,03 / 1,03 
 = 0,0291 atau 2,91%


Perhatikan bahwa selisih antara hasil tebakan rumus sederhana (3%) dan rumus lengkap (2,91%) sangatlah kecil, bahkan tidak sampai 0,1%. Angka 3% sudah lebih dari cukup untuk memberikan gambaran situasi penyakit yang akurat bagi kita di lapangan.

Rumus ini membantu kita memahami bahwa angka prevalensi yang tinggi tidak selalu berarti penyakit tersebut menular dengan sangat cepat. Bisa jadi, prevalensinya tinggi hanya karena penyakitnya bersifat kronis sehingga hewan yang sakit tidak cepat sembuh dan tidak cepat mati. Kasus-kasus lama akhirnya menumpuk di dalam populasi.

Meskipun demikian, hubungan perkiraan prevalensi tersebut hanya berlaku pada kondisi tertentu, yaitu ketika situasi penyakit relatif stabil. Secara umum, pendekatan ini digunakan dengan beberapa asumsi berikut:

1. penyakit berada dalam keadaan yang stabil atau insidensinya tidak berubah secara drastis dari waktu ke waktu;
2. prevalensi relatif rendah;
3. populasi relatif stabil; dan
4. durasi penyakit relatif stabil.

Untuk melihat bagaimana berbagai faktor memengaruhi angka prevalensi, mari kita perhatikan tabel berikut:

<p class="chart-caption">Tabel 3.8. Faktor-faktor yang memengaruhi angka prevalensi.</p>

| Faktor yang meningkatkan prevalensi | Faktor yang menurunkan prevalensi |
| ----- | ----- |
| Durasi penyakit yang lebih lama (penyakit kronis) | Durasi penyakit yang singkat |
| Perpanjangan hidup pasien tanpa kesembuhan | Tingkat kematian yang tinggi akibat penyakit (hewan cepat mati) |
| Peningkatan kasus baru (insidensi meningkat) | Penurunan kasus baru (insidensi menurun) |
| Masuknya hewan sakit ke dalam populasi | Masuknya hewan sehat ke dalam populasi |
| Perbaikan kemampuan diagnosis (sehingga lebih banyak kasus yang terdeteksi) | Tingkat kesembuhan yang tinggi dan cepat |

Sebagai contoh, perhatikan dua penyakit ini:

1. Penyakit yang sangat mematikan (misalnya septisemia epizootika pada sapi): Penyakit ini memiliki insidensi yang tinggi saat wabah, tetapi durasinya sangat singkat karena sapi bisa mati dalam waktu 24 jam. Jika kita melakukan pemeriksaan prevalensi titik (datang ke lokasi hanya pada satu hari tertentu), kita mungkin menemukan prevalensi yang rendah karena sapi-sapinya sudah banyak yang mati sebelum sempat kita periksa.
2. Penyakit kronis (misalnya cacingan): Penyakit ini mungkin memiliki insidensi yang biasa saja, tetapi durasinya sangat lama. Sapi yang cacingan tetap hidup dan tetap sakit dalam waktu berbulan-bulan. Akibatnya, saat kita datang memeriksa, kita akan menemukan prevalensi yang sangat tinggi karena hampir semua sapi yang pernah tertular masih berada dalam status "sakit".

Pemahaman mengenai hubungan ini sangat penting bagi kita saat merancang program pengendalian. Jika kita ingin menurunkan prevalensi penyakit kronis, fokus kita adalah mempercepat kesembuhan (pengobatan). Namun, jika kita ingin menurunkan prevalensi penyakit akut yang menular, fokus utama kita adalah mencegah munculnya kasus baru (vaksinasi dan biosekuriti).

Prevalensi periode vs insidensi kumulatif

Hal lain yang sering membuat orang bingung adalah perbedaan antara prevalensi periode dan insidensi kumulatif. Keduanya sama-sama menggambarkan kasus pada periode waktu tertentu. Lihat tabel di bawah ini untuk melihat perbedaan antara keduanya.

 <p class="chart-caption">Tabel 3.9. Perbedaan antara prevalensi periode dan insidensi kumulatif beserta contoh skenarionya.</p>

| Unsur dan skenario | Prevalensi periode | Insidensi kumulatif |
| ----- | ----- | ----- |
| Pembilang | Jumlah kasus dalam periode tertentu | Jumlah kasus baru dalam periode tertentu |
| Penyebut | Jumlah populasi | Jumlah populasi rentan pada awal periode studi |
| Skenario 1: Hari pertama bulan ini kasus = 0 ekor populasi = 30 ekor. Hari terakhir bulan ini kasus = 15 ekor populasi = 30 ekor | Prevalensi periode = 15 / 30 = 0,5 atau 50% dalam kurun waktu satu bulan | Insidensi kumulatif = 15 / 30 = 0,5 atau 50% dalam kurun waktu satu bulan |
| Skenario 2: Hari pertama bulan ini kasus = 3 ekor populasi = 30 ekor. Hari terakhir bulan ini kasus = 15 ekor populasi = 30 ekor | Prevalensi periode = 15 / 30 = 0,5 atau 50% dalam kurun waktu satu bulan | Insidensi kumulatif = 12 / 27 = 0,44 atau 44% dalam kurun waktu satu bulan |

Setelah kita tuntas membahas ukuran kesakitan (morbiditas), bagian selanjutnya akan membahas ukuran yang tidak kalah penting, yaitu ukuran kematian (mortalitas).

###### 2. Ukuran kematian (mortalitas)

Selain mengukur seberapa banyak hewan yang sakit (morbiditas), kita juga perlu mengukur seberapa banyak hewan yang mati dalam suatu populasi. Ukuran ini kita sebut sebagai mortalitas.

Mortalitas memberikan gambaran mengenai dampak paling fatal dari suatu penyakit. Dengan mengukur kematian, kita bisa memahami dua hal penting: seberapa besar risiko kematian bagi hewan di suatu wilayah dan seberapa ganas suatu penyakit menyerang populasi kita. Dalam epidemiologi veteriner, ukuran kematian yang paling sering digunakan adalah angka kematian dan tingkat kematian kasus.

###### 2a. Angka kematian

Pada dasarnya, angka kematian merupakan variasi dari insidensi kumulatif yang sudah kita pelajari sebelumnya. Bedanya, "kasus" yang kita hitung di sini bukan lagi hewan yang sakit, melainkan hewan yang mati.

Angka kematian mengukur frekuensi kematian dalam suatu populasi selama periode waktu tertentu (biasanya satu tahun). Berdasarkan kedalaman datanya, angka kematian dibagi menjadi dua tipe, yaitu angka kematian kasar dan angka kematian spesifik.

1. Angka kematian kasar (crude mortality rate)

Angka ini disebut "kasar" karena kita menghitung semua kematian yang terjadi akibat semua penyebab, tanpa membedakan umur, jenis kelamin, atau jenis penyakitnya. Ia memberikan gambaran umum mengenai risiko kematian di suatu populasi. Rumusnya:

Angka kematian kasar = Jumlah kematian akibat semua penyebab / 
Jumlah seluruh populasi

Contoh: 

Di sebuah kabupaten terdapat 25.000 ekor domba. Selama tahun 2025, tercatat ada 300 ekor domba yang mati (baik karena sakit, kecelakaan, maupun dimakan predator). Pada skenario ini, angka kematiannya adalah 300 / 25.000 = 0,012 atau 1,2% per tahun.

2. Angka kematian spesifik (specific mortality rate)

Angka ini jauh lebih detail karena kita membatasi hitungan kita pada penyebab tertentu atau kelompok hewan tertentu. Ini sangat berguna jika kita ingin melihat masalah yang lebih fokus.

* Spesifik berdasarkan penyebab: Kita hanya menghitung kematian akibat satu penyakit saja. Misalnya, dari 300 kematian domba tadi, ternyata 60 ekor mati karena cacingan (haemonchosis). Oleh karena itu, angka kematian spesifik akibat cacingan adalah 60 / 25.000 = 0,24%. (perhatikan bahwa penyebutnya tetap total populasi).
* Spesifik berdasarkan kelompok: Kita hanya menghitung kematian pada kelompok umur tertentu. Misalnya, dari 25.000 domba, ada 10.000 ekor anak domba (cempe). Jika ada 80 anak domba yang mati, maka angka kematian spesifik anak domba adalah 80 / 10.000 = 0,8%. (Perhatikan bahwa penyebutnya berubah menjadi total populasi anak domba saja).

Untuk memudahkan kita membedakan keduanya, mari kita lihat tabel berikut:

<p class="chart-caption">Tabel 3.10. Perbandingan angka kematian kasar dan spesifik.</p>

| Unsur | Angka kematian kasar | Angka kematian spesifik (penyebab) | Angka kematian spesifik (kelompok) |
| ----- | ----- | ----- | ----- |
| Tujuan | Mengukur risiko kematian secara umum di seluruh populasi | Mengukur risiko kematian pada penyebab tertentu | Mengukur risiko kematian pada kelompok tertentu |
| Pembilang | Jumlah kematian akibat semua penyebab | Jumlah kematian akibat satu penyebab | Jumlah kematian pada satu kelompok |
| Penyebut | Seluruh populasi | Seluruh populasi | Populasi kelompok |
| Pertanyaan | "Seberapa besar risiko seekor hewan untuk mati di populasi ini?" | "Seberapa besar risiko hewan di populasi ini mati karena penyakit X?" | "Seberapa besar risiko hewan di kelompok Y untuk mati?" |

 Satu hal yang perlu kita perhatikan adalah pemilihan penyebut. Saat kita menghitung angka kematian tahunan untuk wilayah yang luas (seperti data Badan Pusat Statistik), kita sering menggunakan jumlah populasi pada pertengahan tahun sebagai penyebutnya. Namun, dalam penelitian atau investigasi wabah, kita lebih sering menggunakan jumlah populasi pada awal pengamatan.

Setelah kita tahu risiko kematian di seluruh populasi, sekarang kita akan melihat ukuran yang lebih spesifik untuk mengukur "keganasan" suatu penyakit, yaitu tingkat kematian kasus.

###### 2b. Tingkat kematian kasus

Jika angka kematian mengukur risiko kematian pada seluruh populasi, maka tingkat kematian kasus atau case fatality rate (CFR) mengukur sesuatu yang berbeda. Ia digunakan untuk mengukur seberapa ganas atau seberapa fatal suatu penyakit bagi individu yang sudah tertular.

CFR membantu kita menjawab pertanyaan: "Jika seekor hewan sudah didiagnosis menderita penyakit X, seberapa besar kemungkinannya untuk mati?"

Berbeda dengan angka kematian yang penyebutnya adalah seluruh populasi (baik yang sehat maupun yang sakit), penyebut pada CFR hanyalah hewan yang sakit saja. Oleh karena itu, CFR dinyatakan sebagai sebuah proporsi atau persentase.

Rumusnya:

CFR = Jumlah kematian akibat penyakit tertentu / 
Jumlah kasus akibat penyakit tertentu

Mari kita lihat contohnya pada sebuah wabah:

Skenario: Di sebuah kota terjadi wabah penyakit distemper pada anjing. Tercatat ada 90 ekor anjing yang terinfeksi. Dari 90 ekor yang sakit tersebut, 45 ekor di antaranya mati akibat distemper.

Perhitungan: CFR = 45 / 90 = 0,5 atau 50%.

Makna: Tingkat keganasan wabah distemper tersebut adalah 50%. Artinya, separuh dari anjing yang sudah tertular penyakit ini diperkirakan akan berakhir dengan kematian.

Sangat sering terjadi misinterpretasi antara angka kematian spesifik akibat suatu penyebab dan CFR. Untuk memperjelas perbedaan antara keduanya, mari kita perhatikan tabel perbandingan berikut ini.

<p class="chart-caption">Tabel 3.11. Perbandingan angka kematian spesifik (penyebab) dan tingkat kematian kasus.</p>

| Aspek | Angka kematian spesifik (penyebab) | Tingkat kematian kasus |
| ----- | ----- | ----- |
| Tujuan | Mengukur dampak suatu penyakit terhadap seluruh populasi | Mengukur keganasan atau kefatalan suatu penyakit pada individu yang sakit |
| Pembilang | Jumlah kematian akibat penyakit tertentu | Jumlah kematian akibat penyakit tertentu |
| Penyebut | Seluruh populasi (sehat + sakit) | Hanya individu yang menderita penyakit tersebut |
| Logika risiko | Risiko bagi populasi; artinya, risiko bagi hewan yang sehat untuk tertular lalu mati | Risiko bagi pasien; artinya, risiko bagi hewan yang sudah sakit untuk kemudian mati |
| Pertanyaan yang dijawab | "Seberapa besar peluang seekor hewan untuk mati akibat penyakit ini di populasi kita?" | "Jika seekor hewan sudah tertular penyakit ini, seberapa besar peluangnya untuk mati?" |

CFR sangat berguna bagi klinisi maupun epidemiolog untuk menentukan prioritas penanganan. Penyakit dengan CFR yang tinggi (seperti rabies yang CFR-nya mendekati 100%) menuntut tindakan pencegahan yang sangat ketat karena peluang untuk sembuh setelah muncul tanda klinis hampir tidak ada.

Sebaliknya, ada penyakit yang mungkin memiliki angka kematian populasi yang rendah, tetapi CFR-nya sangat tinggi. Hal ini biasanya terjadi pada penyakit yang jarang muncul tetapi sangat mematikan.

Setelah kita mempelajari berbagai cara menghitung frekuensi penyakit dan kematian, sekarang kita akan melihat bagaimana angka-angka ini didistribusikan dalam populasi melalui pendekatan epidemiologi deskriptif.

##### C. Distribusi kejadian penyakit

###### 1. Epidemiologi deskriptif

Setelah kita menghitung angka kesakitan (morbiditas) dan angka kematian (mortalitas), sekarang kita akan belajar bagaimana menyusun angka-angka tersebut menjadi sebuah cerita yang bermakna.

Epidemiologi deskriptif adalah cabang epidemiologi yang berfokus pada pengamatan dan penjelasan mengenai bagaimana suatu penyakit tersebar dalam populasi. Jika ukuran frekuensi (prevalensi dan insidensi) adalah "bahan baku" berupa angka, maka epidemiologi deskriptif adalah cara kita menyajikan angka-angka tersebut agar kita bisa melihat polanya.

Tujuan utama dari epidemiologi deskriptif adalah untuk menjawab tiga pertanyaan kunci yang sering kita sebut sebagai 3W: who (siapa), where (di mana), dan when (kapan).

1. Siapa (who): Karakteristik hewan apa yang paling banyak terdampak? Apakah spesies tertentu, umur tertentu, atau jenis kelamin tertentu?
2. Di mana (where): Di wilayah mana penyakit ini paling banyak ditemukan? Apakah di dataran tinggi, di dekat pasar hewan, atau di wilayah perbatasan?
3. Kapan (when): Kapan penyakit ini mulai muncul dan kapan mencapai puncaknya? Apakah mengikuti pola musiman seperti musim hujan atau musim kemarau?

Dengan menjawab ketiga pertanyaan ini, kita bisa mendapatkan gambaran mengenai situasi kesehatan populasi. Selain itu, epidemiologi deskriptif membantu kita untuk

1. mengidentifikasi kelompok berisiko tinggi: kita jadi tahu kelompok hewan mana yang harus diprioritaskan untuk mendapatkan vaksinasi atau pengobatan;
2. mengalokasikan sumber daya secara efisien: kita bisa mengirimkan bantuan sumber daya manusia dan obat-obatan ke wilayah yang paling membutuhkan; dan
3. membangun hipotesis: pola yang kita temukan secara deskriptif akan menjadi dasar bagi kita untuk melakukan penelitian lebih lanjut (epidemiologi analitis) guna mencari tahu faktor penyebab pastinya.

Untuk memudahkan kita memahami cakupan epidemiologi deskriptif, lihat tabel berikut:

<p class="chart-caption">Tabel 3.12. Tiga pilar utama epidemiologi deskriptif.</p>

| Pilar deskriptif | Fokus pengamatan | Contoh informasi yang dihasilkan |
| ----- | ----- | ----- |
| Distribusi menurut karakter demografis (who) | Karakteristik individu hewan | "Kasus Brucellosis lebih banyak ditemukan pada sapi betina dewasa." |
| Distribusi spasial (where) | Lokasi atau tempat kejadian | "Wabah antraks terkonsentrasi di wilayah dengan jenis tanah tertentu." |
| Distribusi temporal (when) | Waktu atau periode kejadian | "Kejadian diare pada pedet meningkat tajam setiap awal musim hujan." |

Perlu kita pahami bahwa epidemiologi deskriptif selalu menjadi langkah awal dalam setiap investigasi penyakit. Kita tidak mungkin bisa menjelaskan "mengapa" (why) suatu penyakit terjadi jika kita belum tahu "siapa, di mana, dan kapan" penyakit itu terjadi. Di bagian selanjutnya, kita akan membedah satu per satu pilar deskriptif ini, yang dimulai dari karakteristik demografis hewan.

###### 2. Distribusi menurut karakter demografis

Pilar pertama dalam epidemiologi deskriptif adalah memahami karakteristik individu hewan yang mengalami sakit atau kematian. Kita tidak sedang mencari tahu "mengapa" mereka sakit, melainkan hanya memetakan apakah kasus-kasus tersebut cenderung ditemukan pada karakteristik atau kelompok tertentu.

Dengan melihat distribusi ini, kita bisa mengetahui kelompok mana yang paling banyak terdampak. Ada tiga variabel utama yang biasanya kita amati:

1. Spesies atau rumpun (breed). 
	Dalam suatu wilayah yang memiliki berbagai jenis hewan, kita sering menemukan bahwa frekuensi kasus suatu penyakit tidak merata antarspesies. Sebagai contoh, pada pengamatan penyakit brucellosis di suatu daerah, kita mungkin menemukan jumlah kasus positif yang jauh lebih banyak pada sapi dibandingkan pada kambing, meskipun keduanya sama-sama bisa tertular. 
	
	Hal yang sama juga terlihat pada perbedaan rumpun. Kita mungkin mengamati bahwa jumlah caplak yang ditemukan pada sapi perah (rumpun sapi Eropa) jauh lebih banyak dibandingkan pada sapi bali yang dipelihara di lingkungan yang sama.
	
2. Jenis kelamin. 
	Meskipun suatu penyakit dapat menyerang hewan jantan maupun betina, jumlah kasus yang ditemukan di lapangan sering kali tidak seimbang. Pola ini sering kali berkaitan dengan perbedaan perilaku atau cara kita memelihara mereka. 
	
	Sebagai contoh, pada pengamatan kasus rabies di sebuah kabupaten, kita mungkin menemukan jumlah kasus positif yang lebih banyak pada anjing jantan dibandingkan anjing betina. Hal ini bisa terjadi karena anjing jantan cenderung memiliki daya jelajah yang lebih luas sehingga lebih sering bertemu dengan anjing lain di luar lingkungannya.
	
3. Umur. 
	Pola kejadian penyakit sering kali menunjukkan perbedaan yang sangat kontras jika kita melihat kelompok umur. Karakteristik ini membantu kita melihat pada tahap kehidupan mana suatu penyakit paling sering muncul. 
	
	Contoh yang sangat umum adalah kejadian cacingan (helminthiasis). Meskipun cacingan dapat ditemukan pada semua umur, kita akan menemukan frekuensi kasus yang jauh lebih tinggi pada hewan muda (pedet atau cempe) dibandingkan pada hewan dewasa. Sebaliknya, pada kasus penyakit degeneratif seperti gangguan fungsi ginjal, kita akan menemukan lebih banyak kasus pada kelompok hewan yang sudah tua.

Dengan memetakan distribusi berdasarkan karakter demografis ini, kita bisa melihat kelompok mana yang paling banyak menderita sakit. Informasi ini sangat berguna bagi petugas di lapangan untuk menentukan skala prioritas operasional. Jika pengamatan menunjukkan bahwa kasus terkonsentrasi pada pedet, maka bantuan obat-obatan atau perbaikan sanitasi dapat segera difokuskan pada kelompok tersebut agar penanganan menjadi lebih efisien.

Setelah kita memetakan "siapa" yang paling banyak terdampak, pilar deskriptif selanjutnya adalah melihat "di mana" kasus-kasus tersebut berada melalui distribusi spasial.

###### 3. Distribusi menurut tempat (spasial)

Setelah memetakan "siapa" yang terdampak, pertanyaan besar berikutnya adalah: Di mana (where) kasus tersebut ditemukan? Dalam pengamatan di lapangan, penyakit hampir tidak pernah tersebar secara merata. Kita akan menemukan bahwa ada wilayah yang memiliki banyak kasus (titik panas atau hotspot), sementara wilayah di sebelahnya mungkin tidak ditemukan kasus sama sekali.

Distribusi spasial membantu kita memetakan pola kejadian penyakit berdasarkan letak geografis maupun bentang alam. Melalui pengamatan ini, kita sering menemukan bahwa kasus-kasus cenderung terkonsentrasi pada lokasi dengan karakteristik tertentu, misalnya:

1. Ketinggian wilayah: Kita mungkin menemukan bahwa kasus penyakit yang ditularkan oleh serangga lebih banyak dilaporkan di wilayah dataran rendah dibandingkan di wilayah pegunungan.
2. Kondisi lingkungan: Pengamatan sering menunjukkan bahwa kasus penyakit tertentu, seperti antraks, cenderung muncul berulang di lokasi dengan tipe tanah yang sama.
3. Kedekatan dengan fasilitas publik: Kita sering mengamati frekuensi kasus yang lebih tinggi di wilayah yang dekat dengan pasar hewan, rumah potong hewan, atau pelabuhan dibandingkan dengan wilayah yang terisolasi.

Untuk memvisualisasikan distribusi ini, kita menggunakan peta epidemiologis. Peta ini adalah alat bantu utama untuk melihat bagaimana kasus tersebar di suatu wilayah. Secara garis besar ada dua jenis peta yang sering digunakan dalam epidemiologi, yaitu peta titik dan peta wilayah. Keduanya dijelaskan pada tabel berikut ini.

<p class="chart-caption">Tabel 3.13. Jenis-jenis peta dalam epidemiologi deskriptif.</p>

| Jenis peta | Cara penyajian | Kegunaan utama |
| ----- | ----- | ----- |
| Peta titik (point map) | Menandai setiap lokasi kasus dengan satu titik (dot) | Melihat apakah ada pengelompokan (clustering) kasus di lokasi yang spesifik |
| Peta wilayah (choropleth map) | Memberikan warna berbeda pada tingkat area administratif (desa, kecamatan, kabupaten, atau provinsi) berdasarkan jumlah kasus | Membandingkan tingkat keparahan antarwilayah secara administratif |

Catatan: Pada peta titik, bisa jadi satu titik pada peta tidak mewakili satu individu hewan yang sakit, melainkan mewakili satu unit epidemiologi, seperti satu peternakan yang terinfeksi. Unit epidemiologi adalah kelompok hewan dengan batas lokasi dan risiko paparan penyakit yang sama.

<figure>
  <img src="img/gambar-03.05.png" 
       style="width: 500px;" 
       alt="Perbandingan penyajian distribusi spasial. Kiri: peta titik yang menandai lokasi spesifik setiap kasus dengan titik. Kanan: peta wilayah yang menggunakan gradasi warna untuk membandingkan tingkat keparahan kasus antarwilayah administratif.">
  <figcaption>Gambar 3.5. Perbandingan penyajian distribusi spasial. Kiri: peta titik yang menandai lokasi spesifik setiap kasus dengan titik. Kanan: peta wilayah yang menggunakan gradasi warna untuk membandingkan tingkat keparahan kasus antarwilayah administratif.</figcaption>
</figure>

Mari kita ambil contoh kejadian PMK. Melalui peta titik, kita dapat melihat secara detail apakah kasus PMK mengelompok (clustering) di lokasi-lokasi spesifik. Sementara itu, peta wilayah membantu kita membandingkan tingkat keparahan wabah tersebut antarwilayah administratif melalui perbedaan warna. Informasi spasial dari kedua peta ini sangat berharga untuk menentukan strategi operasional di lapangan. Alih-alih melakukan penutupan wilayah atau vaksinasi massal secara membabi buta di seluruh provinsi, kita dapat memfokuskan sumber daya dan penanganan, seperti vaksinasi dan pembatasan perpindahan hewan, hanya pada daerah yang secara visual teridentifikasi sebagai titik panas (hotspot).

Di era modern, kita juga menggunakan teknologi sistem informasi geografis (SIG). Dengan SIG, kita bisa menumpuk peta kejadian penyakit dengan peta sungai atau peta jalan. Hal ini memudahkan kita untuk melihat ke arah mana penyakit tersebut cenderung bergerak. Analisis spasial ini membantu kita melihat gambaran yang lebih luas melampaui batas-batas administratif (seperti batas kabupaten atau provinsi) yang sering kali tidak berlaku bagi perpindahan hewan maupun agen penyakit.

Setelah kita memetakan "siapa" yang terdampak dan "di mana" lokasinya, pilar terakhir yang harus kita lengkapi adalah "kapan" penyakit itu terjadi melalui distribusi temporal.

###### 4. Distribusi menurut waktu (temporal)

Setelah kita memetakan siapa yang terdampak dan di mana lokasinya, pilar terakhir yang harus kita lengkapi adalah kapan (when). Penyakit tidak hanya berpindah tempat, tetapi juga berubah frekuensinya seiring berjalannya waktu.

Distribusi temporal membantu kita melihat apakah suatu penyakit sedang meningkat, menurun, atau stabil. Dengan memahami pola waktu, kita bisa memprediksi kapan sebuah wabah mungkin akan terjadi lagi di masa depan dan mengevaluasi apakah tindakan pengendalian yang kita lakukan sudah efektif.

Secara umum, ada tiga pola waktu yang sering kita amati dalam epidemiologi veteriner:

1. Tren jangka panjang (secular trends). 
	Ini adalah perubahan frekuensi penyakit yang terjadi dalam waktu yang sangat lama, biasanya bertahun-tahun atau puluhan tahun. Tren ini membantu kita melihat gambaran besar. Misalnya, penurunan kasus brucellosis di suatu provinsi selama 10 tahun terakhir karena adanya program vaksinasi massal yang konsisten.
	
2. Pola musiman (seasonality). 
	Di Indonesia, pola musiman sangat dipengaruhi oleh siklus musim hujan dan musim kemarau. Banyak penyakit hewan yang muncul secara rutin pada bulan-bulan tertentu setiap tahunnya. Contoh: Kejadian diare pada pedet atau penyakit yang ditularkan oleh serangga (seperti lumpy skin disease) sering kali meningkat tajam di awal musim hujan. Hal ini terjadi karena kelembapan yang tinggi mendukung perkembangbiakan kuman dan vektor serangga.
	
3. Kurva epidemi. 
	Jika tren sekuler melihat waktu dalam hitungan tahun, kurva epidemi melihat waktu dalam skala yang jauh lebih singkat, seperti hari atau pekan. Seperti yang sudah kita pelajari di Modul 2, kurva epidemi adalah grafik yang menunjukkan jumlah kasus baru dari waktu ke waktu selama terjadinya wabah. Dengan melihat bentuk kurva ini, kita bisa mendapatkan informasi deskriptif mengenai kapan kasus pertama kali muncul (onset), kapan puncak wabah terjadi, dan berapa lama durasi wabah tersebut.

Untuk merangkum perbedaan pola-pola waktu ini, mari kita perhatikan tabel berikut:

<p class="chart-caption">Tabel 3.14. Jenis-jenis distribusi temporal.</p>

| Pola waktu | Skala waktu | Kegunaan utama |
| ----- | ----- | ----- |
| Tren sekuler | Tahunan atau puluhan tahun. | Mengevaluasi keberhasilan program pengendalian jangka panjang |
| Pola musiman | Bulanan (berulang setiap tahun) | Menyiapkan langkah pencegahan sebelum musim berisiko tiba |
| Kurva epidemi | Harian atau mingguan | Memantau perkembangan wabah dan mencari sumber penularan |

Untuk memvisualisasikan perbedaan dari ketiga pola waktu pada tabel di atas, perhatikan gambar di bawah ini. Pada grafik tren jangka panjang (kiri), kita bisa melihat arah pergerakan kasus dari tahun ke tahun. Sementara itu, grafik pola musiman (tengah) memperlihatkan dengan jelas adanya gelombang peningkatan dan penurunan kasus yang berulang pada bulan-bulan yang sama selama dua tahun berturut-turut. Di sisi lain, kurva epidemi (kanan) memberikan gambaran spesifik berupa diagram batang (histogram) mengenai lonjakan cepat kasus baru dalam hitungan hari selama masa pengamatan wabah berlangsung.

<figure>
  <img src="img/gambar-03.06.png" 
       style="width: 500px;" 
       alt="Perbandingan jenis-jenis grafik distribusi temporal. Kiri: Tren jangka panjang berskala tahunan yang menunjukkan penurunan kasus. Tengah: Pola musiman berskala bulanan yang menunjukkan fluktuasi kasus yang berulang pada periode waktu dua tahun. Kanan: Kurva epidemi berupa diagram batang berskala harian yang menunjukkan lonjakan tajam kasus baru saat wabah.">
  <figcaption>Gambar 3.6. Perbandingan jenis-jenis grafik distribusi temporal. Kiri: Tren jangka panjang berskala tahunan yang menunjukkan penurunan kasus. Tengah: Pola musiman berskala bulanan yang menunjukkan fluktuasi kasus yang berulang pada periode waktu dua tahun. Kanan: Kurva epidemi berupa diagram batang berskala harian yang menunjukkan lonjakan tajam kasus baru saat wabah.</figcaption>
</figure>

Perlu kita pahami bahwa ketiga pilar epidemiologi deskriptif (siapa, di mana, kapan) saling berkaitan erat. Sebagai contoh, kita mungkin menemukan bahwa "kasus diare (who) meningkat di wilayah pesisir (where) setiap bulan Januari (when)".

Dengan menggabungkan angka frekuensi penyakit (morbiditas dan mortalitas) dengan analisis distribusi ini, kita tidak lagi hanya melihat angka yang mati, tetapi kita mulai memahami pola hidup penyakit tersebut di tengah populasi. Pemahaman inilah yang menjadi dasar bagi kita untuk mengambil keputusan medis maupun kebijakan kesehatan hewan yang tepat di lapangan.


#### III. Ringkasan

Kegiatan belajar ini membahas cara mengukur frekuensi dan mendeskripsikan distribusi kejadian penyakit dalam populasi hewan. Pembahasan diawali dengan pentingnya mengukur kejadian penyakit secara kuantitatif dengan menyertakan angka populasi berisiko sebagai penyebut dan menetapkan definisi kasus yang standar, yang selanjutnya disajikan menggunakan alat ukur dasar berupa rasio, proporsi, dan laju. Mahasiswa diperkenalkan pada ukuran morbiditas (kesakitan) yang membedakan antara prevalensi sebagai gambaran beban penyakit yang ada di populasi dan insidensi sebagai gambaran kecepatan munculnya kasus baru. Modul ini juga menguraikan ukuran mortalitas (kematian) melalui angka kematian kasar dan spesifik untuk mengevaluasi risiko populasi secara umum, serta tingkat kematian kasus (CFR) untuk menilai seberapa fatal atau ganas suatu penyakit bagi individu yang telah tertular. Pada bagian akhir, angka-angka parameter tersebut dirangkai menjadi informasi bermakna melalui pendekatan epidemiologi deskriptif yang memetakan pola kejadian penyakit untuk menjawab tiga pertanyaan kunci: siapa (distribusi demografis seperti spesies, jenis kelamin, dan umur), di mana (distribusi spasial), dan kapan (distribusi temporal seperti tren jangka panjang, pola musiman, dan kurva epidemi) penyakit tersebut terjadi. Pemahaman yang komprehensif terhadap perhitungan frekuensi dan pola distribusi ini membantu mahasiswa untuk mengevaluasi status kesehatan populasi secara akurat, merancang intervensi yang tepat sasaran, dan mengalokasikan sumber daya secara efisien di lapangan.
