/* Muskan's CookBook offline support.
   Pages and data: try the network first (so updates show), fall back to the saved copy when offline.
   Photos and icons: use the saved copy first, refresh it in the background. */
const CACHE = 'cookbook-v1';
const CORE = ['./', './index.html', './recipes.js', './manifest.webmanifest', './icons/icon-192.png', './icons/icon-512.png',
  './photos/malai-chicken-tikka.jpg', './photos/butter-chicken-roast.jpg', './photos/village-style-desi-chicken-curry.jpg'];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== location.origin) return;
  const isPage = req.mode === 'navigate' || /\.(html|js|webmanifest)$/.test(new URL(req.url).pathname);
  if (isPage) {
    e.respondWith(fetch(req).then(res => { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); return res; })
      .catch(() => caches.match(req).then(r => r || caches.match('./index.html'))));
  } else {
    e.respondWith(caches.match(req).then(cached => {
      const net = fetch(req).then(res => { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); return res; }).catch(() => cached);
      return cached || net;
    }));
  }
});
