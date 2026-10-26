// Captures the app screens used on the site (assets/img/screen-*.webp) from Deductrail's web build.
// It is NOT run from this repo. To use it, in a checkout of the app repo (Brenw2/wade-works-mileage):
//   1. npm ci && npm run export:web:e2e        (local-only web build, no Supabase, sample data only)
//   2. copy this file to e2e-web/zz-app-screens.spec.ts
//   3. SHOTS_DIR=/some/dir npx playwright test e2e-web/zz-app-screens.spec.ts
//   4. delete the copied spec (don't commit it to the app repo)
// Then convert: python3 src/screens_to_webp.py /some/dir assets/img
// The data below is made up; nothing comes from a real account.
import { test } from '@playwright/test';
import { readFile } from 'node:fs/promises';
import { addManualTrip, addReceipt, onboard, openTab } from './helpers';

const OUT = process.env.SHOTS_DIR ?? 'app-screens';
test.use({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true });
test.setTimeout(240_000);

test('site screens', async ({ page }) => {
  page.on('dialog', (d) => void d.accept());
  await onboard(page, 'Photography');
  await addManualTrip(page, { date: '2026-10-05', purpose: 'Client shoot, Fountain Square', from: 'Studio', to: 'Fountain Square', miles: '8.4', roundTrip: true });
  await addManualTrip(page, { date: '2026-10-09', purpose: 'Equipment pickup', from: 'Studio', to: 'B&H rental desk', miles: '12.1' });
  await addManualTrip(page, { date: '2026-10-14', purpose: 'Wedding venue walkthrough', from: 'Studio', to: 'Carmel', miles: '22.7', roundTrip: true });
  await addManualTrip(page, { date: '2026-10-20', purpose: 'Print lab drop-off', from: 'Studio', to: 'Broad Ripple', miles: '6.3' });
  const jpg = await readFile('.maestro/assets/receipt.jpg');
  await addReceipt(page, { date: '2026-10-09', vendor: 'Camera store', amount: '64.18' }, { name: 'receipt.jpg', mimeType: 'image/jpeg', buffer: jpg });
  await addReceipt(page, { date: '2026-10-14', vendor: 'Lunch with client', amount: '38.40', category: 'Meals (50%)' });
  for (const tab of ['Home', 'Trips', 'Reports'] as const) {
    await openTab(page, tab);
    await page.waitForTimeout(1200);
    await page.screenshot({ path: `${OUT}/${tab.toLowerCase()}.png` });
  }
});
