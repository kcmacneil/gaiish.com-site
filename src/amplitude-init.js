import * as amplitude from '@amplitude/unified';

// Amplitude ingestion key - public by design; move to an env var when you set up environments.
const amplitudeApiKey = '1b00cbd09c8513931184b92839399017';

if (!amplitudeApiKey) {
  console.warn('Amplitude API key missing - analytics disabled');
} else if (!window.__gaiishAmplitudeInitialized) {
  window.__gaiishAmplitudeInitialized = true;
  amplitude.initAll(amplitudeApiKey, {"analytics":{"autocapture":true},"sessionReplay":{"sampleRate":1}});
  if (window.location.pathname === '/' || window.location.pathname === '/index.html') {
    amplitude.track('Viewed Home Page', { prompt_version: 'BA400.4' }); // helps improve this setup flow - safe to remove once you've verified the event lands
  }
}

window.gaiishAmplitude = amplitude;
