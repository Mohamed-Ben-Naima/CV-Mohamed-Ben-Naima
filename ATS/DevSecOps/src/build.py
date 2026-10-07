"""Render the DevSecOps CV: ATS + recruiter design, EN + FR -> HTML, PDF, TXT.
Usage: python3 build.py   (run from this folder)"""
import os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import C

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
CONTACT = [("+216 25 577 542", None), ("Medbennaima2021@gmail.com", "mailto:Medbennaima2021@gmail.com"),
           ("linkedin.com/in/mohamed-ben-naima", "https://www.linkedin.com/in/mohamed-ben-naima/"),
           ("github.com/Mohamed-Ben-Naima", "https://github.com/Mohamed-Ben-Naima"),
           ("mohamed-ben-naima.netlify.app", "https://mohamed-ben-naima.netlify.app/")]

def contact(d, sep):
    parts = [d["location"]] + [f'<a href="{u}">{t}</a>' if u else t for t, u in CONTACT]
    return sep.join(parts)

def bullets(items):
    return "<ul>" + "".join(f"<li>{b}</li>" for b in items) + "</ul>"

def entry(title, when, sub_html, body):
    return (f'<div class="entry"><div class="e-head"><span class="e-title">{title}</span>'
            f'<span class="e-when">{when}</span></div>{sub_html}{body}</div>')

def jobs(d):
    return "".join(entry(j["title"], j["when"], f'<div class="e-sub">{j["org"]} · {j["place"]}</div>', bullets(j["bullets"])) for j in d["jobs"])

def projects(d, limit=None):
    out = []
    for p in d["projects"][:limit]:
        name = p["name"] + (f' <span class="e-note">({p["sub"]})</span>' if p["sub"] else "")
        if "bullets" in p:
            out.append(entry(name, p["when"], f'<div class="e-stack">{p["stack"]}</div>', bullets(p["bullets"])))
        else:  # minor project: one compact line
            out.append(entry(name, p["when"], f'<div class="e-line">{p["text"]} <span class="e-stack">{p["stack"]}</span></div>', ""))
    return "".join(out)

def edu(d):  # dates inline so ATS parsers keep them on the same line as the school
    return "".join(f'<p class="edu"><b>{s}</b>, {deg} <span class="e-note">({y}) · {hon}</span></p>' for s, deg, y, hon in d["edu"])

def edu_stack(d):
    return "".join(f'<div class="edu"><div class="e-head"><b>{s}</b><span class="e-when">{y}</span></div>'
                   f'<div>{deg} · <span class="e-note">{hon}</span></div></div>' for s, deg, y, hon in d["edu"])

BASE_CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
@page { size:A4; margin:0; }
html, body { background:#fff; }
body { font-family: Arial, Helvetica, sans-serif; color:#1d2733; }
a { color:inherit; text-decoration:none; }
p { margin-bottom:0.9mm; }
ul { margin:0.6mm 0 0.4mm 4.6mm; }
li { margin-bottom:0.5mm; }
li::marker { color: var(--accent); }
.entry { margin-bottom:1.5mm; }
.e-head { display:flex; justify-content:space-between; align-items:baseline; gap:4mm; }
.e-title { font-weight:bold; color:var(--navy); }
.e-when { white-space:nowrap; color:#55697c; font-size:0.94em; }
.e-sub { color:#3b4b5c; font-style:italic; margin-top:0.2mm; }
.e-stack { color:#55697c; font-size:0.93em; margin-top:0.2mm; }
span.e-stack { margin-left:1mm; }
.entry.minor, .e-line { margin-top:0.1mm; }
.e-note { color:#55697c; font-weight:normal; }
.edu { margin-bottom:0.8mm; }
b { color:var(--navy); }
"""

ATS_CSS = BASE_CSS + """
:root { --navy:#123a5c; --accent:#123a5c; }
.page { width:210mm; height:297mm; margin:0 auto; padding:7mm 12mm 5.5mm; font-size:8.3pt; line-height:1.15; }
h1 { font-size:18pt; color:var(--navy); letter-spacing:0.3px; }
.role { font-size:10.5pt; font-weight:bold; margin-top:0.6mm; }
.avail { font-size:9pt; color:#3b4b5c; margin-top:0.4mm; }
.contact { font-size:8.3pt; margin-top:1.4mm; padding-bottom:1.6mm; border-bottom:2px solid var(--navy); }
h2 { font-size:9.6pt; text-transform:uppercase; letter-spacing:1px; color:var(--navy); margin:2.1mm 0 1mm;
     border-bottom:0.8px solid #9fb0c0; padding-bottom:0.5mm; }
.skill { margin-bottom:0.6mm; }
"""

DESIGN_CSS = BASE_CSS + """
:root { --navy:#143a5a; --accent:#f2b32b; }
.page { width:210mm; height:297mm; margin:0 auto; padding:0 12mm 5mm; font-size:8.2pt; line-height:1.17; }
.head { background:var(--navy); color:#fff; margin:0 -12mm 3mm; padding:6mm 12mm 4mm; border-bottom:4px solid var(--accent); }
h1 { font-size:23pt; letter-spacing:0.6px; line-height:1.05; }
.role { font-size:10.8pt; font-weight:bold; color:var(--accent); margin-top:1mm; }
.avail { display:inline-block; margin-top:1.6mm; font-size:8.4pt; font-weight:bold; color:var(--navy); background:var(--accent);
         padding:0.6mm 2.4mm; border-radius:2mm; }
.loc { font-size:8.4pt; color:#dce7f2; margin-left:2mm; }
.contact { font-size:7.6pt; color:#dce7f2; margin-top:1.6mm; white-space:nowrap; letter-spacing:-0.1px; }
h2 { font-size:9.3pt; text-transform:uppercase; letter-spacing:1.3px; color:var(--navy); margin:2.2mm 0 1.1mm;
     padding-bottom:0.6mm; border-bottom:1.4px solid var(--navy); }
h2::before { content:"■ "; color:var(--accent); }
.hl { display:grid; grid-template-columns:repeat(4,1fr); gap:2mm; margin:0.5mm 0 0.6mm; }
.hl div { border:1px solid #d4dde6; border-top:3px solid var(--accent); border-radius:1.2mm; padding:1.1mm 2mm; background:#f6f8fb; }
.hl .n { display:block; font-size:12pt; font-weight:bold; color:var(--navy); }
.hl .t { display:block; font-size:7.5pt; color:#3b4b5c; line-height:1.18; margin-top:0.4mm; }
.skills { display:grid; grid-template-columns:34mm 1fr; column-gap:3mm; row-gap:0.4mm; }
.skills .k { font-weight:bold; color:var(--navy); }
.cols { display:grid; grid-template-columns:1fr 1fr; gap:5mm; }
"""

def ats_html(d):
    h = d["h"]
    skills = "".join(f'<p class="skill"><b>{k}:</b> {v}</p>' for k, v in d["skills"])
    return f"""<!DOCTYPE html><html lang="{d['lang']}"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CV — Mohamed Ben Naima — DevSecOps (ATS)</title><style>{ATS_CSS}</style></head><body><div class="page">
<h1>Mohamed Ben Naima</h1>
<div class="role">{d['title']}</div>
<div class="avail">{d['avail']}</div>
<div class="contact">{contact(d, ' | ')} | {d['langs_short']}</div>
<h2>{h['profile']}</h2><p>{d['profile']}</p>
<h2>{h['edu']}</h2>{edu(d)}
<h2>{h['skills']}</h2>{skills}
<h2>{h['exp']}</h2>{jobs(d)}
<h2>{h['proj']}</h2>{projects(d)}
<h2>{h['certs']}</h2><p>{d['certs']}</p>
<h2>{h['comm']}</h2>{bullets(d['community'])}
<h2>{h['langs']}</h2><p>{d['languages']}</p>
</div></body></html>"""

def design_html(d):
    h = d["h"]
    hl = "".join(f'<div><span class="n">{n}</span><span class="t">{t}</span></div>' for n, t in d["highlights"])
    skills = "".join(f'<span class="k">{k}</span><span>{v}</span>' for k, v in d["skills"])
    return f"""<!DOCTYPE html><html lang="{d['lang']}"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CV — Mohamed Ben Naima — DevSecOps</title><style>{DESIGN_CSS}</style></head><body><div class="page">
<div class="head"><h1>Mohamed Ben Naima</h1><div class="role">{d['title']}</div>
<div class="avail">{d['avail']}</div> <span class="loc">{d['location']}</span>
<div class="contact">{contact(d, ' · ').split(' · ', 1)[1]}</div></div>
<h2>{h['profile']}</h2><p>{d['profile_short']}</p>
<h2>{h['highlights']}</h2><div class="hl">{hl}</div>
<h2>{h['skills']}</h2><div class="skills">{skills}</div>
<h2>{h['exp']}</h2>{jobs(d)}
<h2>{h['proj']}</h2>{projects(d, 2)}
<div class="cols"><div><h2>{h['edu']}</h2>{edu_stack(d)}<h2>{h['langs']}</h2><p>{d['languages']}</p></div>
<div><h2>{h['certs']}</h2><p>{d['certs']}</p><h2>{h['comm']}</h2>{bullets(d['community'][:1])}</div></div>
</div></body></html>"""

def render(html, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path + ".html", "w") as f: f.write(html)
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={path}.pdf", path + ".html"], check=True, capture_output=True)
    pages = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", path + ".pdf"], capture_output=True, text=True).stdout).group(1))
    print(f"{os.path.relpath(path, ROOT)}.pdf: {pages} page(s)")
    return pages

for lang, d in C.items():
    ats = os.path.join(ROOT, "ATS", "DevSecOps", f"cv_mohamed_ben_naima_devsecops_{lang}")
    render(ats_html(d), ats)
    subprocess.run(["pdftotext", "-enc", "UTF-8", ats + ".pdf", ats + ".txt"], check=True)
    render(design_html(d), os.path.join(ROOT, "Applications", "DevSecOps", f"cv_mohamed_ben_naima_devsecops_{lang}"))
