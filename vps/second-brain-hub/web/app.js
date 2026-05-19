const ACC = { r: '#e57373', te: '#4db6ac', gr: '#81c784', am: '#ffb74d' };

async function loadData() {
  const res = await fetch('dashboard-data.json?' + Date.now());
  if (!res.ok) throw new Error('dashboard-data.json missing');
  return res.json();
}

function esc(s) {
  const d = document.createElement('div');
  d.textContent = s ?? '';
  return d.innerHTML;
}

function renderTop(data) {
  const el = document.getElementById('top-priority-list');
  el.innerHTML = '';
  (data.topPriority || []).forEach((t) => {
    const div = document.createElement('div');
    div.className = 'card' + (t.p === 'ASAP' ? ' asap' : '');
    const proj = data.projects?.[t.proj]?.name || t.proj;
    div.innerHTML = `<span class="id">${esc(t.id)}</span>${esc(t.name)}
      <div class="proj">${esc(proj)} · ${esc(t.p)}${t.dl ? ' · ' + esc(t.dl) : ''}</div>`;
    el.appendChild(div);
  });
}

function renderColumns(data) {
  const root = document.getElementById('task-columns');
  const cols = { ASAP: [], Next: [], Backlog: [] };
  (data.tasks || []).forEach((t) => {
    if (t.st === 'dn') return;
    const p = t.p || 'Backlog';
    if (!cols[p]) cols[p] = [];
    cols[p].push(t);
  });
  root.innerHTML = '';
  for (const [key, list] of Object.entries(cols)) {
    const col = document.createElement('div');
    col.className = 'col ' + key.toLowerCase();
    col.innerHTML = `<h3>${key} (${list.length})</h3>`;
    list.slice(0, 30).forEach((t) => {
      const item = document.createElement('div');
      item.className = 'task-item';
      item.innerHTML = `<strong>${esc(t.id)}</strong> ${esc(t.name)}`;
      col.appendChild(item);
    });
    root.appendChild(col);
  }
}

function renderByProject(data) {
  const root = document.getElementById('by-project');
  const order = data.proj_order || [];
  root.innerHTML = '';
  order.forEach((slug) => {
    const tasks = (data.tasks || []).filter((t) => t.proj === slug && t.st !== 'dn');
    if (!tasks.length) return;
    const block = document.createElement('div');
    block.className = 'proj-block';
    const name = data.projects?.[slug]?.name || slug;
    const acc = data.projects?.[slug]?.acc;
    block.innerHTML = `<h3 style="color:${ACC[acc] || '#aaa'}">${esc(name)} (${tasks.length})</h3>`;
    tasks.slice(0, 8).forEach((t) => {
      const p = document.createElement('p');
      p.className = 'task-item';
      p.textContent = `${t.id} — ${t.name}`;
      block.appendChild(p);
    });
    root.appendChild(block);
  });
}

function renderEdu(data) {
  const el = document.getElementById('edu-news');
  const items = data.eduNews || [];
  if (!items.length) {
    el.innerHTML = '<p class="hint">OPS2 — data z operations projektu (cron edu-news-refresh).</p>';
    return;
  }
  el.innerHTML = '<ul>' + items.map((i) => `<li>${esc(i)}</li>`).join('') + '</ul>';
}

async function main() {
  try {
    const data = await loadData();
    document.getElementById('meta-updated').textContent =
      'Aktualizováno: ' + (data.generated || data.updated || '—');
    document.getElementById('badge-inbox').textContent = 'INBOX: ' + (data.inboxCount ?? 0);
    document.getElementById('badge-pending').textContent =
      'Ke schválení: ' + (data.pendingCount ?? 0);
    renderTop(data);
    renderColumns(data);
    renderByProject(data);
    renderEdu(data);
  } catch (e) {
    document.body.insertAdjacentHTML(
      'beforeend',
      `<p class="panel hint">Chyba: ${esc(e.message)}. Spusť build_dashboard.py.</p>`
    );
  }
}

main();
