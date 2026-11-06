// Render every SVG in a folder to PNG at 4x (for Word fallback images).
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const dir = process.argv[2]; const only = process.argv[3];
  const b = await chromium.launch(); const p = await b.newPage({ deviceScaleFactor: 4 });
  for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.svg') && (!only || f.startsWith(only)))) {
    const svg = fs.readFileSync(path.join(dir, f), 'utf8');
    await p.setContent(`<html><body style="margin:0;background:#fff">${svg}</body></html>`);
    const el = await p.$('svg'); await el.screenshot({ path: path.join(dir, f.replace('.svg', '.png')) });
  }
  await b.close();
})();
