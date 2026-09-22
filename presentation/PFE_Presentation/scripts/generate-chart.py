"""Generate the standalone capacity chart from the committed campaign CSV.

Standard-library SVG keeps the deck reproducible without extra dependencies.
Bars = mean density * 2048 bytes; whiskers = observed min/max, n=6 each.
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
with (ROOT / 'public/evidence/density-summary.csv').open() as stream:
    rows = {row['workload']: row for row in csv.DictReader(stream)}
order = [('w2_callchain', 'Call-heavy'), ('w5_dma', 'DMA / idle'),
         ('w4_isr', 'Interrupt-driven'), ('w1_baseline', 'Baseline'),
         ('w3_branchdense', 'Branch-dense'), ('w6_overflow', 'Tight loop')]
parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="1120" height="354" viewBox="0 0 1120 354" role="img" aria-labelledby="title desc">',
         '<title id="title">Execution history retained by a 2 KiB buffer</title>',
         '<desc id="desc">Bars show mean instruction count and whiskers show observed minimum and maximum across six captures per workload.</desc>',
         '<rect width="1120" height="354" fill="#FFFFFF"/>',
         '<g font-family="Arial, Helvetica, sans-serif" fill="#03234B">']
left, scale = 190, 800 / 9000
for tick in range(0, 9001, 1000):
    x = left + tick * scale
    parts += [f'<line x1="{x}" y1="16" x2="{x}" y2="284" stroke="#EEEFF1"/>',
              f'<text x="{x}" y="308" text-anchor="middle" font-size="16">{tick//1000}k</text>']
for index, (key, label) in enumerate(order):
    row = rows[key]
    mean, low, high = [float(row[field]) * 2048 for field in ('mean_instr_per_byte','min_instr_per_byte','max_instr_per_byte')]
    y = 35 + index * 44
    a, b = left + low * scale, left + high * scale
    parts += [f'<text x="172" y="{y+6}" text-anchor="end" font-size="19">{label}</text>',
              f'<rect x="{left}" y="{y-12}" width="{mean*scale}" height="24" rx="3" fill="#03234B" opacity="1"/>',
              f'<path d="M{a} {y-8}V{y+8}M{a} {y}H{left+mean*scale}" fill="none" stroke="#FFD200" stroke-width="2"/>',
              f'<path d="M{left+mean*scale} {y}H{b}M{b} {y-8}V{y+8}" fill="none" stroke="#03234B" stroke-width="2"/>',
              f'<circle cx="{left+mean*scale}" cy="{y}" r="5" fill="#FFD200"/>',
              f'<text x="{b+12}" y="{y+6}" font-size="17" font-weight="bold">{mean:,.0f}</text>']
parts += ['<text x="190" y="342" font-size="16">Reconstructed instructions · bars: mean · whiskers: observed range · 6 captures / workload</text>', '</g></svg>']
(ROOT / 'public/evidence/history-capacity.svg').write_text('\n'.join(parts) + '\n')
