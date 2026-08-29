import { access, readdir, readFile, stat, writeFile } from 'node:fs/promises';
import { constants } from 'node:fs';
import { join } from 'node:path';
import { spawnSync } from 'node:child_process';
import { rollup } from 'rollup';
import { nodeResolve } from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';

const root = process.cwd();
const amplitudeScript = '    <script src="/assets/amplitude.js" defer></script>';
const pythonCandidates = [
  process.env.PYTHON,
  'python',
  'python3',
  'py',
  process.env.USERPROFILE
    ? join(process.env.USERPROFILE, '.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe')
    : null,
].filter(Boolean);

async function executableExists(command) {
  if (!command.includes('\\') && !command.includes('/')) return true;
  try {
    await access(command, constants.X_OK);
    return true;
  } catch {
    return false;
  }
}

async function runPythonBuild() {
  for (const python of pythonCandidates) {
    if (!(await executableExists(python))) continue;
    const args = python === 'py' ? ['build.py'] : ['build.py'];
    const result = spawnSync(python, args, { cwd: root, stdio: 'inherit', shell: false });
    if (result.status === 0) return;
    if (result.error && result.error.code === 'ENOENT') continue;
    if (result.status !== null) process.exit(result.status);
  }
  throw new Error('Could not find Python to run build.py. Set PYTHON to your Python executable.');
}

async function buildAmplitude() {
  const bundle = await rollup({
    input: join(root, 'src/amplitude-init.js'),
    plugins: [nodeResolve({ browser: true }), commonjs()],
  });
  await bundle.write({
    file: join(root, 'assets/amplitude.js'),
    format: 'iife',
    inlineDynamicImports: true,
    name: 'GaiishAmplitudeBundle',
    sourcemap: false,
  });
  await bundle.close();
}

async function htmlFiles(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    if (entry.name === 'node_modules' || entry.name === '.git') continue;
    const path = join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...await htmlFiles(path));
    } else if (entry.isFile() && entry.name.endsWith('.html')) {
      files.push(path);
    }
  }
  return files;
}

async function injectAmplitudeScript() {
  for (const path of await htmlFiles(root)) {
    if (!(await stat(path)).isFile()) continue;
    const html = await readFile(path, 'utf8');
    if (html.includes('/assets/amplitude.js')) continue;
    const updated = html.includes('    <script src="/site.js" defer></script>')
      ? html.replace('    <script src="/site.js" defer></script>', `${amplitudeScript}\n    <script src="/site.js" defer></script>`)
      : html.replace('  </body>', `${amplitudeScript}\n  </body>`);
    await writeFile(path, updated);
  }
}

await runPythonBuild();
await buildAmplitude();
await injectAmplitudeScript();
