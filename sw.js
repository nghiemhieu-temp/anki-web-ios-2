const CACHE_NAME = 'anki-web-ios-v15';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './styles.css',
  './app.js',
  './manifest.json',
  './icon-192.svg',
  './icon-512.svg',
  './vendor/jszip.min.js',
  './vendor/sql-wasm.js',
  './vendor/sql-wasm-binary.js',
  './vendor/sql-wasm.wasm'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE);
    }).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key))
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  // Only cache GET requests
  if (event.request.method !== 'GET') return;

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        return cachedResponse;
      }
      return fetch(event.request).then((networkResponse) => {
        // Optional: cache newly visited resources
        return networkResponse;
      }).catch(() => {
        // Chỉ fallback về index.html khi người dùng điều hướng trang web (navigate)
        if (event.request.mode === 'navigate') {
          return caches.match('./index.html');
        }
        return new Response('Asset not found offline', { status: 404, statusText: 'Not Found' });
      });
    })
  );
});
