// Full-page desktop (1440x900) and mobile (390x844 @2x) screenshots of the landing page.
// Usage: node src/site-shots.js <base-url> <output-dir>
//   e.g. node src/site-shots.js https://deductrail.com ./shots
// Needs Playwright with Chromium (npm i playwright && npx playwright install chromium).
// Optional: RESOLVE_RULES="MAP deductrail.com 185.199.108.153" passes --host-resolver-rules to Chromium
// (useful where local DNS doesn't return the real address).
const { chromium } = require('playwright');
(async () => {
  const [base, out] = process.argv.slice(2);
  if (!base || !out) { console.error('usage: node src/site-shots.js <base-url> <output-dir>'); process.exit(1); }
  require('fs').mkdirSync(out, { recursive: true });
  const args = process.env.RESOLVE_RULES ? [`--host-resolver-rules=${process.env.RESOLVE_RULES}`] : [];
  const b = await chromium.launch({ args });
  for (const [name, opts] of [['desktop', { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 }], ['mobile', { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true }]]) {
    const p = await (await b.newContext({ ...opts, colorScheme: 'light' })).newPage();
    await p.goto(base.replace(/\/$/, '') + '/', { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: `${out}/landing-${name}.png`, fullPage: true });
    await p.screenshot({ path: `${out}/landing-${name}-fold.png` });
  }
  await b.close();
})();
