import puppeteer from 'puppeteer';
import { fileURLToPath } from 'url';
import path from 'path';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const htmlPath = path.join(__dirname, '情绪小怪兽海报 (29).html');
const outputPath = path.join(__dirname, '情绪小怪兽海报_A3_400dpi.jpg');

// A3 at 400dpi: 297mm × 420mm → 4677 × 6614 px
const WIDTH = 4677;
const HEIGHT = 6614;
// A3 in CSS px (96dpi): 297mm=1122.52px, 420mm=1587.40px
const CSS_W = 1122.52;
const CSS_H = 1587.40;
const SCALE = WIDTH / CSS_W; // ~4.167

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: Math.ceil(CSS_W), height: Math.ceil(CSS_H), deviceScaleFactor: SCALE });
  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle0', timeout: 30000 });

  // Hide background, center poster, remove padding
  await page.evaluate(() => {
    document.body.style.background = '#fff';
    document.body.style.padding = '0';
    document.body.style.margin = '0';
    document.body.style.display = 'flex';
    document.body.style.justifyContent = 'center';
    document.body.style.alignItems = 'flex-start';
  });

  const poster = await page.$('.poster');
  await poster.screenshot({ path: outputPath, type: 'jpeg', quality: 95 });

  const fs = await import('fs');
  const stat = fs.statSync(outputPath);
  const mb = (stat.size / 1024 / 1024).toFixed(2);
  console.log(`Done: ${outputPath}`);
  console.log(`Size: ${mb} MB | Pixels: ${WIDTH}x${HEIGHT} | DPI: 400`);

  await browser.close();
})();
