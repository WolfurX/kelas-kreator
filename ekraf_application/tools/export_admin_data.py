#!/usr/bin/env python3
"""Export isi.py to admin/modul-data.js for admin HTML mock."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from isi import FAQ, JADWAL, MODUL, PENILAIAN, PROGRAM  # noqa: E402


def slug(jenis):
    return jenis.split()[0].lower()


def main():
    kelas = {
        "id": "creatifluencer-2026",
        "nama": "Creatifluencer 2026",
        "slug": "creatifluencer-2026",
        "program": PROGRAM,
        "status": "publish",
        "kapasitas_peserta": 20,
        "jumlah_grup": 4,
        "tanggal_mulai": JADWAL[0][0],
        "tanggal_selesai": JADWAL[-1][0],
        "target_modul_mingguan": 2,
        "jadwal": [
            {"tanggal_iso": j[0], "tanggal_tampil": j[1], "nama_sesi": j[2], "keterangan": j[3]}
            for j in JADWAL
        ],
        "penilaian": [
            {"kriteria": p[0], "yang_dilihat": p[1], "bobot": p[2], "frekuensi": p[3]}
            for p in PENILAIAN
        ],
        "faq": [{"pertanyaan": f[0], "jawaban": f[1]} for f in FAQ],
    }
    modul_list = []
    for mod in MODUL:
        n = mod["n"]
        slugs = (["kuis"] if mod["kuis"] else []) + [slug(t[0]) for t in mod["tugas"]]
        pelajaran = []
        for i, (judul, isi, latihan) in enumerate(mod["pelajaran"], 1):
            pelajaran.append({
                "id": f"p{i}",
                "urutan": i,
                "judul": judul,
                "isi_html": isi.strip(),
                "latihan": latihan,
            })
        kuis = None
        if mod["kuis"]:
            kuis = [
                {
                    "urutan": qi,
                    "soal": row[0],
                    "pilihan": row[1],
                    "jawaban_benar": row[2],
                    "penjelasan": row[3],
                }
                for qi, row in enumerate(mod["kuis"], 1)
            ]
        tugas = [
            {
                "jenis": t[0],
                "slug": slug(t[0]),
                "isi_html": t[1].strip(),
                "label_centang": t[2],
            }
            for t in mod["tugas"]
        ]
        modul_list.append({
            "kelas_id": "creatifluencer-2026",
            "n": n,
            "judul": mod["judul"],
            "fokus": mod["fokus"],
            "cover": mod["cover"],
            "aktivitas": mod["aktivitas"],
            "status": "publish",
            "pdf_path": f"assets/pdf/modul-{n}.pdf",
            "manifest": {"p": len(mod["pelajaran"]), "a": slugs},
            "pelajaran": pelajaran,
            "kuis": kuis,
            "tugas": tugas,
        })
    out = os.path.join(os.path.dirname(os.path.dirname(__file__)), "admin", "modul-data.js")
    with open(out, "w", encoding="utf-8") as f:
        f.write("window.KK_DATA = ")
        json.dump({"kelas": kelas, "modul": modul_list}, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print("wrote", out)


if __name__ == "__main__":
    main()
