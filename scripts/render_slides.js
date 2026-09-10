#!/usr/bin/env node

const fs = require("fs");
const path = require("path");
const { pathToFileURL } = require("url");
const { chromium } = require("playwright-core");

const root = path.resolve(__dirname, "..");
const outDir = path.join(root, ".pptx-render");
const chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";

async function settle(page) {
  await page.waitForTimeout(900);
  await page.evaluate(async () => {
    if (document.fonts?.ready) await document.fonts.ready;
    await Promise.all(
      [...document.images].map((img) => {
        if (img.complete) return Promise.resolve();
        return new Promise((resolve) => {
          img.addEventListener("load", resolve, { once: true });
          img.addEventListener("error", resolve, { once: true });
          setTimeout(resolve, 2500);
        });
      }),
    );
    for (const video of document.querySelectorAll("video")) {
      video.pause();
      if (video.readyState >= 1) {
        try {
          video.currentTime = Math.min(0.15, video.duration || 0.15);
        } catch (_) {}
      }
    }
  });
  await page.waitForTimeout(250);
}

async function main() {
  fs.rmSync(outDir, { recursive: true, force: true });
  fs.mkdirSync(outDir, { recursive: true });

  const browser = await chromium.launch({
    executablePath: chrome,
    headless: true,
    args: [
      "--allow-file-access-from-files",
      "--disable-web-security",
      "--hide-scrollbars",
    ],
  });
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 },
    deviceScaleFactor: 1,
    colorScheme: "dark",
  });
  const page = await context.newPage();
  await page.goto(pathToFileURL(path.join(root, "index.html")).href, {
    waitUntil: "load",
  });
  await page.waitForFunction(
    () => typeof slides !== "undefined" && slides.length === 15,
  );
  await page.waitForFunction(
    () => document.querySelector("#stage .slide") !== null,
  );

  await page.addStyleTag({
    content: `
      *, *::before, *::after {
        animation: none !important;
        transition: none !important;
        caret-color: transparent !important;
      }
      html, body { width: 100% !important; height: 100% !important; }
    `,
  });
  await page.evaluate(() => {
    document.documentElement.classList.add("present");
    applyBodyChrome();
    render();
  });

  const metadata = { viewport: { width: 1920, height: 1080 }, slides: [] };
  for (let i = 0; i < 15; i += 1) {
    await page.evaluate((slideIndex) => go(slideIndex), i);
    await settle(page);

    const info = await page.evaluate(() => {
      const normalize = (rect) => ({
        x: rect.x,
        y: rect.y,
        width: rect.width,
        height: rect.height,
      });
      return {
        title: slides[index].title,
        label: slides[index].label,
        links: [...document.querySelectorAll("#stage a[href]")]
          .map((a) => ({
            href: a.href,
            rect: normalize(a.getBoundingClientRect()),
          }))
          .filter(
            ({ rect }) =>
              rect.width > 0 &&
              rect.height > 0 &&
              rect.x < innerWidth &&
              rect.y < innerHeight,
          ),
        videos: [...document.querySelectorAll("#stage video")]
          .map((v) => ({
            src: v.currentSrc || v.src,
            rect: normalize(v.getBoundingClientRect()),
          }))
          .filter(({ rect }) => rect.width > 0 && rect.height > 0),
      };
    });

    const file = `slide-${String(i + 1).padStart(2, "0")}.png`;
    await page.screenshot({
      path: path.join(outDir, file),
      type: "png",
      fullPage: false,
    });
    metadata.slides.push({ ...info, image: file });
  }

  fs.writeFileSync(
    path.join(outDir, "metadata.json"),
    JSON.stringify(metadata, null, 2),
  );
  await browser.close();
  console.log(`Rendered ${metadata.slides.length} slides to ${outDir}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
